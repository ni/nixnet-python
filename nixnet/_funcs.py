import ctypes  # type: ignore
import typing  # NOQA: F401

from nixnet import _cfuncs
from nixnet import _ctypedefs
from nixnet import _enums  # NOQA: F401
from nixnet import _errors


def nx_create_session(
    database_name,  # type: typing.Text
    cluster_name,  # type: typing.Text
    list,  # type: typing.Text
    interface,  # type: typing.Text
    mode,  # type: _enums.CreateSessionMode
):
    # type: (...) -> int
    database_name_ctypes = ctypes.create_string_buffer(database_name.encode('ascii'))
    cluster_name_ctypes = ctypes.create_string_buffer(cluster_name.encode('ascii'))
    list_ctypes = ctypes.create_string_buffer(list.encode('ascii'))
    interface_ctypes = ctypes.create_string_buffer(interface.encode('ascii'))
    mode_ctypes = _ctypedefs.u32(mode.value)
    session_ref_ctypes = _ctypedefs.nxSessionRef_t()
    result = _cfuncs.lib.nx_create_session(
        database_name_ctypes,  # type: ignore
        cluster_name_ctypes,  # type: ignore
        list_ctypes,  # type: ignore
        interface_ctypes,  # type: ignore
        mode_ctypes,
        ctypes.pointer(session_ref_ctypes),
    )
    _errors.check_for_error(result.value)
    return session_ref_ctypes.value


def nx_create_session_by_ref(
    database_refs,  # type: typing.List[_ctypedefs.nxDatabaseRef_t]
    interface,  # type: typing.Text
    mode,  # type: _enums.CreateSessionMode
):
    # type: (...) -> int
    size_of_database_refs_ctypes = _ctypedefs.u32(len(database_refs) * _ctypedefs.nxDatabaseRef_t.BYTES)
    database_refs_ctypes = (_ctypedefs.nxDatabaseRef_t * len(database_refs))(*database_refs)  # type: ignore
    interface_ctypes = ctypes.create_string_buffer(interface.encode('ascii'))
    mode_ctypes = _ctypedefs.u32(mode.value)
    session_ref_ctypes = _ctypedefs.nxSessionRef_t()
    result = _cfuncs.lib.nx_create_session_by_ref(
        size_of_database_refs_ctypes,
        database_refs_ctypes,
        interface_ctypes,  # type: ignore
        mode_ctypes,
        ctypes.pointer(session_ref_ctypes),
    )
    _errors.check_for_error(result.value)
    return session_ref_ctypes.value


def nx_get_property_size(
    session_ref,  # type: int
    property_id,  # type: int
):
    # type: (...) -> int
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    property_id_ctypes = _ctypedefs.u32(property_id)
    property_size_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nx_get_property_size(
        session_ref_ctypes,
        property_id_ctypes,
        ctypes.pointer(property_size_ctypes),
    )
    _errors.check_for_error(result.value)
    return property_size_ctypes.value


def nx_get_sub_property_size(
    session_ref,  # type: int
    active_index,  # type: int
    property_id,  # type: int
):
    # type: (...) -> int
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    active_index_ctypes = _ctypedefs.u32(active_index)
    property_id_ctypes = _ctypedefs.u32(property_id)
    property_size_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nx_get_sub_property_size(
        session_ref_ctypes,
        active_index_ctypes,
        property_id_ctypes,
        ctypes.pointer(property_size_ctypes),
    )
    _errors.check_for_error(result.value)
    return property_size_ctypes.value


def nx_read_frame(
    session_ref,  # type: int
    bytes_to_read,  # type: int
    timeout,  # type: float
):
    # type: (...) -> typing.Tuple[bytes, int]
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    buffer_ctypes = (_ctypedefs.byte * bytes_to_read)()  # type: ignore
    size_of_buffer_ctypes = _ctypedefs.u32(_ctypedefs.byte.BYTES * bytes_to_read)
    number_of_bytes_returned_ctypes = _ctypedefs.u32()
    timeout_ctypes = _ctypedefs.f64(timeout)
    result = _cfuncs.lib.nx_read_frame(
        session_ref_ctypes,
        buffer_ctypes,
        size_of_buffer_ctypes,
        timeout_ctypes,
        ctypes.pointer(number_of_bytes_returned_ctypes))
    _errors.check_for_error(result.value)
    return buffer_ctypes.raw, number_of_bytes_returned_ctypes.value  # type: ignore


