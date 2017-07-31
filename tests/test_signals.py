from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time

import pytest  # type: ignore

import nixnet
from nixnet import _ctypedefs
from nixnet._session import signals as session_signals


@pytest.fixture
def nixnet_in_interface(request):
    interface = request.config.getoption("--nixnet-in-interface")
    return interface


@pytest.fixture
def nixnet_out_interface(request):
    interface = request.config.getoption("--nixnet-out-interface")
    return interface


@pytest.mark.integration
def test_signals_container(nixnet_in_interface):
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    signal_name = 'CANEventSignal1'

    with nixnet.SignalInSinglePointSession(
            nixnet_in_interface,
            database_name,
            cluster_name,
            signal_name) as input_session:
        assert signal_name in input_session.signals
        assert 0 in input_session.signals

        assert len(input_session.signals) == 1
        signals = list(input_session.signals)
        assert len(signals) == 1
        signal = signals[0]

        assert str(signal) == signal_name
        assert int(signal) == 0

        assert signal == input_session.signals[0]
        assert signal == input_session.signals[signal_name]
        with pytest.raises(IndexError):
            input_session.signals[1]
        with pytest.raises(KeyError):
            input_session.signals["<random>"]

        assert signal == input_session.signals.get(0)
        assert signal == input_session.signals.get(signal_name)
        assert input_session.signals.get(1) is None
        assert input_session.signals.get("<random>") is None


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


def test_waveform_unflatten_empty():
    signals = session_signals.WaveformInSignals._unflatten_signals([], 0, 0)
    assert len(signals) == 0


def test_waveform_unflatten_single_signal():
    signals = session_signals.WaveformInSignals._unflatten_signals(
        [_ctypedefs.f64(v) for v in [0, 1, 2, 3]],
        4,
        1)
    assert signals == [[0, 1, 2, 3]]


def test_waveform_unflatten_multi_signal():
    signals = session_signals.WaveformInSignals._unflatten_signals(
        [_ctypedefs.f64(v) for v in [0, 1, 2, 3]],
        2,
        2)
    assert signals == [[0, 1], [2, 3]]


def generate_ramp(min, max, rate, length):
    """Generate ramp for test data

    Args:
        min(float): minimum value
        max(float): maximum value
        rate(float): rate data is transmitted (Hz)
        length(float): Duration of ramp (secs)
    """
    samples = int(rate * length)
    step = (max - min) / samples
    return [
        min + step * i
        for i in range(samples)
    ]


@pytest.mark.integration
def test_waveform_loopback(nixnet_in_interface, nixnet_out_interface):
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    signal_names = 'CANEventSignal1'

    with nixnet.SignalInWaveformSession(
            nixnet_in_interface,
            database_name,
            cluster_name,
            signal_names) as input_session:
        with nixnet.SignalOutWaveformSession(
                nixnet_out_interface,
                database_name,
                cluster_name,
                signal_names) as output_session:
            output_session.signals.resamp_rate = 1000
            input_session.signals.resamp_rate = output_session.signals.resamp_rate / 2
            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start()

            signal_ramp = generate_ramp(4, 11, output_session.signals.resamp_rate, 0.25)
            output_session.signals.write([signal_ramp])

            # Wait 1 s and then read the received values.
            # They should be the same as the ones sent.
            time.sleep(1)

            t0, dt, waveforms = input_session.signals.read(len(signal_ramp))
            print(t0)
            assert pytest.approx(dt, 1 / input_session.signals.resamp_rate)
            assert len(waveforms) == 1
            for expected, actual in zip(signal_ramp, waveforms[0]):
                assert pytest.approx(expected, rel=0.1) == actual
