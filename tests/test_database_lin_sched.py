from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest  # type: ignore

from nixnet import constants
from nixnet import database


@pytest.mark.integration
def test_database_lin_sched_container():
    with database.Database('NIXNET_exampleLDF') as db:
        cluster = db.clusters['Cluster']  # type: database.Cluster
        sched_1 = cluster.lin_schedules['FastSchedule']  # type: database.LinSched
        sched_2 = cluster.lin_schedules['FastSchedule']  # type: database.LinSched
        sched_3 = cluster.lin_schedules['SlowSchedule']  # type: database.LinSched

        # test dunders
        assert sched_1 == sched_2
        assert sched_1 != sched_3
        assert len({sched_1, sched_2, sched_3}) == 2  # testing `__hash__`
        print(repr(sched_1))


@pytest.mark.integration
def test_database_lin_sched_functions():
    with database.Database('NIXNET_exampleLDF') as db:
        sched = db.find(database.LinSched, 'FastSchedule')  # type: database.LinSched
        sched.check_config_status()
        sched.find(database.LinSchedEntry, 'se1')


@pytest.mark.integration
def test_database_lin_sched_properties():
    with database.Database('NIXNET_exampleLDF') as db:
        sched = db.find(database.LinSched, 'FastSchedule')  # type: database.LinSched

        # test references
        print(sched.clst)
        assert len(sched.entries) > 0

        # test setters
        sched.comment = 'This is a comment.'
        sched.name = 'NewScheduleName'
        sched.priority = sched.priority
        sched.run_mode = constants.LinSchedRunMode.NULL

        # test getters
        print(sched.comment)
        print(sched.name)
        print(sched.run_mode)
