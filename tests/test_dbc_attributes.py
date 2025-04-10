from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import pytest  # type: ignore
from unittest import mock  # type: ignore

from nixnet import _cfuncs
from nixnet import _ctypedefs
from nixnet import database
from nixnet.database import _dbc_attributes

MockXnetLibrary = mock.create_autospec(_cfuncs.XnetLibrary, spec_set=True, instance=True)
MockXnetLibrary.nxdb_get_dbc_attribute_size.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nxdb_get_dbc_attribute.return_value = _ctypedefs.u32(0)


@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
def test_dbc_attributes():
    dbc_attributes120 = _dbc_attributes.DbcAttributeCollection(120)
    dbc_attributes130_1 = _dbc_attributes.DbcAttributeCollection(130)
    dbc_attributes130_2 = _dbc_attributes.DbcAttributeCollection(130)

    # test dunders
    assert str(dbc_attributes120) == 'DbcAttributeCollection(handle=120)'
    assert dbc_attributes130_1 == dbc_attributes130_2
    assert dbc_attributes130_1 != dbc_attributes120
    assert len({dbc_attributes120, dbc_attributes130_1, dbc_attributes130_2}) == 2  # testing `__hash__`
    assert len(dbc_attributes120) == 0
    for key in dbc_attributes120:
        print(dbc_attributes120[key])
    with pytest.raises(KeyError):
        print(dbc_attributes120[''])
    with pytest.raises(TypeError):
        print(dbc_attributes120[5])

    # test container
    assert sorted(dbc_attributes120.keys()) == []
    assert sorted(dbc_attributes120.values()) == []
    assert sorted(dbc_attributes120.items()) == []


@pytest.mark.integration
def test_cluster_dbc_attributes():
    database_filepath = os.path.join(os.path.dirname(__file__), 'databases\\attributes.dbc')
    with database.Database(database_filepath) as db:
        cluster = db.clusters['Cluster']
        frame1 = cluster.frames['Msg1']

        # test dunders
        assert len(cluster.dbc_attributes) == 2
        assert len({cluster.dbc_attributes, cluster.dbc_attributes}) == 1  # testing `__hash__`
        assert len({cluster.dbc_attributes, frame1.dbc_attributes}) == 2  # testing `__hash__`
        assert cluster.dbc_attributes == cluster.dbc_attributes
        assert cluster.dbc_attributes != frame1.dbc_attributes
        for key in cluster.dbc_attributes:
            print(cluster.dbc_attributes[key])

        # test container
        assert sorted(cluster.dbc_attributes.keys()) == ['BusType', 'NetworkAttr1']
        assert sorted(cluster.dbc_attributes.values()) == [('CAN', True), ('abc', True)]
        assert sorted(cluster.dbc_attributes.items()) == [('BusType', ('CAN', True)), ('NetworkAttr1', ('abc', True))]

        # test values
        assert cluster.dbc_attributes['BusType'] == ('CAN', True)
        assert cluster.dbc_attributes['NetworkAttr1'] == ('abc', True)


@pytest.mark.integration
def test_ecu_dbc_attributes():
    database_filepath = os.path.join(os.path.dirname(__file__), 'databases\\attributes.dbc')
    with database.Database(database_filepath) as db:
        cluster = db.clusters['Cluster']
        ecu1 = cluster.ecus['ECU1']
        ecu2 = cluster.ecus['ECU2']

        # test dunders
        assert len(ecu1.dbc_attributes) == 1
        assert len({ecu1.dbc_attributes, ecu1.dbc_attributes}) == 1  # testing `__hash__`
        assert len({ecu1.dbc_attributes, ecu2.dbc_attributes}) == 2  # testing `__hash__`
        assert ecu1.dbc_attributes == ecu1.dbc_attributes
        assert ecu1.dbc_attributes != ecu2.dbc_attributes
        for key in ecu1.dbc_attributes:
            print(ecu1.dbc_attributes[key])

        # test container
        assert sorted(ecu1.dbc_attributes.keys()) == ['EcuAttr1']
        assert sorted(ecu1.dbc_attributes.items()) == [('EcuAttr1', ('xEcu1', True))]
        assert sorted(ecu1.dbc_attributes.values()) == [('xEcu1', True)]

        # test values
        assert ecu1.dbc_attributes['EcuAttr1'] == ('xEcu1', True)
        assert ecu2.dbc_attributes['EcuAttr1'] == ('xEcu2-Set', False)


