from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes

from nixnet import _cfuncs
from nixnet import _ctypedefs
from nixnet import _errors


def nx_create_session(
        database_name,
        cluster_name,
        list,
        interface,
        mode):
    database_name_ctypes = _ctypedefs.char_p(database_name)
    cluster_name_ctypes = _ctypedefs.char_p(cluster_name)
    list_ctypes = _ctypedefs.char_p(list)
    interface_ctypes = _ctypedefs.char_p(interface)
    mode_ctypes = _ctypedefs.u32(mode)
    session_ref_ctypes = ctypes.POINTER(_ctypedefs.nxSessionRef_t)()
    status = _cfuncs.lib.nx_create_session(
        database_name_ctypes,
        cluster_name_ctypes,
        list_ctypes,
        interface_ctypes,
        mode_ctypes,
        session_ref_ctypes)
    _errors.check_for_error(status)
    return session_ref_ctypes.value


def nx_create_session_by_ref(
        database_refs,
        interface,
        mode):
    size_of_database_refs_ctypes = _ctypedefs.u32(len(database_refs) * _ctypedefs.nxDatabaseRef_t.BYTES)
    database_refs_ctypes = ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)(database_refs)
    interface_ctypes = _ctypedefs.char_p(interface)
    mode_ctypes = _ctypedefs.u32(mode)
    session_ref_ctypes = ctypes.POINTER(_ctypedefs.nxSessionRef_t)()
    status = _cfuncs.lib.nx_create_session_by_ref(
        size_of_database_refs_ctypes,
        database_refs_ctypes,
        interface_ctypes,
        mode_ctypes,
        session_ref_ctypes)
    _errors.check_for_error(status)
    return session_ref_ctypes.value


def nx_get_property_size(
        session_ref,
        property_id):
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    property_id_ctypes = _ctypedefs.u32(property_id)
    property_size_ctypes = ctypes.POINTER(_ctypedefs.u32)()
    status = _cfuncs.lib.nx_get_property_size(
        session_ref_ctypes,
        property_id_ctypes,
        property_size_ctypes)
    _errors.check_for_error(status)
    return property_size_ctypes.value


def nx_get_sub_property_size(
        session_ref,
        active_index,
        property_id):
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    active_index_ctypes = _ctypedefs.u32(active_index)
    property_id_ctypes = _ctypedefs.u32(property_id)
    property_size_ctypes = ctypes.POINTER(_ctypedefs.u32)()
    status = _cfuncs.lib.nx_get_sub_property_size(
        session_ref_ctypes,
        active_index_ctypes,
        property_id_ctypes,
        property_size_ctypes)
    _errors.check_for_error(status)
    return property_size_ctypes.value


def nx_read_signal_single_point(session_ref, num_signals):
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    value_buffer_ctypes = _ctypedefs.f64 * num_signals
    size_of_value_buffer_ctypes = _ctypedefs.f64.BYTES * num_signals
    timestamp_buffer_ctypes = _ctypedefs.nxTimestamp_t * num_signals
    size_of_timestamp_buffer_ctypes = _ctypedefs.nxTimestamp_t.BYTES * num_signals
    status = _cfuncs.lib.nx_read_signal_single_point(
        session_ref_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes,
        timestamp_buffer_ctypes,
        size_of_timestamp_buffer_ctypes)
    _errors.check_for_error(status)
    return timestamp_buffer_ctypes.value, value_buffer_ctypes.value


def nx_write_signal_single_point(
        session_ref,
        value_buffer):
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    value_buffer_ctypes = ctypes.POINTER(_ctypedefs.f64)(value_buffer)
    size_of_value_buffer_ctypes = _ctypedefs.u32(len(value_buffer) * _ctypedefs.f64.BYTES)
    status = _cfuncs.lib.nx_write_signal_single_point(
        session_ref_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes)
    _errors.check_for_error(status)


def nx_write_signal_waveform(
        session_ref,
        timeout,
        value_buffer):
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    timeout_ctypes = _ctypedefs.f64(timeout)
    value_buffer_ctypes = ctypes.POINTER(_ctypedefs.f64)(value_buffer)
    size_of_value_buffer_ctypes = _ctypedefs.u32(len(value_buffer) * _ctypedefs.f64.BYTES)
    status = _cfuncs.lib.nx_write_signal_waveform(
        session_ref_ctypes,
        timeout_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes)
    _errors.check_for_error(status)


