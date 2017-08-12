from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time

import mock  # type: ignore

import pytest  # type: ignore

import nixnet
from nixnet import _frames
from nixnet import constants
from nixnet import errors
from nixnet import types


def raise_code(code):
    raise errors.XnetError("", code)


def test_iterate_frames_with_empty_payload():
    payload = b'\x00\x00\x00\x00\x00\x00\x00\x00'
    empty_bytes = b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x04\x05\x00' + payload
    (empty_frame, ) = list(_frames.iterate_frames(empty_bytes))
    assert repr(empty_frame) == 'RawFrame(timestamp=0x1, identifier=0x2, type=FrameType.CAN_DATA, flags=0x4, info=0x5)'
    assert empty_frame.payload == b''


def test_iterate_frames_with_base_payload():
    payload = b'\x01\x02\x03\x04\x05\x06\x07\x08'
    base_bytes = b'\x06\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x08\x09\x08' + payload
    (base_frame, ) = list(_frames.iterate_frames(base_bytes))
    assert repr(base_frame) == 'RawFrame(timestamp=0x6, identifier=0x7, type=FrameType.CAN_DATA, flags=0x8, info=0x9, len(payload)=8)'  # NOQA: E501
    assert base_frame.payload == b'\x01\x02\x03\x04\x05\x06\x07\x08'


def test_iterate_frames_with_partial_base_payload():
    frame_bytes = b'\xd8\xb7@B\xeb\xff\xd2\x01\x00\x00\x00\x00\x00\x00\x00\x04\x02\x04\x08\x10\x00\x00\x00\x00'
    (frame, ) = list(_frames.iterate_frames(frame_bytes))
    assert repr(frame) == 'RawFrame(timestamp=0x1d2ffeb4240b7d8, identifier=0x0, type=FrameType.CAN_DATA, len(payload)=4)'  # NOQA: E501
    assert frame.payload == b'\x02\x04\x08\x10'


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


@mock.patch('nixnet._errors.check_for_error', raise_code)
def test_iterate_frames_corrupted_frame():
    empty_bytes = b'\x01\x00\x00\x00\x00\x00\x00'
    with pytest.raises(errors.XnetError):
        list(_frames.iterate_frames(empty_bytes))


def test_can_identifier_equality():
    assert types.CanIdentifier(130) == types.CanIdentifier(130)
    assert types.CanIdentifier(130, True) == types.CanIdentifier(130, True)
    assert not (types.CanIdentifier(130) == types.CanIdentifier(13))
    assert not (types.CanIdentifier(130) == types.CanIdentifier(130, True))
    assert not (types.CanIdentifier(130) == "<invalid>")

    assert not (types.CanIdentifier(130) != types.CanIdentifier(130))
    assert not (types.CanIdentifier(130, True) != types.CanIdentifier(130, True))
    assert types.CanIdentifier(130) != types.CanIdentifier(13)
    assert types.CanIdentifier(130) != types.CanIdentifier(130, True)
    assert types.CanIdentifier(130) != "<invalid>"


@mock.patch('nixnet._errors.check_for_error', raise_code)
def test_can_identifier_overflow():
    valid_extended_identifier = 0xFFFF
    int(types.CanIdentifier(valid_extended_identifier, extended=True))
    with pytest.raises(errors.XnetError):
        int(types.CanIdentifier(valid_extended_identifier))


@mock.patch('nixnet._errors.check_for_error', raise_code)
def test_can_identifier_extended_overflow():
    with pytest.raises(errors.XnetError):
        int(types.CanIdentifier(0xFFFFFFFF, True))


def test_raw_frame_equality():
    empty_frame = types.RawFrame(1, 2, constants.FrameType.CAN_DATA, 4, 5, b'')
    base_frame = types.RawFrame(1, 2, constants.FrameType.CAN_DATA, 4, 5, b'\x01')

    assert empty_frame == empty_frame
    assert not (empty_frame == base_frame)
    assert not (empty_frame == 5)

    assert not (empty_frame != empty_frame)
    assert empty_frame != base_frame
    assert empty_frame != 5