@pytest.mark.integration
def test_frame_dbc_attributes():
    database_filepath = os.path.join(os.path.dirname(__file__), 'databases\\attributes.dbc')
    with database.Database(database_filepath) as db:
        cluster = db.clusters['Cluster']
        frame1 = cluster.frames['Msg1']
        frame2 = cluster.frames['Msg2']

        # test dunders
        assert len(frame1.dbc_attributes) == 4
        assert len({frame1.dbc_attributes, frame1.dbc_attributes}) == 1  # testing `__hash__`
        assert len({frame1.dbc_attributes, frame2.dbc_attributes}) == 2  # testing `__hash__`
        assert frame1.dbc_attributes == frame1.dbc_attributes
        assert frame1.dbc_attributes != frame2.dbc_attributes
        for key in frame1.dbc_attributes:
            print(frame1.dbc_attributes[key])

        # test container
        assert sorted(frame1.dbc_attributes.keys()) == ['MsgAttr1', 'MsgAttr2', 'MsgAttr3', 'MsgAttr4']
        assert sorted(frame1.dbc_attributes.values()) == [('-11.1', True),
                                                          ('2', True),
                                                          ('2', True),
                                                          ('DefaultMsgAttr3String', True)]
        assert sorted(frame1.dbc_attributes.items()) == [('MsgAttr1', ('2', True)),
                                                         ('MsgAttr2', ('-11.1', True)),
                                                         ('MsgAttr3', ('DefaultMsgAttr3String', True)),
                                                         ('MsgAttr4', ('2', True))]

        # test values
        assert frame1.dbc_attributes['MsgAttr1'] == ('2', True)
        assert frame1.dbc_attributes['MsgAttr2'] == ('-11.1', True)
        assert frame1.dbc_attributes['MsgAttr3'] == ('DefaultMsgAttr3String', True)
        assert frame1.dbc_attributes['MsgAttr4'] == ('2', True)
        assert frame2.dbc_attributes['MsgAttr1'] == ('22', False)
        assert frame2.dbc_attributes['MsgAttr2'] == ('-23.33', False)
        assert frame2.dbc_attributes['MsgAttr3'] == ('MsgAttr3String', False)
        assert frame2.dbc_attributes['MsgAttr4'] == ('1', False)


@pytest.mark.integration
def test_signal_dbc_attributes():
    database_filepath = os.path.join(os.path.dirname(__file__), 'databases\\attributes.dbc')
    with database.Database(database_filepath) as db:
        cluster = db.clusters['Cluster']
        frame1 = cluster.frames['Msg1']
        sig1 = frame1.mux_static_signals['Sig1']
        sig2 = frame1.mux_static_signals['Sig2']

        # test dunders
        assert len(sig1.dbc_attributes) == 1
        assert len({sig1.dbc_attributes, sig1.dbc_attributes}) == 1  # testing `__hash__`
        assert len({sig1.dbc_attributes, sig2.dbc_attributes}) == 2  # testing `__hash__`
        assert sig1.dbc_attributes == sig1.dbc_attributes
        assert sig1.dbc_attributes != sig2.dbc_attributes
        for key in sig1.dbc_attributes:
            print(sig1.dbc_attributes[key])

        # test container
        assert sorted(sig2.dbc_attributes.keys()) == ['SigAttr1']
        assert sorted(sig2.dbc_attributes.values()) == [('11', False)]
        assert sorted(sig2.dbc_attributes.items()) == [('SigAttr1', ('11', False))]

        # test values
        assert sig1.dbc_attributes['SigAttr1'] == ('1', True)
        assert sig2.dbc_attributes['SigAttr1'] == ('11', False)
