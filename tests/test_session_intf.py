from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pytest  # type: ignore

import nixnet
from nixnet import constants
from nixnet import errors
from nixnet import types


@pytest.fixture
def nixnet_out_interface(request):
    interface = request.config.getoption("--nixnet-out-interface")
    return interface


@pytest.mark.integration
def test_interface_props(nixnet_out_interface):
    """Verify Interface properties.

    Ensure interface properties can only be modified when the session is stopped.
    """
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CANEventFrame1'

    with nixnet.FrameOutQueuedSession(
            nixnet_out_interface,
            database_name,
            cluster_name,
            frame_name) as output_session:
        # Start the session manually
        output_session.start()

        # These should error because interfrace properties can only be modified
        # when the session is stopped.
        with pytest.raises(errors.XnetError) as term_excinfo:
            output_session.intf.can_term = constants.CanTerm.OFF
        assert term_excinfo.value.error_type == constants.Err.OBJECT_STARTED

        with pytest.raises(errors.XnetError) as baud_rate_excinfo:
            output_session.intf.baud_rate = 125000
        assert baud_rate_excinfo.value.error_type == constants.Err.OBJECT_STARTED

        with pytest.raises(errors.XnetError) as transmit_pause_excinfo:
            output_session.intf.can_transmit_pause = True
        assert transmit_pause_excinfo.value.error_type == constants.Err.OBJECT_STARTED

        output_session.stop()

        # Should not error because the session has stopped.
        output_session.intf.can_term = constants.CanTerm.OFF
        output_session.intf.baud_rate = 125000
        output_session.intf.can_transmit_pause = True

        assert output_session.intf.can_term == constants.CanTerm.OFF
        assert output_session.intf.baud_rate == 125000
        assert output_session.intf.can_transmit_pause == True

        output_session.start()

        payload_list = [2, 4, 8, 16]
        expected_frames = [
            types.CanFrame(0, False, constants.FrameType.CAN_DATA, bytes(bytearray(payload_list)))]
        output_session.frames.write_can(expected_frames)


@pytest.mark.integration
def test_stream_session_without_baud_rate(nixnet_out_interface):
    """Stream session without setting baud rate.

    Ensure Stream session cannot start without setting the baud_rate property.
    """
    with nixnet.FrameOutStreamSession(nixnet_out_interface) as output_session:
        with pytest.raises(errors.XnetError) as start_excinfo:
            output_session.start()
        assert start_excinfo.value.error_type == constants.Err.BAUD_RATE_NOT_CONFIGURED

        output_session.intf.baud_rate = 125000
        assert output_session.intf.baud_rate == 125000

        # Starting the stream session does not error because the baud_rate is set
        output_session.start()

        payload_list = [2, 4, 8, 16]
        expected_frames = [
            types.CanFrame(0, False, constants.FrameType.CAN_DATA, bytes(bytearray(payload_list)))]
        output_session.frames.write_can(expected_frames)