def nx_write_signal_xy(
        session_ref,
        timeout,
        value_buffer,
        timestamp_buffer,
        num_pairs_buffer):
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    timeout_ctypes = _ctypedefs.f64(timeout)
    value_buffer_ctypes = ctypes.POINTER(_ctypedefs.f64)(value_buffer)
    size_of_value_buffer_ctypes = _ctypedefs.u32(len(value_buffer) * _ctypedefs.f64.BYTES)
    timestamp_buffer_ctypes = ctypes.POINTER(_ctypedefs.nxTimestamp_t)(timestamp_buffer)
    size_of_timestamp_buffer_ctypes = _ctypedefs.u32(len(timestamp_buffer) * _ctypedefs.nxTimestamp_t.BYTES)
    num_pairs_buffer_ctypes = ctypes.POINTER(_ctypedefs.u32)(num_pairs_buffer)
    size_of_num_pairs_buffer_ctypes = _ctypedefs.u32(len(num_pairs_buffer) * _ctypedefs.u32.BYTES)
    status = _cfuncs.lib.nx_write_signal_xy(
        session_ref_ctypes,
        timeout_ctypes,
        value_buffer_ctypes,
        size_of_value_buffer_ctypes,
        timestamp_buffer_ctypes,
        size_of_timestamp_buffer_ctypes,
        num_pairs_buffer_ctypes,
        size_of_num_pairs_buffer_ctypes)
    _errors.check_for_error(status)


def nx_blink(
        interface_ref,
        modifier):
    interface_ref_ctypes = _ctypedefs.nxSessionRef_t(interface_ref)
    modifier_ctypes = _ctypedefs.u32(modifier)
    status = _cfuncs.lib.nx_blink(
        interface_ref_ctypes,
        modifier_ctypes)
    _errors.check_for_error(status)


def nx_clear(
        session_ref):
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    status = _cfuncs.lib.nx_clear(
        session_ref_ctypes)
    _errors.check_for_error(status)


def nx_connect_terminals(
        session_ref,
        source,
        destination):
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    source_ctypes = _ctypedefs.char_p(source)
    destination_ctypes = _ctypedefs.char_p(destination)
    status = _cfuncs.lib.nx_connect_terminals(
        session_ref_ctypes,
        source_ctypes,
        destination_ctypes)
    _errors.check_for_error(status)


def nx_disconnect_terminals(
        session_ref,
        source,
        destination):
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    source_ctypes = _ctypedefs.char_p(source)
    destination_ctypes = _ctypedefs.char_p(destination)
    status = _cfuncs.lib.nx_disconnect_terminals(
        session_ref_ctypes,
        source_ctypes,
        destination_ctypes)
    _errors.check_for_error(status)


def nx_flush(
        session_ref):
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    status = _cfuncs.lib.nx_flush(
        session_ref_ctypes)
    _errors.check_for_error(status)


def nx_start(
        session_ref,
        scope):
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    scope_ctypes = _ctypedefs.u32(scope)
    status = _cfuncs.lib.nx_start(
        session_ref_ctypes,
        scope_ctypes)
    _errors.check_for_error(status)


def nx_stop(
        session_ref,
        scope):
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    scope_ctypes = _ctypedefs.u32(scope)
    status = _cfuncs.lib.nx_stop(
        session_ref_ctypes,
        scope_ctypes)
    _errors.check_for_error(status)


def nx_system_open():
    system_ref_ctypes = ctypes.POINTER(_ctypedefs.nxSessionRef_t)()
    status = _cfuncs.lib.nx_system_open(
        system_ref_ctypes)
    _errors.check_for_error(status)
    return system_ref_ctypes.value


def nx_system_close(
        system_ref):
    system_ref_ctypes = _ctypedefs.nxSessionRef_t(system_ref)
    status = _cfuncs.lib.nx_system_close(
        system_ref_ctypes)
    _errors.check_for_error(status)


