from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _props
from nixnet import constants


class LinSchedEntry(object):

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
        return 'LinSchedEntry(handle={0})'.format(self._handle)

    @property
    def collision_res_sched(self):
        return _props.get_lin_sched_entry_collision_res_sched(self._handle)

    @collision_res_sched.setter
    def collision_res_sched(self, value):
        _props.set_lin_sched_entry_collision_res_sched(self._handle, value)

    @property
    def delay(self):
        return _props.get_lin_sched_entry_delay(self._handle)

    @delay.setter
    def delay(self, value):
        _props.set_lin_sched_entry_delay(self._handle, value)

    @property
    def event_id(self):
        return _props.get_lin_sched_entry_event_id(self._handle)

    @event_id.setter
    def event_id(self, value):
        _props.set_lin_sched_entry_event_id(self._handle, value)

    @property
    def frames(self):
        return _props.get_lin_sched_entry_frames(self._handle)

    @frames.setter
    def frames(self, value):
        _props.set_lin_sched_entry_frames(self._handle, value)

    @property
    def name(self):
        return _props.get_lin_sched_entry_name(self._handle)

    @name.setter
    def name(self, value):
        _props.set_lin_sched_entry_name(self._handle, value)

    @property
    def name_unique_to_cluster(self):
        return _props.get_lin_sched_entry_name_unique_to_cluster(self._handle)

    @property
    def sched(self):
        return _props.get_lin_sched_entry_sched(self._handle)

    @property
    def type(self):
        return constants.LinSchedEntryType(_props.get_lin_sched_entry_type(self._handle))

    @type.setter
    def type(self, value):
        _props.set_lin_sched_entry_type(self._handle, value.value)

    @property
    def nc_ff_data_bytes(self):
        return _props.get_lin_sched_entry_nc_ff_data_bytes(self._handle)

    @nc_ff_data_bytes.setter
    def nc_ff_data_bytes(self, value):
        _props.set_lin_sched_entry_nc_ff_data_bytes(self._handle, value)
