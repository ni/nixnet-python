from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest  # type: ignore

import nixnet


@pytest.mark.integration
def test_session_j1939_properties(can_in_interface):
    database_name = 'NIXNET_example'
    cluster_name = 'J1939_Over_CAN'
    frame_name = 'J1939_Gloabal_Event_HighPrio'

    with nixnet.FrameInQueuedSession(
            can_in_interface,
            database_name,
            cluster_name,
            frame_name) as input_session:
        # todo: Add testing to cover more J1939 properties.
        input_session.j1939.include_dest_addr_in_pgn = True
        assert input_session.j1939.include_dest_addr_in_pgn
