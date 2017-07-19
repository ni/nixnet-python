from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import typing  # NOQA: F401

import six

from nixnet import _funcs
from nixnet import _props
from nixnet import constants


class Interface(object):

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(Interface, other._handle)
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
        return 'Interface(handle={0})'.format(self._handle)

    # `dev_ref`: Intentionally not exposed to avoid circular imports

    @property
    def num(self):
        # type: () -> int
        return _props.get_interface_num(self._handle)

    @property
    def port_num(self):
        # type: () -> int
        return _props.get_interface_port_num(self._handle)

    @property
    def protocol(self):
        # type: () -> constants.Protocol
        return constants.Protocol(_props.get_interface_protocol(self._handle))

    @property
    def can_term_cap(self):
        # type: () -> constants.CanTermCap
        return constants.CanTermCap(_props.get_interface_can_term_cap(self._handle))

    @property
    def can_tcvr_cap(self):
        # type: () -> constants.CanTcvrCap
        return constants.CanTcvrCap(_props.get_interface_can_tcvr_cap(self._handle))

    @property
    def dongle_state(self):
        # type: () -> constants.DongleState
        return constants.DongleState(_props.get_interface_dongle_state(self._handle))

    @property
    def dongle_id(self):
        # type: () -> constants.DongleId
        return constants.DongleId(_props.get_interface_dongle_id(self._handle))

    @property
    def dongle_revision(self):
        # type: () -> int
        return _props.get_interface_dongle_revision(self._handle)

    @property
    def dongle_firmware_version(self):
        # type: () -> int
        return _props.get_interface_dongle_firmware_version(self._handle)

    @property
    def dongle_compatible_revision(self):
        # type: () -> int
        return _props.get_interface_dongle_compatible_revision(self._handle)

    @property
    def dongle_compatible_firmware_version(self):
        # type: () -> int
        return _props.get_interface_dongle_compatible_firmware_version(self._handle)

    def blink(self, modifier):
        # type: (constants.BlinkMode) -> None
        _funcs.nx_blink(self._handle, modifier)

    @property
    def _name(self):
        # type: () -> typing.Text
        return _props.get_interface_name(self._handle)
