from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes

from nixnet import _cfuncs
from nixnet import _ctypedefs
from nixnet import _errors
from nixnet import _funcs


CHAR_SIZE = 1
BOOL_SIZE = 1
U8_SIZE = 1
U32_SIZE = 4
U64_SIZE = 4
F64_SIZE = 4
REF_SIZE = 4


def get_session_bool(ref, prop_id):
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(BOOL_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.u8)()
    status = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return bool(value_ctypes.value)


def set_session_bool(ref, prop_id, value):
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(BOOL_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.u8)(1 if value else 0)
    status = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_session_u32(ref, prop_id):
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(U32_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.u32)()
    status = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_session_u32(ref, prop_id, value):
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(U32_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.u32)(value)
    status = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_session_u32_array(ref, prop_id):
    value_size = _funcs.get_property_size(ref, prop_id)

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.u32 * (value_size // U32_SIZE)
    status = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_session_u32_array(ref, prop_id, value):
    value_size = len(value) * U32_SIZE

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.u32 * (value_size // U32_SIZE)(value)
    status = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_session_u64(ref, prop_id):
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(U64_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.u64)()
    status = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_session_u64(ref, prop_id, value):
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(U64_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.u64)(value)
    status = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_session_f64(ref, prop_id):
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(F64_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.f64)()
    status = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_session_f64(ref, prop_id, value):
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(F64_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.f64)(value)
    status = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_session_string(ref, prop_id):
    value_size = _funcs.get_property_size(ref, prop_id)

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.char * (value_size // CHAR_SIZE)
    status = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_session_string(ref, prop_id, value):
    value_size = len(value) * CHAR_SIZE

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.u32 * (value_size // CHAR_SIZE)(value.encode("ascii"))
    status = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_session_string_array(ref, prop_id):
    value = get_session_string(ref, prop_id)
    return value.split(",")


def get_session_ref(ref, prop_id):
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(REF_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.nxSessionRef_t)()
    status = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_session_ref(ref, prop_id, value):
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(REF_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.nxSessionRef_t)(value)
    status = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_session_ref_array(ref, prop_id):
    value_size = _funcs.get_property_size(ref, prop_id)

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.nxSessionRef_t * (value_size // REF_SIZE)
    status = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_session_ref_array(ref, prop_id, value):
    value_size = len(value) * REF_SIZE

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.nxSessionRef_t * (value_size // REF_SIZE)(value)
    status = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def set_session_sub_u32(ref, sub, prop_id, value):
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    sub_ctypes = _ctypedefs.u32(sub)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(U32_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.u32)(value)
    status = _cfuncs.lib.nx_set_sub_property(
        ref_ctypes,
        sub_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def set_session_sub_f64(ref, sub, prop_id, value):
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    sub_ctypes = _ctypedefs.u32(sub)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(F64_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.f64)(value)
    status = _cfuncs.lib.nx_set_sub_property(
        ref_ctypes,
        sub_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def set_session_sub_string(ref, sub, prop_id, value):
    value_size = len(value) * CHAR_SIZE

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    sub_ctypes = _ctypedefs.u32(sub)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.u32 * (value_size // CHAR_SIZE)(value.encode("ascii"))
    status = _cfuncs.lib.nx_set_sub_property(
        ref_ctypes,
        sub_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_database_bool(ref, prop_id):
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(BOOL_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.u8)()
    status = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return bool(value_ctypes.value)


def set_database_bool(ref, prop_id, value):
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(BOOL_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.u8)(1 if value else 0)
    status = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_database_u8_array(ref, prop_id):
    value_size = _funcs.get_property_size(ref, prop_id)

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.u8 * (value_size // U8_SIZE)
    status = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_database_u8_array(ref, prop_id, value):
    value_size = len(value) * U8_SIZE

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.u8 * (value_size // U8_SIZE)(value)
    status = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_database_u32(ref, prop_id):
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(U32_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.u32)()
    status = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_database_u32(ref, prop_id, value):
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(U32_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.u32)(value)
    status = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_database_u32_array(ref, prop_id):
    value_size = _funcs.get_property_size(ref, prop_id)

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.u32 * (value_size // U32_SIZE)
    status = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_database_u32_array(ref, prop_id, value):
    value_size = len(value) * U32_SIZE

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.u32 * (value_size // U32_SIZE)(value)
    status = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_database_u64(ref, prop_id):
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(U64_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.u64)()
    status = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_database_u64(ref, prop_id, value):
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(U64_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.u64)(value)
    status = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_database_f64(ref, prop_id):
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(F64_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.f64)()
    status = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_database_f64(ref, prop_id, value):
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(F64_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.f64)(value)
    status = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_database_string(ref, prop_id):
    value_size = _funcs.get_property_size(ref, prop_id)

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.char * (value_size // CHAR_SIZE)
    status = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_database_string(ref, prop_id, value):
    value_size = len(value) * CHAR_SIZE

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.u32 * (value_size // CHAR_SIZE)(value.encode("ascii"))
    status = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_database_ref(ref, prop_id):
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(REF_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)()
    status = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_database_ref(ref, prop_id, value):
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(REF_SIZE)
    value_ctypes = ctypes.POINTER(_ctypedefs.nxDatabaseRef_t)(value)
    status = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)


def get_database_ref_array(ref, prop_id):
    value_size = _funcs.get_property_size(ref, prop_id)

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.nxDatabaseRef_t * (value_size // REF_SIZE)
    status = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
    return value_ctypes.value


def set_database_ref_array(ref, prop_id, value):
    value_size = len(value) * REF_SIZE

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = _ctypedefs.nxDatabaseRef_t * (value_size // REF_SIZE)(value)
    status = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)
    _errors.check_for_error(status)
