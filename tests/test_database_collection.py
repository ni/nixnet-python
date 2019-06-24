from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest  # type: ignore

from nixnet import database
from nixnet import errors

from nixnet.database import _collection  # NOQA: F401


@pytest.mark.integration
def test_database_collection_container():
    test_cluster_name = '__cluster__name__for__testing__'
    with database.Database('NIXNET_example') as db:
        collection_1 = db.clusters  # type: _collection.DbCollection
        collection_2 = db.clusters  # type: _collection.DbCollection
        collection_3 = db.clusters['CAN_Cluster'].ecus  # type: _collection.DbCollection

        # test dunders
        assert collection_1 == collection_2
        assert collection_1 != collection_3
        assert len({collection_1, collection_2, collection_3}) == 2  # testing `__hash__`
        print(repr(collection_1))
        for key in collection_1:
            print(collection_1[key])
        with pytest.raises(errors.XnetError):
            print(collection_1[test_cluster_name])
        with pytest.raises(TypeError):
            print(collection_1[5])

        # test '__del__' after using the add function
        cluster = db.clusters.add(test_cluster_name)
        assert (cluster == db.clusters[test_cluster_name])
        del db.clusters[test_cluster_name]
        with pytest.raises(errors.XnetError):
            print(db.clusters[test_cluster_name])

        # test container
        assert len(list(collection_1.keys())) > 0
        assert len(list(collection_1.values())) > 0
        assert len(list(collection_1.items())) > 0
