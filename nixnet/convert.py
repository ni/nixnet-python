from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools
import typing  # NOQA: F401
import warnings

from nixnet import _frames
from nixnet import _funcs
from nixnet import _props
from nixnet import _utils
from nixnet import constants
from nixnet import errors
from nixnet import types

from nixnet._session import j1939 as session_j1939
from nixnet._session import signals as session_signals


__all__ = [
    "SignalConversionSinglePointSession"]


class SignalConversionSinglePointSession(object):
    """Convert NI-XNET signal data to frame data or vice versa.

    Conversion works similar to Single-Point mode. You specify a set of signals
    that can span multiple frames. Signal to frame conversion reads a set of
    values for the signals specified and writes them to the respective
    frame(s). Frame to signal conversion parses a set of frames and returns the
    latest signal value read from a corresponding frame.
    """

    def __init__(
            self,
            database_name,  # type: typing.Text
            cluster_name,  # type: typing.Text
            signals,  # type: typing.Union[typing.Text, typing.List[typing.Text]]
    ):
        # type: (...) -> None
        """Create an XNET session at run time using named references to database objects.

        Args:
            database_name(str): XNET database name to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name(str): XNET cluster name to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the ``signals`` parameter.
            signals(list of str): Strings describing signals for the session. The
                list syntax is as follows:

                ``signals`` contains one or more XNET Signal names. Each name must
                be one of the following options, whichever uniquely
                identifies a signal within the database given:

                    - ``<Signal>``
                    - ``<Frame>.<Signal>``
                    - ``<Cluster>.<Frame>.<Signal>``
                    - ``<PDU>.<Signal>``
                    - ``<Cluster>.<PDU>.<Signal>``

                ``signals`` may also contain one or more trigger signals. For
                information about trigger signals, refer to Signal Output
                Single-Point Mode or Signal Input Single-Point Mode.
        """
        flattened_list = _utils.flatten_items(signals)

        self._handle = None  # To satisfy `__del__` in case nx_create_session throws
        self._handle = _funcs.nx_create_session(
            database_name,
            cluster_name,
            flattened_list,
            "",
            constants.CreateSessionMode.SIGNAL_CONVERSION_SINGLE_POINT)
        self._j1939 = session_j1939.J1939(self._handle)
        self._signals = session_signals.Signals(self._handle)

    def __del__(self):
        if self._handle is not None:
            warnings.warn(
                'Session was not explicitly closed before it was destructed. '
                'Resources on the device may still be reserved.',
                errors.XnetResourceWarning)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(SignalConversionSinglePointSession, other._handle)
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        # type: () -> typing.Text
        return 'Session(handle={0})'.format(self._handle)

    def close(self):
        # type: () -> None
        """Close (clear) the XNET session."""
        if self._handle is None:
            warnings.warn(
                'Attempting to close NI-XNET session but session was already '
                'closed', errors.XnetResourceWarning)
            return

        _funcs.nx_clear(self._handle)

        self._handle = None

    @property
    def signals(self):
        # type: () -> session_signals.Signals
        """:any:`nixnet._session.signals.Signals`: Operate on session's signals"""
        return self._signals

    @property
    def j1939(self):
        # type: () -> session_j1939.J1939
        """:any:`nixnet._session.j1939.J1939`: Returns the J1939 configuration object for the session."""
        return self._j1939

    @property
    def application_protocol(self):
        # type: () -> constants.AppProtocol
        """:any:`nixnet._enums.AppProtocol`: This property returns the application protocol that the session uses.

        The database used with the session determines the application protocol.
        """
        return constants.AppProtocol(_props.get_session_application_protocol(self._handle))

    @property
    def cluster_name(self):
        # type: () -> typing.Text
        """str: This property returns the cluster (network) name used with the session."""
        return _props.get_session_cluster_name(self._handle)

    @property
    def database_name(self):
        # type: () -> typing.Text
        """str: This property returns the database name used with the session."""
        return _props.get_session_database_name(self._handle)

    @property
    def mode(self):
        # type: () -> constants.CreateSessionMode
        """:any:`nixnet._enums.CreateSessionMode`: This property returns the mode associated with the session.

        For more information, refer to :any:`nixnet._enums.CreateSessionMode`.
        """
        return constants.CreateSessionMode(_props.get_session_mode(self._handle))

    @property
    def protocol(self):
        # type: () -> constants.Protocol
        """:any:`nixnet._enums.Protocol`: This property returns the protocol that the interface in the session uses."""
        return constants.Protocol(_props.get_session_protocol(self._handle))

    def _convert_bytes_to_signals(self, bytes):
        # type: (bytes) -> typing.Iterable[typing.Tuple[int, float]]
        num_signals = len(self.signals)
        timestamps, values = _funcs.nx_convert_frames_to_signals_single_point(self._handle, bytes, num_signals)
        for timestamp, value in zip(timestamps, values):
            yield timestamp.value, value.value

    def convert_frames_to_signals(self, frames):
        # type: (typing.Iterable[types.Frame]) -> typing.Iterable[typing.Tuple[int, float]]
        """Convert Frames to signals.

        The frames passed into the ``frames`` array are read one by one, and
        the signal values found are written to internal buffers for each
        signal. Frames are identified by their identifier (FlexRay: slot)
        field. After all frames in ``frames`` array are processed, the internal
        signal buffers' status is returned with the corresponding timestamps
        from the frames where a signal value was found. The signal internal
        buffers' status is being preserved over multiple calls to this
        function.

        This way, for example, data returned from multiple calls of nxFrameRead
        for a Frame Input Stream Mode session (or any other Frame Input
        session) can be passed to this function directly.

        .. note:: Frames unknown to the session are silently ignored.
        """
        units = itertools.chain.from_iterable(
            _frames.serialize_frame(frame.to_raw())
            for frame in frames)
        bytes = b"".join(units)
        return self._convert_bytes_to_signals(bytes)

    def _convert_signals_to_bytes(self, signals, num_bytes):
        # type: (typing.Iterable[float], int) -> bytes
        buffer, number_of_bytes_returned = _funcs.nx_convert_signals_to_frames_single_point(
            self._handle,
            list(signals),
            num_bytes)
        return buffer[0:number_of_bytes_returned]

    def convert_signals_to_frames(self, signals, frame_type=types.XnetFrame):
        # type: (typing.Iterable[float], typing.Type[types.FrameFactory]) -> typing.Iterable[types.Frame]
        """Convert signals to frames.

        The signal values written to the ``signals`` array are written to a raw
        frame buffer array. For each frame included in the session, one frame
        is generated in the array that contains the signal values. Signals not
        present in the session are written as their respective default values;
        empty space in the frames that signals do not occupy is written with
        the frame's default payload.

        The frame header values are filled with appropriate values so that this
        function's output can be directly written to a Frame Output session.

        Args:
            signals(list of float): Values corresponding to signals configured
                in this session.
            frame_type(:any:`nixnet.types.FrameFactory`): A factory for the
                desired frame formats.

        Yields:
            :any:`nixnet.types.Frame`
        """
        from_raw = typing.cast(typing.Callable[[types.RawFrame], types.Frame], frame_type.from_raw)
        # Unlike some session reads, this should be safe from asking to read too much.
        num_frames_to_read = 5
        while True:
            try:
                num_bytes_to_read = num_frames_to_read * _frames.nxFrameFixed_t.size
                buffer = self._convert_signals_to_bytes(signals, num_bytes_to_read)
                break
            except errors.XnetError as e:
                if e.error_type == constants.Err.BUFFER_TOO_SMALL:
                    num_bytes_to_read *= 2
                else:
                    raise
        for frame in _frames.iterate_frames(buffer):
            yield from_raw(frame)
