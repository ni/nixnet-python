from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import mock  # type: ignore
import os
import pytest  # type: ignore

from nixnet import _cfuncs
from nixnet import _ctypedefs
from nixnet import database
from nixnet.database import _dbc_signal_value_table

MockXnetLibrary = mock.create_autospec(_cfuncs.XnetLibrary, spec_set=True, instance=True)
MockXnetLibrary.nxdb_get_dbc_attribute_size.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nxdb_get_dbc_attribute.return_value = _ctypedefs.u32(0)


@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
def test_dbc_signal_value_table():
    dbc_sig_val_table120 = _dbc_signal_value_table.DbcSignalValueTable(120)
    dbc_sig_val_table130_1 = _dbc_signal_value_table.DbcSignalValueTable(130)
    dbc_sig_val_table130_2 = _dbc_signal_value_table.DbcSignalValueTable(130)

    # test dunders
    assert str(dbc_sig_val_table120) == 'DbcSignalValueTable(handle=120)'
    assert dbc_sig_val_table130_1 == dbc_sig_val_table130_2
    assert dbc_sig_val_table130_1 != dbc_sig_val_table120
    assert len({dbc_sig_val_table120, dbc_sig_val_table130_1, dbc_sig_val_table130_2}) == 2  # testing `__hash__`
    assert len(dbc_sig_val_table120) == 0
    for key in dbc_sig_val_table120:
        print(dbc_sig_val_table120[key])
    with pytest.raises(KeyError):
        print(dbc_sig_val_table120[''])
    with pytest.raises(TypeError):
        print(dbc_sig_val_table120[5])

    # test container
    assert sorted(dbc_sig_val_table120.keys()) == []
    assert sorted(dbc_sig_val_table120.values()) == []
    assert sorted(dbc_sig_val_table120.items()) == []


@pytest.mark.integration
def test_signal_dbc_signal_value_table():
    database_filepath = os.path.join(os.path.dirname(__file__), 'databases\\attributes.dbc')
    with database.Database(database_filepath) as db:
        cluster = db.clusters['Cluster']
        frame1 = cluster.frames['Msg1']
        sig1 = frame1.mux_static_signals['Sig1']
        sig2 = frame1.mux_static_signals['Sig2']

        # test dunders
        assert len(sig1.dbc_signal_value_table) == 3
        assert len(sig2.dbc_signal_value_table) == 0
        assert len({sig1.dbc_signal_value_table, sig1.dbc_signal_value_table}) == 1  # testing `__hash__`
        assert len({sig1.dbc_signal_value_table, sig2.dbc_signal_value_table}) == 2  # testing `__hash__`
        assert sig1.dbc_signal_value_table == sig1.dbc_signal_value_table
        assert sig1.dbc_signal_value_table != sig2.dbc_signal_value_table
        for key in sig1.dbc_signal_value_table:
            print(sig1.dbc_signal_value_table[key])

        # test container
        assert sorted(sig1.dbc_signal_value_table.keys()) == ['High', 'Low', 'Zero']
        assert sorted(sig1.dbc_signal_value_table.values()) == ['-10', '0', '4']
        assert sorted(sig1.dbc_signal_value_table.items()) == [('High', '4'), ('Low', '-10'), ('Zero', '0')]

        # test values
        assert sig1.dbc_signal_value_table['Low'] == '-10'
        assert sig1.dbc_signal_value_table['High'] == '4'
        assert sig1.dbc_signal_value_table['Zero'] == '0'
