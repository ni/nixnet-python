from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _funcs
from nixnet import _utils
from nixnet import constants

from nixnet._session import base
from nixnet._session import frames as session_frames
from nixnet._session import signals as session_signals


__all__ = [
    "FrameInStreamSession",
    "FrameOutStreamSession",
    "FrameInQueuedSession",
    "FrameOutQueuedSession",
    "FrameInSinglePointSession",
    "FrameOutSinglePointSession",
    "SignalInSinglePointSession",
    "SignalOutSinglePointSession"]


class FrameInStreamSession(base.SessionBase):
    """Frame Input Stream session.

    This session reads all frames received from the network using a single
    stream. It typically is used for analyzing and/or logging all frame traffic
    in the network.

    The input data is returned as a list of frames. Because all frames are
    returned, your application must evaluate identification in each frame (such
    as a CAN identifier or FlexRay slot/cycle/channel) to interpret the frame
    payload data.

    Previously, you could use only one Frame Input Stream session for a given
    interface. Now, multiple Frame Input Stream sessions can be open at the same
    time on CAN and LIN interfaces.

    While using one or more Frame Input Stream sessions, you can use other
    sessions with different input modes. Received frames are copied to Frame
    Input Stream sessions in addition to any other applicable input session. For
    example, if you create a Frame Input Single-Point session for frame_a, then
    create a Frame Input Stream session, when frame_a is received, its data is
    returned from the call to read function of both sessions. This duplication
    of incoming frames enables you to analyze overall traffic while running a
    higher level application that uses specific frame or signal data.

    When used with a FlexRay interface, frames from both channels are returned.
    For example, if a frame is received in a static slot on both channel A and
    channel B, two frames are returned from the read function.
    """

    def __init__(
            self,
            interface_name,
            database_name=':memory:',
            cluster_name=''):
        """Create a Frame Input Stream session.

        This function creates a Frame Input Stream session using the named
        references to database objects.

        Args:
            interface_name: A string representing the XNET Interface to use for
                this session.
            database_name: A string representing the XNET database to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name: A string representing the XNET cluster to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter.

        Returns:
            A Frame Input Stream session object.
        """
        flattened_list = _utils.flatten_items(None)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.FRAME_IN_STREAM)
        self._frames = session_frames.InFrames(self._handle)

    @property
    def frames(self):
        return self._frames


class FrameOutStreamSession(base.SessionBase):
    """Frame Output Stream session.

    This session transmits an arbitrary sequence of frame values using a single
    stream. The values are not limited to a single frame in the database, but
    can transmit any frame.

    The data passed to the write frame function is a list of frame values,
    each of which transmits as soon as possible. Frames transmit sequentially
    (one after another).

    This session is not supported for FlexRay.

    Like Frame Input Stream sessions, you can create more than one Frame Output
    Stream session for a given interface.

    For CAN, frame values transmit on the network based entirely on the time
    when you call the write frame function. The timing of each frame as
    specified in the database is ignored. For example, if you provide four frame
    values to the the write frame function, the first frame value transmits
    immediately, followed by the next three values transmitted back to back. For
    this session, the CAN frame payload length in the database is ignored, and
    the write frame function is always used.

    Similarly for LIN, frame values transmit on the network based entirely on
    the time when you call the write frame function. The timing of each frame as
    specified in the database is ignored. The LIN frame payload length in the
    database is ignored, and the write frame function is always used. For LIN,
    this session/mode is allowed only on the interface as master. If the payload
    for a frame is empty, only the header part of the frame is transmitted. For
    a nonempty payload, the header + response for the frame is transmitted. If a
    frame for transmit is defined in the database (in-memory or otherwise), it
    is transmitted using its database checksum type. If the frame for transmit
    is not defined in the database, it is transmitted using enhanced checksum.

    The frame values for this session are stored in a queue, such that every value
    provided is transmitted.
    """

    def __init__(
            self,
            interface_name,
            database_name=':memory:',
            cluster_name=''):
        """Create a Frame Input Stream session.

        This function creates a Frame Output Stream session using the named
        references to database objects.

        Args:
            interface_name: A string representing the XNET Interface to use for
                this session.
            database_name: A string representing the XNET database to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name: A string representing the XNET cluster to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter.

        Returns:
            A Frame Output Stream session object.
        """
        flattened_list = _utils.flatten_items(None)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.FRAME_OUT_STREAM)
        self._frames = session_frames.OutFrames(self._handle)

    @property
    def frames(self):
        return self._frames


