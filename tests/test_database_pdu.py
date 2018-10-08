from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest  # type: ignore

from nixnet import database
from nixnet import errors


@pytest.mark.integration
def test_database_pdu_container():
    with database.Database('NIXNET_example') as db:
        cluster = db.clusters['CAN_Cluster']  # type: database.Cluster
        pdu_1 = cluster.pdus['CANCyclicFrame1_pdu']  # type: database.Pdu
        pdu_2 = cluster.pdus['CANCyclicFrame1_pdu']  # type: database.Pdu
        pdu_3 = cluster.pdus['CANCyclicFrame2_pdu']  # type: database.Pdu

        # test dunders
        assert pdu_1 == pdu_2
        assert pdu_1 != pdu_3
        assert len({pdu_1, pdu_2, pdu_3}) == 2  # testing `__hash__`
        print(repr(pdu_1))


@pytest.mark.integration
def test_database_pdu_functions():
    with database.Database('NIXNET_example') as db:
        pdu = db.find(database.Pdu, 'CANCyclicFrame1_pdu')  # type: database.Pdu
        pdu.check_config_status()


@pytest.mark.integration
def test_database_pdu_properties():
    with database.Database('NIXNET_example') as db:
        pdu = db.find(database.Pdu, 'CANCyclicFrame1_pdu')  # type: database.Pdu

        # test references
        print(pdu.cluster)
        assert len(list(pdu.frms)) > 0
        assert len(pdu.signals) > 0
        assert len(list(pdu.mux_static_sigs)) > 0
        assert len(list(pdu.mux_subframes)) == 0
        with pytest.raises(errors.XnetError):
            print(pdu.mux_data_mux_sig)

        # test setters
        pdu.comment = 'This is a comment.'
        pdu.name = 'NewPduName'
        pdu.payload_len = pdu.payload_len

        # test getters
        print(pdu.comment)
        print(pdu.name)
        print(pdu.mux_is_muxed)
