import os
import pytest  # type: ignore
import tempfile

from nixnet import constants
from nixnet import database


@pytest.mark.integration
def test_database_cluster_container():
    with database.Database('NIXNET_example') as db:
        cluster_1 = db.clusters['CAN_Cluster']  # type: database.Cluster
        cluster_2 = db.clusters['CAN_Cluster']  # type: database.Cluster
        cluster_3 = db.clusters['CAN_Demo_Box_Cluster']  # type: database.Cluster

        # test dunders
        assert cluster_1 == cluster_2
        assert cluster_1 != cluster_3
        assert len({cluster_1, cluster_2, cluster_3}) == 2  # testing `__hash__`
        print(repr(cluster_1))


@pytest.mark.integration
def test_database_cluster_functions():
    with database.Database('NIXNET_example') as db:
        cluster = db.find(database.Cluster, 'CAN_Cluster')  # type: database.Cluster
        cluster.check_config_status()
        cluster.find(database.Signal, 'CANCyclicSignal1')


@pytest.mark.integration
def test_database_cluster_properties_common():
    with database.Database('NIXNET_example') as db:
        cluster = db.find(database.Cluster, 'CAN_Demo_Box_Cluster')  # type: database.Cluster

        # test references
        assert len(cluster.ecus) > 0
        assert len(cluster.frames) > 0
        assert len(cluster.pdus) > 0
        assert len(list(cluster.sigs)) > 0

        # test setters
        cluster.application_protocol = constants.AppProtocol.NONE
        cluster.baud_rate = cluster.baud_rate
        cluster.comment = 'This is a comment.'
        cluster.name = 'NewClusterName'
        cluster.protocol = constants.Protocol.CAN

        # test getters
        print(cluster.application_protocol)
        print(cluster.comment)
        print(cluster.name)
        print(cluster.pdus_reqd)
        print(cluster.protocol)


@pytest.mark.integration
def test_database_cluster_export():
    input_filepath = os.path.join(os.path.dirname(__file__), 'databases\\attributes.dbc')
    output_filepath = tempfile.NamedTemporaryFile(suffix='.dbc', delete=False).name
    with database.Database(input_filepath) as db:
        cluster = db.clusters['Cluster']  # type: database.Cluster
        cluster.export(output_filepath)


@pytest.mark.integration
def test_database_cluster_properties_can():
    with database.Database('NIXNET_example') as db:
        cluster = db.find(database.Cluster, 'CAN_Cluster')  # type: database.Cluster

        # test setters
        cluster.can_fd_baud_rate = cluster.can_fd_baud_rate
        cluster.can_io_mode = constants.CanIoMode.CAN

        # test getters
        print(cluster.can_fd_iso_mode)
        print(cluster.can_io_mode)


@pytest.mark.integration
def test_database_cluster_properties_lin():
    with database.Database('NIXNET_exampleLDF') as db:
        cluster = db.clusters['Cluster']  # type: database.Cluster
        assert len(cluster.lin_schedules) > 0
        cluster.lin_tick = cluster.lin_tick
