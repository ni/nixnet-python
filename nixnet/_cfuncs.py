import ctypes  # type: ignore
import threading
import typing  # NOQA: F401

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
        self._load_lock = threading.Lock()
        self._nx_create_session = None
        self._nx_create_session_by_ref = None
        self._nx_get_property = None
        self._nx_get_property_size = None
        self._nx_set_property = None
        self._nx_get_sub_property = None
        self._nx_get_sub_property_size = None
        self._nx_set_sub_property = None
        self._nx_read_frame = None
        self._nx_read_signal_single_point = None
        self._nx_read_signal_waveform = None
        self._nx_read_signal_xy = None
        self._nx_read_state = None
        self._nx_write_frame = None
        self._nx_write_signal_single_point = None
        self._nx_write_state = None
        self._nx_write_signal_waveform = None
        self._nx_write_signal_xy = None
        self._nx_convert_frames_to_signals_single_point = None
        self._nx_convert_signals_to_frames_single_point = None
        self._nx_blink = None
        self._nx_clear = None
        self._nx_connect_terminals = None
        self._nx_disconnect_terminals = None
        self._nx_flush = None
        self._nx_start = None
        self._nx_stop = None
        self._nx_status_to_string = None
        self._nx_system_open = None
        self._nx_system_close = None
        self._nx_wait = None
        self._nxdb_open_database = None
        self._nxdb_close_database = None
        self._nxdb_create_object = None
        self._nxdb_find_object = None
        self._nxdb_delete_object = None
        self._nxdb_save_database = None
        self._nxdb_get_property = None
        self._nxdb_get_property_size = None
        self._nxdb_set_property = None
        self._nxdb_get_dbc_attribute_size = None
        self._nxdb_get_dbc_attribute = None
        self._nxdb_merge = None
        self._nxdb_add_alias = None
        self._nxdb_add_alias64 = None
        self._nxdb_remove_alias = None
        self._nxdb_deploy = None
        self._nxdb_undeploy = None
        self._nxdb_get_database_list = None
        self._nxdb_get_database_list_sizes = None

    @property
    def cdll(self):
        # type: (...) -> _lib.XnetLibrary
        if self._cdll is None:
            self._cdll = _lib.import_lib()
        return self._cdll

    def nx_create_session(
            self,
            database_name,  # type: _ctypedefs.char_p
            cluster_name,  # type: _ctypedefs.char_p
            list,  # type: _ctypedefs.char_p
            interface,  # type: _ctypedefs.char_p
            mode,  # type: _ctypedefs.u32
            session_ref,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_create_session is None:
            with self._load_lock:
                cfunc = self.cdll.nxCreateSession
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    _ctypedefs.char_p,
                    _ctypedefs.char_p,
                    _ctypedefs.char_p,
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.nxSessionRef_t)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_create_session = cfunc
        return self._nx_create_session(
            database_name,
            cluster_name,
            list,
            interface,
            mode,
            session_ref)

    def nx_create_session_by_ref(
            self,
            size_of_database_refs,  # type: _ctypedefs.u32
            database_refs,  # type: typing.Any
            interface,  # type: _ctypedefs.char_p
            mode,  # type: _ctypedefs.u32
            session_ref,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_create_session_by_ref is None:
            with self._load_lock:
                cfunc = self.cdll.nxCreateSessionByRef
                cfunc.argtypes = [
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.nxDatabaseRef_t),
                    _ctypedefs.char_p,
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.nxSessionRef_t)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_create_session_by_ref = cfunc
        return self._nx_create_session_by_ref(
            size_of_database_refs,
            database_refs,
            interface,
            mode,
            session_ref)

    def nx_get_property(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: _ctypedefs.u32
            property_value,  # type: _ctypedefs.nxVoidPtr
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_get_property is None:
            with self._load_lock:
                cfunc = self.cdll.nxGetProperty
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_get_property = cfunc
        return self._nx_get_property(
            session_ref,
            property_id,
            property_size,
            property_value)

    def nx_get_property_size(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_get_property_size is None:
            with self._load_lock:
                cfunc = self.cdll.nxGetPropertySize
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_get_property_size = cfunc
        return self._nx_get_property_size(
            session_ref,
            property_id,
            property_size)

    def nx_set_property(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: _ctypedefs.u32
            property_value,  # type: _ctypedefs.nxVoidPtr
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_set_property is None:
            with self._load_lock:
                cfunc = self.cdll.nxSetProperty
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_set_property = cfunc
        return self._nx_set_property(
            session_ref,
            property_id,
            property_size,
            property_value)

    def nx_get_sub_property(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            active_index,  # type: _ctypedefs.u32
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: _ctypedefs.u32
            property_value,  # type: _ctypedefs.nxVoidPtr
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_get_sub_property is None:
            with self._load_lock:
                cfunc = self.cdll.nxGetSubProperty
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_get_sub_property = cfunc
        return self._nx_get_sub_property(
            session_ref,
            active_index,
            property_id,
            property_size,
            property_value)

    def nx_get_sub_property_size(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            active_index,  # type: _ctypedefs.u32
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_get_sub_property_size is None:
            with self._load_lock:
                cfunc = self.cdll.nxGetSubPropertySize
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_get_sub_property_size = cfunc
        return self._nx_get_sub_property_size(
            session_ref,
            active_index,
            property_id,
            property_size)

    def nx_set_sub_property(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            active_index,  # type: _ctypedefs.u32
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: _ctypedefs.u32
            property_value,  # type: _ctypedefs.nxVoidPtr
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_set_sub_property is None:
            with self._load_lock:
                cfunc = self.cdll.nxSetSubProperty
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_set_sub_property = cfunc
        return self._nx_set_sub_property(
            session_ref,
            active_index,
            property_id,
            property_size,
            property_value)

    def nx_read_frame(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            buffer,  # type: typing.Any
            size_of_buffer,  # type: _ctypedefs.u32
            timeout,  # type: _ctypedefs.f64
            number_of_bytes_returned,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_read_frame is None:
            with self._load_lock:
                cfunc = self.cdll.nxReadFrame
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    ctypes.POINTER(_ctypedefs.byte),
                    _ctypedefs.u32,
                    _ctypedefs.f64,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_read_frame = cfunc
        return self._nx_read_frame(
            session_ref,
            buffer,
            size_of_buffer,
            timeout,
            number_of_bytes_returned)

    def nx_read_signal_single_point(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
            timestamp_buffer,  # type: typing.Any
            size_of_timestamp_buffer,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_read_signal_single_point is None:
            with self._load_lock:
                cfunc = self.cdll.nxReadSignalSinglePoint
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    ctypes.POINTER(_ctypedefs.f64),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.nxTimestamp_t),
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_read_signal_single_point = cfunc
        return self._nx_read_signal_single_point(
            session_ref,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer)

    def nx_read_signal_waveform(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            timeout,  # type: _ctypedefs.f64
            start_time,  # type: typing.Any
            delta_time,  # type: typing.Any
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
            number_of_values_returned,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_read_signal_waveform is None:
            with self._load_lock:
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
                self._nx_read_signal_waveform = cfunc
        return self._nx_read_signal_waveform(
            session_ref,
            timeout,
            start_time,
            delta_time,
            value_buffer,
            size_of_value_buffer,
            number_of_values_returned)

    def nx_read_signal_xy(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            time_limit,  # type: typing.Any
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
            timestamp_buffer,  # type: typing.Any
            size_of_timestamp_buffer,  # type: _ctypedefs.u32
            num_pairs_buffer,  # type: typing.Any
            size_of_num_pairs_buffer,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_read_signal_xy is None:
            with self._load_lock:
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
                self._nx_read_signal_xy = cfunc
        return self._nx_read_signal_xy(
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
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            state_id,  # type: _ctypedefs.u32
            state_size,  # type: _ctypedefs.u32
            state_value,  # type: _ctypedefs.nxVoidPtr
            fault,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_read_state is None:
            with self._load_lock:
                cfunc = self.cdll.nxReadState
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr,
                    ctypes.POINTER(_ctypedefs.nxStatus_t)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_read_state = cfunc
        return self._nx_read_state(
            session_ref,
            state_id,
            state_size,
            state_value,
            fault)

    def nx_write_frame(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            buffer,  # type: typing.Any
            size_of_buffer,  # type: _ctypedefs.u32
            timeout,  # type: _ctypedefs.f64
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_write_frame is None:
            with self._load_lock:
                cfunc = self.cdll.nxWriteFrame
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    ctypes.POINTER(_ctypedefs.byte),
                    _ctypedefs.u32,
                    _ctypedefs.f64]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_write_frame = cfunc
        return self._nx_write_frame(
            session_ref,
            buffer,
            size_of_buffer,
            timeout)

    def nx_write_signal_single_point(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_write_signal_single_point is None:
            with self._load_lock:
                cfunc = self.cdll.nxWriteSignalSinglePoint
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    ctypes.POINTER(_ctypedefs.f64),
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_write_signal_single_point = cfunc
        return self._nx_write_signal_single_point(
            session_ref,
            value_buffer,
            size_of_value_buffer)

    def nx_write_state(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            state_id,  # type: _ctypedefs.u32
            state_size,  # type: _ctypedefs.u32
            state_value,  # type: _ctypedefs.nxVoidPtr
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_write_state is None:
            with self._load_lock:
                cfunc = self.cdll.nxWriteState
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_write_state = cfunc
        return self._nx_write_state(
            session_ref,
            state_id,
            state_size,
            state_value)

    def nx_write_signal_waveform(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            timeout,  # type: _ctypedefs.f64
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_write_signal_waveform is None:
            with self._load_lock:
                cfunc = self.cdll.nxWriteSignalWaveform
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.f64,
                    ctypes.POINTER(_ctypedefs.f64),
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_write_signal_waveform = cfunc
        return self._nx_write_signal_waveform(
            session_ref,
            timeout,
            value_buffer,
            size_of_value_buffer)

    def nx_write_signal_xy(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            timeout,  # type: _ctypedefs.f64
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
            timestamp_buffer,  # type: typing.Any
            size_of_timestamp_buffer,  # type: _ctypedefs.u32
            num_pairs_buffer,  # type: typing.Any
            size_of_num_pairs_buffer,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_write_signal_xy is None:
            with self._load_lock:
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
                self._nx_write_signal_xy = cfunc
        return self._nx_write_signal_xy(
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
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            frame_buffer,  # type: typing.Any
            size_of_frame_buffer,  # type: _ctypedefs.u32
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
            timestamp_buffer,  # type: typing.Any
            size_of_timestamp_buffer,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_convert_frames_to_signals_single_point is None:
            with self._load_lock:
                cfunc = self.cdll.nxConvertFramesToSignalsSinglePoint
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    ctypes.POINTER(_ctypedefs.byte),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.f64),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.nxTimestamp_t),
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_convert_frames_to_signals_single_point = cfunc
        return self._nx_convert_frames_to_signals_single_point(
            session_ref,
            frame_buffer,
            size_of_frame_buffer,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer)

    def nx_convert_signals_to_frames_single_point(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            value_buffer,  # type: typing.Any
            size_of_value_buffer,  # type: _ctypedefs.u32
            buffer,  # type: typing.Any
            size_of_buffer,  # type: _ctypedefs.u32
            number_of_bytes_returned,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_convert_signals_to_frames_single_point is None:
            with self._load_lock:
                cfunc = self.cdll.nxConvertSignalsToFramesSinglePoint
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    ctypes.POINTER(_ctypedefs.f64),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.byte),
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_convert_signals_to_frames_single_point = cfunc
        return self._nx_convert_signals_to_frames_single_point(
            session_ref,
            value_buffer,
            size_of_value_buffer,
            buffer,
            size_of_buffer,
            number_of_bytes_returned)

    def nx_blink(
            self,
            interface_ref,  # type: _ctypedefs.nxSessionRef_t
            modifier,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_blink is None:
            with self._load_lock:
                cfunc = self.cdll.nxBlink
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_blink = cfunc
        return self._nx_blink(
            interface_ref,
            modifier)

    def nx_clear(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_clear is None:
            with self._load_lock:
                cfunc = self.cdll.nxClear
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_clear = cfunc
        return self._nx_clear(
            session_ref)

    def nx_connect_terminals(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            source,  # type: _ctypedefs.char_p
            destination,  # type: _ctypedefs.char_p
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_connect_terminals is None:
            with self._load_lock:
                cfunc = self.cdll.nxConnectTerminals
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.char_p,
                    _ctypedefs.char_p]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_connect_terminals = cfunc
        return self._nx_connect_terminals(
            session_ref,
            source,
            destination)

    def nx_disconnect_terminals(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            source,  # type: _ctypedefs.char_p
            destination,  # type: _ctypedefs.char_p
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_disconnect_terminals is None:
            with self._load_lock:
                cfunc = self.cdll.nxDisconnectTerminals
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.char_p,
                    _ctypedefs.char_p]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_disconnect_terminals = cfunc
        return self._nx_disconnect_terminals(
            session_ref,
            source,
            destination)

    def nx_flush(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_flush is None:
            with self._load_lock:
                cfunc = self.cdll.nxFlush
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_flush = cfunc
        return self._nx_flush(
            session_ref)

    def nx_start(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            scope,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_start is None:
            with self._load_lock:
                cfunc = self.cdll.nxStart
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_start = cfunc
        return self._nx_start(
            session_ref,
            scope)

    def nx_stop(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            scope,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_stop is None:
            with self._load_lock:
                cfunc = self.cdll.nxStop
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_stop = cfunc
        return self._nx_stop(
            session_ref,
            scope)

    def nx_status_to_string(
            self,
            status,  # type: _ctypedefs.nxStatus_t
            size_of_status_description,  # type: _ctypedefs.u32
            status_description,  # type: _ctypedefs.char_p
    ):
        # type: (...) -> None
        if self._nx_status_to_string is None:
            with self._load_lock:
                cfunc = self.cdll.nxStatusToString
                cfunc.argtypes = [
                    _ctypedefs.nxStatus_t,
                    _ctypedefs.u32,
                    _ctypedefs.char_p]
                cfunc.restype = None
                self._nx_status_to_string = cfunc
        return self._nx_status_to_string(
            status,
            size_of_status_description,
            status_description)

    def nx_system_open(
            self,
            system_ref,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_system_open is None:
            with self._load_lock:
                cfunc = self.cdll.nxSystemOpen
                cfunc.argtypes = [
                    ctypes.POINTER(_ctypedefs.nxSessionRef_t)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_system_open = cfunc
        return self._nx_system_open(
            system_ref)

    def nx_system_close(
            self,
            system_ref,  # type: _ctypedefs.nxSessionRef_t
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_system_close is None:
            with self._load_lock:
                cfunc = self.cdll.nxSystemClose
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_system_close = cfunc
        return self._nx_system_close(
            system_ref)

    def nx_wait(
            self,
            session_ref,  # type: _ctypedefs.nxSessionRef_t
            condition,  # type: _ctypedefs.u32
            param_in,  # type: _ctypedefs.u32
            timeout,  # type: _ctypedefs.f64
            param_out,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nx_wait is None:
            with self._load_lock:
                cfunc = self.cdll.nxWait
                cfunc.argtypes = [
                    _ctypedefs.nxSessionRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.f64,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nx_wait = cfunc
        return self._nx_wait(
            session_ref,
            condition,
            param_in,
            timeout,
            param_out)

    def nxdb_open_database(
            self,
            database_name,  # type: _ctypedefs.char_p
            database_ref,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_open_database is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbOpenDatabase
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_open_database = cfunc
        return self._nxdb_open_database(
            database_name,
            database_ref)

    def nxdb_close_database(
            self,
            database_ref,  # type: _ctypedefs.nxDatabaseRef_t
            close_all_refs,  # type: _ctypedefs.bool32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_close_database is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbCloseDatabase
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.bool32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_close_database = cfunc
        return self._nxdb_close_database(
            database_ref,
            close_all_refs)

    def nxdb_create_object(
            self,
            parent_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
            object_class,  # type: _ctypedefs.u32
            object_name,  # type: _ctypedefs.char_p
            db_object_ref,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_create_object is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbCreateObject
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_create_object = cfunc
        return self._nxdb_create_object(
            parent_object_ref,
            object_class,
            object_name,
            db_object_ref)

    def nxdb_find_object(
            self,
            parent_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
            object_class,  # type: _ctypedefs.u32
            object_name,  # type: _ctypedefs.char_p
            db_object_ref,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_find_object is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbFindObject
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_find_object = cfunc
        return self._nxdb_find_object(
            parent_object_ref,
            object_class,
            object_name,
            db_object_ref)

    def nxdb_delete_object(
            self,
            db_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_delete_object is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbDeleteObject
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_delete_object = cfunc
        return self._nxdb_delete_object(
            db_object_ref)

    def nxdb_save_database(
            self,
            database_ref,  # type: _ctypedefs.nxDatabaseRef_t
            db_filepath,  # type: _ctypedefs.char_p
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_save_database is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbSaveDatabase
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.char_p]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_save_database = cfunc
        return self._nxdb_save_database(
            database_ref,
            db_filepath)

    def nxdb_get_property(
            self,
            db_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: _ctypedefs.u32
            property_value,  # type: _ctypedefs.nxVoidPtr
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_get_property is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbGetProperty
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_get_property = cfunc
        return self._nxdb_get_property(
            db_object_ref,
            property_id,
            property_size,
            property_value)

    def nxdb_get_property_size(
            self,
            db_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_get_property_size is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbGetPropertySize
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_get_property_size = cfunc
        return self._nxdb_get_property_size(
            db_object_ref,
            property_id,
            property_size)

    def nxdb_set_property(
            self,
            db_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
            property_id,  # type: _ctypedefs.u32
            property_size,  # type: _ctypedefs.u32
            property_value,  # type: _ctypedefs.nxVoidPtr
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_set_property is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbSetProperty
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.u32,
                    _ctypedefs.nxVoidPtr]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_set_property = cfunc
        return self._nxdb_set_property(
            db_object_ref,
            property_id,
            property_size,
            property_value)

    def nxdb_get_dbc_attribute_size(
            self,
            db_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
            mode,  # type: _ctypedefs.u32
            attribute_name,  # type: _ctypedefs.char_p
            attribute_text_size,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_get_dbc_attribute_size is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbGetDBCAttributeSize
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_get_dbc_attribute_size = cfunc
        return self._nxdb_get_dbc_attribute_size(
            db_object_ref,
            mode,
            attribute_name,
            attribute_text_size)

    def nxdb_get_dbc_attribute(
            self,
            db_object_ref,  # type: _ctypedefs.nxDatabaseRef_t
            mode,  # type: _ctypedefs.u32
            attribute_name,  # type: _ctypedefs.char_p
            attribute_text_size,  # type: _ctypedefs.u32
            attribute_text,  # type: _ctypedefs.char_p
            is_default,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_get_dbc_attribute is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbGetDBCAttribute
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_get_dbc_attribute = cfunc
        return self._nxdb_get_dbc_attribute(
            db_object_ref,
            mode,
            attribute_name,
            attribute_text_size,
            attribute_text,
            is_default)

    def nxdb_merge(
            self,
            target_cluster_ref,  # type: _ctypedefs.nxDatabaseRef_t
            source_obj_ref,  # type: _ctypedefs.nxDatabaseRef_t
            copy_mode,  # type: _ctypedefs.u32
            prefix,  # type: _ctypedefs.char_p
            wait_for_complete,  # type: _ctypedefs.bool32
            percent_complete,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_merge is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbMerge
                cfunc.argtypes = [
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.nxDatabaseRef_t,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    _ctypedefs.bool32,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_merge = cfunc
        return self._nxdb_merge(
            target_cluster_ref,
            source_obj_ref,
            copy_mode,
            prefix,
            wait_for_complete,
            percent_complete)

    def nxdb_add_alias(
            self,
            database_alias,  # type: _ctypedefs.char_p
            database_filepath,  # type: _ctypedefs.char_p
            default_baud_rate,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_add_alias is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbAddAlias
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    _ctypedefs.char_p,
                    _ctypedefs.u32]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_add_alias = cfunc
        return self._nxdb_add_alias(
            database_alias,
            database_filepath,
            default_baud_rate)

    def nxdb_add_alias64(
            self,
            database_alias,  # type: _ctypedefs.char_p
            database_filepath,  # type: _ctypedefs.char_p
            default_baud_rate,  # type: _ctypedefs.u64
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_add_alias64 is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbAddAlias64
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    _ctypedefs.char_p,
                    _ctypedefs.u64]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_add_alias64 = cfunc
        return self._nxdb_add_alias64(
            database_alias,
            database_filepath,
            default_baud_rate)

    def nxdb_remove_alias(
            self,
            database_alias,  # type: _ctypedefs.char_p
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_remove_alias is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbRemoveAlias
                cfunc.argtypes = [
                    _ctypedefs.char_p]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_remove_alias = cfunc
        return self._nxdb_remove_alias(
            database_alias)

    def nxdb_deploy(
            self,
            ip_address,  # type: _ctypedefs.char_p
            database_alias,  # type: _ctypedefs.char_p
            wait_for_complete,  # type: _ctypedefs.bool32
            percent_complete,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_deploy is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbDeploy
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    _ctypedefs.char_p,
                    _ctypedefs.bool32,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_deploy = cfunc
        return self._nxdb_deploy(
            ip_address,
            database_alias,
            wait_for_complete,
            percent_complete)

    def nxdb_undeploy(
            self,
            ip_address,  # type: _ctypedefs.char_p
            database_alias,  # type: _ctypedefs.char_p
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_undeploy is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbUndeploy
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    _ctypedefs.char_p]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_undeploy = cfunc
        return self._nxdb_undeploy(
            ip_address,
            database_alias)

    def nxdb_get_database_list(
            self,
            ip_address,  # type: _ctypedefs.char_p
            size_of_alias_buffer,  # type: _ctypedefs.u32
            alias_buffer,  # type: _ctypedefs.char_p
            size_of_filepath_buffer,  # type: _ctypedefs.u32
            filepath_buffer,  # type: _ctypedefs.char_p
            number_of_databases,  # type: typing.Any
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_get_database_list is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbGetDatabaseList
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    _ctypedefs.u32,
                    _ctypedefs.char_p,
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_get_database_list = cfunc
        return self._nxdb_get_database_list(
            ip_address,
            size_of_alias_buffer,
            alias_buffer,
            size_of_filepath_buffer,
            filepath_buffer,
            number_of_databases)

    def nxdb_get_database_list_sizes(
            self,
            ip_address,  # type: _ctypedefs.char_p
            sizeof_alias_buffer,  # type: _ctypedefs.u32
            sizeof_filepath_buffer,  # type: _ctypedefs.u32
    ):
        # type: (...) -> _ctypedefs.nxStatus_t
        if self._nxdb_get_database_list_sizes is None:
            with self._load_lock:
                cfunc = self.cdll.nxdbGetDatabaseListSizes
                cfunc.argtypes = [
                    _ctypedefs.char_p,
                    ctypes.POINTER(_ctypedefs.u32),
                    ctypes.POINTER(_ctypedefs.u32)]
                cfunc.restype = _ctypedefs.nxStatus_t
                self._nxdb_get_database_list_sizes = cfunc
        return self._nxdb_get_database_list_sizes(
            ip_address,
            sizeof_alias_buffer,
            sizeof_filepath_buffer)


lib = XnetLibrary()
