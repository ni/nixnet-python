from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import typing  # NOQA: F401

from nixnet import _props
from nixnet import constants

from nixnet.system import _interface


class Device(object):
    '''Physical XNET devices in the system.'''

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(Device, other._handle)
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

    def __repr__(self):
        # type: () -> typing.Text
        return 'Device(handle={0})'.format(self._handle)

    @property
    def form_fac(self):
        # type: () -> constants.DevForm
        ''':any:`nixnet._enums.DevForm`: XNET board form factor.'''
        return constants.DevForm(_props.get_device_form_fac(self._handle))

    @property
    def intf_refs(self):
        # type: () -> typing.Iterable[_interface.Interface]
        '''iter of :any:`nixnet.system._interface.Interface`: Interfaces associated with this device.'''
        for ref in _props.get_device_intf_refs(self._handle):
            yield _interface.Interface(ref)

    @property
    def intf_refs_all(self):
        # type: () -> typing.Iterable[_interface.Interface]
        '''iter of :any:`nixnet.system._interface.Interface`: Interfaces associated with this device.

        This Includes those not equipped with a Transceiver Cable.
        '''
        for ref in _props.get_device_intf_refs_all(self._handle):
            yield _interface.Interface(ref)

    @property
    def num_ports(self):
        # type: () -> int
        '''int: The number of physical port connectors on the XNET board.'''
        return _props.get_device_num_ports(self._handle)

    @property
    def num_ports_all(self):
        # type: () -> int
        '''int: The number of physical port connectors on the XNET board.

        This Includes those not equipped with a Transceiver Cable.
        '''
        return _props.get_device_num_ports_all(self._handle)

    @property
    def product_num(self):
        # type: () -> int
        '''int: The numeric portion of the XNET device product name.'''
        return _props.get_device_product_num(self._handle)

    @property
    def product_name(self):
        # type: () -> typing.Text
        '''str: The XNET device product name.'''
        return _props.get_device_name(self._handle)

    @property
    def ser_num(self):
        # type: () -> int
        '''int: Serial number associated with the XNET device.'''
        return _props.get_device_ser_num(self._handle)

    @property
    def slot_num(self):
        # type: () -> int
        '''int: Physical slot where the module is located within a chassis.'''
        return _props.get_device_slot_num(self._handle)
