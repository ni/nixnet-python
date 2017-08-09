from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools
import typing  # NOQA: F401

from nixnet import _frames
from nixnet import _funcs
from nixnet import _props
from nixnet._session import collection
from nixnet import constants
from nixnet import types


class Frames(collection.Collection):
    """Frames in a session."""

    def __repr__(self):
        return 'Session.Frames(handle={0})'.format(self._handle)

    def _create_item(self, handle, index, name):
        return Frame(handle, index, name)

    @property
    def payld_len_max(self):
        # type: () -> int
        """int: Returns the maximum payload length of all frames in this session, expressed as bytes (0-254).

        For CAN Stream (Input and Output), this property depends on the XNET
        Cluster CAN I/O Mode property. If the I/O mode is
        `constants.CanIoMode.CAN`, this property is 8 bytes. If the I/O mode is
        'constants.CanIoMode.CAN_FD' or 'constants.CanIoMode.CAN_FD_BRS', this
        property is 64 bytes.

        For LIN Stream (Input and Output), this property always is 8 bytes.

        For FlexRay Stream (Input and Output), this property is the same as the
        XNET Cluster FlexRay Payload Length Maximum property value.

        For Queued and Single-Point (Input and Output), this is the maximum
        payload of all frames specified in the List property.
        """
        return _props.get_session_payld_len_max(self._handle)


class InFrames(Frames):
    """Frames in a session."""

    def __repr__(self):
        return 'Session.InFrames(handle={0})'.format(self._handle)

    def read_bytes(
            self,
            num_bytes,
            timeout=constants.TIMEOUT_NONE):
        # type: (int, float) -> bytes
        """Read data as a list of raw bytes (frame data).

        The raw bytes encode one or more frames using the Raw Frame Format.

        Args:
            num_bytes(int): The number of bytes to read.
            timeout(float): The time in seconds to wait for number to read
                frame bytes to become available.

                To avoid returning a partial frame, even when
                'num_bytes' are available from the hardware, this
                read may return fewer bytes in buffer. For example, assume you
                pass 'num_bytes' 70 bytes and 'timeout' of 10
                seconds. During the read, two frames are received, the first 24
                bytes in size, and the second 56 bytes in size, for a total of
                80 bytes. The read returns after the two frames are received,
                but only the first frame is copied to data. If the read copied
                46 bytes of the second frame (up to the limit of 70), that frame
                would be incomplete and therefore difficult to interpret. To
                avoid this problem, the read always returns complete frames in
                buffer.

                If 'timeout' is positive, this function waits for
                'num_bytes' frame bytes to be received, then
                returns complete frames up to that number. If the bytes do not
                arrive prior to the 'timeout', an error is returned.

                If 'timeout' is 'constants.TIMEOUT_INFINITE', this
                function waits indefinitely for 'num_bytes' frame bytes.

                If 'timeout' is 'constants.TIMEOUT_NONE', this
                function does not wait and immediately returns all available
                frame bytes up to the limit 'num_bytes' specifies.

        Returns:
            A list of raw bytes representing the data.
        """
        buffer, number_of_bytes_returned = _funcs.nx_read_frame(self._handle, num_bytes, timeout)
        return buffer[0:number_of_bytes_returned]

    def read(
            self,
            num_frames,
            timeout=constants.TIMEOUT_NONE,
            frame_type=types.XnetFrame):
        # type: (int, float, typing.Type[types.FrameFactory]) -> typing.Iterable[types.Frame]
        """Read frames.

        Args:
            num_frames(int): Number of frames to read.
            timeout(float): The time in seconds to wait for number to read
                frame bytes to become available.

                If 'timeout' is positive, this function waits for
                'num_frames' frames to be received, then
                returns complete frames up to that number. If the frames do not
                arrive prior to the 'timeout', an error is returned.

                If 'timeout' is 'constants.TIMEOUT_INFINITE', this function
                waits indefinitely for 'num_frames' frames.

                If 'timeout' is 'constants.TIMEOUT_NONE', this function does not
                wait and immediately returns all available frames up to the
                limit 'num_frames' specifies.
            frame_type(:any:`nixnet.types.FrameFactory`): A factory for the
                desired frame formats.

        Yields:
            :any:`nixnet.types.Frame`
        """
        from_raw = typing.cast(typing.Callable[[types.RawFrame], types.Frame], frame_type.from_raw)
        # NOTE: If the frame payload exceeds the base unit, this will return
        # less than num_frames
        num_bytes = num_frames * _frames.nxFrameFixed_t.size
        buffer = self.read_bytes(num_bytes, timeout)
        for frame in _frames.iterate_frames(buffer):
            yield from_raw(frame)


