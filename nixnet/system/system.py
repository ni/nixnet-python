from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import typing  # NOQA: F401
import warnings

from nixnet import _funcs
from nixnet import _props
from nixnet import constants
from nixnet import errors
from nixnet import types

from nixnet.system import _device
from nixnet.system import _interface
from nixnet.system import databases


class System(object):
    '''Interact with the NI driver and interface hardware.'''

    def __init__(self):
        # type: () -> None
        self._handle = None  # To satisfy `__del__` in case nx_system_open throws
        self._handle = _funcs.nx_system_open()
        self._databases = databases.Databases(self._handle)

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
    def databases(self):
        """:any:`nixnet.system.databases.Databases`: Operate on systems's database's aliases"""
        return self._databases

    @property
    def dev_refs(self):
        # type: () -> typing.Iterable[_device.Device]
        '''iter of :any:`nixnet.system._device.Device`: Physical XNET devices in the system.'''
        for ref in _props.get_system_dev_refs(self._handle):
            yield _device.Device(ref)

    @property
    def intf_refs(self):
        # type: () -> typing.Iterable[_interface.Interface]
        '''iter of :any:`nixnet.system._interface.Interface`: Available interfaces on the system.'''
        for ref in _props.get_system_intf_refs(self._handle):
            yield _interface.Interface(ref)

    @property
    def intf_refs_all(self):
        # type: () -> typing.Iterable[_interface.Interface]
        '''iter of :any:`nixnet.system._interface.Interface`: Available interfaces on the system.

        This Includes those not equipped with a Transceiver Cable.
        '''
        for ref in _props.get_system_intf_refs_all(self._handle):
            yield _interface.Interface(ref)

    @property
    def intf_refs_can(self):
        # type: () -> typing.Iterable[_interface.Interface]
        '''iter of :any:`nixnet.system._interface.Interface`: Available interfaces on the system (CAN Protocol).'''
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
        '''iter of :any:`nixnet.system._interface.Interface`: Available interfaces on the system (LIN Protocol).'''
        for ref in _props.get_system_intf_refs_lin(self._handle):
            yield _interface.Interface(ref)

    @property
    def ver(self):
        # type: () -> types.DriverVersion
        ''':any:`nixnet.types.DriverVersion`: The driver version (larger numbers imply a newer version).

        Use this for:

        * Determining the driver functionality or release date
        * Determining upgrade availability
        '''
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
