from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import time

import pytest

import nixnet
from nixnet import _frames
from nixnet import constants
from nixnet import types


@pytest.fixture
def nixnet_in_interface(request):
    interface = request.config.getoption("--nixnet-in-interface")
    return interface


@pytest.fixture
def nixnet_out_interface(request):
    interface = request.config.getoption("--nixnet-out-interface")
    return interface


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


def assert_can_frame(sent, received):
    assert sent.identifier == received.identifier
    assert sent.extended == received.extended
    assert sent.echo == received.echo
    assert sent.type == received.type
    assert sent.payload == received.payload

    assert sent.timestamp != received.timestamp


@pytest.mark.integration
def test_stream_loopback(nixnet_in_interface, nixnet_out_interface):
    with nixnet.FrameInStreamSession(nixnet_in_interface) as input_session:
        with nixnet.FrameOutStreamSession(nixnet_out_interface) as output_session:
            input_session.intf.baud_rate = 125000
            output_session.intf.baud_rate = 125000

            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start()

            payload_list = [2, 4, 8, 16]
            expected_frames = [
                types.CanFrame(0, False, constants.FrameType.CAN_DATA, bytes(bytearray(payload_list)))]
            output_session.frames.write_can(expected_frames)

            # Wait 1 s and then read the received values.
            # They should be the same as the ones sent.
            time.sleep(1)

            actual_frames = list(input_session.frames.read_can(1))
            assert len(expected_frames) == len(actual_frames)
            for expected, actual in zip(expected_frames, actual_frames):
                assert_can_frame(expected, actual)
