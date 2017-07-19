from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import typing  # NOQA: F401

import six

from nixnet import _props
from nixnet import constants

from nixnet.system import _interface


class Device(object):

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(Device, other._handle)
        elif isinstance(other, six.string_types):
            return self._name == typing.cast(typing.Text, other)
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._handle)

    def __str__(self):
        # type: () -> typing.Text
        return self._name

    def __repr__(self):
        # type: () -> typing.Text
        return 'Device(handle={0})'.format(self._handle)

    @property
    def form_fac(self):
        # type: () -> constants.DevForm
        return constants.DevForm(_props.get_device_form_fac(self._handle))

    @property
    def intf_refs(self):
        # type: () -> typing.Iterable[_interface.Interface]
        for ref in _props.get_device_intf_refs(self._handle):
            yield _interface.Interface(ref)

    @property
    def num_ports(self):
        # type: () -> int
        return _props.get_device_num_ports(self._handle)

    @property
    def product_num(self):
        # type: () -> int
        return _props.get_device_product_num(self._handle)

    @property
    def ser_num(self):
        # type: () -> int
        return _props.get_device_ser_num(self._handle)

    @property
    def slot_num(self):
        # type: () -> int
        return _props.get_device_slot_num(self._handle)

    @property
    def num_ports_all(self):
        # type: () -> int
        return _props.get_device_num_ports_all(self._handle)

    @property
    def intf_refs_all(self):
        # type: () -> typing.Iterable[_interface.Interface]
        for ref in _props.get_device_intf_refs_all(self._handle):
            yield _interface.Interface(ref)

    @property
    def _name(self):
        # type: () -> typing.Text
        return _props.get_device_name(self._handle)
