from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pytest  # type: ignore

import nixnet
from nixnet import constants
from nixnet import errors


@pytest.mark.integration
def test_intf_container(can_in_interface):
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameInQueuedSession(
            can_in_interface,
            database_name,
            cluster_name,
            frame_name) as input_session:
        assert input_session.intf == input_session.intf
        assert input_session.intf == can_in_interface
        assert not (input_session.intf == "<random>")
        assert not (input_session.intf == 5)

        assert not (input_session.intf != input_session.intf)
        assert not (input_session.intf != can_in_interface)
        assert input_session.intf != "<random>"
        assert input_session.intf != 5

        assert str(input_session.intf) == can_in_interface

        print(repr(input_session.intf))


@pytest.mark.integration
def test_intf_properties_settable_only_when_stopped(can_out_interface):
    """Verify Interface properties settable only when stopped.

    Ensure that Interface properties are only allowed to be set when the session is stopped.
    """
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameOutQueuedSession(
            can_out_interface,
            database_name,
            cluster_name,
            frame_name) as output_session:
        # Start the session manually
        output_session.start()

        # These should error because interfrace properties can only be modified
        # when the session is stopped. Note that we've only picked a select few
        # interface properties to test this behavior.
        with pytest.raises(errors.XnetError) as term_excinfo:
            output_session.intf.can_term = constants.CanTerm.ON
        assert term_excinfo.value.error_type == constants.Err.OBJECT_STARTED

        with pytest.raises(errors.XnetError) as baud_rate_excinfo:
            output_session.intf.baud_rate = 100000
        assert baud_rate_excinfo.value.error_type == constants.Err.OBJECT_STARTED

        with pytest.raises(errors.XnetError) as transmit_pause_excinfo:
            output_session.intf.can_transmit_pause = True
        assert transmit_pause_excinfo.value.error_type == constants.Err.OBJECT_STARTED

        output_session.stop()

        # Should not error because the session has stopped.
        output_session.intf.can_term = constants.CanTerm.ON
        output_session.intf.baud_rate = 100000
        output_session.intf.can_transmit_pause = True

        assert output_session.intf.can_term == constants.CanTerm.ON
        assert output_session.intf.baud_rate == 100000
        assert output_session.intf.can_transmit_pause


@pytest.mark.integration
def test_stream_session_requires_baud_rate(can_out_interface):
    """Stream session requires setting baud rate.

    Ensure Stream session cannot start without setting the baud_rate property.
    """
    with nixnet.FrameOutStreamSession(can_out_interface) as output_session:
        with pytest.raises(errors.XnetError) as start_excinfo:
            output_session.start()
        assert start_excinfo.value.error_type == constants.Err.BAUD_RATE_NOT_CONFIGURED

        output_session.intf.baud_rate = 125000
        assert output_session.intf.baud_rate == 125000

        # Starting the stream session does not error because the baud_rate is set
        output_session.start()


@pytest.mark.integration
def test_sleep_transition(can_in_interface):
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameInQueuedSession(
            can_in_interface,
            database_name,
            cluster_name,
            frame_name) as input_session:
        assert not input_session.can_comm.sleep

        with pytest.raises(errors.XnetError) as excinfo:
            input_session.intf.can_tcvr_state = constants.CanTcvrState.SLEEP
        assert excinfo.value.error_type == constants.Err.SESSION_NOT_STARTED
        assert not input_session.can_comm.sleep

        input_session.start()
        assert not input_session.can_comm.sleep

        input_session.intf.can_tcvr_state = constants.CanTcvrState.SLEEP
        assert input_session.can_comm.sleep

        input_session.intf.can_tcvr_state = constants.CanTcvrState.NORMAL
        assert not input_session.can_comm.sleep