class SinglePointInFrames(Frames):
    """Frames in a session."""

    def __repr__(self):
        return 'Session.SinglePointInFrames(handle={0})'.format(self._handle)

    def read_bytes(
            self,
            num_bytes):
        # type: (int) -> bytes
        """Read data as a list of raw bytes (frame data).

        Args:
            num_bytes(int): Number of bytes to read.

        Returns:
            bytes: Raw bytes representing the data.
        """
        buffer, number_of_bytes_returned = _funcs.nx_read_frame(
            self._handle,
            num_bytes,
            constants.TIMEOUT_NONE)
        return buffer[0:number_of_bytes_returned]

    def read(
            self,
            frame_type=types.XnetFrame):
        # type: (typing.Type[types.FrameFactory]) -> typing.Iterable[types.Frame]
        """Read frames.

        Args:
            frame_type(:any:`nixnet.types.FrameFactory`): A factory for the
                desired frame formats.

        Yields:
            :any:`nixnet.types.Frame`
        """
        from_raw = typing.cast(typing.Callable[[types.RawFrame], types.Frame], frame_type.from_raw)
        # NOTE: If the frame payload exceeds the base unit, this will return
        # less than num_frames
        num_frames = len(self)
        num_bytes = num_frames * _frames.nxFrameFixed_t.size
        buffer = self.read_bytes(num_bytes)
        for frame in _frames.iterate_frames(buffer):
            yield from_raw(frame)


class OutFrames(Frames):
    """Frames in a session."""

    def __repr__(self):
        return 'Session.OutFrames(handle={0})'.format(self._handle)

    def write_bytes(
            self,
            frame_bytes,
            timeout=10):
        # type: (bytes, float) -> None
        """Write a list of raw bytes (frame data).

        The raw bytes encode one or more frames using the Raw Frame Format.

        Args:
            frame_bytes(bytes): Frames to transmit.
            timeout(float): The time in seconds to wait for number to read
                frame bytes to become available.

                If 'timeout' is positive, this function waits up to that 'timeout'
                for space to become available in queues. If the space is not
                available prior to the 'timeout', a 'timeout' error is returned.

                If 'timeout' is 'constants.TIMEOUT_INFINITE', this functions
                waits indefinitely for space to become available in queues.

                If 'timeout' is 'constants.TIMEOUT_NONE', this function does not
                wait and immediately returns with a 'timeout' error if all data
                cannot be queued. Regardless of the 'timeout' used, if a 'timeout'
                error occurs, none of the data is queued, so you can attempt to
                call this function again at a later time with the same data.
        """
        _funcs.nx_write_frame(self._handle, bytes(frame_bytes), timeout)

    def write(
            self,
            frames,
            timeout=10):
        # type: (typing.Iterable[types.Frame], float) -> None
        """Write frame data.

        Args:
            frames(list of float): One or more :any:`nixnet.types.Frame` objects to be
                written to the session.
            timeout(float): The time in seconds to wait for number to read
                frame bytes to become available.

                If 'timeout' is positive, this function waits up to that 'timeout'
                for space to become available in queues. If the space is not
                available prior to the 'timeout', a 'timeout' error is returned.

                If 'timeout' is 'constants.TIMEOUT_INFINITE', this functions
                waits indefinitely for space to become available in queues.

                If 'timeout' is 'constants.TIMEOUT_NONE', this function does not
                wait and immediately returns with a 'timeout' error if all data
                cannot be queued. Regardless of the 'timeout' used, if a 'timeout'
                error occurs, none of the data is queued, so you can attempt to
                call this function again at a later time with the same data.
        """
        units = itertools.chain.from_iterable(
            _frames.serialize_frame(frame.to_raw())
            for frame in frames)
        bytes = b"".join(units)
        self.write_bytes(bytes, timeout)


class SinglePointOutFrames(Frames):
    """Frames in a session."""

    def __repr__(self):
        return 'Session.SinglePointOutFrames(handle={0})'.format(self._handle)

    def write_bytes(
            self,
            frame_bytes):
        # type: (bytes) -> None
        """Write a list of raw bytes (frame data).

        The raw bytes encode one or more frames using the Raw Frame Format.

        Args:
            frame_bytes(bytes): Frames to transmit.
        """
        _funcs.nx_write_frame(self._handle, bytes(frame_bytes), constants.TIMEOUT_NONE)

    def write(
            self,
            frames):
        # type: (typing.Iterable[types.Frame]) -> None
        """Write frame data.

        Args:
            frames(list of float): One or more :any:`nixnet.types.Frame` objects to be
                written to the session.
        """
        units = itertools.chain.from_iterable(
            _frames.serialize_frame(frame.to_raw())
            for frame in frames)
        bytes = b"".join(units)
        self.write_bytes(bytes)


