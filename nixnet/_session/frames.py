from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import itertools

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


class InFrames(Frames):
    """Frames in a session."""

    def __repr__(self):
        return 'Session.InFrames(handle={0})'.format(self._handle)

    def read_bytes(
            self,
            number_of_bytes_to_read,
            timeout=constants.TIMEOUT_NONE):
        """Read data as a list of raw bytes (frame data).

        The raw bytes encode one or more frames using the Raw Frame Format.

        Args:
            number_of_bytes_to_read: An integer repesenting the number of bytes to read.
            timeout: The time to wait for number to read frame bytes to become
                available; the 'timeout' is represented as 64-bit floating-point
                in units of seconds.

                To avoid returning a partial frame, even when
                'number_of_bytes_to_read' are available from the hardware, this
                read may return fewer bytes in buffer. For example, assume you
                pass 'number_of_bytes_to_read' 70 bytes and 'timeout' of 10
                seconds. During the read, two frames are received, the first 24
                bytes in size, and the second 56 bytes in size, for a total of
                80 bytes. The read returns after the two frames are received,
                but only the first frame is copied to data. If the read copied
                46 bytes of the second frame (up to the limit of 70), that frame
                would be incomplete and therefore difficult to interpret. To
                avoid this problem, the read always returns complete frames in
                buffer.

                If 'timeout' is positive, this function waits for
                'number_of_bytes_to_read' frame bytes to be received, then
                returns complete frames up to that number. If the bytes do not
                arrive prior to the 'timeout', an error is returned.

                If 'timeout' is 'constants.TIMEOUT_INFINITE', this
                function waits indefinitely for 'number_of_bytes_to_read' frame bytes.

                If 'timeout' is 'constants.TIMEOUT_NONE', this
                function does not wait and immediately returns all available
                frame bytes up to the limit 'number_of_bytes_to_read' specifies.

        Returns:
            A list of raw bytes representing the data.
        """
        buffer, number_of_bytes_returned = _funcs.nx_read_frame(self._handle, number_of_bytes_to_read, timeout)
        return buffer[0:number_of_bytes_returned]

    def read_raw(
            self,
            number_to_read,
            timeout=constants.TIMEOUT_NONE):
        """Read raw CAN frames.

        Args:
            number_to_read: An integer repesenting the number of raw CAN frames
                to read.
            timeout: The time to wait for number to read frames to become
                available; the 'timeout' is represented as 64-bit floating-point
                in units of seconds.

                If 'timeout' is positive, this function waits for
                'number_to_read' frames to be received, then
                returns complete frames up to that number. If the frames do not
                arrive prior to the 'timeout', an error is returned.

                If 'timeout' is 'constants.TIMEOUT_INFINITE', this function
                waits indefinitely for 'number_to_read' frames.

                If 'timeout' is 'constants.TIMEOUT_NONE', this function does not
                wait and immediately returns all available frames up to the
                limit 'number_to_read' specifies.

        Yields:
            :any:`nixnet.types.RawFrame`
        """
        # NOTE: If the frame payload excedes the base unit, this will return
        # less than number_to_read
        number_of_bytes_to_read = number_to_read * _frames.nxFrameFixed_t.size
        buffer = self.read_bytes(number_of_bytes_to_read, timeout)
        for frame in _frames.iterate_frames(buffer):
            yield frame

    def read_can(
            self,
            number_to_read,
            timeout=constants.TIMEOUT_NONE):
        """Read :any:`nixnet.types.CanFrame` data.

        Args:
            number_to_read: An integer repesenting the number of CAN frames to read.
            timeout: The time to wait for number to read frames to become
                available; the 'timeout' is represented as 64-bit floating-point
                in units of seconds.

                If 'timeout' is positive, this function waits for
                'number_to_read' frames to be received, then
                returns complete frames up to that number. If the frames do not
                arrive prior to the 'timeout', an error is returned.

                If 'timeout' is 'constants.TIMEOUT_INFINITE', this function
                waits indefinitely for 'number_to_read' frames.

                If 'timeout' is 'constants.TIMEOUT_NONE', this function does not
                wait and immediately returns all available frames up to the
                limit 'number_to_read' specifies.
        Yields:
            :any:`nixnet.types.CanFrame`
        """
        for frame in self.read_raw(number_to_read, timeout):
            yield types.CanFrame.from_raw(frame)