class FrameInQueuedSession(base.SessionBase):
    """Frame Input Queued session.

    This session reads data from a dedicated queue per frame. It enables your
    application to read a sequence of data specific to a frame (for example, a
    CAN identifier).

    You specify only one frame for the session, and the read frame function
    returns values for that frame only. If you need sequential data for multiple
    frames, create multiple sessions, one per frame.

    The input data is returned as a list of frame values. These values
    represent all values received for the frame since the previous call to the
    read frame function.
    """

    def __init__(
            self,
            interface_name,
            database_name,
            cluster_name,
            frame):
        """Create a Frame Input Queued session.

        This function creates a Frame Input Queued session using the named
        references to database objects.

        Args:
            interface_name: A string representing the XNET Interface to use for
                this session.
            database_name: A string representing the XNET database to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax(refer to Databases).
            cluster_name: A string representing the XNET cluster to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the 'frame' parameter.
            frame: A string describing one XNET Frame or PDU name. This name
                must be one of the following options, whichever uniquely
                identifies a frame within the database given:

                    -<Frame>
                    -<Cluster>.<Frame>
                    -<PDU>
                    -<Cluster>.<PDU>

        Returns:
            A Frame Input Queued session object.
        """
        flattened_list = _utils.flatten_items(frame)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.FRAME_IN_QUEUED)
        self._frames = session_frames.InFrames(self._handle)

    @property
    def frames(self):
        return self._frames


class FrameOutQueuedSession(base.SessionBase):
    """Frame Output Queued session.

    This session provides a sequence of values for a single frame, for transmit
    using that frame's timing as specified in the database.

    The output data is provided as a list of frame values, to be transmitted
    sequentially for the frame specified in the session.

    You can only specify one frame for this session. To transmit sequential
    values for multiple frames, use a different Frame Output Queued session for
    each frame or use the Frame Output Stream session.

    The frame values for this session are stored in a queue, such that every
    value provided is transmitted.

    For this session, NI-XNET transmits each frame according to its properties
    in the database. Therefore, when you call the write frame function, the
    number of payload bytes in each frame value must match that frame's Payload
    Length property. The other frame value elements are ignored, so you can
    leave them uninitialized. For CAN interfaces, if the number of payload bytes
    you write is smaller than the Payload Length configured in the database, the
    requested number of bytes transmits. If the number of payload bytes is
    larger than the Payload Length configured in the database, the queue is
    flushed and no frames transmit. For other interfaces, transmitting a number
    of payload bytes different than the frame's payload may cause unexpected
    results on the bus.
    """

    def __init__(
            self,
            interface_name,
            database_name,
            cluster_name,
            frame):
        """Create a Frame Output Queued session.

        This function creates a Frame Output Stream session using the named
        references to database objects.

        Args:
            interface_name: A string representing the XNET Interface to use for
                this session.
            database_name: A string representing the XNET database to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name: A string representing the XNET cluster to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the 'frame' parameter.
            frame: A string describing one XNET Frame or PDU name. This name
                must be one of the following options, whichever uniquely
                identifies a frame within the database given:

                    -<Frame>
                    -<Cluster>.<Frame>
                    -<PDU>
                    -<Cluster>.<PDU>

        Returns:
            A Frame Output Queued session object.
        """
        flattened_list = _utils.flatten_items(frame)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.FRAME_OUT_QUEUED)
        self._frames = session_frames.OutFrames(self._handle)

    @property
    def frames(self):
        return self._frames


class FrameInSinglePointSession(base.SessionBase):
    """Frame Input Single-Point session.

    This session reads the most recent value received for each frame. It
    typically is used for control or simulation applications that require lower
    level access to frames (not signals).

    This session does not use queues to store each received frame. If the
    interface receives two frames prior to calling the read frame function, that
    read returns signals for the second frame.

    The input data is returned as a list of frames, one for each frame
    specified for the session.
    """

    def __init__(
            self,
            interface_name,
            database_name,
            cluster_name,
            frames):
        """Create a Frame Input Single-Point session.

        This function creates a Frame Input Single-Point session using the named
        references to database objects.

        Args:
            interface_name: A string representing the XNET Interface to use for
                this session.
            database_name: A string representing the XNET database to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name: A string representing the XNET cluster to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the 'frames' parameter.
            frames: A list of strings describing frames for the session. The
                list syntax is as follows:

                    List contains one or more XNET Frame or PDU names. Each name
                    must be one of the following options, whichever uniquely
                    identifies a frame within the database given:

                        -<Frame>
                        -<Cluster>.<Frame>
                        -<PDU>
                        -<Cluster>.<PDU>

        Returns:
            A Frame Input Single-Point session object.
        """
        flattened_list = _utils.flatten_items(frames)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.FRAME_IN_SINGLE_POINT)
        self._frames = session_frames.SinglePointInFrames(self._handle)

    @property
    def frames(self):
        return self._frames


