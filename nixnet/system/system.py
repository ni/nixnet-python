from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import typing  # NOQA: F401
import warnings

from nixnet import _funcs
from nixnet import _props
from nixnet import constants
from nixnet import errors
from nixnet import types

from nixnet.system import _device
from nixnet.system import _interface


class System(object):

    def __init__(self):
        # type: () -> None
        self._handle = None  # To satisfy `__del__` in case nx_system_open throws
        self._handle = _funcs.nx_system_open()

    def __del__(self):
        if self._handle is not None:
            warnings.warn(
                'System was not explicitly closed before it was destructed. '
                'Resources on the device may still be reserved.',
                errors.XnetResourceWarning)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(System, other._handle)
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        # type: () -> typing.Text
        return 'System(handle={0})'.format(self._handle)

    def close(self):
        # type: () -> None
        if self._handle is None:
            warnings.warn(
                'Attempting to close NI-XNET system but system was already '
                'closed', errors.XnetResourceWarning)
            return

        _funcs.nx_system_close(self._handle)

        self._handle = None

    @property
    def dev_refs(self):
        # type: () -> typing.Iterable[_device.Device]
        for ref in _props.get_system_dev_refs(self._handle):
            yield _device.Device(ref)

    @property
    def intf_refs(self):
        # type: () -> typing.Iterable[_interface.Interface]
        for ref in _props.get_system_intf_refs(self._handle):
            yield _interface.Interface(ref)

    @property
    def intf_refs_can(self):
        # type: () -> typing.Iterable[_interface.Interface]
        for ref in _props.get_system_intf_refs_can(self._handle):
            yield _interface.Interface(ref)

    @property
    def intf_refs_flex_ray(self):
        # type: () -> typing.Iterable[_interface.Interface]
        for ref in _props.get_system_intf_refs_flex_ray(self._handle):
            yield _interface.Interface(ref)

    @property
    def intf_refs_lin(self):
        # type: () -> typing.Iterable[_interface.Interface]
        for ref in _props.get_system_intf_refs_lin(self._handle):
            yield _interface.Interface(ref)

    @property
    def ver(self):
        # type: () -> types.DriverVersion
        return types.DriverVersion(
            self._ver_major,
            self._ver_minor,
            self._ver_update,
            self._ver_phase,
            self._ver_build)

    @property
    def _ver_build(self):
        # type: () -> int
        return _props.get_system_ver_build(self._handle)

    @property
    def _ver_major(self):
        # type: () -> int
        return _props.get_system_ver_major(self._handle)

    @property
    def _ver_minor(self):
        # type: () -> int
        return _props.get_system_ver_minor(self._handle)

    @property
    def _ver_phase(self):
        # type: () -> constants.Phase
        return constants.Phase(_props.get_system_ver_phase(self._handle))

    @property
    def _ver_update(self):
        # type: () -> int
        return _props.get_system_ver_update(self._handle)

    @property
    def cdaq_pkt_time(self):
        # type: () -> float
        return _props.get_system_cdaq_pkt_time(self._handle)

    @cdaq_pkt_time.setter
    def cdaq_pkt_time(self, value):
        # type: (float) -> None
        _props.set_system_cdaq_pkt_time(self._handle, value)

    @property
    def intf_refs_all(self):
        # type: () -> typing.Iterable[_interface.Interface]
        for ref in _props.get_system_intf_refs_all(self._handle):
            yield _interface.Interface(ref)
