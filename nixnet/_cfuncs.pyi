from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes

from nixnet import _ctypedefs
from nixnet import _lib


class XnetLibrary(object):

    def __init__(self) -> None:
        ...

    @property
    def cdll(self) -> _lib.XnetLibrary:
        ...

    def nx_create_session(
            self,
            database_name,
            cluster_name,
            list,
            interface,
            mode,
            session_ref) -> _ctypedefs.nxStatus_t:
        ...

    def nx_create_session_by_ref(
            self,
            number_of_database_ref,
            array_of_database_ref,
            interface,
            mode,
            session_ref) -> _ctypedefs.nxStatus_t:
        ...

    def nx_get_property(
            self,
            session_ref,
            property_id,
            property_size,
            property_value) -> _ctypedefs.nxStatus_t:
        ...

    def nx_get_property_size(
            self,
            session_ref,
            property_id,
            property_size) -> _ctypedefs.nxStatus_t:
        ...

    def nx_set_property(
            self,
            session_ref,
            property_id,
            property_size,
            property_value) -> _ctypedefs.nxStatus_t:
        ...

    def nx_get_sub_property(
            self,
            session_ref,
            active_index,
            property_id,
            property_size,
            property_value) -> _ctypedefs.nxStatus_t:
        ...

    def nx_get_sub_property_size(
            self,
            session_ref,
            active_index,
            property_id,
            property_size) -> _ctypedefs.nxStatus_t:
        ...

    def nx_set_sub_property(
            self,
            session_ref,
            active_index,
            property_id,
            property_size,
            property_value) -> _ctypedefs.nxStatus_t:
        ...

    def nx_read_frame(
            self,
            session_ref,
            buffer,
            size_of_buffer,
            timeout,
            number_of_bytes_returned) -> _ctypedefs.nxStatus_t:
        ...

    def nx_read_signal_single_point(
            self,
            session_ref,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer) -> _ctypedefs.nxStatus_t:
        ...

    def nx_read_signal_waveform(
            self,
            session_ref,
            timeout,
            start_time,
            delta_time,
            value_buffer,
            size_of_value_buffer,
            number_of_values_returned) -> _ctypedefs.nxStatus_t:
        ...

    def nx_read_signal_xy(
            self,
            session_ref,
            time_limit,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer,
            num_pairs_buffer,
            size_of_num_pairs_buffer) -> _ctypedefs.nxStatus_t:
        ...

    def nx_read_state(
            self,
            session_ref,
            state_id,
            state_size,
            state_value,
            fault) -> _ctypedefs.nxStatus_t:
        ...

    def nx_write_frame(
            self,
            session_ref,
            buffer,
            number_of_bytes_for_frames,
            timeout) -> _ctypedefs.nxStatus_t:
        ...

    def nx_write_signal_single_point(
            self,
            session_ref,
            value_buffer,
            size_of_value_buffer) -> _ctypedefs.nxStatus_t:
        ...

    def nx_write_state(
            self,
            session_ref,
            state_id,
            state_size,
            state_value) -> _ctypedefs.nxStatus_t:
        ...

    def nx_write_signal_waveform(
            self,
            session_ref,
            timeout,
            value_buffer,
            size_of_value_buffer) -> _ctypedefs.nxStatus_t:
        ...

    def nx_write_signal_xy(
            self,
            session_ref,
            timeout,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer,
            num_pairs_buffer,
            size_of_num_pairs_buffer) -> _ctypedefs.nxStatus_t:
        ...

    def nx_convert_frames_to_signals_single_point(
            self,
            session_ref,
            frame_buffer,
            number_of_bytes_for_frames,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer) -> _ctypedefs.nxStatus_t:
        ...

    def nx_convert_signals_to_frames_single_point(
            self,
            session_ref,
            value_buffer,
            size_of_value_buffer,
            buffer,
            size_of_buffer,
            number_of_bytes_returned) -> _ctypedefs.nxStatus_t:
        ...

    def nx_blink(
            self,
            interface_ref,
            modifier) -> _ctypedefs.nxStatus_t:
        ...

    def nx_clear(
            self,
            session_ref) -> _ctypedefs.nxStatus_t:
        ...

    def nx_connect_terminals(
            self,
            session_ref,
            source,
            destination) -> _ctypedefs.nxStatus_t:
        ...

    def nx_disconnect_terminals(
            self,
            session_ref,
            source,
            destination) -> _ctypedefs.nxStatus_t:
        ...

    def nx_flush(
            self,
            session_ref) -> _ctypedefs.nxStatus_t:
        ...

    def nx_start(
            self,
            session_ref,
            scope) -> _ctypedefs.nxStatus_t:
        ...

    def nx_stop(
            self,
            session_ref,
            scope) -> _ctypedefs.nxStatus_t:
        ...

    def nx_status_to_string(
            self,
            status,
            sizeof_string,
            status_description) -> None:
        ...

    def nx_system_open(
            self,
            system_ref) -> _ctypedefs.nxStatus_t:
        ...

    def nx_system_close(
            self,
            system_ref) -> _ctypedefs.nxStatus_t:
        ...

    def nx_wait(
            self,
            session_ref,
            condition,
            param_in,
            timeout,
            param_out) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_open_database(
            self,
            database_name,
            database_ref) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_close_database(
            self,
            database_ref,
            close_all_refs) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_create_object(
            self,
            parent_object_ref,
            object_class,
            object_name,
            db_object_ref) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_find_object(
            self,
            parent_object_ref,
            object_class,
            object_name,
            db_object_ref) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_delete_object(
            self,
            db_object_ref) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_save_database(
            self,
            database_ref,
            db_filepath) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_get_property(
            self,
            db_object_ref,
            property_id,
            property_size,
            property_value) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_get_property_size(
            self,
            db_object_ref,
            property_id,
            property_size) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_set_property(
            self,
            db_object_ref,
            property_id,
            property_size,
            property_value) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_get_dbc_attribute_size(
            self,
            db_object_ref,
            mode,
            attribute_name,
            attribute_text_size) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_get_dbc_attribute(
            self,
            db_object_ref,
            mode,
            attribute_name,
            attribute_text_size,
            attribute_text,
            is_default) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_merge(
            self,
            target_cluster_ref,
            source_obj_ref,
            copy_mode,
            prefix,
            wait_for_complete,
            percent_complete) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_add_alias(
            self,
            database_alias,
            database_filepath,
            default_baud_rate) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_add_alias64(
            self,
            database_alias,
            database_filepath,
            default_baud_rate) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_remove_alias(
            self,
            database_alias) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_deploy(
            self,
            ip_address,
            database_alias,
            wait_for_complete,
            percent_complete) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_undeploy(
            self,
            ip_address,
            database_alias) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_get_database_list(
            self,
            ip_address,
            sizeof_alias_buffer,
            alias_buffer,
            sizeof_filepath_buffer,
            filepath_buffer,
            number_of_databases) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_get_database_list_sizes(
            self,
            ip_address,
            sizeof_alias_buffer,
            sizeof_filepath_buffer) -> _ctypedefs.nxStatus_t:
        ...


lib = XnetLibrary()