def nx_read_signal_single_point(
    session_ref,  # type: int
    num_signals,  # type: int
):
    # type: (...) -> typing.Tuple[ctypes.Array[_ctypedefs.nxTimestamp_t], ctypes.Array[_ctypedefs.f64]]
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    value_buffer_ctypes = (_ctypedefs.f64 * num_signals)()  # type: ignore
    size_of_value_buffer_ctypes = _ctypedefs.u32(_ctypedefs.f64.BYTES * num_signals)
    timestamp_buffer_ctypes = (_ctypedefs.nxTimestamp_t * num_signals)()  # type: ignore
    size_of_timestamp_buffer_ctypes = _ctypedefs.u32(_ctypedefs.nxTimestamp_t.BYTES * num_signals)
    result = _cfuncs.lib.nx_read_signal_single_point(
        session_ref_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes,
        timestamp_buffer_ctypes,
        size_of_timestamp_buffer_ctypes
    )
    _errors.check_for_error(result.value)
    return timestamp_buffer_ctypes, value_buffer_ctypes


def nx_read_state(
    session_ref,  # type: int
    state_id,  # type: _enums.ReadState
    state_size,  # type: int
    state_value_ctypes_ptr,  # type: typing.Any
):
    # type: (...) -> int
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    state_id_ctypes = _ctypedefs.u32(state_id.value)
    state_size_ctypes = _ctypedefs.u32(state_size)
    fault_ctypes = _ctypedefs.nxStatus_t()
    result = _cfuncs.lib.nx_read_state(
        session_ref_ctypes,
        state_id_ctypes,
        state_size_ctypes,
        state_value_ctypes_ptr,
        ctypes.pointer(fault_ctypes),
    )
    _errors.check_for_error(result.value)
    return fault_ctypes.value