class SinglePointInFrames(Frames):
    """Frames in a session."""

    def __repr__(self):
        return 'Session.SinglePointInFrames(handle={0})'.format(self._handle)

    def read_bytes(
            self,
            number_of_bytes_to_read):
        """Read data as a list of raw bytes (frame data).

        Args:
            number_of_bytes_to_read: An integer repesenting the number of bytes to read.

        Returns:
            A list of raw bytes representing the data.
        """
        buffer, number_of_bytes_returned = _funcs.nx_read_frame(
            self._handle,
            number_of_bytes_to_read,
            constants.TIMEOUT_NONE)
        return buffer[0:number_of_bytes_returned]

    def read_raw(self):
        """Read raw CAN frames.

        Yields:
            :any:`nixnet.types.RawFrame`
        """
        # NOTE: If the frame payload exceeds the base unit, this will return
        # less than number_to_read
        number_to_read = len(self)
        number_of_bytes_to_read = number_to_read * _frames.nxFrameFixed_t.size
        buffer = self.read_bytes(number_of_bytes_to_read)
        for frame in _frames.iterate_frames(buffer):
            yield frame

    def read_can(self):
        """Read :any:`nixnet.types.CanFrame` data.

        Yields:
            :any:`nixnet.types.CanFrame`
        """
        for frame in self.read_raw():
            yield types.CanFrame.from_raw(frame)


class OutFrames(Frames):
    """Frames in a session."""

    def __repr__(self):
        return 'Session.OutFrames(handle={0})'.format(self._handle)

    def write_bytes(
            self,
            frame_bytes,
            timeout=10):
        """Write a list of raw bytes (frame data).

        The raw bytes encode one or more frames using the Raw Frame Format.

        Args:
            frame_bytes: List of bytes, representing frames to transmit.
            timeout: The time to wait for the data to be queued up for transmit.
                The 'timeout' is represented as 64-bit floating-point in units of seconds.

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

    def write_raw(
            self,
            raw_frames,
            timeout=10):
        """Write raw CAN frame data.

        Args:
            raw_frames: One or more :any:`nixnet.types.RawFrame` objects to be
                written to the session.
            timeout: The time to wait for the data to be queued up for transmit.
                The 'timeout' is represented as 64-bit floating-point in units of seconds.

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
            _frames.serialize_frame(frame)
            for frame in raw_frames)
        bytes = b"".join(units)
        self.write_bytes(bytes, timeout)

    def write_can(
            self,
            can_frames,
            timeout=10):
        """Write CAN frame data.

        Args:
            can_frames: One or more :any:`nixnet.types.CanFrame` objects to be
                written to the session.
            timeout: The time to wait for the data to be queued up for transmit.
                The 'timeout' is represented as 64-bit floating-point in units of seconds.

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
        raw_frames = (frame.to_raw() for frame in can_frames)
        self.write_raw(raw_frames, timeout)


class SinglePointOutFrames(Frames):
    """Frames in a session."""

    def __repr__(self):
        return 'Session.SinglePointOutFrames(handle={0})'.format(self._handle)

    def write_bytes(
            self,
            frame_bytes):
        """Write a list of raw bytes (frame data).

        The raw bytes encode one or more frames using the Raw Frame Format.

        Args:
            frame_bytes: List of bytes, representing frames to transmit.
        """
        _funcs.nx_write_frame(self._handle, bytes(frame_bytes), constants.TIMEOUT_NONE)

    def write_raw(
            self,
            raw_frames):
        """Write raw CAN frame data.

        Args:
            raw_frames: A list of :any:`nixnet.types.RawFrame` objects to be
                written to the session.
        """
        units = itertools.chain.from_iterable(
            _frames.serialize_frame(frame)
            for frame in raw_frames)
        bytes = b"".join(units)
        self.write_bytes(bytes)

    def write_can(
            self,
            can_frames):
        """Write CAN frame data.

        Args:
            can_frames: A list of :any:`nixnet.types.CanFrame` objects to be
                written to the session.
        """
        raw_frames = (frame.to_raw() for frame in can_frames)
        self.write_raw(raw_frames)


class Frame(collection.Item):
    """Frame configuration for a session."""

    def __repr__(self):
        return 'Session.Frame(handle={0}, index={0})'.format(self._handle, self._index)

    def set_can_start_time_off(self, value):
        _props.set_session_can_start_time_off(self._handle, self._index, value)

    def set_can_tx_time(self, value):
        _props.set_session_can_tx_time(self._handle, self._index, value)

    def set_skip_n_cyclic_frames(self, value):
        _props.set_session_skip_n_cyclic_frames(self._handle, self._index, value)

    def set_output_queue_update_freq(self, value):
        _props.set_session_output_queue_update_freq(self._handle, self._index, value)

    def set_lin_tx_n_corrupted_chksums(self, value):
        _props.set_session_lin_tx_n_corrupted_chksums(self._handle, self._index, value)

    def set_j1939_addr_filter(self, value):
        _props.set_session_j1939_addr_filter(self._handle, self._index, value)