class FrameOutSinglePointSession(base.SessionBase):
    """Frame Output Single-Point session.

    This session writes frame values for the next transmit. It typically is used
    for control or simulation applications that require lower level access to
    frames (not signals).

    This session does not use queues to store frame values. If the write frame
    function is called twice before the next transmit, the transmitted frame
    uses the value from the second call to the write frame function.

    The output data is provided as a list of frames, one for each frame
    specified for the session.

    For this session, NI-XNET transmits each frame according to its properties
    in the database. Therefore, when you call the write frame function, the
    number of payload bytes in each frame value must match that frame's Payload
    Length property. The other frame value elements are ignored, so you can
    leave them uninitialized. For CAN interfaces, if the number of payload bytes
    you write is smaller than the Payload Length configured in the database, the
    requested number of bytes transmit. If the number of payload bytes is larger
    than the Payload Length configured in the database, the queue is flushed and
    no frames transmit. For other interfaces, transmitting a number of payload
    bytes different than the frame payload may cause unexpected results on the bus.
    """
    def __init__(
            self,
            interface_name,
            database_name,
            cluster_name,
            frames):
        """Create a Frame Output Single-Point session.

        This function creates a Frame Output Single-Point session using the named
        references to database objects.

        Args:
            interface_name: A string representing the XNET Interface to use for
                this session.
            database_name: A string representing the XNET database to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name: A string representing the XNET cluster to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the 'frames' parameter.
            frames: A list of strings describing frames for the session. The
                list syntax is as follows:

                    List contains one or more XNET Frame or PDU names. Each name
                    must be one of the following options, whichever uniquely
                    identifies a frame within the database given:

                        -<Frame>
                        -<Cluster>.<Frame>
                        -<PDU>
                        -<Cluster>.<PDU>

        Returns:
            A Frame Output Single-Point session object.
        """
        flattened_list = _utils.flatten_items(frames)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.FRAME_OUT_SINGLE_POINT)
        self._frames = session_frames.SinglePointOutFrames(self._handle)

    @property
    def frames(self):
        return self._frames


class SignalInSinglePointSession(base.SessionBase):
    """Signal Input Single-Point session.

    This session reads the most recent value received for each signal. It
    typically is used for control or simulation applications, such as Hardware
    In the Loop (HIL).

    This session does not use queues to store each received frame. If the
    interface receives two frames prior to calling
    :any:`nixnet._session.signals.SinglePointInSignals.read`, that call to
    :any:`nixnet._session.signals.SinglePointInSignals.read` returns signals
    for the second frame.

    Use :any:`nixnet._session.signals.SinglePointInSignals.read` for this session.

    You also can specify a trigger signal for a frame. This signal name is
    :trigger:.<frame name>, and once it is specified in the __init__ 'signals'
    list, it returns a value of 0.0 if the frame did not arrive since the last
    Read (or Start), and 1.0 if at least one frame of this ID arrived. You can
    specify multiple trigger signals for different frames in the same session.
    For multiplexed signals, a signal may or may not be contained in a received
    frame. To define a trigger signal for a multiplexed signal, use the signal
    name :trigger:.<frame name>.<signal name>. This signal returns 1.0 only if a
    frame with appropriate set multiplexer bit has been received since the last
    Read or Start.
    """

    def __init__(
            self,
            interface_name,
            database_name,
            cluster_name,
            signals):
        """Create a Signal Input Single-Point session.

        This function creates a Signal Input Single-Point session using the named
        references to database objects.

        Args:
            interface_name: A string representing the XNET Interface to use for
                this session.
            database_name: A string representing the XNET database to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name: A string representing the XNET cluster to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the signals parameter.
            signals: A list of strings describing signals for the session. The
                list syntax is as follows:

                    List contains one or more XNET Signal names. Each name must
                    be one of the following options, whichever uniquely
                    identifies a signal within the database given:

                        -<Signal>
                        -<Frame>.<Signal>
                        -<Cluster>.<Frame>.<Signal>
                        -<PDU>.<Signal>
                        -<Cluster>.<PDU>.<Signal>

                    List may also contain one or more trigger signals. For
                    information about trigger signals, refer to Signal Output
                    Single-Point Mode or Signal Input Single-Point Mode.

        Returns:
            A Signal Input Single-Point session object.
        """
        flattened_list = _utils.flatten_items(signals)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.SIGNAL_IN_SINGLE_POINT)
        self._signals = session_signals.SinglePointInSignals(self._handle)

    @property
    def signals(self):
        return self._signals