class Frame(collection.Item):
    """Frame configuration for a session."""

    def __repr__(self):
        return 'Session.Frame(handle={0}, index={0})'.format(self._handle, self._index)

    def set_can_start_time_off(self, offset):
        # type: (float) -> None
        """Set CAN Start Time Offset.

        Use this function to have more control over the schedule of frames on
        the bus, to offer more determinism by configuring cyclic frames to be
        spaced evenly.

        If you do not call this function or you set it to a negative number,
        NI-XNET chooses this start time offset based on the arbitration
        identifier and periodic transmit time.

        ``offset`` takes effect whenever a session is started. If you stop a
        session and restart it, the start time offset is re-evaluated.

        Args:
            offset(float): The amount of time that must elapse between the
                session being started and the time that the first frame is
                transmitted across the bus. This is different than the cyclic
                rate, which determines the time between subsequent frame
                transmissions.
        """
        _props.set_session_can_start_time_off(self._handle, self._index, offset)

    def set_can_tx_time(self, time):
        # type: (float) -> None
        """Set CAN Transmit Time.

        If you call this function while a frame object is currently started, the
        frame object is stopped, the cyclic rate updated, and then the frame
        object is restarted. Because of the stopping and starting, the frame's
        start time offset is re-evaluated.

        The first time a queued frame object is started, the XNET frame's
        transmit time determines the object's default queue size. Changing this
        rate has no impact on the queue size. Depending on how you change the
        rate, the queue may not be sufficient to store data for an extended
        period of time. You can mitigate this by setting the session Queue Size
        property to provide sufficient storage for all rates you use. If you are
        using a single-point session, this is not relevant.

        Args:
            time(float): Frame's transmit time while the session is running.
                The transmit time is the amount of time that must elapse
                between subsequent transmissions of a cyclic frame. The default
                value of this property comes from the database (the XNET Frame
                CAN Transmit Time property).
        """
        _props.set_session_can_tx_time(self._handle, self._index, time)

    def set_skip_n_cyclic_frames(self, n):
        # type: (int) -> None
        """Set Skip N Cyclic Frames

        When the frame's transmission time arrives and the skip count is
        nonzero, a frame value is dequeued (if this is not a single-point
        session), and the skip count is decremented, but the frame actually is
        not transmitted across the bus. When the skip count decrements to zero,
        subsequent cyclic transmissions resume.

        This function is useful for testing of ECU behavior when a cyclic frame
        is expected, but is missing for N cycles.

        .. note:: Only CAN interfaces currently support this function.

        .. note:: This property is valid only for output sessions and frames
            with cyclic timing (that is, not event-based frames).

        Args:
            n(int): Skip the next N cyclic frames when nonzero.
        """
        _props.set_session_skip_n_cyclic_frames(self._handle, self._index, n)

    def set_lin_tx_n_corrupted_chksums(self, n):
        # type: (int) -> None
        """Set LIN Transmit N Corrupted Checksums.

        When set to a nonzero value, this function causes the next N number of
        checksums to be corrupted. The checksum is corrupted by negating the
        value calculated per the database; (EnhancedValue * -1) or
        (ClassicValue * -1).

        If the frame is transmitted in an unconditional or sporadic schedule
        slot, N is always decremented for each frame transmission. If the frame
        is transmitted in an event-triggered slot and a collision occurs, N is
        not decremented. In that case, N is decremented only when the collision
        resolving schedule is executed and the frame is successfully
        transmitted.  If the frame is the only one to transmit in the
        event-triggered slot (no collision), N is decremented at
        event-triggered slot time.

        This function is useful for testing ECU behavior when a corrupted
        checksum is transmitted.

        .. note:: This function is valid only for output sessions.

        Args:
            n(int): Number of checksums to be corrupted.
        """
        _props.set_session_lin_tx_n_corrupted_chksums(self._handle, self._index, n)

    def set_j1939_addr_filter(self, address=""):
        # type: (typing.Union[typing.Text, int]) -> None
        """Set J1939 Address Filter.

        Define a filter for the source address of the PGN transmitting node.
        You can use it when multiple nodes with different addresses are
        transmitting the same PGN.

        If the filter is active, the session accepts only frames transmitted by
        a node with the defined address. All other frames with the same PGN but
        transmitted by other nodes are ignored.

        .. note:: You can use this function in input sessions only.

        Args:
            address(str or int): Decimal value of the address. Leave blank to
                reset the filter.
        """
        _props.set_session_j1939_addr_filter(self._handle, self._index, str(address))
