from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import warnings

from nixnet import _props
from nixnet import constants
from nixnet import errors


class Session(object):

    def __init__(
            self,
            database_name,
            cluster_name,
            list,
            interface,
            mode):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesession/"
        # What about http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesessionbyref/
        # Store sessionRef as a member variable
        raise NotImplementedError("Placeholder")

    def __del__(self):
        if self._handle is not None:
            warnings.warn(
                'Session was not explicitly closed before it was destructed. '
                'Resources on the device may still be reserved.',
                errors.XnetResourceWarning)

    def __enter__(self):
        return self

    def __exit__(self):
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

        raise NotImplementedError("Placeholder")

        self._handle = None

    def read_frame(
            self,
            number_to_read=constants.READ_ALL_AVAILABLE,
            timeout=constants.TIMEOUT_NONE):
        """Read frames.

        Valid modes
        - Frame Input Stream Mode
        - Frame Input Queued Mode
        - Frame Input Single-Point Mode
        Frame: one or more
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadframe/
        """
        raise NotImplementedError("Placeholder")

    @property
    def intf_baud_rate(self):
        return _props.get_session_intf_baud_rate(self._handle)

    @intf_baud_rate.setter
    def intf_baud_rate(self, value):
        _props.set_session_intf_baud_rate(self._handle, value)


def create_session_by_ref(
        number_of_database_ref,
        array_of_database_ref,
        interface,
        mode,
        session_ref):
    raise NotImplementedError("Placeholder")


def get_sub_property(
        session_ref,
        active_index,
        property_id,
        property_size,
        property_value):
    raise NotImplementedError("Placeholder")


def get_sub_property_size(
        session_ref,
        active_index,
        property_id,
        property_size):
    raise NotImplementedError("Placeholder")


def set_sub_property(
        session_ref,
        active_index,
        property_id,
        property_size,
        property_value):
    raise NotImplementedError("Placeholder")


def read_signal_single_point(
        session_ref,
        value_buffer,
        size_of_value_buffer,
        timestamp_buffer,
        size_of_timestamp_buffer):
    raise NotImplementedError("Placeholder")


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


def write_frame(
        session_ref,
        buffer,
        number_of_bytes_for_frames,
        timeout):
    raise NotImplementedError("Placeholder")


def write_signal_single_point(
        session_ref,
        value_buffer,
        size_of_value_buffer):
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
        value_buffer,
        size_of_value_buffer):
    raise NotImplementedError("Placeholder")


def write_signal_xy(
        session_ref,
        timeout,
        value_buffer,
        size_of_value_buffer,
        timestamp_buffer,
        size_of_timestamp_buffer,
        num_pairs_buffer,
        size_of_num_pairs_buffer):
    raise NotImplementedError("Placeholder")


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


def blink(
        interface_ref,
        modifier):
    raise NotImplementedError("Placeholder")


def clear(
        session_ref):
    raise NotImplementedError("Placeholder")


def connect_terminals(
        session_ref,
        source,
        destination):
    raise NotImplementedError("Placeholder")


def disconnect_terminals(
        session_ref,
        source,
        destination):
    raise NotImplementedError("Placeholder")


def flush(
        session_ref):
    raise NotImplementedError("Placeholder")


def start(
        session_ref,
        scope):
    raise NotImplementedError("Placeholder")


def stop(
        session_ref,
        scope):
    raise NotImplementedError("Placeholder")


def status_to_string(
        status,
        sizeof_string,
        status_description):
    raise NotImplementedError("Placeholder")


def system_open(
        system_ref):
    raise NotImplementedError("Placeholder")


def system_close(
        system_ref):
    raise NotImplementedError("Placeholder")


def wait(
        session_ref,
        condition,
        param_in,
        timeout,
        param_out):
    raise NotImplementedError("Placeholder")
