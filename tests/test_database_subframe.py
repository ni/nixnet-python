from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest  # type: ignore

from nixnet import database
from nixnet import errors


@pytest.mark.integration
def test_database_subframe_container():
    with database.Database('NIXNET_example') as db:
        cluster = db.clusters['CAN_Cluster']  # type: database.Cluster
        frame = cluster.frames['CANCyclicFrame1']  # type: database.Frame
        subframe_1 = frame.mux_subframes.add('subframe1')  # type: database.SubFrame
        subframe_2 = frame.find(database.SubFrame, 'subframe1')  # type: database.SubFrame
        subframe_3 = frame.mux_subframes.add('subframe3')  # type: database.SubFrame

        # test dunders
        assert subframe_1 == subframe_2
        assert subframe_1 != subframe_3
        assert len({subframe_1, subframe_2, subframe_3}) == 2  # testing `__hash__`
        print(repr(subframe_1))


@pytest.mark.integration
def test_database_subframe_functions():
    with database.Database('NIXNET_example') as db:
        frame = db.find(database.Frame, 'CANCyclicFrame1')  # type: database.Frame
        subframe = frame.mux_subframes.add('subframe1')  # type: database.SubFrame
        subframe.check_config_status()
        with pytest.raises(errors.XnetError):
            subframe.find(database.Signal, 'signal_name')


@pytest.mark.integration
def test_database_subframe_properties():
    with database.Database('NIXNET_example') as db:
        frame = db.find(database.Frame, 'CANCyclicFrame1')  # type: database.Frame
        subframe = frame.mux_subframes.add('subframe1')  # type: database.SubFrame

        # test references
        print(subframe.frm)
        print(subframe.pdu)
        assert len(subframe.dyn_signals) == 0

        # test setters
        subframe.mux_value = 1
        subframe.name = 'NewSubframeName'

        # test getters
        print(subframe.mux_value)
        print(subframe.name)
        print(subframe.name_unique_to_cluster)
