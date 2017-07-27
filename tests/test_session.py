from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

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
            print(output_session.time_communicating)
        assert output_session.state == constants.SessionInfoState.STOPPED

        output_session.start()

        print(output_session.time_start)
        print(output_session.time_communicating)
        assert output_session.state == constants.SessionInfoState.STARTED

        output_session.stop()

        with pytest.raises(errors.XnetError):
            print(output_session.time_start)
            print(output_session.time_communicating)
        assert output_session.state == constants.SessionInfoState.STOPPED


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