def test_raw_frame_conversion():
    base_frame = types.RawFrame(1, 2, constants.FrameType.CAN_DATA, 4, 5, b'\x01')
    assert base_frame == base_frame, "Pre-requisite failed"

    assert base_frame == types.RawFrame.from_raw(base_frame)
    assert base_frame == base_frame.to_raw()


def test_can_frame_equality():
    empty_frame = types.CanFrame(0, constants.FrameType.CAN_DATA, b'')
    base_frame = types.CanFrame(0, constants.FrameType.CAN_DATA, b'\x01')

    assert empty_frame == empty_frame
    assert not (empty_frame == base_frame)
    assert not (empty_frame == 5)

    assert not (empty_frame != empty_frame)
    assert empty_frame != base_frame
    assert empty_frame != 5


def test_can_bus_error_frame_equality():
    frame = types.CanBusErrorFrame(100, constants.CanCommState.BUS_OFF, True, constants.CanLastErr.STUFF, 1, 2)
    other_frame = types.CanBusErrorFrame(100, constants.CanCommState.BUS_OFF, True, constants.CanLastErr.STUFF, 1, 3)

    assert frame == frame
    assert not (frame == other_frame)
    assert not (frame == 5)

    assert not (frame != frame)
    assert frame != other_frame
    assert frame != 5


def test_lin_frame_equality():
    empty_frame = types.LinFrame(2, constants.FrameType.LIN_DATA, b'')
    base_frame = types.LinFrame(2, constants.FrameType.LIN_DATA, b'\x01')

    assert empty_frame == empty_frame
    assert not (empty_frame == base_frame)
    assert not (empty_frame == 5)

    assert not (empty_frame != empty_frame)
    assert empty_frame != base_frame
    assert empty_frame != 5


@mock.patch('nixnet._errors.check_for_error', raise_code)
def test_lin_frame_identifier_overflow():
    with pytest.raises(errors.XnetError):
        types.LinFrame(0xFFFFFFFF).to_raw()


def test_lin_bus_error_frame_equality():
    frame = types.LinBusErrorFrame(100, constants.LinCommState.IDLE, constants.LinLastErr.UNKNOWN_ID, 1, 2, 3)
    other_frame = types.LinBusErrorFrame(100, constants.LinCommState.IDLE, constants.LinLastErr.UNKNOWN_ID, 1, 3, 3)

    assert frame == frame
    assert not (frame == other_frame)
    assert not (frame == 5)

    assert not (frame != frame)
    assert frame != other_frame
    assert frame != 5


def test_delay_frame_equality():
    frame = types.DelayFrame(100)
    other_frame = types.DelayFrame(120)

    assert frame == frame
    assert not (frame == other_frame)
    assert not (frame == 5)

    assert not (frame != frame)
    assert frame != other_frame
    assert frame != 5


def test_log_trigger_frame_equality():
    frame = types.LogTriggerFrame(100)
    other_frame = types.LogTriggerFrame(120)

    assert frame == frame
    assert not (frame == other_frame)
    assert not (frame == 5)

    assert not (frame != frame)
    assert frame != other_frame
    assert frame != 5


def test_start_trigger_frame_equality():
    frame = types.StartTriggerFrame(100)
    other_frame = types.StartTriggerFrame(120)

    assert frame == frame
    assert not (frame == other_frame)
    assert not (frame == 5)

    assert not (frame != frame)
    assert frame != other_frame
    assert frame != 5


def test_serialize_frame_with_empty_payload():
    empty_frame = types.RawFrame(1, 2, constants.FrameType.CAN_DATA, 4, 5, b'')
    (base, ) = list(_frames.serialize_frame(empty_frame))
    assert base[0:16] == b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x04\x05\x00'
    assert base[16:] == b'\x00\x00\x00\x00\x00\x00\x00\x00'


