from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _props


class Pdu(object):

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
        return 'Pdu(handle={0})'.format(self._handle)

    @property
    def cluster_ref(self):
        return _props.get_pdu_cluster_ref(self._handle)

    @property
    def default_payload(self):
        return _props.get_pdu_default_payload(self._handle)

    @default_payload.setter
    def default_payload(self, value):
        _props.set_pdu_default_payload(self._handle, value)

    @property
    def comment(self):
        return _props.get_pdu_comment(self._handle)

    @comment.setter
    def comment(self, value):
        _props.set_pdu_comment(self._handle, value)

    @property
    def config_status(self):
        return _props.get_pdu_config_status(self._handle)

    @property
    def frm_refs(self):
        return _props.get_pdu_frm_refs(self._handle)

    @property
    def name(self):
        return _props.get_pdu_name(self._handle)

    @name.setter
    def name(self, value):
        _props.set_pdu_name(self._handle, value)

    @property
    def payload_len(self):
        return _props.get_pdu_payload_len(self._handle)

    @payload_len.setter
    def payload_len(self, value):
        _props.set_pdu_payload_len(self._handle, value)

    @property
    def sig_refs(self):
        return _props.get_pdu_sig_refs(self._handle)

    @property
    def mux_is_muxed(self):
        return _props.get_pdu_mux_is_muxed(self._handle)

    @property
    def mux_data_mux_sig_ref(self):
        return _props.get_pdu_mux_data_mux_sig_ref(self._handle)

    @property
    def mux_static_sig_refs(self):
        return _props.get_pdu_mux_static_sig_refs(self._handle)

    @property
    def mux_subframe_refs(self):
        return _props.get_pdu_mux_subframe_refs(self._handle)
