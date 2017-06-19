from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes

from nixnet import _ctypedefs
from nixnet import _lib


class XnetLibrary(object):

    def __init__(self: XnetLibrary) -> None:
        ...

    @property
    def cdll(self: XnetLibrary) -> _lib.XnetLibrary:
        ...

    def nx_create_session(
            self: XnetLibrary,
            database_name: _ctypedefs.char_p,
            cluster_name: _ctypedefs.char_p,
            list: _ctypedefs.char_p,
            interface: _ctypedefs.char_p,
            mode: _ctypedefs.u32,
            session_ref: ctypes.POINTER(_ctypedefs.nxSessionRef_t)) -> _ctypedefs.nxStatus_t:
        ...

    def nx_create_session_by_ref(
            self: XnetLibrary,
            size_of_database_refs: _ctypedefs.u32,
            database_refs: ctypes.POINTER(_ctypedefs.nxDatabaseRef_t),
            interface: _ctypedefs.char_p,
            mode: _ctypedefs.u32,
            session_ref: ctypes.POINTER(_ctypedefs.nxSessionRef_t)) -> _ctypedefs.nxStatus_t:
        ...

    def nx_get_property(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            property_id: _ctypedefs.u32,
            property_size: _ctypedefs.u32,
            property_value: _ctypedefs.nxVoidPtr) -> _ctypedefs.nxStatus_t:
        ...

    def nx_get_property_size(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            property_id: _ctypedefs.u32,
            property_size: ctypes.POINTER(_ctypedefs.u32)) -> _ctypedefs.nxStatus_t:
        ...

    def nx_set_property(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            property_id: _ctypedefs.u32,
            property_size: _ctypedefs.u32,
            property_value: _ctypedefs.nxVoidPtr) -> _ctypedefs.nxStatus_t:
        ...

    def nx_get_sub_property(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            active_index: _ctypedefs.u32,
            property_id: _ctypedefs.u32,
            property_size: _ctypedefs.u32,
            property_value: _ctypedefs.nxVoidPtr) -> _ctypedefs.nxStatus_t:
        ...

    def nx_get_sub_property_size(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            active_index: _ctypedefs.u32,
            property_id: _ctypedefs.u32,
            property_size: ctypes.POINTER(_ctypedefs.u32)) -> _ctypedefs.nxStatus_t:
        ...

    def nx_set_sub_property(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            active_index: _ctypedefs.u32,
            property_id: _ctypedefs.u32,
            property_size: _ctypedefs.u32,
            property_value: _ctypedefs.nxVoidPtr) -> _ctypedefs.nxStatus_t:
        ...

    def nx_read_frame(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            buffer,
            size_of_buffer: _ctypedefs.u32,
            timeout: _ctypedefs.f64,
            number_of_bytes_returned: ctypes.POINTER(_ctypedefs.u32)) -> _ctypedefs.nxStatus_t:
        ...

    def nx_read_signal_single_point(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            value_buffer: ctypes.POINTER(_ctypedefs.f64),
            size_of_value_buffer: _ctypedefs.u32,
            timestamp_buffer: ctypes.POINTER(_ctypedefs.nxTimestamp_t),
            size_of_timestamp_buffer: _ctypedefs.u32) -> _ctypedefs.nxStatus_t:
        ...

    def nx_read_signal_waveform(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            timeout: _ctypedefs.f64,
            start_time: ctypes.POINTER(_ctypedefs.nxTimestamp_t),
            delta_time: ctypes.POINTER(_ctypedefs.f64),
            value_buffer: ctypes.POINTER(_ctypedefs.f64),
            size_of_value_buffer: _ctypedefs.u32,
            number_of_values_returned: ctypes.POINTER(_ctypedefs.u32)) -> _ctypedefs.nxStatus_t:
        ...

    def nx_read_signal_xy(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            time_limit: ctypes.POINTER(_ctypedefs.nxTimestamp_t),
            value_buffer: ctypes.POINTER(_ctypedefs.f64),
            size_of_value_buffer: _ctypedefs.u32,
            timestamp_buffer: ctypes.POINTER(_ctypedefs.nxTimestamp_t),
            size_of_timestamp_buffer: _ctypedefs.u32,
            num_pairs_buffer: ctypes.POINTER(_ctypedefs.u32),
            size_of_num_pairs_buffer: _ctypedefs.u32) -> _ctypedefs.nxStatus_t:
        ...

    def nx_read_state(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            state_id: _ctypedefs.u32,
            state_size: _ctypedefs.u32,
            state_value: _ctypedefs.nxVoidPtr,
            fault: ctypes.POINTER(_ctypedefs.nxStatus_t)) -> _ctypedefs.nxStatus_t:
        ...

    def nx_write_frame(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            buffer: _ctypedefs.nxVoidPtr,
            number_of_bytes_for_frames: _ctypedefs.u32,
            timeout: _ctypedefs.f64) -> _ctypedefs.nxStatus_t:
        ...

    def nx_write_signal_single_point(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            value_buffer: ctypes.POINTER(_ctypedefs.f64),
            size_of_value_buffer: _ctypedefs.u32) -> _ctypedefs.nxStatus_t:
        ...

    def nx_write_state(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            state_id: _ctypedefs.u32,
            state_size: _ctypedefs.u32,
            state_value: _ctypedefs.nxVoidPtr) -> _ctypedefs.nxStatus_t:
        ...

    def nx_write_signal_waveform(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            timeout: _ctypedefs.f64,
            value_buffer: ctypes.POINTER(_ctypedefs.f64),
            size_of_value_buffer: _ctypedefs.u32) -> _ctypedefs.nxStatus_t:
        ...

    def nx_write_signal_xy(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            timeout: _ctypedefs.f64,
            value_buffer: ctypes.POINTER(_ctypedefs.f64),
            size_of_value_buffer: _ctypedefs.u32,
            timestamp_buffer: ctypes.POINTER(_ctypedefs.nxTimestamp_t),
            size_of_timestamp_buffer: _ctypedefs.u32,
            num_pairs_buffer: ctypes.POINTER(_ctypedefs.u32),
            size_of_num_pairs_buffer: _ctypedefs.u32) -> _ctypedefs.nxStatus_t:
        ...

    def nx_convert_frames_to_signals_single_point(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            frame_buffer: _ctypedefs.nxVoidPtr,
            number_of_bytes_for_frames: _ctypedefs.u32,
            value_buffer: ctypes.POINTER(_ctypedefs.f64),
            size_of_value_buffer: _ctypedefs.u32,
            timestamp_buffer: ctypes.POINTER(_ctypedefs.nxTimestamp_t),
            size_of_timestamp_buffer: _ctypedefs.u32) -> _ctypedefs.nxStatus_t:
        ...

    def nx_blink(
            self: XnetLibrary,
            interface_ref: _ctypedefs.nxSessionRef_t,
            modifier: _ctypedefs.u32) -> _ctypedefs.nxStatus_t:
        ...

    def nx_clear(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t) -> _ctypedefs.nxStatus_t:
        ...

    def nx_connect_terminals(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            source: _ctypedefs.char_p,
            destination: _ctypedefs.char_p) -> _ctypedefs.nxStatus_t:
        ...

    def nx_disconnect_terminals(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            source: _ctypedefs.char_p,
            destination: _ctypedefs.char_p) -> _ctypedefs.nxStatus_t:
        ...

    def nx_flush(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t) -> _ctypedefs.nxStatus_t:
        ...

    def nx_start(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            scope: _ctypedefs.u32) -> _ctypedefs.nxStatus_t:
        ...

    def nx_stop(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            scope: _ctypedefs.u32) -> _ctypedefs.nxStatus_t:
        ...

    def nx_status_to_string(
            self: XnetLibrary,
            status: _ctypedefs.nxStatus_t,
            size_of_status_description: _ctypedefs.u32,
            status_description: _ctypedefs.char_p) -> None:
        ...

    def nx_system_open(
            self: XnetLibrary,
            system_ref: ctypes.POINTER(_ctypedefs.nxSessionRef_t)) -> _ctypedefs.nxStatus_t:
        ...

    def nx_system_close(
            self: XnetLibrary,
            system_ref: _ctypedefs.nxSessionRef_t) -> _ctypedefs.nxStatus_t:
        ...

    def nx_wait(
            self: XnetLibrary,
            session_ref: _ctypedefs.nxSessionRef_t,
            condition: _ctypedefs.u32,
            param_in: _ctypedefs.u32,
            timeout: _ctypedefs.f64,
            param_out: ctypes.POINTER(_ctypedefs.u32)) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_open_database(
            self: XnetLibrary,
            database_name: _ctypedefs.char_p,
            database_ref: ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_close_database(
            self: XnetLibrary,
            database_ref: _ctypedefs.nxDatabaseRef_t,
            close_all_refs: _ctypedefs.bool32) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_create_object(
            self: XnetLibrary,
            parent_object_ref: _ctypedefs.nxDatabaseRef_t,
            object_class: _ctypedefs.u32,
            object_name: _ctypedefs.char_p,
            db_object_ref: ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_find_object(
            self: XnetLibrary,
            parent_object_ref: _ctypedefs.nxDatabaseRef_t,
            object_class: _ctypedefs.u32,
            object_name: _ctypedefs.char_p,
            db_object_ref: ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_delete_object(
            self: XnetLibrary,
            db_object_ref: _ctypedefs.nxDatabaseRef_t) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_save_database(
            self: XnetLibrary,
            database_ref: _ctypedefs.nxDatabaseRef_t,
            db_filepath: _ctypedefs.char_p) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_get_property(
            self: XnetLibrary,
            db_object_ref: _ctypedefs.nxDatabaseRef_t,
            property_id: _ctypedefs.u32,
            property_size: _ctypedefs.u32,
            property_value: _ctypedefs.nxVoidPtr) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_get_property_size(
            self: XnetLibrary,
            db_object_ref: _ctypedefs.nxDatabaseRef_t,
            property_id: _ctypedefs.u32,
            property_size: ctypes.POINTER(_ctypedefs.u32)) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_set_property(
            self: XnetLibrary,
            db_object_ref: _ctypedefs.nxDatabaseRef_t,
            property_id: _ctypedefs.u32,
            property_size: _ctypedefs.u32,
            property_value: _ctypedefs.nxVoidPtr) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_get_dbc_attribute_size(
            self: XnetLibrary,
            db_object_ref: _ctypedefs.nxDatabaseRef_t,
            mode: _ctypedefs.u32,
            attribute_name: _ctypedefs.char_p,
            attribute_text_size: ctypes.POINTER(_ctypedefs.u32)) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_get_dbc_attribute(
            self: XnetLibrary,
            db_object_ref: _ctypedefs.nxDatabaseRef_t,
            mode: _ctypedefs.u32,
            attribute_name: _ctypedefs.char_p,
            attribute_text_size: _ctypedefs.u32,
            attribute_text: _ctypedefs.char_p,
            is_default: ctypes.POINTER(_ctypedefs.u32)) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_merge(
            self: XnetLibrary,
            target_cluster_ref: _ctypedefs.nxDatabaseRef_t,
            source_obj_ref: _ctypedefs.nxDatabaseRef_t,
            copy_mode: _ctypedefs.u32,
            prefix: _ctypedefs.char_p,
            wait_for_complete: _ctypedefs.bool32,
            percent_complete: ctypes.POINTER(_ctypedefs.u32)) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_add_alias(
            self: XnetLibrary,
            database_alias: _ctypedefs.char_p,
            database_filepath: _ctypedefs.char_p,
            default_baud_rate: _ctypedefs.u32) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_add_alias64(
            self: XnetLibrary,
            database_alias: _ctypedefs.char_p,
            database_filepath: _ctypedefs.char_p,
            default_baud_rate: _ctypedefs.u64) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_remove_alias(
            self: XnetLibrary,
            database_alias: _ctypedefs.char_p) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_deploy(
            self: XnetLibrary,
            ip_address: _ctypedefs.char_p,
            database_alias: _ctypedefs.char_p,
            wait_for_complete: _ctypedefs.bool32,
            percent_complete: ctypes.POINTER(_ctypedefs.u32)) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_undeploy(
            self: XnetLibrary,
            ip_address: _ctypedefs.char_p,
            database_alias: _ctypedefs.char_p) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_get_database_list(
            self: XnetLibrary,
            ip_address: _ctypedefs.char_p,
            size_of_alias_buffer: _ctypedefs.u32,
            alias_buffer: _ctypedefs.char_p,
            size_of_filepath_buffer: _ctypedefs.u32,
            filepath_buffer: _ctypedefs.char_p,
            number_of_databases: ctypes.POINTER(_ctypedefs.u32)) -> _ctypedefs.nxStatus_t:
        ...

    def nxdb_get_database_list_sizes(
            self: XnetLibrary,
            ip_address: _ctypedefs.char_p,
            size_of_alias_buffer: _ctypedefs.u32,
            sizeof_filepath_buffer: _ctypedefs.u32) -> _ctypedefs.nxStatus_t:
        ...
