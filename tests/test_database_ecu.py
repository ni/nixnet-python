from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest  # type: ignore

from nixnet import constants
from nixnet import database


@pytest.mark.integration
def test_database_ecu_container():
    with database.Database('NIXNET_example') as db:
        cluster = db.clusters['CAN_Demo_Box_Cluster']  # type: database.Cluster
        ecu_1 = cluster.ecus['CAN_Demo_Box']  # type: database.Ecu
        ecu_2 = cluster.ecus['CAN_Demo_Box']  # type: database.Ecu
        ecu_3 = cluster.ecus['PC_Master']  # type: database.Ecu

        # test dunders
        assert ecu_1 == ecu_2
        assert ecu_1 != ecu_3
        assert len({ecu_1, ecu_2, ecu_3}) == 2  # testing `__hash__`
        print(repr(ecu_1))


@pytest.mark.integration
def test_database_ecu_functions():
    with database.Database('NIXNET_example') as db:
        ecu = db.find(database.Ecu, 'PC_Master')  # type: database.Ecu
        ecu.check_config_status()


@pytest.mark.integration
def test_database_ecu_properties():
    with database.Database('NIXNET_exampleLDF') as db:
        ecu = db.find(database.Ecu, 'Master1')  # type: database.Ecu

        # test references
        assert len(list(ecu.rx_frms)) > 0
        assert len(list(ecu.tx_frms)) > 0

        # test setters
        ecu.comment = 'This is a comment.'
        ecu.name = 'NewEcuName'

        # test getters
        print(ecu.clst)
        print(ecu.comment)
        print(ecu.name)


@pytest.mark.integration
def test_database_ecu_properties_lin():
    with database.Database('NIXNET_exampleLDF') as db:
        ecu = db.find(database.Ecu, 'Master1')  # type: database.Ecu

        # test setters
        ecu.lin_master = ecu.lin_master
        ecu.lin_protocol_ver = constants.LinProtocolVer.VER_2_1
        ecu.lin_initial_nad = 0
        ecu.lin_config_nad = 0
        ecu.lin_supplier_id = 0
        ecu.lin_function_id = 0
        ecu.lin_p2_min = 0
        ecu.lin_st_min = 0

        # test getters
        print(ecu.lin_protocol_ver)
        print(ecu.lin_initial_nad)
        print(ecu.lin_config_nad)
        print(ecu.lin_supplier_id)
        print(ecu.lin_function_id)
        print(ecu.lin_p2_min)
        print(ecu.lin_st_min)
