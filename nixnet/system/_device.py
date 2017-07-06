from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _props
from nixnet import constants

from nixnet.system import _interface


class Device(object):

    def __init__(self, handle):
        self._handle = handle

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._handle)

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Device(handle={0})'.format(self._handle)

    @property
    def form_fac(self):
        return constants.DevForm(_props.get_device_form_fac(self._handle))

    @property
    def intf_refs(self):
        for ref in _props.get_device_intf_refs(self._handle):
            yield _interface.Interface(ref)

    @property
    def name(self):
        return _props.get_device_name(self._handle)

    @property
    def num_ports(self):
        return _props.get_device_num_ports(self._handle)

    @property
    def product_num(self):
        return _props.get_device_product_num(self._handle)

    @property
    def ser_num(self):
        return _props.get_device_ser_num(self._handle)

    @property
    def slot_num(self):
        return _props.get_device_slot_num(self._handle)

    @property
    def num_ports_all(self):
        return _props.get_device_num_ports_all(self._handle)

    @property
    def intf_refs_all(self):
        for ref in _props.get_device_intf_refs_all(self._handle):
            yield _interface.Interface(ref)
