from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


def create_session(
        database_name,
        cluster_name,
        list,
        interface,
        mode,
        session_ref):
    raise NotImplementedError("Placeholder")


def create_session_by_ref(
        number_of_database_ref,
        array_of_database_ref,
        interface,
        mode,
        session_ref):
    raise NotImplementedError("Placeholder")


def get_property(
        session_ref,
        property_id,
        property_size,
        property_value):
    raise NotImplementedError("Placeholder")


def get_property_size(
        session_ref,
        property_id,
        property_size):
    raise NotImplementedError("Placeholder")


def set_property(
        session_ref,
        property_id,
        property_size,
        property_value):
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


def read_frame(
        session_ref,
        buffer,
        size_of_buffer,
        timeout,
        number_of_bytes_returned):
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