class SignalOutSinglePointSession(base.SessionBase):
    """Signal Out Single-Point session.

    This session writes signal values for the next frame transmit. It typically
    is used for control or simulation applications, such as Hardware In the Loop
    (HIL).

    This session does not use queues to store signal values. If
    :any:`nixnet._session.signals.SinglePointOutSignals.write` is called twice
    before the next transmit, the transmitted frame uses signal values from the
    second call to :any:`nixnet._session.signals.SinglePointOutSignals.write`.

    Use :any:`nixnet._session.signals.SinglePointOutSignals.write` for this session.

    You also can specify a trigger signal for a frame. This signal name is
    :trigger:.<frame name>, and once it is specified in the __init__ 'signals'
    list, you can write a value of 0.0 to suppress writing of that frame, or any
    value not equal to 0.0 to write the frame. You can specify multiple trigger
    signals for different frames in the same session.
    """

    def __init__(
            self,
            interface_name,
            database_name,
            cluster_name,
            signals):
        """Create a Signal Output Single-Point session.

        This function creates a Signal Output Single-Point session using the named
        references to database objects.

        Args:
            interface_name: A string representing the XNET Interface to use for
                this session.
            database_name: A string representing the XNET database to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name: A string representing the XNET cluster to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the signals parameter.
            signals: A list of strings describing signals for the session. The
                list syntax is as follows:

                    List contains one or more XNET Signal names. Each name must
                    be one of the following options, whichever uniquely
                    identifies a signal within the database given:

                        -<Signal>
                        -<Frame>.<Signal>
                        -<Cluster>.<Frame>.<Signal>
                        -<PDU>.<Signal>
                        -<Cluster>.<PDU>.<Signal>

                    List may also contain one or more trigger signals. For
                    information about trigger signals, refer to Signal Output
                    Single-Point Mode or Signal Output Single-Point Mode.

        Returns:
            A Signal Output Single-Point session object.
        """
        flattened_list = _utils.flatten_items(signals)
        base.SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface_name,
            constants.CreateSessionMode.SIGNAL_OUT_SINGLE_POINT)
        self._signals = session_signals.SinglePointOutSignals(self._handle)

    @property
    def signals(self):
        return self._signals


def create_session_by_ref(
        database_refs,
        interface_name,
        mode):
    return _funcs.nx_create_session_by_ref(database_refs, interface_name, mode)


def read_signal_waveform(
        session_ref,
        timeout,
        start_time,
        delta_time,
        value_buffer,
        size_of_value_buffer,
        number_of_values_returned):
    raise NotImplementedError("Placeholder")


def read_signal_xy(
        session_ref,
        time_limit,
        value_buffer,
        size_of_value_buffer,
        timestamp_buffer,
        size_of_timestamp_buffer,
        num_pairs_buffer,
        size_of_num_pairs_buffer):
    raise NotImplementedError("Placeholder")


def read_state(
        session_ref,
        state_id,
        state_size,
        state_value,
        fault):
    raise NotImplementedError("Placeholder")


def write_state(
        session_ref,
        state_id,
        state_size,
        state_value):
    raise NotImplementedError("Placeholder")


def write_signal_waveform(
        session_ref,
        timeout,
        value_buffer):
    _funcs.nx_write_signal_waveform(session_ref, timeout, value_buffer)


def write_signal_xy(
        session_ref,
        timeout,
        value_buffer,
        timestamp_buffer,
        num_pairs_buffer):
    _funcs.nx_write_signal_xy(session_ref, timeout, value_buffer, timestamp_buffer, num_pairs_buffer)


def convert_frames_to_signals_single_point(
        session_ref,
        frame_buffer,
        number_of_bytes_for_frames,
        value_buffer,
        size_of_value_buffer,
        timestamp_buffer,
        size_of_timestamp_buffer):
    raise NotImplementedError("Placeholder")


def convert_signals_to_frames_single_point(
        session_ref,
        value_buffer,
        size_of_value_buffer,
        buffer,
        size_of_buffer,
        number_of_bytes_returned):
    raise NotImplementedError("Placeholder")
