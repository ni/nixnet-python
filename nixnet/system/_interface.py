from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import typing  # NOQA: F401

import six

from nixnet import _funcs
from nixnet import _props
from nixnet import constants


class Interface(object):
    '''Interfaces associated with a physical hardware device.'''

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(Interface, other._handle)
        elif isinstance(other, six.string_types):
            return self._name == typing.cast(typing.Text, other)
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __str__(self):
        # type: () -> typing.Text
        return self._name

    def __repr__(self):
        # type: () -> typing.Text
        return 'Interface(handle={0})'.format(self._handle)

    # `dev_ref`: Intentionally not exposed to avoid circular imports

    @property
    def num(self):
        # type: () -> int
        '''int: The unique number associated with the XNET interface.

        The XNET driver assigns each port connector in the system a unique
        number XNET driver. This number, plus its protocol name, is the
        interface name.
        '''
        return _props.get_interface_num(self._handle)

    @property
    def port_num(self):
        # type: () -> int
        '''int: Physical port number printed near the connector on the XNET device.

        The port numbers on an XNET board are physically identified with
        numbering. Use this property, along with the XNET Device Serial Number
        property, to associate an XNET interface with a physical (XNET board
        and port) combination.
        '''
        return _props.get_interface_port_num(self._handle)

    @property
    def protocol(self):
        # type: () -> constants.Protocol
        ''':any:`nixnet._enums.Protocol`: Protocol supported by the interface.'''
        return constants.Protocol(_props.get_interface_protocol(self._handle))

    @property
    def can_term_cap(self):
        # type: () -> constants.CanTermCap
        ''':any:`nixnet._enums.CanTermCap`: Indicates whether the XNET interface can terminate the CAN bus.

        Signal reflections on the CAN bus can cause communication failure. To
        prevent reflections, termination can be present as external resistance
        or resistance the XNET board applies internally. This property
        determines whether the XNET board can add termination to the bus.
        '''
        return constants.CanTermCap(_props.get_interface_can_term_cap(self._handle))

    @property
    def can_tcvr_cap(self):
        # type: () -> constants.CanTcvrCap
        ''':any:`nixnet._enums.CanTcvrCap`: Indicates the CAN bus physical transceiver support.'''
        return constants.CanTcvrCap(_props.get_interface_can_tcvr_cap(self._handle))

    @property
    def dongle_state(self):
        # type: () -> constants.DongleState
        ''':any:`nixnet._enums.DongleState`: Indicates the connected Transceiver Cable's state.

        Some Transceiver Cable types require external power from the network
        connector for operation. Refer to the hardware-specific manual for more
        information.
        '''
        return constants.DongleState(_props.get_interface_dongle_state(self._handle))

    @property
    def dongle_id(self):
        # type: () -> constants.DongleId
        ''':any:`nixnet._enums.DongleId`: Indicates the connected Transceiver Cable's type.

        Dongle-Less Design indicates this interface is not a Transceiver Cable
        but a regular XNET expansion card, cDAQ Module, and so on.
        '''
        return constants.DongleId(_props.get_interface_dongle_id(self._handle))

    @property
    def dongle_revision(self):
        # type: () -> int
        '''int: The connected Transceiver Cable's hardware revision number.'''
        return _props.get_interface_dongle_revision(self._handle)

    @property
    def dongle_firmware_version(self):
        # type: () -> int
        '''int: The connected Transceiver Cable's firmware revision number.'''
        return _props.get_interface_dongle_firmware_version(self._handle)

    @property
    def dongle_compatible_revision(self):
        # type: () -> int
        '''int: The oldest driver version compatible with the connected Transceiver Cable's hardware revision.

        The number is relative to the first driver version that supported the
        particular Transceiver Cable model, starting with 1 for the original
        revision.

        .. note:: A Transceiver Cable hardware revision might require a later
           XNET driver than the version that introduced support for this model for
           operation.
        '''
        return _props.get_interface_dongle_compatible_revision(self._handle)

    @property
    def dongle_compatible_firmware_version(self):
        # type: () -> int
        '''int: The oldest driver version compatible with the connected Transceiver Cable's firmware.

        The number is relative to the first driver version that supported the
        Transceiver Cable, starting with 1 for the original revision.

        ..note:: A Transceiver Cable running an updated firmware version may
           require a later XNET driver than the version it shipped with for
           operation.
        '''
        return _props.get_interface_dongle_compatible_firmware_version(self._handle)

    def blink(self, modifier):
        # type: (constants.BlinkMode) -> None
        '''Blinks LEDs for the XNET interface to identify its physical port in the system.

        Each XNET device contains one or two physical ports. Each port is
        labeled on the hardware as Port 1 or Port 2. The XNET device also
        provides two LEDs per port. For a two-port board, LEDs 1 and 2 are
        assigned to Port 1, and LEDs 3 and 4 are assigned to physical Port 2.

        When your application uses multiple XNET devices, this function helps
        to identify each interface to associate its software behavior to its
        hardware connection (port). Prior to running your XNET sessions, you
        can call this function to blink the interface LEDs.

        For example, if you have a system with three PCI CAN cards, each with
        two ports, you can use this function to blink the LEDs for interface
        CAN4, to identify it among the six CAN ports.

        The LEDs of each port support two states:
            Identification:
                Blink LEDs to identify the physical port assigned to the interface.
            In Use:
                LED behavior that XNET sessions control.

        **Identification LED State**

        You can use the ``blink`` function only in the Identification state. If
        you call this function while one or more XNET sessions for the
        interface are open (created), it returns an error, because the port's
        LEDs are in the In Use state.

        **In Use LED State**

        When you create an XNET session for the interface, the LEDs for that
        physical port transition to the In Use state. If you called the ``blink``
        function previously to enable blinking for identification, that LED
        behavior no longer applies. The In Use LED state remains until all XNET
        sessions are cleared. This typically occurs when the application
        terminates. The patterns that appear on the LEDs while In Use are
        documented in LEDs.

        Args:
            moodifier (:any:`nixnet._enums.BlinkMode`): Controls LED blinking

                Both LEDs blink green (not red). The blinking rate is approximately
                three times per second.
        '''
        _funcs.nx_blink(self._handle, modifier)

    @property
    def _name(self):
        # type: () -> typing.Text
        return _props.get_interface_name(self._handle)
