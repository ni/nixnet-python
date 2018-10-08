from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest  # type: ignore

from nixnet import database
from nixnet import errors


@pytest.mark.integration
def test_database_lin_sched_entry_container():
    with database.Database('NIXNET_exampleLDF') as db:
        cluster = db.clusters['Cluster']  # type: database.Cluster
        sched = cluster.lin_schedules['FastSchedule']  # type: database.LinSched
        entry_1 = sched.entries['se1']  # type: database.LinSchedEntry
        entry_2 = sched.entries['se1']  # type: database.LinSchedEntry
        entry_3 = sched.entries['se2']  # type: database.LinSchedEntry

        # test dunders
        assert entry_1 == entry_2
        assert entry_1 != entry_3
        assert len({entry_1, entry_2, entry_3}) == 2  # testing `__hash__`
        print(repr(entry_1))


@pytest.mark.integration
def test_database_lin_sched_entry_properties():
    with database.Database('NIXNET_exampleLDF') as db:
        entry = db.find(database.LinSchedEntry, 'se1')  # type: database.LinSchedEntry

        # test references
        assert len(list(entry.frames)) > 0
        print(entry.sched)
        with pytest.raises(errors.XnetError):
            print(entry.collision_res_sched)

        # test setters
        entry.delay = entry.delay
        entry.event_id = 1
        entry.name = 'NewEntryName'
        entry.type = entry.type

        # test getters
        print(entry.event_id)
        print(entry.name)
        print(entry.name_unique_to_cluster)
