import pytest  # type: ignore

from nixnet import constants
from nixnet import database
from nixnet import errors


@pytest.mark.integration
def test_database_frame_container():
    with database.Database('NIXNET_example') as db:
        cluster = db.clusters['CAN_Cluster']  # type: database.Cluster
        frame_1 = cluster.frames['CANCyclicFrame1']  # type: database.Frame
        frame_2 = cluster.frames['CANCyclicFrame1']  # type: database.Frame
        frame_3 = cluster.frames['CANCyclicFrame2']  # type: database.Frame

        # test dunders
        assert frame_1 == frame_2
        assert frame_1 != frame_3
        assert len({frame_1, frame_2, frame_3}) == 2  # testing `__hash__`
        print(repr(frame_1))


@pytest.mark.integration
def test_database_frame_functions():
    with database.Database('NIXNET_example') as db:
        frame = db.find(database.Frame, 'CANCyclicFrame1')  # type: database.Frame
        frame.check_config_status()
        frame.find(database.Signal, 'CANCyclicSignal1')


@pytest.mark.integration
def test_database_frame_properties_common():
    with database.Database('NIXNET_example') as db:
        frame = db.find(database.Frame, 'CANCyclicFrame1')  # type: database.Frame

        # test references
        print(frame.cluster)
        assert len(list(frame.sigs)) > 0
        assert len(list(frame.pdu_properties)) > 0
        assert len(frame.mux_static_signals) > 0
        assert len(frame.mux_subframes) == 0
        with pytest.raises(errors.XnetError):
            print(frame.mux_data_mux_sig)

        # test setters
        frame.application_protocol = constants.AppProtocol.NONE
        frame.comment = 'This is a comment.'
        frame.default_payload = list(frame.default_payload)
        frame.id = frame.id
        frame.name = 'NewFrameName'
        frame.payload_len = frame.payload_len
        frame.variable_payload = frame.variable_payload

        # test getters
        print(frame.application_protocol)
        print(frame.comment)
        print(frame.name)
        print(frame.mux_is_muxed)


@pytest.mark.integration
def test_database_frame_properties_can():
    with database.Database('NIXNET_example') as db:
        frame = db.find(database.Frame, 'CANCyclicFrame1')  # type: database.Frame
        frame.can_ext_id = frame.can_ext_id
        frame.can_tx_time = frame.can_tx_time
        frame.can_timing_type = constants.FrmCanTiming.CYCLIC_DATA
        print(frame.can_timing_type)


@pytest.mark.integration
def test_database_frame_properties_lin():
    with database.Database('NIXNET_exampleLDF') as db:
        frame = db.find(database.Frame, 'MasterFrame1')  # type: database.Frame
        print(frame.lin_checksum)
