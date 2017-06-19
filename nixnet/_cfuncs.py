from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes  # type: ignore

from nixnet import _ctypedefs
from nixnet import _lib


class XnetLibrary(object):
    """NI-XNET C library

    This mostly serves to benefit testing by
    - Delay loading the DLL so we can import this without it being loaded.
    - Provide a mockable interface for verifying how we use ctypes
    """

    def __init__(self):
        self._cdll = None

    @property
    def cdll(self):
        if self._cdll is None:
            self._cdll = _lib.import_lib()
        return self._cdll

    def nx_create_session(
            self,
            database_name,
            cluster_name,
            list,
            interface,
            mode,
            session_ref):
        cfunc = self.cdll.nxCreateSession
        cfunc.argtypes = [
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.char),
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.nxSessionRef_t)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            database_name,
            cluster_name,
            list,
            interface,
            mode,
            session_ref)

    def nx_create_session_by_ref(
            self,
            number_of_database_ref,
            array_of_database_ref,
            interface,
            mode,
            session_ref):
        cfunc = self.cdll.nxCreateSessionByRef
        cfunc.argtypes = [
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.nxDatabaseRef_t),
            ctypes.POINTER(_ctypedefs.char),
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.nxSessionRef_t)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            number_of_database_ref,
            array_of_database_ref,
            interface,
            mode,
            session_ref)

    def nx_get_property(
            self,
            session_ref,
            property_id,
            property_size,
            property_value):
        cfunc = self.cdll.nxGetProperty
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.u32,
            _ctypedefs.u32,
            _ctypedefs.nxVoidPtr]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            property_id,
            property_size,
            property_value)

    def nx_get_property_size(
            self,
            session_ref,
            property_id,
            property_size):
        cfunc = self.cdll.nxGetPropertySize
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.u32)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            property_id,
            property_size)

    def nx_set_property(
            self,
            session_ref,
            property_id,
            property_size,
            property_value):
        cfunc = self.cdll.nxSetProperty
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.u32,
            _ctypedefs.u32,
            _ctypedefs.nxVoidPtr]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            property_id,
            property_size,
            property_value)

    def nx_get_sub_property(
            self,
            session_ref,
            active_index,
            property_id,
            property_size,
            property_value):
        cfunc = self.cdll.nxGetSubProperty
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.u32,
            _ctypedefs.u32,
            _ctypedefs.u32,
            _ctypedefs.nxVoidPtr]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            active_index,
            property_id,
            property_size,
            property_value)

    def nx_get_sub_property_size(
            self,
            session_ref,
            active_index,
            property_id,
            property_size):
        cfunc = self.cdll.nxGetSubPropertySize
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.u32,
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.u32)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            active_index,
            property_id,
            property_size)

    def nx_set_sub_property(
            self,
            session_ref,
            active_index,
            property_id,
            property_size,
            property_value):
        cfunc = self.cdll.nxSetSubProperty
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.u32,
            _ctypedefs.u32,
            _ctypedefs.u32,
            _ctypedefs.nxVoidPtr]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            active_index,
            property_id,
            property_size,
            property_value)

    def nx_read_frame(
            self,
            session_ref,
            buffer,
            size_of_buffer,
            timeout,
            number_of_bytes_returned):
        cfunc = self.cdll.nxReadFrame
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.nxVoidPtr,
            _ctypedefs.u32,
            _ctypedefs.f64,
            ctypes.POINTER(_ctypedefs.u32)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            buffer,
            size_of_buffer,
            timeout,
            number_of_bytes_returned)

    def nx_read_signal_single_point(
            self,
            session_ref,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer):
        cfunc = self.cdll.nxReadSignalSinglePoint
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            ctypes.POINTER(_ctypedefs.f64),
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.nxTimestamp_t),
            _ctypedefs.u32]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer)

    def nx_read_signal_waveform(
            self,
            session_ref,
            timeout,
            start_time,
            delta_time,
            value_buffer,
            size_of_value_buffer,
            number_of_values_returned):
        cfunc = self.cdll.nxReadSignalWaveform
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.f64,
            ctypes.POINTER(_ctypedefs.nxTimestamp_t),
            ctypes.POINTER(_ctypedefs.f64),
            ctypes.POINTER(_ctypedefs.f64),
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.u32)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            timeout,
            start_time,
            delta_time,
            value_buffer,
            size_of_value_buffer,
            number_of_values_returned)

    def nx_read_signal_xy(
            self,
            session_ref,
            time_limit,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer,
            num_pairs_buffer,
            size_of_num_pairs_buffer):
        cfunc = self.cdll.nxReadSignalXY
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            ctypes.POINTER(_ctypedefs.nxTimestamp_t),
            ctypes.POINTER(_ctypedefs.f64),
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.nxTimestamp_t),
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.u32),
            _ctypedefs.u32]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            time_limit,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer,
            num_pairs_buffer,
            size_of_num_pairs_buffer)

    def nx_read_state(
            self,
            session_ref,
            state_id,
            state_size,
            state_value,
            fault):
        cfunc = self.cdll.nxReadState
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.u32,
            _ctypedefs.u32,
            _ctypedefs.nxVoidPtr,
            ctypes.POINTER(_ctypedefs.nxStatus_t)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            state_id,
            state_size,
            state_value,
            fault)

    def nx_write_frame(
            self,
            session_ref,
            buffer,
            number_of_bytes_for_frames,
            timeout):
        cfunc = self.cdll.nxWriteFrame
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.nxVoidPtr,
            _ctypedefs.u32,
            _ctypedefs.f64]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            buffer,
            number_of_bytes_for_frames,
            timeout)

    def nx_write_signal_single_point(
            self,
            session_ref,
            value_buffer,
            size_of_value_buffer):
        cfunc = self.cdll.nxWriteSignalSinglePoint
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            ctypes.POINTER(_ctypedefs.f64),
            _ctypedefs.u32]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            value_buffer,
            size_of_value_buffer)

    def nx_write_state(
            self,
            session_ref,
            state_id,
            state_size,
            state_value):
        cfunc = self.cdll.nxWriteState
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.u32,
            _ctypedefs.u32,
            _ctypedefs.nxVoidPtr]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            state_id,
            state_size,
            state_value)

    def nx_write_signal_waveform(
            self,
            session_ref,
            timeout,
            value_buffer,
            size_of_value_buffer):
        cfunc = self.cdll.nxWriteSignalWaveform
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.f64,
            ctypes.POINTER(_ctypedefs.f64),
            _ctypedefs.u32]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            timeout,
            value_buffer,
            size_of_value_buffer)

    def nx_write_signal_xy(
            self,
            session_ref,
            timeout,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer,
            num_pairs_buffer,
            size_of_num_pairs_buffer):
        cfunc = self.cdll.nxWriteSignalXY
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.f64,
            ctypes.POINTER(_ctypedefs.f64),
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.nxTimestamp_t),
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.u32),
            _ctypedefs.u32]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            timeout,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer,
            num_pairs_buffer,
            size_of_num_pairs_buffer)

    def nx_convert_frames_to_signals_single_point(
            self,
            session_ref,
            frame_buffer,
            number_of_bytes_for_frames,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer):
        cfunc = self.cdll.nxConvertFramesToSignalsSinglePoint
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.nxVoidPtr,
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.f64),
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.nxTimestamp_t),
            _ctypedefs.u32]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            frame_buffer,
            number_of_bytes_for_frames,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer)

    def nx_convert_signals_to_frames_single_point(
            self,
            session_ref,
            value_buffer,
            size_of_value_buffer,
            buffer,
            size_of_buffer,
            number_of_bytes_returned):
        cfunc = self.cdll.nxConvertSignalsToFramesSinglePoint
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            ctypes.POINTER(_ctypedefs.f64),
            _ctypedefs.u32,
            _ctypedefs.nxVoidPtr,
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.u32)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            value_buffer,
            size_of_value_buffer,
            buffer,
            size_of_buffer,
            number_of_bytes_returned)

    def nx_blink(
            self,
            interface_ref,
            modifier):
        cfunc = self.cdll.nxBlink
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.u32]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            interface_ref,
            modifier)

    def nx_clear(
            self,
            session_ref):
        cfunc = self.cdll.nxClear
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref)

    def nx_connect_terminals(
            self,
            session_ref,
            source,
            destination):
        cfunc = self.cdll.nxConnectTerminals
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.char)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            source,
            destination)

    def nx_disconnect_terminals(
            self,
            session_ref,
            source,
            destination):
        cfunc = self.cdll.nxDisconnectTerminals
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.char)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            source,
            destination)

    def nx_flush(
            self,
            session_ref):
        cfunc = self.cdll.nxFlush
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref)

    def nx_start(
            self,
            session_ref,
            scope):
        cfunc = self.cdll.nxStart
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.u32]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            scope)

    def nx_stop(
            self,
            session_ref,
            scope):
        cfunc = self.cdll.nxStop
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.u32]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            scope)

    def nx_status_to_string(
            self,
            status,
            sizeof_string,
            status_description):
        cfunc = self.cdll.nxStatusToString
        cfunc.argtypes = [
            _ctypedefs.nxStatus_t,
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.char)]
        cfunc.restype = None
        return cfunc(
            status,
            sizeof_string,
            status_description)

    def nx_system_open(
            self,
            system_ref):
        cfunc = self.cdll.nxSystemOpen
        cfunc.argtypes = [
            ctypes.POINTER(_ctypedefs.nxSessionRef_t)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            system_ref)

    def nx_system_close(
            self,
            system_ref):
        cfunc = self.cdll.nxSystemClose
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            system_ref)

    def nx_wait(
            self,
            session_ref,
            condition,
            param_in,
            timeout,
            param_out):
        cfunc = self.cdll.nxWait
        cfunc.argtypes = [
            _ctypedefs.nxSessionRef_t,
            _ctypedefs.u32,
            _ctypedefs.u32,
            _ctypedefs.f64,
            ctypes.POINTER(_ctypedefs.u32)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            session_ref,
            condition,
            param_in,
            timeout,
            param_out)

    def nxdb_open_database(
            self,
            database_name,
            database_ref):
        cfunc = self.cdll.nxdbOpenDatabase
        cfunc.argtypes = [
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            database_name,
            database_ref)

    def nxdb_close_database(
            self,
            database_ref,
            close_all_refs):
        cfunc = self.cdll.nxdbCloseDatabase
        cfunc.argtypes = [
            _ctypedefs.nxDatabaseRef_t,
            _ctypedefs.u32]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            database_ref,
            close_all_refs)

    def nxdb_create_object(
            self,
            parent_object_ref,
            object_class,
            object_name,
            db_object_ref):
        cfunc = self.cdll.nxdbCreateObject
        cfunc.argtypes = [
            _ctypedefs.nxDatabaseRef_t,
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            parent_object_ref,
            object_class,
            object_name,
            db_object_ref)

    def nxdb_find_object(
            self,
            parent_object_ref,
            object_class,
            object_name,
            db_object_ref):
        cfunc = self.cdll.nxdbFindObject
        cfunc.argtypes = [
            _ctypedefs.nxDatabaseRef_t,
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            parent_object_ref,
            object_class,
            object_name,
            db_object_ref)

    def nxdb_delete_object(
            self,
            db_object_ref):
        cfunc = self.cdll.nxdbDeleteObject
        cfunc.argtypes = [
            _ctypedefs.nxDatabaseRef_t]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            db_object_ref)

    def nxdb_save_database(
            self,
            database_ref,
            db_filepath):
        cfunc = self.cdll.nxdbSaveDatabase
        cfunc.argtypes = [
            _ctypedefs.nxDatabaseRef_t,
            ctypes.POINTER(_ctypedefs.char)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            database_ref,
            db_filepath)

    def nxdb_get_property(
            self,
            db_object_ref,
            property_id,
            property_size,
            property_value):
        cfunc = self.cdll.nxdbGetProperty
        cfunc.argtypes = [
            _ctypedefs.nxDatabaseRef_t,
            _ctypedefs.u32,
            _ctypedefs.u32,
            _ctypedefs.nxVoidPtr]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            db_object_ref,
            property_id,
            property_size,
            property_value)

    def nxdb_get_property_size(
            self,
            db_object_ref,
            property_id,
            property_size):
        cfunc = self.cdll.nxdbGetPropertySize
        cfunc.argtypes = [
            _ctypedefs.nxDatabaseRef_t,
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.u32)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            db_object_ref,
            property_id,
            property_size)

    def nxdb_set_property(
            self,
            db_object_ref,
            property_id,
            property_size,
            property_value):
        cfunc = self.cdll.nxdbSetProperty
        cfunc.argtypes = [
            _ctypedefs.nxDatabaseRef_t,
            _ctypedefs.u32,
            _ctypedefs.u32,
            _ctypedefs.nxVoidPtr]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            db_object_ref,
            property_id,
            property_size,
            property_value)

    def nxdb_get_dbc_attribute_size(
            self,
            db_object_ref,
            mode,
            attribute_name,
            attribute_text_size):
        cfunc = self.cdll.nxdbGetDBCAttributeSize
        cfunc.argtypes = [
            _ctypedefs.nxDatabaseRef_t,
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.u32)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            db_object_ref,
            mode,
            attribute_name,
            attribute_text_size)

    def nxdb_get_dbc_attribute(
            self,
            db_object_ref,
            mode,
            attribute_name,
            attribute_text_size,
            attribute_text,
            is_default):
        cfunc = self.cdll.nxdbGetDBCAttribute
        cfunc.argtypes = [
            _ctypedefs.nxDatabaseRef_t,
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.char),
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.u32)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            db_object_ref,
            mode,
            attribute_name,
            attribute_text_size,
            attribute_text,
            is_default)

    def nxdb_merge(
            self,
            target_cluster_ref,
            source_obj_ref,
            copy_mode,
            prefix,
            wait_for_complete,
            percent_complete):
        cfunc = self.cdll.nxdbMerge
        cfunc.argtypes = [
            _ctypedefs.nxDatabaseRef_t,
            _ctypedefs.nxDatabaseRef_t,
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.char),
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.u32)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            target_cluster_ref,
            source_obj_ref,
            copy_mode,
            prefix,
            wait_for_complete,
            percent_complete)

    def nxdb_add_alias(
            self,
            database_alias,
            database_filepath,
            default_baud_rate):
        cfunc = self.cdll.nxdbAddAlias
        cfunc.argtypes = [
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.char),
            _ctypedefs.u32]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            database_alias,
            database_filepath,
            default_baud_rate)

    def nxdb_add_alias64(
            self,
            database_alias,
            database_filepath,
            default_baud_rate):
        cfunc = self.cdll.nxdbAddAlias64
        cfunc.argtypes = [
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.char),
            _ctypedefs.u64]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            database_alias,
            database_filepath,
            default_baud_rate)

    def nxdb_remove_alias(
            self,
            database_alias):
        cfunc = self.cdll.nxdbRemoveAlias
        cfunc.argtypes = [
            ctypes.POINTER(_ctypedefs.char)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            database_alias)

    def nxdb_deploy(
            self,
            ip_address,
            database_alias,
            wait_for_complete,
            percent_complete):
        cfunc = self.cdll.nxdbDeploy
        cfunc.argtypes = [
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.char),
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.u32)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            ip_address,
            database_alias,
            wait_for_complete,
            percent_complete)

    def nxdb_undeploy(
            self,
            ip_address,
            database_alias):
        cfunc = self.cdll.nxdbUndeploy
        cfunc.argtypes = [
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.char)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            ip_address,
            database_alias)

    def nxdb_get_database_list(
            self,
            ip_address,
            sizeof_alias_buffer,
            alias_buffer,
            sizeof_filepath_buffer,
            filepath_buffer,
            number_of_databases):
        cfunc = self.cdll.nxdbGetDatabaseList
        cfunc.argtypes = [
            ctypes.POINTER(_ctypedefs.char),
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.char),
            _ctypedefs.u32,
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.u32)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            ip_address,
            sizeof_alias_buffer,
            alias_buffer,
            sizeof_filepath_buffer,
            filepath_buffer,
            number_of_databases)

    def nxdb_get_database_list_sizes(
            self,
            ip_address,
            sizeof_alias_buffer,
            sizeof_filepath_buffer):
        cfunc = self.cdll.nxdbGetDatabaseListSizes
        cfunc.argtypes = [
            ctypes.POINTER(_ctypedefs.char),
            ctypes.POINTER(_ctypedefs.u32),
            ctypes.POINTER(_ctypedefs.u32)]
        cfunc.restype = _ctypedefs.nxStatus_t
        return cfunc(
            ip_address,
            sizeof_alias_buffer,
            sizeof_filepath_buffer)


lib = XnetLibrary()
