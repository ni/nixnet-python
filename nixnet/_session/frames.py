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


class InFrames(Frames):
    """Frames in a session."""

    def __repr__(self):
        return 'Session.InFrames(handle={0})'.format(self._handle)

    def read_bytes(
            self,
            number_of_bytes_to_read,
            timeout=constants.TIMEOUT_NONE):
        """Read frames.

        Valid modes
        - Frame Input Stream Mode
        - Frame Input Queued Mode
        - Frame Input Single-Point Mode
        Frame: one or more
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadframe/
        """
        buffer, number_of_bytes_returned = _funcs.nx_read_frame(self._handle, number_of_bytes_to_read, timeout)
        return buffer[0:number_of_bytes_returned]

    def read_raw(
            self,
            number_to_read,
            timeout=constants.TIMEOUT_NONE):
        """Read frames.

        Valid modes
        - Frame Input Stream Mode
        - Frame Input Queued Mode
        - Frame Input Single-Point Mode
        Frame: one or more
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadframe/
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
        """Read frames.

        Valid modes
        - Frame Input Stream Mode
        - Frame Input Queued Mode
        - Frame Input Single-Point Mode
        Frame: one or more
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadframe/
        """
        for frame in self.read_raw(number_to_read, timeout):
            yield types.CanFrame.from_raw(frame)


class SinglePointInFrames(Frames):
    """Frames in a session."""

    def __repr__(self):
        return 'Session.SinglePointInFrames(handle={0})'.format(self._handle)

    def read_bytes(
            self,
            number_of_bytes_to_read,
            timeout=constants.TIMEOUT_NONE):
        """Read frames.

        Valid modes
        - Frame Input Stream Mode
        - Frame Input Queued Mode
        - Frame Input Single-Point Mode
        Frame: one or more
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadframe/
        """
        buffer, number_of_bytes_returned = _funcs.nx_read_frame(self._handle, number_of_bytes_to_read, timeout)
        return buffer[0:number_of_bytes_returned]

    def read_raw(
            self,
            timeout=constants.TIMEOUT_NONE):
        """Read frames.

        Valid modes
        - Frame Input Stream Mode
        - Frame Input Queued Mode
        - Frame Input Single-Point Mode
        Frame: one or more
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadframe/
        """
        # NOTE: If the frame payload excedes the base unit, this will return
        # less than number_to_read
        number_to_read = len(self)
        number_of_bytes_to_read = number_to_read * _frames.nxFrameFixed_t.size
        buffer = self.read_bytes(number_of_bytes_to_read, timeout)
        for frame in _frames.iterate_frames(buffer):
            yield frame

    def read_can(
            self,
            number_to_read,
            timeout=constants.TIMEOUT_NONE):
        """Read frames.

        Valid modes
        - Frame Input Stream Mode
        - Frame Input Queued Mode
        - Frame Input Single-Point Mode
        Frame: one or more
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadframe/
        """
        for frame in self.read_raw(number_to_read, timeout):
            yield types.CanFrame.from_raw(frame)


class OutFrames(Frames):
    """Frames in a session."""

    def __repr__(self):
        return 'Session.OutFrames(handle={0})'.format(self._handle)

    def write_bytes(
            self,
            frame_bytes,
            timeout=10):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwriteframe/"
        _funcs.nx_write_frame(self._handle, bytes(frame_bytes), timeout)

    def write_raw(
            self,
            raw_frames,
            timeout=10):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwriteframe/"
        units = itertools.chain.from_iterable(
            _frames.serialize_frame(frame)
            for frame in raw_frames)
        bytes = b"".join(units)
        self.write_bytes(bytes, timeout)

    def write_can(
            self,
            can_frames,
            timeout=10):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwriteframe/"
        raw_frames = (frame.to_raw() for frame in can_frames)
        self.write_raw(raw_frames, timeout)


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
