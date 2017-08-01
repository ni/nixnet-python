from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest  # type: ignore

from nixnet import constants
from nixnet import convert
from nixnet import errors


def raise_code(code):
    raise errors.XnetError("", code)


@pytest.mark.integration
def test_session_container():
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    signals = ['CANEventSignal1', 'CANEventSignal2']

    with convert.SignalConversionSinglePointSession(
            database_name,
            cluster_name,
            signals) as session:
        with convert.SignalConversionSinglePointSession(
                database_name,
                cluster_name,
                signals) as dup_session:
            assert session == session
            assert not (session == dup_session)
            assert not (session == 1)

            assert not (session != session)
            assert session != dup_session
            assert session != 1

        set([session])  # Testing `__hash__`

        print(repr(session))

    with pytest.warns(errors.XnetResourceWarning):
        session.close()


@pytest.mark.integration
def test_session_properties():
    """Verify Session properties.

    Ideally, mutable properties would be set to multiple values and we'd test
    for the intended side-effect.  That'll be a massive undertaking.  For now,
    ensure they are settable and getttable.
    """
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    signals = ['CANEventSignal1', 'CANEventSignal2']

    with convert.SignalConversionSinglePointSession(
            database_name,
            cluster_name,
            signals) as session:
        assert session.database_name == database_name
        assert session.cluster_name == cluster_name
        assert session.mode == constants.CreateSessionMode.SIGNAL_CONVERSION_SINGLE_POINT
        assert session.application_protocol == constants.AppProtocol.NONE
        assert session.protocol == constants.Protocol.CAN


@pytest.mark.integration
def test_conversion_roundtrip():
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    signal_names = ['CANEventSignal1', 'CANEventSignal2']

    with convert.SignalConversionSinglePointSession(
            database_name,
            cluster_name,
            signal_names) as session:

        expected_signals = [2, 3]
        frames = session.convert_signals_to_frames(expected_signals)
        converted_signals = session.convert_frames_to_signals(frames)
        for expected, (_, converted) in zip(expected_signals, converted_signals):
            assert pytest.approx(expected) == converted
