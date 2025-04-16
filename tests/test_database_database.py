import os
import pytest  # type: ignore
import tempfile

from nixnet import database


@pytest.mark.integration
def test_database_database_container():
    with database.Database('NIXNET_example') as db_1:
        with database.Database('NIXNET_exampleLDF') as db_2:
            db_3 = database.Database('NIXNET_example')

            # test dunders
            assert db_1 == db_3
            assert db_1 != db_2
            assert len({db_1, db_2, db_3}) == 2  # testing `__hash__`
            print(repr(db_1))

            db_3.close()
            del db_3


@pytest.mark.integration
def test_database_database_find():
    with database.Database('NIXNET_example') as db:
        cluster = db.clusters['CAN_Cluster']  # type: database.Cluster
        frame_1 = cluster.frames['CANEventFrame1']
        frame_2 = db.find(database.Frame, 'CANEventFrame1')
        assert frame_1 == frame_2


@pytest.mark.integration
def test_database_database_properties():
    with database.Database('NIXNET_example') as db:
        assert len(db.clusters) > 0
        assert db.name == 'NIXNET_example'
        db.show_invalid_from_open = db.show_invalid_from_open


@pytest.mark.integration
def test_database_database_save():
    # Avoid using an installed example database for saving to ensure those aren't modified.
    # Instead, save the pre-existing 'attributes.dbc' database to a temp XML (FIBEX).
    input_filepath = os.path.join(os.path.dirname(__file__), 'databases\\attributes.dbc')
    output_filepath = tempfile.NamedTemporaryFile(suffix='.xml', delete=False).name
    with database.Database(input_filepath) as db:
        db.save(output_filepath)
