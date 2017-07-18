from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import struct

from nixnet import _cconsts
from nixnet import _errors
from nixnet import constants
from nixnet import types


nxFrameFixed_t = struct.Struct('QIBBBB8s')  # NOQA: N801
assert nxFrameFixed_t.size == 24, 'Incorrectly specified frame.'
FRAME_TIMESTAMP_INDEX = 0
FRAME_IDENTIFIER_INDEX = 1
FRAME_TYPE_INDEX = 2
FRAME_FLAG_INDEX = 3
FRAME_INFO_INDEX = 4
FRAME_PAYLOAD_LENGTH_INDEX = 5
FRAME_PAYLOAD_INDEX = 6

MAX_BASE_UNIT_PAYLOAD_LENGTH = 8


def _get_frame_payload_length(base):
    """Extract the payload length from a base unit.

    >>> blank_payload = 8 * b'\\0'
    >>> no_payload = nxFrameFixed_t.unpack(nxFrameFixed_t.pack(0, 0, 0, 0, 0, 0x0, blank_payload))
    >>> _get_frame_payload_length(no_payload)
    0
    >>> base_payload = nxFrameFixed_t.unpack(nxFrameFixed_t.pack(0, 0, 0, 0, 0, 0x8, blank_payload))
    >>> _get_frame_payload_length(base_payload)
    8
    >>> extra_payload = nxFrameFixed_t.unpack(nxFrameFixed_t.pack(0, 0, 0, 0, 0, 0xFF, blank_payload))
    >>> _get_frame_payload_length(extra_payload)
    255
    >>> j1939_type = _cconsts.NX_FRAME_TYPE_J1939_DATA
    >>> j1939 = nxFrameFixed_t.unpack(nxFrameFixed_t.pack(0, 0, j1939_type, 0, 0xFF, 0xFF, blank_payload))
    >>> _get_frame_payload_length(j1939)
    2047
    """
    payload_length = base[FRAME_PAYLOAD_LENGTH_INDEX]
    if base[FRAME_TYPE_INDEX] == _cconsts.NX_FRAME_TYPE_J1939_DATA:
        # J1939 uses three bits from the Info field as the high bites.
        payload_length |= (base[FRAME_INFO_INDEX] & _cconsts.NX_FRAME_PAYLD_LEN_HIGH_MASK_J1939) << 8
    return payload_length


def _calculate_payload_size(payload_length):
    """For a given payload, return the bytes needed for the payload.

    This is for the entire payload with padding, regardless of which unit it is
    stored in.

    >>> _calculate_payload_size(0)
    8
    >>> _calculate_payload_size(8)
    8
    >>> _calculate_payload_size(9)
    16
    >>> _calculate_payload_size(16)
    16
    """
    if 8 < payload_length:
        return (payload_length + 7) & 0x07F8
    else:
        return 8


def _calculate_payload_unit_size(payload_length):
    """For a given payload, return the bytes needed for the payload unit.

    This includes padding bytes

    >>> _calculate_payload_unit_size(0)
    0
    >>> _calculate_payload_unit_size(8)
    0
    >>> _calculate_payload_unit_size(9)
    8
    >>> _calculate_payload_unit_size(16)
    8
    """
    return _calculate_payload_size(payload_length) - MAX_BASE_UNIT_PAYLOAD_LENGTH


def _split_payload_length(payload_length):
    """Return how much of the payload is stored in the base unit verse the payload unit.

    This is without padding bytes.

    >>> _split_payload_length(0)
    (0, 0)
    >>> _split_payload_length(8)
    (8, 0)
    >>> _split_payload_length(9)
    (8, 1)
    >>> _split_payload_length(16)
    (8, 8)
    """
    payload_unit_length = max(payload_length - MAX_BASE_UNIT_PAYLOAD_LENGTH, 0)
    base_unit_length = payload_length - payload_unit_length
    return base_unit_length, payload_unit_length


def iterate_frames(bytes):
    """Yields RawFrames from the bytes"""
    base_pos = 0
    next_pos = base_pos
    while next_pos != len(bytes):
        base_pos = next_pos
        next_pos += nxFrameFixed_t.size
        if len(bytes) < next_pos:
            _errors.check_for_error(_cconsts.NX_ERR_INTERNAL_ERROR)

        raw_base = bytes[base_pos:next_pos]
        base_unit = nxFrameFixed_t.unpack(raw_base)
        payload_length = _get_frame_payload_length(base_unit)
        base_unit_length, payload_unit_length = _split_payload_length(payload_length)

        payload_pos = next_pos
        payload_pad_pos = payload_pos + payload_unit_length
        next_pos += _calculate_payload_unit_size(payload_length)

        base_unit_payload = base_unit[FRAME_PAYLOAD_INDEX][0:base_unit_length]
        payload_unit = bytes[payload_pos:payload_pad_pos]
        payload = base_unit_payload + payload_unit
        yield types.RawFrame(
            base_unit[FRAME_TIMESTAMP_INDEX],
            base_unit[FRAME_IDENTIFIER_INDEX],
            constants.FrameType(base_unit[FRAME_TYPE_INDEX]),
            base_unit[FRAME_FLAG_INDEX],
            base_unit[FRAME_INFO_INDEX],
            payload)


def serialize_frame(frame):
    """Yields units that compose the frame."""
    payload = bytes(frame.payload)
    base_unit_payload = payload[0:MAX_BASE_UNIT_PAYLOAD_LENGTH]
    base_unit_padding_length = max(MAX_BASE_UNIT_PAYLOAD_LENGTH - len(base_unit_payload), 0)
    base_unit_payload += b'\0' * base_unit_padding_length

    payload_unit = payload[MAX_BASE_UNIT_PAYLOAD_LENGTH:]
    payload_unit_padding_length = _calculate_payload_unit_size(len(payload)) - len(payload_unit)
    payload_unit += b'\0' * payload_unit_padding_length

    payload_length = len(payload)
    if frame.type == constants.FrameType.J1939_DATA:
        if (frame.info & _cconsts.NX_FRAME_PAYLD_LEN_HIGH_MASK_J1939) != 0:
            # Invalid data where info_length will go.
            _errors.check_for_error(_cconsts.NX_ERR_INTERNAL_ERROR)
        info_length = payload_length >> 8
        if info_length != (info_length & _cconsts.NX_FRAME_PAYLD_LEN_HIGH_MASK_J1939):
            _errors.check_for_error(_cconsts.NX_ERR_FRAME_WRITE_TOO_LARGE)
        info = frame.info | info_length
        payload_length &= 0xFF
    else:
        if payload_length != (payload_length & 0xFF):
            _errors.check_for_error(_cconsts.NX_ERR_NON_J1939_FRAME_SIZE)
        info = frame.info

    base_unit = nxFrameFixed_t.pack(
        frame.timestamp,
        frame.identifier,
        frame.type.value,
        frame.flags,
        info,
        payload_length,
        base_unit_payload)
    yield base_unit

    if payload_unit:
        yield payload_unit
