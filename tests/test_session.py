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


def raise_code(code):
    raise errors.XnetError("", code)


@mock.patch('nixnet._errors.check_for_error', raise_code)
def test_flatten_items_invalid():
    with pytest.raises(errors.XnetError):
        _utils.flatten_items('A,B')
    with pytest.raises(errors.XnetError):
        _utils.flatten_items(5)


@pytest.mark.integration
def test_session_container(can_in_interface, can_out_interface):
    with nixnet.FrameInStreamSession(can_in_interface) as input_session:
        with nixnet.FrameInStreamSession(can_out_interface) as output_session:
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
def test_session_properties(can_out_interface):
    """Verify Session properties.

    Ideally, mutable properties would be set to multiple values and we'd test
    for the intended side-effect.  That'll be a massive undertaking.  For now,
    ensure they are settable and getttable.
    """
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameOutQueuedSession(
            can_out_interface,
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
def test_session_lin_properties(lin_in_interface):
    """Verify Session properties.

    Ideally, mutable properties would be set to multiple values and we'd test
    for the intended side-effect.  That'll be a massive undertaking.  For now,
    ensure they are settable and getttable.
    """
    database_name = 'NIXNET_exampleLDF'

    with nixnet.FrameInStreamSession(lin_in_interface, database_name) as input_session:
        print(input_session.lin_comm)


@pytest.mark.integration
def test_session_properties_transition(can_out_interface):
    """Verify Session properties relationship to session start/stop."""
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameOutQueuedSession(
            can_out_interface,
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


def test_parse_lin_comm_bitfield():
    """A part of Session.lin_comm"""
    comm = _utils.parse_lin_comm_bitfield(0, 0)
    assert comm == types.LinComm(
        sleep=False,
        state=constants.LinCommState.IDLE,
        last_err=constants.LinLastErr.NONE,
        err_received=0,
        err_expected=0,
        err_id=0,
        tcvr_rdy=False,
        sched_index=0)

    comm = _utils.parse_lin_comm_bitfield(0xFFFFFF6B, 0xFFFFFFFF)
    assert comm == types.LinComm(
        sleep=True,
        state=constants.LinCommState.INACTIVE,
        last_err=constants.LinLastErr.CRC,
        err_received=255,
        err_expected=255,
        err_id=63,
        tcvr_rdy=False,
        sched_index=255)


def assert_can_frame(index, sent, received):
    assert sent.identifier == received.identifier
    assert sent.echo == received.echo
    assert sent.type == received.type
    assert sent.payload == received.payload

    assert sent.timestamp != received.timestamp


@pytest.mark.integration
def test_start_explicit(can_in_interface, can_out_interface):
    """Demonstrate that data is properly sent out on an explicit start.

    Assumes test_frames.test_queued_loopback works
    """
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


@pytest.mark.integration
def test_flush_baseline(can_in_interface, can_out_interface):
    """Demonstrate that the non-flush version of the code works.

    Assumes test_frames.test_queued_loopback works.
    """
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
            output_session.auto_start = False
            input_session.start()

            dropped_frames = [
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x01\x02\x03\x04')]
            output_session.frames.write(dropped_frames)

            expected_frames = [
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x05\x06\x08\x09')]
            output_session.frames.write(expected_frames)

            expected_frames = dropped_frames + expected_frames

            output_session.start()
            # Wait 1 s and then read the received values.
            # They should be the same as the ones sent.
            time.sleep(1)

            actual_frames = list(input_session.frames.read(2))
            assert len(expected_frames) == len(actual_frames)
            for i, (expected, actual) in enumerate(zip(expected_frames, actual_frames)):
                assert_can_frame(i, expected, actual)


@pytest.mark.integration
def test_flush_output_queue(can_in_interface, can_out_interface):
    """Verifies that `flush` drops frames in the output queue

    Assumes test_frames.test_queued_loopback works.
    """
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
            output_session.auto_start = False
            input_session.start()

            dropped_frames = [
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x01\x02\x03\x04')]
            output_session.frames.write(dropped_frames)
            output_session.flush()

            expected_frames = [
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x05\x06\x08\x09')]
            output_session.frames.write(expected_frames)

            output_session.start()
            # Wait 1 s and then read the received values.
            # They should be the same as the ones sent.
            time.sleep(1)

            actual_frames = list(input_session.frames.read(2))
            assert len(expected_frames) == len(actual_frames)
            for i, (expected, actual) in enumerate(zip(expected_frames, actual_frames)):
                assert_can_frame(i, expected, actual)


@pytest.mark.integration
def test_wait_for_intf_communicating(can_in_interface):
    """Verifies wait_for_intf_communicating does not catastrophically fail.

    Considering the wait time is so short, it'd be hard to verify it,
    especially in a reproducible way.

    Assumes test_frames.test_queued_loopback works.
    """
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameInQueuedSession(
            can_in_interface,
            database_name,
            cluster_name,
            frame_name) as input_session:
        input_session.start()
        input_session.wait_for_intf_communicating()

        expected_frames = []
        actual_frames = list(input_session.frames.read(1))
        assert len(expected_frames) == len(actual_frames)
        for i, (expected, actual) in enumerate(zip(expected_frames, actual_frames)):
            assert_can_frame(i, expected, actual)


@pytest.mark.integration
def test_wait_for_transmit_complete(can_in_interface, can_out_interface):
    """Verifies wait_for_transmit_complete does not fail catastrophically.

    We can at least see how long it takes us to wait.  Longer term, we should
    switch the test to start waiting and then call ``input_session.start`` and
    ensure it unblocks after that call.

    To see the wait time, run py.test with ``-s``_.

    Assumes test_frames.test_queued_loopback works.
    """
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
            output_session.auto_start = False
            input_session.start()

            expected_frames = [
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x01\x02\x03\x04'),
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x05\x06\x08\x09'),
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x01\x02\x03\x04'),
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x05\x06\x08\x09'),
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x01\x02\x03\x04'),
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x05\x06\x08\x09'),
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x01\x02\x03\x04'),
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x05\x06\x08\x09'),
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x01\x02\x03\x04'),
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x05\x06\x08\x09'),
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x01\x02\x03\x04'),
                types.CanFrame(66, constants.FrameType.CAN_DATA, b'\x05\x06\x08\x09')]

            output_session.start()
            initial = time.time()
            output_session.frames.write(expected_frames)
            written = time.time()
            output_session.wait_for_transmit_complete(10)
            finished = time.time()

            print("Write took {} s".format(written - initial))
            print("Wait took {} s".format(finished - written))


@pytest.mark.integration
def test_wait_for_intf_remote_wakeup(can_in_interface, can_out_interface):
    """Verifies wait_for_intf_remote_wakeup does not fail catastrophically.

    We can at least see how long it takes us to wait.  Longer term, we should
    switch the test to start waiting and then call ``input_session.start`` and
    ensure it unblocks after that call.

    To see the wait time, run py.test with ``-s``_.

    Assumes test_frames.test_queued_loopback works.
    """
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameInQueuedSession(
            can_in_interface,
            database_name,
            cluster_name,
            frame_name) as input_session:
        input_session.start()
        input_session.intf.can_tcvr_state = constants.CanTcvrState.SLEEP
        assert input_session.can_comm.sleep

        with pytest.raises(errors.XnetError) as excinfo:
            input_session.wait_for_intf_remote_wakeup(5)
        assert excinfo.value.error_type == constants.Err.EVENT_TIMEOUT

        # Add a successful wait_for_intf_remote_wakeup (frame written to
        # output_session causes the input_session to wake up).


@pytest.mark.integration
def test_connect_terminals_failures(can_in_interface):
    """Verifies connect_terminals fails when expected to."""
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameInQueuedSession(
            can_in_interface,
            database_name,
            cluster_name,
            frame_name) as input_session:
        with pytest.raises(errors.XnetError) as excinfo:
            input_session.connect_terminals("FrontPanel0", "FrontPanel1")
        assert excinfo.value.error_type in [
            constants.Err.SYNCHRONIZATION_NOT_ALLOWED,
            constants.Err.INVALID_SYNCHRONIZATION_COMBINATION]


@pytest.mark.integration
def test_disconnect_terminals_failures(can_in_interface):
    """Verifies disconnect_terminals fails when expected to."""
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameInQueuedSession(
            can_in_interface,
            database_name,
            cluster_name,
            frame_name) as input_session:
        with pytest.raises(errors.XnetError) as excinfo:
            input_session.disconnect_terminals("FrontPanel0", "FrontPanel1")
        assert excinfo.value.error_type in [
            constants.Err.SYNCHRONIZATION_NOT_ALLOWED,
            constants.Err.INVALID_SYNCHRONIZATION_COMBINATION]
