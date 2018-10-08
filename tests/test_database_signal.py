from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest  # type: ignore

from nixnet import constants
from nixnet import database
from nixnet import errors


@pytest.mark.integration
def test_database_signal_container():
    with database.Database('NIXNET_example') as db:
        cluster = db.clusters['CAN_Cluster']  # type: database.Cluster
        frame = cluster.frames['CANCyclicFrame1']  # type: database.Frame
        sig_1 = frame.mux_static_signals['CANCyclicSignal1']  # type: database.Signal
        sig_2 = frame.mux_static_signals['CANCyclicSignal1']  # type: database.Signal
        sig_3 = frame.mux_static_signals['CANCyclicSignal2']  # type: database.Signal

        # test dunders
        assert sig_1 == sig_2
        assert sig_1 != sig_3
        assert len({sig_1, sig_2, sig_3}) == 2  # testing `__hash__`
        print(repr(sig_1))


@pytest.mark.integration
def test_database_signal_functions():
    with database.Database('NIXNET_example') as db:
        signal = db.find(database.Signal, 'CANCyclicSignal1')  # type: database.Signal
        signal.check_config_status()


@pytest.mark.integration
def test_database_signal_properties():
    with database.Database('NIXNET_example') as db:
        signal = db.find(database.Signal, 'CANCyclicSignal1')  # type: database.Signal

        # test references
        print(signal.frame)
        print(signal.pdu)
        with pytest.raises(errors.XnetError):
            print(signal.mux_subfrm)

        # test setters
        signal.byte_ordr = constants.SigByteOrdr.BIG_ENDIAN
        signal.data_type = constants.SigDataType.IEEE_FLOAT
        signal.comment = 'This is a comment.'
        signal.default = signal.default
        signal.max = signal.max
        signal.min = signal.min
        signal.name = 'NewSignalName'
        signal.num_bits = signal.num_bits
        signal.scale_fac = signal.scale_fac
        signal.scale_off = signal.scale_off
        signal.start_bit = signal.start_bit
        signal.unit = 'Volts'
        signal.mux_is_data_mux = signal.mux_is_data_mux

        # test getters
        print(signal.byte_ordr)
        print(signal.comment)
        print(signal.data_type)
        print(signal.name)
        print(signal.name_unique_to_cluster)
        print(signal.unit)
        print(signal.mux_is_dynamic)
        print(signal.mux_value)
