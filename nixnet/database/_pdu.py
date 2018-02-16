from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from nixnet import _cconsts
from nixnet import _props
from nixnet import constants

from nixnet.database import _collection
from nixnet.database import _signal
from nixnet.database import _subframe


class Pdu(object):

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle
        self._signals = _collection.DbCollection(
            self._handle, constants.ObjectClass.SIGNAL, _cconsts.NX_PROP_PDU_SIG_REFS, _signal.Signal)
        self._mux_subframes = _collection.DbCollection(
            self._handle, constants.ObjectClass.SUBFRAME, _cconsts.NX_PROP_PDU_MUX_SUBFRAME_REFS, _subframe.SubFrame)

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
    def signals(self):
        return self._signals

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
    def mux_subframes(self):
        return self._mux_subframes
