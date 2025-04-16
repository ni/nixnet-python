import ctypes  # type: ignore
import typing  # NOQA: F401

from nixnet import _cfuncs
from nixnet import _ctypedefs
from nixnet import _errors
from nixnet import _funcs


def get_session_bool(ref, prop_id):
    # type: (int, int) -> bool
    return bool(get_session_u8(ref, prop_id))


def set_session_bool(ref, prop_id, value):
    # type: (int, int, bool) -> None
    set_session_u8(ref, prop_id, 1 if value else 0)


def get_session_u8(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.bool8.BYTES)
    value_ctypes = _ctypedefs.u8()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_session_u8(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.bool8.BYTES)
    value_ctypes = _ctypedefs.u8(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_session_u32(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u32.BYTES)
    value_ctypes = _ctypedefs.u32()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_session_u32(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u32.BYTES)
    value_ctypes = _ctypedefs.u32(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_session_u32_array(ref, prop_id):
    # type: (int, int) -> typing.Iterable[int]
    value_size = _funcs.nx_get_property_size(ref, prop_id)
    elements = value_size // _ctypedefs.u32.BYTES

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.u32 * (elements))()  # type: ignore
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
    for value in value_ctypes:
        yield value.value


def set_session_u32_array(ref, prop_id, value):
    # type: (int, int, typing.List[int]) -> None
    value_size = len(value) * _ctypedefs.u32.BYTES
    elements = value_size // _ctypedefs.u32.BYTES

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.u32 * (elements))(*value)  # type: ignore
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)


def get_session_u64(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u64.BYTES)
    value_ctypes = _ctypedefs.u64()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_session_u64(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u64.BYTES)
    value_ctypes = _ctypedefs.u64(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_session_f64(ref, prop_id):
    # type: (int, int) -> float
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.f64.BYTES)
    value_ctypes = _ctypedefs.f64()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_session_f64(ref, prop_id, value):
    # type: (int, int, float) -> None
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.f64.BYTES)
    value_ctypes = _ctypedefs.f64(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_session_string(ref, prop_id):
    # type: (int, int) -> typing.Text
    value_size = _funcs.nx_get_property_size(ref, prop_id)

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = ctypes.create_string_buffer(value_size)
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value.decode("ascii")


def set_session_string(ref, prop_id, value):
    # type: (int, int, typing.Text) -> None
    value_bytes = value.encode("ascii")
    value_size = len(value_bytes) * _ctypedefs.char.BYTES

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = ctypes.create_string_buffer(value_bytes)
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)


def get_session_string_array(ref, prop_id):
    # type: (int, int) -> typing.List[typing.Text]
    value = get_session_string(ref, prop_id)
    return value.split(",")


def get_session_ref(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.nxSessionRef_t.BYTES)
    value_ctypes = _ctypedefs.nxSessionRef_t()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_session_ref(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.nxSessionRef_t.BYTES)
    value_ctypes = _ctypedefs.nxSessionRef_t(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_session_ref_array_len(ref, prop_id):
    # type: (int, int) -> int
    value_size = _funcs.nx_get_property_size(ref, prop_id)
    elements = value_size // _ctypedefs.nxSessionRef_t.BYTES
    return elements


def get_session_ref_array(ref, prop_id):
    # type: (int, int) -> typing.Iterable[int]
    value_size = _funcs.nx_get_property_size(ref, prop_id)
    elements = value_size // _ctypedefs.nxSessionRef_t.BYTES

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.nxSessionRef_t * (elements))()  # type: ignore
    result = _cfuncs.lib.nx_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
    for value in value_ctypes:
        yield value.value


def set_session_ref_array(ref, prop_id, value):
    # type: (int, int, typing.List[int]) -> None
    value_size = len(value) * _ctypedefs.nxSessionRef_t.BYTES
    elements = value_size // _ctypedefs.nxSessionRef_t.BYTES

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.nxSessionRef_t * (elements))(*value)  # type: ignore
    result = _cfuncs.lib.nx_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)


