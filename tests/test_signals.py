from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import time

import pytest

import nixnet


@pytest.fixture
def nixnet_in_interface(request):
    interface = request.config.getoption("--nixnet-in-interface")
    return interface


@pytest.fixture
def nixnet_out_interface(request):
    interface = request.config.getoption("--nixnet-out-interface")
    return interface


@pytest.mark.integration
def test_singlepoint_loopback(nixnet_in_interface, nixnet_out_interface):
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    signal_names = ['CANEventSignal1', 'CANEventSignal2']

    with nixnet.SignalInSinglePointSession(
            nixnet_in_interface,
            database_name,
            cluster_name,
            signal_names) as input_session:
        with nixnet.SignalOutSinglePointSession(
                nixnet_out_interface,
                database_name,
                cluster_name,
                signal_names) as output_session:
            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start()

            expected_signals = [24.5343, 77.0129]
            output_session.signals.write(expected_signals)

            # Wait 1 s and then read the received values.
            # They should be the same as the ones sent.
            time.sleep(1)

            actual_signals = list(input_session.signals.read())
            for expected, (_, actual) in zip(expected_signals, actual_signals):
                assert pytest.approx(expected, rel=1) == actual