def test_serialize_frame_with_base_payload():
    payload = b'\x01\x02\x03\x04\x05\x06\x07\x08'
    base_frame = types.RawFrame(1, 2, constants.FrameType.CAN_DATA, 4, 5, payload)
    (base, ) = list(_frames.serialize_frame(base_frame))
    assert base[0:16] == b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x04\x05\x08'
    assert base[16:] == b'\x01\x02\x03\x04\x05\x06\x07\x08'


def test_serialize_frame_with_payload_unit():
    payload = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B'
    base_frame = types.RawFrame(1, 2, constants.FrameType.CAN_DATA, 4, 5, payload)
    (base, payload) = list(_frames.serialize_frame(base_frame))
    assert base[0:16] == b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x04\x05\x0b'
    assert base[16:] == b'\x01\x02\x03\x04\x05\x06\x07\x08'
    assert payload == b'\x09\x0A\x0B\x00\x00\x00\x00\x00'


@mock.patch('nixnet._errors.check_for_error', raise_code)
def test_serialize_frame_with_excessive_payload():
    payload = 0xFF * b'\x01\x02\x03\x04\x05\x06\x07\x08'
    base_frame = types.RawFrame(1, 2, constants.FrameType.CAN_DATA, 4, 5, payload)
    with pytest.raises(errors.XnetError):
        list(_frames.serialize_frame(base_frame))


def assert_can_frame(index, sent, received):
    assert sent.identifier == received.identifier
    assert sent.echo == received.echo
    assert sent.type == received.type
    assert sent.payload == received.payload

    assert sent.timestamp != received.timestamp


@pytest.mark.integration
def test_stream_loopback(can_in_interface, can_out_interface):
    with nixnet.FrameInStreamSession(can_in_interface) as input_session:
        with nixnet.FrameOutStreamSession(can_out_interface) as output_session:
            input_session.intf.baud_rate = 125000
            output_session.intf.baud_rate = 125000

            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start()

            payload_list = [2, 4, 8, 16]
            expected_frames = [
                types.CanFrame(0, constants.FrameType.CAN_DATA, bytes(bytearray(payload_list)))]
            output_session.frames.write(expected_frames)

            # Wait 1 s and then read the received values.
            # They should be the same as the ones sent.
            time.sleep(1)

            actual_frames = list(input_session.frames.read(1))
            assert len(expected_frames) == len(actual_frames)
            for i, (expected, actual) in enumerate(zip(expected_frames, actual_frames)):
                assert_can_frame(i, expected, actual)


@pytest.mark.integration
def test_queued_loopback(can_in_interface, can_out_interface):
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameInQueuedSession(
            can_in_interface,
            database_name,
            cluster_name,
            frame_name) as input_session:
        with nixnet.FrameOutQueuedSession(
                can_out_interface,
                database_name,
                cluster_name,
                frame_name) as output_session:
            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start()

            payload_list = [2, 4, 8, 16]
            expected_frames = [
                types.CanFrame(66, constants.FrameType.CAN_DATA, bytes(bytearray(payload_list)))]
            output_session.frames.write(expected_frames)

            # Wait 1 s and then read the received values.
            # They should be the same as the ones sent.
            time.sleep(1)

            actual_frames = list(input_session.frames.read(1))
            assert len(expected_frames) == len(actual_frames)
            for i, (expected, actual) in enumerate(zip(expected_frames, actual_frames)):
                assert_can_frame(i, expected, actual)