def nx_wait(
        session_ref,
        condition,
        param_in,
        timeout):
    session_ref_ctypes = _ctypedefs.nxSessionRef_t(session_ref)
    condition_ctypes = _ctypedefs.u32(condition)
    param_in_ctypes = _ctypedefs.u32(param_in)
    timeout_ctypes = _ctypedefs.f64(timeout)
    param_out_ctypes = ctypes.POINTER(_ctypedefs.u32)()
    status = _cfuncs.lib.nx_wait(
        session_ref_ctypes,
        condition_ctypes,
        param_in_ctypes,
        timeout_ctypes,
        param_out_ctypes)
    _errors.check_for_error(status)
    return param_out_ctypes.value


def nxdb_open_database(
        database_name):
    database_name_ctypes = _ctypedefs.char_p(database_name)
    database_ref_ctypes = ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)()
    status = _cfuncs.lib.nxdb_open_database(
        database_name_ctypes,
        database_ref_ctypes)
    _errors.check_for_error(status)
    return database_ref_ctypes.value


def nxdb_close_database(
        database_ref,
        close_all_refs):
    database_ref_ctypes = _ctypedefs.nxDatabaseRef_t(database_ref)
    close_all_refs_ctypes = _ctypedefs.bool32(close_all_refs)
    status = _cfuncs.lib.nxdb_close_database(
        database_ref_ctypes,
        close_all_refs_ctypes)
    _errors.check_for_error(status)


def nxdb_create_object(
        parent_object_ref,
        object_class,
        object_name):
    parent_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(parent_object_ref)
    object_class_ctypes = _ctypedefs.u32(object_class)
    object_name_ctypes = _ctypedefs.char_p(object_name)
    db_object_ref_ctypes = ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)()
    status = _cfuncs.lib.nxdb_create_object(
        parent_object_ref_ctypes,
        object_class_ctypes,
        object_name_ctypes,
        db_object_ref_ctypes)
    _errors.check_for_error(status)
    return db_object_ref_ctypes.value


def nxdb_find_object(
        parent_object_ref,
        object_class,
        object_name):
    parent_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(parent_object_ref)
    object_class_ctypes = _ctypedefs.u32(object_class)
    object_name_ctypes = _ctypedefs.char_p(object_name)
    db_object_ref_ctypes = ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)()
    status = _cfuncs.lib.nxdb_find_object(
        parent_object_ref_ctypes,
        object_class_ctypes,
        object_name_ctypes,
        db_object_ref_ctypes)
    _errors.check_for_error(status)
    return db_object_ref_ctypes.value


def nxdb_delete_object(
        db_object_ref):
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(db_object_ref)
    status = _cfuncs.lib.nxdb_delete_object(
        db_object_ref_ctypes)
    _errors.check_for_error(status)


def nxdb_save_database(
        database_ref,
        db_filepath):
    database_ref_ctypes = _ctypedefs.nxDatabaseRef_t(database_ref)
    db_filepath_ctypes = _ctypedefs.char_p(db_filepath)
    status = _cfuncs.lib.nxdb_save_database(
        database_ref_ctypes,
        db_filepath_ctypes)
    _errors.check_for_error(status)


def nxdb_get_property_size(
        db_object_ref,
        property_id):
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(db_object_ref)
    property_id_ctypes = _ctypedefs.u32(property_id)
    property_size_ctypes = ctypes.POINTER(_ctypedefs.u32)()
    status = _cfuncs.lib.nxdb_get_property_size(
        db_object_ref_ctypes,
        property_id_ctypes,
        property_size_ctypes)
    _errors.check_for_error(status)
    return property_size_ctypes.value


def nxdb_get_dbc_attribute_size(
        db_object_ref,
        mode,
        attribute_name):
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(db_object_ref)
    mode_ctypes = _ctypedefs.u32(mode)
    attribute_name_ctypes = _ctypedefs.char_p(attribute_name)
    attribute_text_size_ctypes = ctypes.POINTER(_ctypedefs.u32)()
    status = _cfuncs.lib.nxdb_get_dbc_attribute_size(
        db_object_ref_ctypes,
        mode_ctypes,
        attribute_name_ctypes,
        attribute_text_size_ctypes)
    _errors.check_for_error(status)
    return attribute_text_size_ctypes.value


