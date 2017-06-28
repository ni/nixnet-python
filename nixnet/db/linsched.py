from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _props
from nixnet import constants


class LinSched(object):

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

    def __repr__(self):
        return 'LinSched(handle={0})'.format(self._handle)

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
        return _props.get_lin_sched_entries(self._handle)

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
