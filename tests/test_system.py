from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import time

import pytest  # type: ignore

import nixnet
from nixnet import constants
from nixnet import errors
from nixnet import system


@pytest.fixture
def nixnet_in_interface(request):
    interface = request.config.getoption("--nixnet-in-interface")
    return interface


@pytest.fixture
def nixnet_out_interface(request):
    interface = request.config.getoption("--nixnet-out-interface")
    return interface


@pytest.mark.integration
def test_system_properties():
    """Verify System properties.

    These are pretty transient and can't easily be verified against known good
    values.  For now, we'll just verify the calls don't call catastrophically
    and someone can always run py.test with ``-s``_.
    """
    with system.System() as sys:
        print(sys.ver)
        print(sys.cdaq_pkt_time)


@pytest.mark.integration
def test_system_intf_refs_all_superset(nixnet_in_interface, nixnet_out_interface):
    with system.System() as sys:
        intfs = set(sys.intf_refs_all)
        can_intfs = set(sys.intf_refs_can)
        flex_ray_intfs = set(sys.intf_refs_flex_ray)
        lin_intfs = set(sys.intf_refs_lin)
        assert intfs == can_intfs | flex_ray_intfs | lin_intfs


@pytest.mark.integration
def test_device_container():
    with system.System() as sys:
        devs = list(sys.dev_refs)
        assert 0 < len(devs), "Pre-requisite failed"
        dev = devs[0]
        assert dev == str(dev)


@pytest.mark.integration
def test_device_properties(nixnet_in_interface):
    """Verify Device properties.

    Ideally we'd match these against a known piece of hardware to ensure the
    correct values are being returned.  That makes it hard though for someone
    to run these tests with any piece of hardware for most properties.  For
    now, we'll just verify the calls don't call catastrophically and someone
    can always run py.test with ``-s``_.  For ``int_refs_all``, we can at least
    make sure that one device reports ``nixnet_in_interface``_.
    """
    with system.System() as sys:
        devs = list(sys.dev_refs)
        assert 0 < len(devs), "Pre-requisite failed"
        for dev in devs:
            in_intfs = [intf for intf in dev.intf_refs_all if intf == nixnet_in_interface]
            if len(in_intfs) == 1:
                break
        else:
            raise RuntimeError("Pre-requisite failed: can't find device for interface")

        print(dev.form_fac)
        print(dev.num_ports)
        print(dev.product_num)
        print(dev.ser_num)
        print(dev.slot_num)
        print(dev.num_ports_all)


@pytest.mark.integration
def test_intf_container(nixnet_in_interface):
    with system.System() as sys:
        intfs = set(sys.intf_refs_all)

        in_intfs = [intf for intf in intfs if intf == nixnet_in_interface]
        assert len(in_intfs) == 1
        in_intf = in_intfs[0]

        assert str(in_intf) == nixnet_in_interface


@pytest.mark.integration
def test_intf_blink(nixnet_in_interface):
    """Verify LEDs can be blinked.

    Since we don't have a camera watching the LEDs, we can at least test if we
    are having an impact by checking

    - `ENABLE` works anytime except a session is in use
    - `DISABLE` always works

    Sleeps are in place in case this in case a visual confirmation is possible
    by the developer.
    """
    with system.System() as sys:
        intfs = set(sys.intf_refs_all)
        in_intfs = [intf for intf in intfs if intf == nixnet_in_interface]
        assert len(in_intfs) == 1, "Pre-requisite failed"
        in_intf = in_intfs[0]

        # Smoke-test the function calls
        in_intf.blink(constants.BlinkMode.ENABLE)
        time.sleep(0.01)
        in_intf.blink(constants.BlinkMode.DISABLE)
        time.sleep(0.01)
        with nixnet.FrameInStreamSession(nixnet_in_interface) as input_session:
            input_session.intf.baud_rate = 125000
            input_session.start()
            with pytest.raises(errors.XnetError) as excinfo:
                in_intf.blink(constants.BlinkMode.ENABLE)
            assert excinfo.value.error_type == constants.Err.PORT_LE_DS_BUSY
            in_intf.blink(constants.BlinkMode.DISABLE)
        in_intf.blink(constants.BlinkMode.ENABLE)
        in_intf.blink(constants.BlinkMode.DISABLE)


@pytest.mark.integration
def test_intf_properties(nixnet_in_interface):
    """Verify Interface properties.

    Ideally we'd match these against a known piece of hardware to ensure the
    correct values are being returned.  That makes it hard though for someone
    to run these tests with any piece of hardware.  For now, we'll just verify
    the calls don't call catastrophically and someone can always run py.test
    with ``-s``_.
    """
    with system.System() as sys:
        intfs = set(sys.intf_refs_all)
        in_intfs = [intf for intf in intfs if intf == nixnet_in_interface]
        assert len(in_intfs) == 1, "Pre-requisite failed"
        in_intf = in_intfs[0]

        print(in_intf.num)
        print(in_intf.port_num)
        print(in_intf.protocol)
        print(in_intf.can_term_cap)
        print(in_intf.dongle_state)
        print(in_intf.dongle_id)
        if in_intf.dongle_id not in [constants.DongleId.DONGLE_LESS, constants.DongleId.UNKNOWN]:
            print(in_intf.dongle_revision)
            print(in_intf.dongle_firmware_version)
            print(in_intf.dongle_compatible_revision)
            print(in_intf.dongle_compatible_firmware_version)