def nxdb_get_dbc_attribute(
        db_object_ref,
        mode,
        attribute_name,
        attribute_text_size,
        attribute_text):
    db_object_ref_ctypes = _ctypedefs.nxDatabaseRef_t(db_object_ref)
    mode_ctypes = _ctypedefs.u32(mode)
    attribute_name_ctypes = _ctypedefs.char_p(attribute_name)
    attribute_text_size_ctypes = _ctypedefs.u32(attribute_text_size)
    attribute_text_ctypes = _ctypedefs.char_p(attribute_text)
    is_default_ctypes = ctypes.POINTER(_ctypedefs.u32)()
    status = _cfuncs.lib.nxdb_get_dbc_attribute(
        db_object_ref_ctypes,
        mode_ctypes,
        attribute_name_ctypes,
        attribute_text_size_ctypes,
        attribute_text_ctypes,
        is_default_ctypes)
    _errors.check_for_error(status)
    return is_default_ctypes.value


def nxdb_merge(
        target_cluster_ref,
        source_obj_ref,
        copy_mode,
        prefix,
        wait_for_complete):
    target_cluster_ref_ctypes = _ctypedefs.nxDatabaseRef_t(target_cluster_ref)
    source_obj_ref_ctypes = _ctypedefs.nxDatabaseRef_t(source_obj_ref)
    copy_mode_ctypes = _ctypedefs.u32(copy_mode)
    prefix_ctypes = _ctypedefs.char_p(prefix)
    wait_for_complete_ctypes = _ctypedefs.bool32(wait_for_complete)
    percent_complete_ctypes = ctypes.POINTER(_ctypedefs.u32)()
    status = _cfuncs.lib.nxdb_merge(
        target_cluster_ref_ctypes,
        source_obj_ref_ctypes,
        copy_mode_ctypes,
        prefix_ctypes,
        wait_for_complete_ctypes,
        percent_complete_ctypes)
    _errors.check_for_error(status)
    return percent_complete_ctypes.value


def nxdb_add_alias(
        database_alias,
        database_filepath,
        default_baud_rate):
    database_alias_ctypes = _ctypedefs.char_p(database_alias)
    database_filepath_ctypes = _ctypedefs.char_p(database_filepath)
    default_baud_rate_ctypes = _ctypedefs.u32(default_baud_rate)
    status = _cfuncs.lib.nxdb_add_alias(
        database_alias_ctypes,
        database_filepath_ctypes,
        default_baud_rate_ctypes)
    _errors.check_for_error(status)


def nxdb_add_alias64(
        database_alias,
        database_filepath,
        default_baud_rate):
    database_alias_ctypes = _ctypedefs.char_p(database_alias)
    database_filepath_ctypes = _ctypedefs.char_p(database_filepath)
    default_baud_rate_ctypes = _ctypedefs.u64(default_baud_rate)
    status = _cfuncs.lib.nxdb_add_alias64(
        database_alias_ctypes,
        database_filepath_ctypes,
        default_baud_rate_ctypes)
    _errors.check_for_error(status)


def nxdb_remove_alias(
        database_alias):
    database_alias_ctypes = _ctypedefs.char_p(database_alias)
    status = _cfuncs.lib.nxdb_remove_alias(
        database_alias_ctypes)
    _errors.check_for_error(status)


def nxdb_deploy(
        ip_address,
        database_alias,
        wait_for_complete):
    ip_address_ctypes = _ctypedefs.char_p(ip_address)
    database_alias_ctypes = _ctypedefs.char_p(database_alias)
    wait_for_complete_ctypes = _ctypedefs.bool32(wait_for_complete)
    percent_complete_ctypes = ctypes.POINTER(_ctypedefs.u32)()
    status = _cfuncs.lib.nxdb_deploy(
        ip_address_ctypes,
        database_alias_ctypes,
        wait_for_complete_ctypes,
        percent_complete_ctypes)
    _errors.check_for_error(status)
    return percent_complete_ctypes.value


def nxdb_undeploy(
        ip_address,
        database_alias):
    ip_address_ctypes = _ctypedefs.char_p(ip_address)
    database_alias_ctypes = _ctypedefs.char_p(database_alias)
    status = _cfuncs.lib.nxdb_undeploy(
        ip_address_ctypes,
        database_alias_ctypes)
    _errors.check_for_error(status)
