from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _props
from nixnet import constants

from nixnet.database import _collection
from nixnet.database import _lin_sched_entry


class LinSched(object):

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle
        self._entries = _collection.DbCollection(
            self._handle,
            constants.ObjectClass.LIN_SCHED_ENTRY,
            _cconsts.NX_PROP_LIN_SCHED_ENTRIES,
            _lin_sched_entry.LinSchedEntry)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
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
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    @property
    def clst_ref(self):
        return _props.get_lin_sched_clst_ref(self._handle)

    @property
    def comment(self):
        return _props.get_lin_sched_comment(self._handle)

    @comment.setter
    def comment(self, value):
        _props.set_lin_sched_comment(self._handle, value)

    @property
    def config_status(self):
        return _props.get_lin_sched_config_status(self._handle)

    @property
    def entries(self):
        return self._entries

    @property
    def name(self):
        return _props.get_lin_sched_name(self._handle)

    @name.setter
    def name(self, value):
        _props.set_lin_sched_name(self._handle, value)

    @property
    def priority(self):
        return _props.get_lin_sched_priority(self._handle)

    @priority.setter
    def priority(self, value):
        _props.set_lin_sched_priority(self._handle, value)

    @property
    def run_mode(self):
        return constants.LinSchedRunMode(_props.get_lin_sched_run_mode(self._handle))

    @run_mode.setter
    def run_mode(self, value):
        _props.set_lin_sched_run_mode(self._handle, value.value)