def set_session_sub_u32(ref, sub, prop_id, value):
    # type: (int, int, int, int) -> None
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    sub_ctypes = _ctypedefs.u32(sub)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u32.BYTES)
    value_ctypes = _ctypedefs.u32(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_set_sub_property(
        ref_ctypes,
        sub_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def set_session_sub_f64(ref, sub, prop_id, value):
    # type: (int, int, int, float) -> None
    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    sub_ctypes = _ctypedefs.u32(sub)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.f64.BYTES)
    value_ctypes = _ctypedefs.f64(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nx_set_sub_property(
        ref_ctypes,
        sub_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def set_session_sub_string(ref, sub, prop_id, value):
    # type: (int, int, int, typing.Text) -> None
    value_bytes = value.encode("ascii")
    value_size = len(value_bytes) * _ctypedefs.char.BYTES

    ref_ctypes = _ctypedefs.nxSessionRef_t(ref)
    sub_ctypes = _ctypedefs.u32(sub)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = ctypes.create_string_buffer(value_bytes)
    result = _cfuncs.lib.nx_set_sub_property(
        ref_ctypes,
        sub_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_bool(ref, prop_id):
    # type: (int, int) -> bool
    return bool(get_database_u8(ref, prop_id))


def set_database_bool(ref, prop_id, value):
    # type: (int, int, bool) -> None
    set_database_u8(ref, prop_id, 1 if value else 0)


def get_database_u8(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.bool8.BYTES)
    value_ctypes = _ctypedefs.u8()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_database_u8(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.bool8.BYTES)
    value_ctypes = _ctypedefs.u8(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_u8_array(ref, prop_id):
    # type: (int, int) -> typing.Iterable[int]
    value_size = _funcs.nxdb_get_property_size(ref, prop_id)
    elements = value_size // _ctypedefs.u8.BYTES

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.u8 * (elements))()  # type: ignore
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
    for value in value_ctypes:
        yield value.value


def set_database_u8_array(ref, prop_id, value):
    # type: (int, int, typing.List[int]) -> None
    value_size = len(value) * _ctypedefs.u8.BYTES
    elements = value_size // _ctypedefs.u8.BYTES

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.u8 * (elements))(*value)  # type: ignore
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_u32(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u32.BYTES)
    value_ctypes = _ctypedefs.u32()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_database_u32(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u32.BYTES)
    value_ctypes = _ctypedefs.u32(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_u32_array(ref, prop_id):
    # type: (int, int) -> typing.Iterable[int]
    value_size = _funcs.nxdb_get_property_size(ref, prop_id)
    elements = value_size // _ctypedefs.u32.BYTES

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.u32 * (elements))()  # type: ignore
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
    for value in value_ctypes:
        yield value.value


def set_database_u32_array(ref, prop_id, value):
    # type: (int, int, typing.List[int]) -> None
    value_size = len(value) * _ctypedefs.u32.BYTES
    elements = value_size // _ctypedefs.u32.BYTES

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.u32 * (elements))(*value)  # type: ignore
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_u64(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u64.BYTES)
    value_ctypes = _ctypedefs.u64()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_database_u64(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.u64.BYTES)
    value_ctypes = _ctypedefs.u64(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_f64(ref, prop_id):
    # type: (int, int) -> float
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.f64.BYTES)
    value_ctypes = _ctypedefs.f64()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_database_f64(ref, prop_id, value):
    # type: (int, int, float) -> None
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.f64.BYTES)
    value_ctypes = _ctypedefs.f64(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_string(ref, prop_id):
    # type: (int, int) -> typing.Text
    value_size = _funcs.nxdb_get_property_size(ref, prop_id)

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = ctypes.create_string_buffer(value_size)
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value.decode("ascii")


def set_database_string(ref, prop_id, value):
    # type: (int, int, typing.Text) -> None
    value_bytes = value.encode("ascii")
    value_size = len(value_bytes) * _ctypedefs.char.BYTES

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = ctypes.create_string_buffer(value_bytes)
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_ref(ref, prop_id):
    # type: (int, int) -> int
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.nxDatabaseRef_t.BYTES)
    value_ctypes = _ctypedefs.nxDatabaseRef_t()
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)
    return value_ctypes.value


def set_database_ref(ref, prop_id, value):
    # type: (int, int, int) -> None
    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(_ctypedefs.nxDatabaseRef_t.BYTES)
    value_ctypes = _ctypedefs.nxDatabaseRef_t(value)
    value_ctypes_ptr = ctypes.pointer(value_ctypes)
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes_ptr)  # type: ignore
    _errors.check_for_error(result.value)


def get_database_ref_array_len(ref, prop_id):
    # type: (int, int) -> int
    value_size = _funcs.nxdb_get_property_size(ref, prop_id)
    elements = value_size // _ctypedefs.nxDatabaseRef_t.BYTES
    return elements


def get_database_ref_array(ref, prop_id):
    # type: (int, int) -> typing.Iterable[int]
    value_size = _funcs.nxdb_get_property_size(ref, prop_id)
    elements = value_size // _ctypedefs.nxDatabaseRef_t.BYTES

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.nxDatabaseRef_t * (elements))()  # type: ignore
    result = _cfuncs.lib.nxdb_get_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
    for value in value_ctypes:
        yield value.value


def set_database_ref_array(ref, prop_id, value):
    # type: (int, int, typing.List[int]) -> None
    value_size = len(value) * _ctypedefs.nxDatabaseRef_t.BYTES
    elements = value_size // _ctypedefs.nxDatabaseRef_t.BYTES

    ref_ctypes = _ctypedefs.nxDatabaseRef_t(ref)
    prop_id_ctypes = _ctypedefs.u32(prop_id)
    prop_size_ctypes = _ctypedefs.u32(value_size)
    value_ctypes = (_ctypedefs.nxDatabaseRef_t * (elements))(*value)  # type: ignore
    result = _cfuncs.lib.nxdb_set_property(
        ref_ctypes,
        prop_id_ctypes,
        prop_size_ctypes,
        value_ctypes)  # type: ignore
    _errors.check_for_error(result.value)