@pytest.mark.integration
def test_singlepoint_loopback(can_in_interface, can_out_interface):
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = ['CANEventFrame1', 'CANEventFrame2']

    with nixnet.FrameInSinglePointSession(
            can_in_interface,
            database_name,
            cluster_name,
            frame_name) as input_session:
        with nixnet.FrameOutSinglePointSession(
                can_out_interface,
                database_name,
                cluster_name,
                frame_name) as output_session:
            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start()

            first_payload_list = [2, 4, 8, 16]
            second_payload_list = [1, 3]
            expected_frames = [
                types.CanFrame(66, constants.FrameType.CAN_DATA, bytes(bytearray(first_payload_list))),
                types.CanFrame(67, constants.FrameType.CAN_DATA, bytes(bytearray(second_payload_list)))]
            output_session.frames.write(expected_frames)

            # Wait 1 s and then read the received values.
            # They should be the same as the ones sent.
            time.sleep(1)

            actual_frames = list(input_session.frames.read())
            assert len(expected_frames) == len(actual_frames)
            for i, (expected, actual) in enumerate(zip(expected_frames, actual_frames)):
                assert_can_frame(i, expected, actual)


@pytest.mark.integration
def test_session_frames_container(can_in_interface):
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameInQueuedSession(
            can_in_interface,
            database_name,
            cluster_name,
            frame_name) as input_session:
        assert input_session.frames == input_session.frames
        assert not (input_session.frames == 5)

        assert not (input_session.frames != input_session.frames)
        assert input_session.frames != 5

        print(repr(input_session.frames))

        assert frame_name in input_session.frames
        assert 0 in input_session.frames
        with pytest.raises(TypeError):
            (1, 2) in input_session.frames

        assert len(input_session.frames) == 1
        frames = list(input_session.frames)
        assert len(frames) == 1
        frame = frames[0]

        assert str(frame) == frame_name
        assert int(frame) == 0

        assert frame == input_session.frames[0]
        assert frame == input_session.frames[frame_name]
        with pytest.raises(IndexError):
            input_session.frames[1]
        with pytest.raises(KeyError):
            input_session.frames["<random>"]
        with pytest.raises(TypeError):
            input_session.frames[(1, 2)]

        assert frame == input_session.frames.get(0)
        assert frame == input_session.frames.get(frame_name)
        assert input_session.frames.get(1) is None
        assert input_session.frames.get("<random>") is None
        with pytest.raises(TypeError):
            input_session.frames.get((1, 2))


@pytest.mark.integration
def test_session_frames_properties(can_out_interface):
    """Verify Frames properties.

    These are pretty transient and can't easily be verified against known good
    values.  For now, we'll just verify the calls don't call catastrophically
    and someone can always run py.test with ``-s``_.
    """
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameOutQueuedSession(
            can_out_interface,
            database_name,
            cluster_name,
            frame_name) as output_session:
        print(output_session.frames.payld_len_max)


@pytest.mark.integration
def test_session_frame_container(can_in_interface):
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameInQueuedSession(
            can_in_interface,
            database_name,
            cluster_name,
            frame_name) as input_session:
        frames = input_session.frames
        assert len(frames) == 1, "Pre-requisite failed"
        frame = frames[0]

        assert frame == frame
        assert not (frame == 5)

        assert not (frame != frame)
        assert frame != 5

        print(repr(frame))


@pytest.mark.integration
def test_lin_stream_loopback(lin_in_interface, lin_out_interface):
    database_name = 'NIXNET_exampleLDF'

    with nixnet.FrameInStreamSession(lin_in_interface, database_name) as input_session:
        with nixnet.FrameOutStreamSession(lin_out_interface, database_name) as output_session:
            output_session.intf.lin_master = True

            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start()

            # Set the schedule. This will also automically enable
            # master mode
            output_session.change_lin_schedule(0)

            payload_list = [2, 4, 8, 16]
            expected_frames = [
                types.LinFrame(0, constants.FrameType.LIN_DATA, bytes(bytearray(payload_list)))]
            output_session.frames.write(expected_frames)

            # Wait 1 s and then read the received values.
            # They should be the same as the ones sent.
            time.sleep(1)

            actual_frames = list(input_session.frames.read(1))
            assert len(expected_frames) == len(actual_frames)
            for i, (expected, actual) in enumerate(zip(expected_frames, actual_frames)):
                assert_can_frame(i, expected, actual)