def nx_write_frame(
    session_ref,  # type: int
    buffer,  # type: typing.Any
    timeout,  # type: float
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    buffer_ctypes = (_ctypedefs.byte * len(buffer))(*buffer)  # type: ignore
    size_of_buffer_ctypes = _ctypedefs.u32(len(buffer) * _ctypedefs.byte.BYTES)
    timeout_ctypes = _ctypedefs.f64(timeout)
    result = _cfuncs.lib.nx_write_frame(
        session_ref_ctypes,
        buffer_ctypes,
        size_of_buffer_ctypes,
        timeout_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_write_signal_single_point(
    session_ref,  # type: int
    value_buffer,  # type: typing.List[float]
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    value_buffer_ctypes = (_ctypedefs.f64 * len(value_buffer))(*value_buffer)  # type: ignore
    size_of_value_buffer_ctypes = _ctypedefs.u32(len(value_buffer) * _ctypedefs.f64.BYTES)
    result = _cfuncs.lib.nx_write_signal_single_point(
        session_ref_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_write_signal_waveform(
    session_ref,  # type: int
    timeout,  # type: float
    value_buffer,  # type: typing.List[float]
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    timeout_ctypes = _ctypedefs.f64(timeout)
    value_buffer_ctypes = (_ctypedefs.f64 * len(value_buffer))(*value_buffer)  # type: ignore
    size_of_value_buffer_ctypes = _ctypedefs.u32(len(value_buffer) * _ctypedefs.f64.BYTES)
    result = _cfuncs.lib.nx_write_signal_waveform(
        session_ref_ctypes,
        timeout_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_write_signal_xy(
    session_ref,  # type: int
    timeout,  # type: float
    value_buffer,  # type: typing.List[float]
    timestamp_buffer,  # type: typing.List[int]
    num_pairs_buffer,  # type: typing.List[int]
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    timeout_ctypes = _ctypedefs.f64(timeout)
    value_buffer_ctypes = (_ctypedefs.f64 * len(value_buffer))(*value_buffer)  # type: ignore
    size_of_value_buffer_ctypes = _ctypedefs.u32(len(value_buffer) * _ctypedefs.f64.BYTES)
    timestamp_buffer_ctypes = (_ctypedefs.nxTimestamp_t * len(timestamp_buffer))(*timestamp_buffer)  # type: ignore
    size_of_timestamp_buffer_ctypes = _ctypedefs.u32(len(timestamp_buffer) * _ctypedefs.nxTimestamp_t.BYTES)
    num_pairs_buffer_ctypes = (_ctypedefs.u32 * len(num_pairs_buffer))(*num_pairs_buffer)  # type: ignore
    size_of_num_pairs_buffer_ctypes = _ctypedefs.u32(len(num_pairs_buffer) * _ctypedefs.u32.BYTES)
    result = _cfuncs.lib.nx_write_signal_xy(
        session_ref_ctypes,
        timeout_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes,
        timestamp_buffer_ctypes,
        size_of_timestamp_buffer_ctypes,
        num_pairs_buffer_ctypes,
        size_of_num_pairs_buffer_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_write_state(
    session_ref,  # type: int
    state_id,  # type: _enums.WriteState
    state_value_ctypes,  # type: typing.Any
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    state_id_ctypes = _ctypedefs.u32(state_id.value)
    state_size_ctypes = state_value_ctypes.BYTES
    result = _cfuncs.lib.nx_write_state(
        session_ref_ctypes,
        state_id_ctypes,
        state_size_ctypes,
        ctypes.pointer(state_value_ctypes),  # type: ignore
    )
    _errors.check_for_error(result.value)


def nx_convert_frames_to_signals_single_point(
    session_ref,  # type: int
    frame_buffer,  # type: bytes
    num_signals,  # type: int
):
    # type: (...) -> typing.Tuple[ctypes.Array[_ctypedefs.nxTimestamp_t], ctypes.Array[_ctypedefs.f64]]
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    frame_buffer_ctypes = (_ctypedefs.byte * len(frame_buffer))(*frame_buffer)  # type: ignore
    size_of_frame_buffer_ctypes = _ctypedefs.u32(len(frame_buffer) * _ctypedefs.byte.BYTES)
    value_buffer_ctypes = (_ctypedefs.f64 * num_signals)()  # type: ignore
    size_of_value_buffer_ctypes = _ctypedefs.u32(_ctypedefs.f64.BYTES * num_signals)
    timestamp_buffer_ctypes = (_ctypedefs.nxTimestamp_t * num_signals)()  # type: ignore
    size_of_timestamp_buffer_ctypes = _ctypedefs.u32(_ctypedefs.nxTimestamp_t.BYTES * num_signals)
    result = _cfuncs.lib.nx_convert_frames_to_signals_single_point(
        session_ref_ctypes,
        frame_buffer_ctypes,
        size_of_frame_buffer_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes,
        timestamp_buffer_ctypes,
        size_of_timestamp_buffer_ctypes,
    )
    _errors.check_for_error(result.value)
    return timestamp_buffer_ctypes, value_buffer_ctypes


def nx_convert_signals_to_frames_single_point(
    session_ref,  # type: int
    value_buffer,  # type: typing.List[float]
    bytes_to_read,  # type: int
):
    # type: (...) -> typing.Tuple[bytes, int]
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    value_buffer_ctypes = (_ctypedefs.f64 * len(value_buffer))(*value_buffer)  # type: ignore
    size_of_value_buffer_ctypes = _ctypedefs.u32(len(value_buffer) * _ctypedefs.f64.BYTES)
    buffer_ctypes = (_ctypedefs.byte * bytes_to_read)()  # type: ignore
    size_of_buffer_ctypes = _ctypedefs.u32(_ctypedefs.byte.BYTES * bytes_to_read)
    number_of_bytes_returned_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nx_convert_signals_to_frames_single_point(
        session_ref_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes,
        buffer_ctypes,
        size_of_buffer_ctypes,
        ctypes.pointer(number_of_bytes_returned_ctypes),
    )
    _errors.check_for_error(result.value)
    return buffer_ctypes.raw, number_of_bytes_returned_ctypes.value  # type: ignore


def nx_blink(
    interface_ref,  # type: int
    modifier,  # type: _enums.BlinkMode
):
    # type: (...) -> None
    interface_ref_ctypes = _ctypedefs.nxSessionRef_t(interface_ref)
    modifier_ctypes = _ctypedefs.u32(modifier.value)
    result = _cfuncs.lib.nx_blink(
        interface_ref_ctypes,
        modifier_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_clear(
    session_ref,  # type: int
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    result = _cfuncs.lib.nx_clear(
        session_ref_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_connect_terminals(
    session_ref,  # type: int
    source,  # type: typing.Text
    destination,  # type: typing.Text
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    source_ctypes = ctypes.create_string_buffer(source.encode('ascii'))
    destination_ctypes = ctypes.create_string_buffer(destination.encode('ascii'))
    result = _cfuncs.lib.nx_connect_terminals(
        session_ref_ctypes,
        source_ctypes,  # type: ignore
        destination_ctypes,  # type: ignore
    )
    _errors.check_for_error(result.value)


def nx_disconnect_terminals(
    session_ref,  # type: int
    source,  # type: typing.Text
    destination,  # type: typing.Text
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    source_ctypes = ctypes.create_string_buffer(source.encode('ascii'))
    destination_ctypes = ctypes.create_string_buffer(destination.encode('ascii'))
    result = _cfuncs.lib.nx_disconnect_terminals(
        session_ref_ctypes,
        source_ctypes,  # type: ignore
        destination_ctypes,  # type: ignore
    )
    _errors.check_for_error(result.value)


def nx_flush(
    session_ref,  # type: int
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    result = _cfuncs.lib.nx_flush(
        session_ref_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_start(
    session_ref,  # type: int
    scope,  # type: _enums.StartStopScope
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    scope_ctypes = _ctypedefs.u32(scope.value)
    result = _cfuncs.lib.nx_start(
        session_ref_ctypes,
        scope_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_stop(
    session_ref,  # type: int
    scope,  # type: _enums.StartStopScope
):
    # type: (...) -> None
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    scope_ctypes = _ctypedefs.u32(scope.value)
    result = _cfuncs.lib.nx_stop(
        session_ref_ctypes,
        scope_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_system_open(
):
    # type: (...) -> int
    system_ref_ctypes = _ctypedefs.nxSessionRef_t()
    result = _cfuncs.lib.nx_system_open(
        ctypes.pointer(system_ref_ctypes),
    )
    _errors.check_for_error(result.value)
    return system_ref_ctypes.value


def nx_system_close(
    system_ref,  # type: int
):
    # type: (...) -> None
    system_ref_ctypes = _ctypedefs.nxSessionRef_t(system_ref)
    result = _cfuncs.lib.nx_system_close(
        system_ref_ctypes,
    )
    _errors.check_for_error(result.value)


def nx_wait(
    session_ref,  # type: int
    condition,  # type: _enums.Condition
    param_in,  # type: int
    timeout,  # type: float
):
    # type: (...) -> int
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    condition_ctypes = _ctypedefs.u32(condition.value)
    param_in_ctypes = _ctypedefs.u32(param_in)
    timeout_ctypes = _ctypedefs.f64(timeout)
    param_out_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nx_wait(
        session_ref_ctypes,
        condition_ctypes,
        param_in_ctypes,
        timeout_ctypes,
        ctypes.pointer(param_out_ctypes),
    )
    _errors.check_for_error(result.value)
    return param_out_ctypes.value


def nxdb_open_database(
    database_name,  # type: typing.Text
):
    # type: (...) -> int
    database_name_ctypes = ctypes.create_string_buffer(database_name.encode('ascii'))
    database_ref_ctypes = _ctypedefs.nxDatabaseRef_t()
    result = _cfuncs.lib.nxdb_open_database(
        database_name_ctypes,  # type: ignore
        ctypes.pointer(database_ref_ctypes),
    )
    _errors.check_for_error(result.value)
    return database_ref_ctypes.value


def nxdb_close_database(
    database_ref,  # type: int
    close_all_refs,  # type: bool
):
    # type: (...) -> None
    database_ref_ctypes = _ctypedefs.nxDatabaseRef_t(database_ref)
    close_all_refs_ctypes = _ctypedefs.bool32(close_all_refs)
    result = _cfuncs.lib.nxdb_close_database(
        database_ref_ctypes,
        close_all_refs_ctypes,
    )
    _errors.check_for_error(result.value)


def nxdb_create_object(
    parent_object_ref,  # type: int
    object_class,  # type: _enums.ObjectClass
    object_name,  # type: typing.Text
):
    # type: (...) -> int
    parent_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(parent_object_ref)
    object_class_ctypes = _ctypedefs.u32(object_class.value)
    object_name_ctypes = ctypes.create_string_buffer(object_name.encode('ascii'))
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t()
    result = _cfuncs.lib.nxdb_create_object(
        parent_object_ref_ctypes,
        object_class_ctypes,
        object_name_ctypes,  # type: ignore
        ctypes.pointer(db_object_ref_ctypes),
    )
    _errors.check_for_error(result.value)
    return db_object_ref_ctypes.value


def nxdb_find_object(
    parent_object_ref,  # type: int
    object_class,  # type: _enums.ObjectClass
    object_name,  # type: typing.Text
):
    # type: (...) -> int
    parent_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(parent_object_ref)
    object_class_ctypes = _ctypedefs.u32(object_class.value)
    object_name_ctypes = ctypes.create_string_buffer(object_name.encode('ascii'))
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t()
    result = _cfuncs.lib.nxdb_find_object(
        parent_object_ref_ctypes,
        object_class_ctypes,
        object_name_ctypes,  # type: ignore
        ctypes.pointer(db_object_ref_ctypes),
    )
    _errors.check_for_error(result.value)
    return db_object_ref_ctypes.value


def nxdb_delete_object(
    db_object_ref,  # type: int
):
    # type: (...) -> None
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(db_object_ref)
    result = _cfuncs.lib.nxdb_delete_object(
        db_object_ref_ctypes,
    )
    _errors.check_for_error(result.value)


def nxdb_save_database(
    database_ref,  # type: int
    db_filepath,  # type: typing.Text
):
    # type: (...) -> None
    database_ref_ctypes = _ctypedefs.nxDatabaseRef_t(database_ref)
    db_filepath_ctypes = ctypes.create_string_buffer(db_filepath.encode('ascii'))
    result = _cfuncs.lib.nxdb_save_database(
        database_ref_ctypes,
        db_filepath_ctypes,  # type: ignore
    )
    _errors.check_for_error(result.value)


def nxdb_get_property_size(
    db_object_ref,  # type: int
    property_id,  # type: int
):
    # type: (...) -> int
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(db_object_ref)
    property_id_ctypes = _ctypedefs.u32(property_id)
    property_size_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nxdb_get_property_size(
        db_object_ref_ctypes,
        property_id_ctypes,
        ctypes.pointer(property_size_ctypes),
    )
    _errors.check_for_error(result.value)
    return property_size_ctypes.value


def nxdb_get_dbc_attribute_size(
    db_object_ref,  # type: int
    mode,  # type: _enums.GetDbcAttributeMode
    attribute_name,  # type: typing.Text
):
    # type: (...) -> int
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(db_object_ref)
    mode_ctypes = _ctypedefs.u32(mode.value)
    attribute_name_ctypes = ctypes.create_string_buffer(attribute_name.encode('ascii'))
    attribute_text_size_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nxdb_get_dbc_attribute_size(
        db_object_ref_ctypes,
        mode_ctypes,
        attribute_name_ctypes,  # type: ignore
        ctypes.pointer(attribute_text_size_ctypes),
    )
    _errors.check_for_error(result.value)
    return attribute_text_size_ctypes.value


def nxdb_get_dbc_attribute(
    db_object_ref,  # type: int
    mode,  # type:  _enums.GetDbcAttributeMode
    attribute_name,  # type: typing.Text
    attribute_text_size,  # type: int
):
    # type: (...) -> typing.Tuple[typing.Text, bool]
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(db_object_ref)
    mode_ctypes = _ctypedefs.u32(mode.value)
    attribute_name_ctypes = ctypes.create_string_buffer(attribute_name.encode('ascii'))
    attribute_text_size_ctypes = _ctypedefs.u32(attribute_text_size)
    attribute_text_ctypes = ctypes.create_string_buffer(attribute_text_size)
    is_default_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nxdb_get_dbc_attribute(
        db_object_ref_ctypes,
        mode_ctypes,
        attribute_name_ctypes,  # type: ignore
        attribute_text_size_ctypes,
        attribute_text_ctypes,  # type: ignore
        ctypes.pointer(is_default_ctypes),
    )
    _errors.check_for_error(result.value)
    attribute_text = attribute_text_ctypes.value.decode("ascii")
    is_default = bool(is_default_ctypes.value)
    return attribute_text, is_default


def nxdb_merge(
    target_cluster_ref,  # type: int
    source_obj_ref,  # type: int
    copy_mode,  # type: int
    prefix,  # type: typing.Text
    wait_for_complete,  # type: bool
):
    # type: (...) -> int
    target_cluster_ref_ctypes = _ctypedefs.nxDatabaseRef_t(target_cluster_ref)
    source_obj_ref_ctypes = _ctypedefs.nxDatabaseRef_t(source_obj_ref)
    copy_mode_ctypes = _ctypedefs.u32(copy_mode)
    prefix_ctypes = ctypes.create_string_buffer(prefix.encode('ascii'))
    wait_for_complete_ctypes = _ctypedefs.bool32(wait_for_complete)
    percent_complete_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nxdb_merge(
        target_cluster_ref_ctypes,
        source_obj_ref_ctypes,
        copy_mode_ctypes,
        prefix_ctypes,  # type: ignore
        wait_for_complete_ctypes,
        ctypes.pointer(percent_complete_ctypes),
    )
    _errors.check_for_error(result.value)
    return percent_complete_ctypes.value


def nxdb_add_alias(
    database_alias,  # type: typing.Text
    database_filepath,  # type: typing.Text
    default_baud_rate,  # type: int
):
    # type: (...) -> None
    database_alias_ctypes = ctypes.create_string_buffer(database_alias.encode('ascii'))
    database_filepath_ctypes = ctypes.create_string_buffer(database_filepath.encode('ascii'))
    default_baud_rate_ctypes = _ctypedefs.u32(default_baud_rate)
    result = _cfuncs.lib.nxdb_add_alias(
        database_alias_ctypes,  # type: ignore
        database_filepath_ctypes,  # type: ignore
        default_baud_rate_ctypes,
    )
    _errors.check_for_error(result.value)


def nxdb_add_alias64(
    database_alias,  # type: typing.Text
    database_filepath,  # type: typing.Text
    default_baud_rate,  # type: int
):
    # type: (...) -> None
    database_alias_ctypes = ctypes.create_string_buffer(database_alias.encode('ascii'))
    database_filepath_ctypes = ctypes.create_string_buffer(database_filepath.encode('ascii'))
    default_baud_rate_ctypes = _ctypedefs.u64(default_baud_rate)
    result = _cfuncs.lib.nxdb_add_alias64(
        database_alias_ctypes,  # type: ignore
        database_filepath_ctypes,  # type: ignore
        default_baud_rate_ctypes,
    )
    _errors.check_for_error(result.value)


def nxdb_remove_alias(
    database_alias,  # type: typing.Text
):
    # type: (...) -> None
    database_alias_ctypes = ctypes.create_string_buffer(database_alias.encode('ascii'))
    result = _cfuncs.lib.nxdb_remove_alias(
        database_alias_ctypes,  # type: ignore
    )
    _errors.check_for_error(result.value)


def nxdb_deploy(
    ip_address,  # type: typing.Text
    database_alias,  # type: typing.Text
    wait_for_complete,  # type: bool
):
    # type: (...) -> int
    ip_address_ctypes = ctypes.create_string_buffer(ip_address.encode('ascii'))
    database_alias_ctypes = ctypes.create_string_buffer(database_alias.encode('ascii'))
    wait_for_complete_ctypes = _ctypedefs.bool32(wait_for_complete)
    percent_complete_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nxdb_deploy(
        ip_address_ctypes,  # type: ignore
        database_alias_ctypes,  # type: ignore
        wait_for_complete_ctypes,
        ctypes.pointer(percent_complete_ctypes),
    )
    _errors.check_for_error(result.value)
    return percent_complete_ctypes.value


def nxdb_undeploy(
    ip_address,  # type: typing.Text
    database_alias,  # type: typing.Text
):
    # type: (...) -> None
    ip_address_ctypes = ctypes.create_string_buffer(ip_address.encode('ascii'))
    database_alias_ctypes = ctypes.create_string_buffer(database_alias.encode('ascii'))
    result = _cfuncs.lib.nxdb_undeploy(
        ip_address_ctypes,  # type: ignore
        database_alias_ctypes,  # type: ignore
    )
    _errors.check_for_error(result.value)


def nxdb_get_database_list(
    ip_address,  # type: typing.Text
    size_of_alias_buffer,  # type: int
    size_of_filepath_buffer,  # type: int
):
    # type: (...) -> typing.Tuple[typing.Text, typing.Text, int]
    ip_address_ctypes = ctypes.create_string_buffer(ip_address.encode('ascii'))
    size_of_alias_buffer_ctypes = _ctypedefs.u32(size_of_alias_buffer)
    size_of_filepath_buffer_ctypes = _ctypedefs.u32(size_of_filepath_buffer)
    alias_buffer_ctypes = ctypes.create_string_buffer(size_of_alias_buffer)
    filepath_buffer_ctypes = ctypes.create_string_buffer(size_of_filepath_buffer)
    number_of_databases_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nxdb_get_database_list(
        ip_address_ctypes,  # type: ignore
        size_of_alias_buffer_ctypes,
        alias_buffer_ctypes,  # type: ignore
        size_of_filepath_buffer_ctypes,
        filepath_buffer_ctypes,  # type: ignore
        number_of_databases_ctypes,
    )
    _errors.check_for_error(result.value)
    alias_buffer = alias_buffer_ctypes.value.decode("ascii")
    filepath_buffer = filepath_buffer_ctypes.value.decode("ascii")
    return alias_buffer, filepath_buffer, number_of_databases_ctypes.value


def nxdb_get_database_list_sizes(
    ip_address,  # type: typing.Text
):
    # type: (...) -> typing.Tuple[int, int]
    ip_address_ctypes = ctypes.create_string_buffer(ip_address.encode('ascii'))
    size_of_alias_buffer_ctypes = _ctypedefs.u32()
    size_of_filepath_buffer_ctypes = _ctypedefs.u32()
    result = _cfuncs.lib.nxdb_get_database_list_sizes(
        ip_address_ctypes,  # type: ignore
        size_of_alias_buffer_ctypes,
        size_of_filepath_buffer_ctypes,
    )
    _errors.check_for_error(result.value)
    return size_of_alias_buffer_ctypes.value, size_of_filepath_buffer_ctypes.value
