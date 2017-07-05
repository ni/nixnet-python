from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _frames
from nixnet import constants
from nixnet import types


def test_iterate_frames_with_empty_payload():
    payload = b'\x00\x00\x00\x00\x00\x00\x00\x00'
    empty_bytes = b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x04\x05\x00' + payload
    (empty_frame, ) = list(_frames.iterate_frames(empty_bytes))
    assert repr(empty_frame) == 'RawFrame(timestamp=0x1, identifier=0x2, type=FrameType.CAN_DATA, flags=0x4, info=0x5, payload=...)'  # NOQA: E501
    assert empty_frame.payload == b''


def test_iterate_frames_with_base_payload():
    payload = b'\x01\x02\x03\x04\x05\x06\x07\x08'
    base_bytes = b'\x06\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x08\x09\x08' + payload
    (base_frame, ) = list(_frames.iterate_frames(base_bytes))
    assert repr(base_frame) == 'RawFrame(timestamp=0x6, identifier=0x7, type=FrameType.CAN_DATA, flags=0x8, info=0x9, payload=...)'  # NOQA: E501
    assert base_frame.payload == b'\x01\x02\x03\x04\x05\x06\x07\x08'


def test_iterate_frames_with_multiple_frames():
    payload = b'\x00\x00\x00\x00\x00\x00\x00\x00'
    empty_bytes = b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x04\x05\x00' + payload
    (empty_frame, ) = list(_frames.iterate_frames(empty_bytes))

    payload = b'\x01\x02\x03\x04\x05\x06\x07\x08'
    base_bytes = b'\x06\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x08\x09\x08' + payload
    (base_frame, ) = list(_frames.iterate_frames(base_bytes))

    multi_frame = empty_bytes + base_bytes
    (empty_frame_2, base_frame_2) = list(_frames.iterate_frames(multi_frame))
    assert empty_frame == empty_frame_2
    assert base_frame == base_frame_2


def test_serialize_frame_with_empty_payload():
    empty_frame = types.RawFrame(1, 2, constants.FrameType.CAN_DATA, 4, 5, b'')
    (bytes, ) = list(_frames.serialize_frame(empty_frame))
    assert bytes == b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x04\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00'


def test_serialize_frame_with_base_payload():
    payload = b'\x01\x02\x03\x04\x05\x06\x07\x08'
    base_frame = types.RawFrame(1, 2, constants.FrameType.CAN_DATA, 4, 5, payload)
    (bytes, ) = list(_frames.serialize_frame(base_frame))
    assert bytes == b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x04\x05\x08\x01\x02\x03\x04\x05\x06\x07\x08'
