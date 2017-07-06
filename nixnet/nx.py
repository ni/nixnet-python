from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import itertools
import warnings

from nixnet import _frames
from nixnet import _funcs
from nixnet import _props
from nixnet import constants
from nixnet import errors
from nixnet import types

from nixnet._session import frames
from nixnet._session import intf
from nixnet._session import j1939


class Session(object):

    def __init__(
            self,
            database_name,
            cluster_name,
            list,
            interface,
            mode):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesession/"
        self._handle = None  # To satisfy `__del__` in case nx_create_session throws
        self._handle = _funcs.nx_create_session(database_name, cluster_name, list, interface, mode)
        self._frames = frames.Frames(self._handle)
        self._intf = intf.Interface(self._handle)
        self._j1939 = j1939.J1939(self._handle)

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
            return self._handle == other._handle
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        return 'Session(handle={0})'.format(self._handle)

    def close(self):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxclear/"
        if self._handle is None:
            warnings.warn(
                'Attempting to close NI-XNET session but session was already '
                'closed', errors.XnetResourceWarning)
            return

        _funcs.nx_clear(self._handle)

        self._handle = None

    def start(self, scope):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxstart/"
        _funcs.nx_start(self._handle, scope)

    def read_frame_bytes(
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

    def read_raw_frame(
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
        buffer = self.read_frame_bytes(number_of_bytes_to_read, timeout)
        for frame in _frames.iterate_frames(buffer):
            yield frame

    def read_can_frame(
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
        for frame in self.read_raw_frame(number_to_read, timeout):
            yield types.CanFrame.from_raw(frame)

    def read_signal_single_point(
            self,
            num_signals):
        """Read signal single point.

        Valid modes
        - Single Input Single-Point
        Timestamps
        - Optional in C API
        - Timestamp per data point
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadsignalsinglepoint/
        """
        timestamps, values = _funcs.nx_read_signal_single_point(self._handle, num_signals)
        for timestamp, value in zip(timestamps, values):
            yield timestamp.value, value.value

    def write_frame_bytes(
            self,
            frame_bytes,
            timeout=10):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwriteframe/"
        _funcs.nx_write_frame(self._handle, bytes(frame_bytes), timeout)

    def write_raw_frame(
            self,
            raw_frames,
            timeout=10):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwriteframe/"
        units = itertools.chain.from_iterable(
            _frames.serialize_frame(frame)
            for frame in raw_frames)
        bytes = b"".join(units)
        self.write_frame_bytes(bytes, timeout)

    def write_can_frame(
            self,
            can_frames,
            timeout=10):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwriteframe/"
        raw_frames = (frame.to_raw() for frame in can_frames)
        self.write_raw_frame(raw_frames, timeout)

    def write_signal_single_point(
            self,
            value_buffer):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwritesignalsinglepoint/"
        _funcs.nx_write_signal_single_point(self._handle, value_buffer)

    @property
    def frames(self):
        return self._frames

    @property
    def intf(self):
        return self._intf

    @property
    def j1939(self):
        return self._j1939

    @property
    def application_protocol(self):
        return constants.AppProtocol(_props.get_session_application_protocol(self._handle))

    @property
    def auto_start(self):
        return _props.get_session_auto_start(self._handle)

    @auto_start.setter
    def auto_start(self, value):
        _props.set_session_auto_start(self._handle, value)

    @property
    def cluster_name(self):
        return _props.get_session_cluster_name(self._handle)

    @property
    def database_name(self):
        return _props.get_session_database_name(self._handle)

    @property
    def list(self):
        return _props.get_session_list(self._handle)

    @property
    def mode(self):
        return constants.CreateSessionMode(_props.get_session_mode(self._handle))

    @property
    def num_frames(self):
        return _props.get_session_num_frames(self._handle)

    @property
    def num_in_list(self):
        return _props.get_session_num_in_list(self._handle)

    @property
    def num_pend(self):
        return _props.get_session_num_pend(self._handle)

    @property
    def num_unused(self):
        return _props.get_session_num_unused(self._handle)

    @property
    def payld_len_max(self):
        return _props.get_session_payld_len_max(self._handle)

    @property
    def protocol(self):
        return constants.Protocol(_props.get_session_protocol(self._handle))

    @property
    def queue_size(self):
        return _props.get_session_queue_size(self._handle)

    @queue_size.setter
    def queue_size(self, value):
        _props.set_session_queue_size(self._handle, value)

    @property
    def resamp_rate(self):
        return _props.get_session_resamp_rate(self._handle)

    @resamp_rate.setter
    def resamp_rate(self, value):
        _props.set_session_resamp_rate(self._handle, value)


def create_session_by_ref(
        database_refs,
        interface,
        mode):
    return _funcs.nx_create_session_by_ref(database_refs, interface, mode)


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


def clear(
        session_ref):
    _funcs.nx_clear(session_ref)


def connect_terminals(
        session_ref,
        source,
        destination):
    _funcs.nx_connect_terminals(session_ref, source, destination)


def disconnect_terminals(
        session_ref,
        source,
        destination):
    _funcs.nx_disconnect_terminals(session_ref, source, destination)


def flush(
        session_ref):
    _funcs.nx_flush(session_ref)


def stop(
        session_ref,
        scope):
    _funcs.nx_stop(session_ref, scope)


def wait(
        session_ref,
        condition,
        param_in,
        timeout):
    return _funcs.nx_wait(session_ref, condition, param_in, timeout)
