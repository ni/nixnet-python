"""
Definition of types for calling into NI-XNET.

Distinct types (rather than aliases) are used to allow more accurate type
checking.
"""


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes  # type: ignore


class char(ctypes.c_char):  # NOQA: N801

    BYTES = 1


class char_p(ctypes.c_char_p):  # NOQA: N801
    pass


class bool8(ctypes.c_ubyte):  # NOQA: N801
    """32-bit boolean C-type."""

    BYTES = 1

    @classmethod
    def from_param(cls, param):
        return ctypes.c_ubyte(1) if bool(param) else ctypes.c_ubyte(0)


class bool32(ctypes.c_uint):  # NOQA: N801
    """32-bit boolean C-type."""

    BYTES = 4

    @classmethod
    def from_param(cls, param):
        return ctypes.c_uint(1) if bool(param) else ctypes.c_uint(0)


class byte(ctypes.c_char):  # NOQA: N801

    BYTES = 1


class i8(ctypes.c_byte):  # NOQA: N801

    BYTES = 1


class i16(ctypes.c_short):  # NOQA: N801

    BYTES = 2


class i32(ctypes.c_int):  # NOQA: N801

    BYTES = 4


class i64(ctypes.c_longlong):  # NOQA: N801

    BYTES = 8


class u8(ctypes.c_ubyte):  # NOQA: N801

    BYTES = 1


class u16(ctypes.c_ushort):  # NOQA: N801

    BYTES = 2


class u32(ctypes.c_uint):  # NOQA: N801

    BYTES = 4


class u64(ctypes.c_ulonglong):  # NOQA: N801

    BYTES = 8


class f32(ctypes.c_float):  # NOQA: N801

    BYTES = 4


class f64(ctypes.c_double):  # NOQA: N801

    BYTES = 8


class nxVoidPtr(ctypes.c_void_p):  # NOQA: N801
    pass


class nxSessionRef_t(u32):  # NOQA: N801
    pass


class nxDatabaseRef_t(u32):  # NOQA: N801
    pass


class nxStatus_t(u32):  # NOQA: N801
    pass


class nxTimestamp_t(u64):  # NOQA: N801
    """"Absolute time, given in 100 ns increments since Jan 1, 1601, 12:00 AM UTC."""
    pass


class nxFlexRayStats_t(ctypes.Structure):  # NOQA: N801
    _fields_ = [
        ("NumSyntaxErrorChA", u32),
        ("NumSyntaxErrorChB", u32),
        ("NumContextErrorChA", u32),
        ("NumContextErrorChB", u32),
        ("NumSlotBoundaryViolationChA", u32),
        ("NumSlotBoundaryViolationChB", u32)]


class nxJ1939CommState_t(ctypes.Structure):  # NOQA: N801
    _fields_ = [
        ("PGN", u32),
        ("SourceAddress", u8),
        ("DestinationAddress", u8),
        ("TransmitError", u8),
        ("ReceiveError", u8),
        ("Reserved1", u32),
        ("Reserved2", u32)]
