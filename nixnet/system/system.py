from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import warnings

import constants
from nixnet import _funcs
from nixnet import _props
from nixnet import errors


class System(object):

    def __init__(self):
        self._handle = _funcs.nx_system_open()

    def __del__(self):
        if self._handle is not None:
            warnings.warn(
                'System was not explicitly closed before it was destructed. '
                'Resources on the device may still be reserved.',
                errors.XnetResourceWarning)

    def __enter__(self):
        return self

    def __exit__(self):
        self.close()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        return 'System(handle={0})'.format(self._handle)

    def close(self):
        if self._handle is None:
            warnings.warn(
                'Attempting to close NI-XNET system but system was already '
                'closed', errors.XnetResourceWarning)
            return

        _funcs.nx_system_close(self._handle)

        self._handle = None

    @property
    def dev_refs(self):
        return _props.get_system_dev_refs(self._handle)

    @property
    def intf_refs(self):
        return _props.get_system_intf_refs(self._handle)

    @property
    def intf_refs_can(self):
        return _props.get_system_intf_refs_can(self._handle)

    @property
    def intf_refs_flex_ray(self):
        return _props.get_system_intf_refs_flex_ray(self._handle)

    @property
    def intf_refs_lin(self):
        return _props.get_system_intf_refs_lin(self._handle)

    @property
    def ver_build(self):
        return _props.get_system_ver_build(self._handle)

    @property
    def ver_major(self):
        return _props.get_system_ver_major(self._handle)

    @property
    def ver_minor(self):
        return _props.get_system_ver_minor(self._handle)

    @property
    def ver_phase(self):
        return constants.Phase(_props.get_system_ver_phase(self._handle))

    @property
    def ver_update(self):
        return _props.get_system_ver_update(self._handle)

    @property
    def cdaq_pkt_time(self):
        return _props.get_system_cdaq_pkt_time(self._handle)

    @cdaq_pkt_time.setter
    def cdaq_pkt_time(self, value):
        _props.set_system_cdaq_pkt_time(self._handle, value)

    @property
    def intf_refs_all(self):
        return _props.get_system_intf_refs_all(self._handle)
