from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import mock  # type: ignore
import time

import pytest  # type: ignore

import nixnet
from nixnet import _utils
from nixnet import constants
from nixnet import errors
from nixnet import types


@pytest.fixture
def nixnet_in_interface(request):
    interface = request.config.getoption("--nixnet-in-interface")
    return interface


@pytest.fixture
def nixnet_out_interface(request):
    interface = request.config.getoption("--nixnet-out-interface")
    return interface


def raise_code(code):
    raise errors.XnetError("", code)


@mock.patch('nixnet._errors.check_for_error', raise_code)
def test_flatten_items_invalid():
    with pytest.raises(errors.XnetError):
        _utils.flatten_items('A,B')
    with pytest.raises(errors.XnetError):
        _utils.flatten_items(5)


@pytest.mark.integration
def test_session_container(nixnet_in_interface, nixnet_out_interface):
    with nixnet.FrameInStreamSession(nixnet_in_interface) as input_session:
        with nixnet.FrameInStreamSession(nixnet_out_interface) as output_session:
            assert input_session == input_session
            assert not (input_session == output_session)
            assert not (input_session == 1)

            assert not (input_session != input_session)
            assert input_session != output_session
            assert input_session != 1

        set([input_session])  # Testing `__hash__`

        print(repr(input_session))

    with pytest.warns(errors.XnetResourceWarning):
        input_session.close()


@pytest.mark.integration
def test_session_properties(nixnet_out_interface):
    """Verify Session properties.

    Ideally, mutable properties would be set to multiple values and we'd test
    for the intended side-effect.  That'll be a massive undertaking.  For now,
    ensure they are settable and getttable.
    """
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameOutQueuedSession(
            nixnet_out_interface,
            database_name,
            cluster_name,
            frame_name) as output_session:
        print(output_session.time_current)
        assert output_session.state == constants.SessionInfoState.STOPPED
        print(output_session.can_comm)

        assert output_session.database_name == database_name
        assert output_session.cluster_name == cluster_name
        assert output_session.mode == constants.CreateSessionMode.FRAME_OUT_QUEUED
        assert output_session.application_protocol == constants.AppProtocol.NONE
        assert output_session.protocol == constants.Protocol.CAN

        assert output_session.auto_start
        output_session.auto_start = False
        assert not output_session.auto_start

        print(output_session.num_pend)
        print(output_session.num_unused)

        print(output_session.queue_size)
        output_session.queue_size = 2040
        assert output_session.queue_size == 2040


@pytest.mark.integration
def test_session_properties_transition(nixnet_out_interface):
    """Verify Session properties relationship to session start/stop."""
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameOutQueuedSession(
            nixnet_out_interface,
            database_name,
            cluster_name,
            frame_name) as output_session:
        with pytest.raises(errors.XnetError):
            print(output_session.time_start)
        with pytest.raises(errors.XnetError):
            print(output_session.time_communicating)
        assert output_session.state == constants.SessionInfoState.STOPPED

        output_session.start()

        print(output_session.time_start)
        print(output_session.time_communicating)
        assert output_session.state == constants.SessionInfoState.STARTED

        output_session.stop()

        with pytest.raises(errors.XnetError):
            print(output_session.time_start)
        with pytest.raises(errors.XnetError):
            print(output_session.time_communicating)
        assert output_session.state == constants.SessionInfoState.STOPPED

        output_session.check_fault()


def test_parse_can_comm_bitfield():
    """A part of Session.can_comm"""
    comm = _utils.parse_can_comm_bitfield(0)
    assert comm == types.CanComm(
        constants.CanCommState.ERROR_ACTIVE,
        tcvr_err=False,
        sleep=False,
        last_err=constants.CanLastErr.NONE,
        tx_err_count=0,
        rx_err_count=0)

    comm = _utils.parse_can_comm_bitfield(0xFFFFF6F3)
    assert comm == types.CanComm(
        constants.CanCommState.INIT,
        tcvr_err=True,
        sleep=True,
        last_err=constants.CanLastErr.CRC,
        tx_err_count=255,
        rx_err_count=255)


def assert_can_frame(index, sent, received):
    assert sent.identifier == received.identifier
    assert sent.echo == received.echo
    assert sent.type == received.type
    assert sent.payload == received.payload

    assert sent.timestamp != received.timestamp


@pytest.mark.integration
def test_start_explicit(nixnet_in_interface, nixnet_out_interface):
    """Demonstrate that data is properly sent out on an explicit start.

    Assumes test_frames.test_queued_loopback works
    """
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameInQueuedSession(
            nixnet_in_interface,
            database_name,
            cluster_name,
            frame_name) as input_session:
        with nixnet.FrameOutQueuedSession(
                nixnet_out_interface,
                database_name,
                cluster_name,
                frame_name) as output_session:
            output_session.auto_start = False
            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start()

            expected_frames = [
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x01\x02\x03\x04')]
            output_session.frames.write(expected_frames)

            output_session.start()
            # Wait 1 s and then read the received values.
            # They should be the same as the ones sent.
            time.sleep(1)

            actual_frames = list(input_session.frames.read(1))
            assert len(expected_frames) == len(actual_frames)
            for i, (expected, actual) in enumerate(zip(expected_frames, actual_frames)):
                assert_can_frame(i, expected, actual)