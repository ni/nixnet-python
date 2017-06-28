from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _props


class SubFrame(object):

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
        return 'SubFrame(handle={0})'.format(self._handle)

    @property
    def config_status(self):
        return _props.get_subframe_config_status(self._handle)

    @property
    def dyn_sig_refs(self):
        return _props.get_subframe_dyn_sig_refs(self._handle)

    @property
    def frm_ref(self):
        return _props.get_subframe_frm_ref(self._handle)

    @property
    def mux_value(self):
        return _props.get_subframe_mux_value(self._handle)

    @mux_value.setter
    def mux_value(self, value):
        _props.set_subframe_mux_value(self._handle, value)

    @property
    def name(self):
        return _props.get_subframe_name(self._handle)

    @name.setter
    def name(self, value):
        _props.set_subframe_name(self._handle, value)

    @property
    def pdu_ref(self):
        return _props.get_subframe_pdu_ref(self._handle)

    @property
    def name_unique_to_cluster(self):
        return _props.get_subframe_name_unique_to_cluster(self._handle)
