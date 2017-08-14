from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from nixnet import _props
from nixnet import constants


class Frame(object):

    def __init__(self, handle):
        self._handle = handle

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
        return 'Frame(handle={0})'.format(self._handle)

    @property
    def application_protocol(self):
        return _props.get_frame_application_protocol(self._handle)

    @application_protocol.setter
    def application_protocol(self, value):
        _props.set_frame_application_protocol(self._handle, value)

    @property
    def cluster_ref(self):
        return _props.get_frame_cluster_ref(self._handle)

    @property
    def comment(self):
        return _props.get_frame_comment(self._handle)

    @comment.setter
    def comment(self, value):
        _props.set_frame_comment(self._handle, value)

    @property
    def config_status(self):
        return _props.get_frame_config_status(self._handle)

    @property
    def default_payload(self):
        return _props.get_frame_default_payload(self._handle)

    @default_payload.setter
    def default_payload(self, value):
        _props.set_frame_default_payload(self._handle, value)

    @property
    def id(self):
        return _props.get_frame_id(self._handle)

    @id.setter
    def id(self, value):
        _props.set_frame_id(self._handle, value)

    @property
    def name(self):
        return _props.get_frame_name(self._handle)

    @name.setter
    def name(self, value):
        _props.set_frame_name(self._handle, value)

    @property
    def payload_len(self):
        return _props.get_frame_payload_len(self._handle)

    @payload_len.setter
    def payload_len(self, value):
        _props.set_frame_payload_len(self._handle, value)

    @property
    def sig_refs(self):
        return _props.get_frame_sig_refs(self._handle)

    @property
    def can_ext_id(self):
        return _props.get_frame_can_ext_id(self._handle)

    @can_ext_id.setter
    def can_ext_id(self, value):
        _props.set_frame_can_ext_id(self._handle, value)

    @property
    def can_timing_type(self):
        return constants.TimeType(_props.get_frame_can_timing_type(self._handle))

    @can_timing_type.setter
    def can_timing_type(self, value):
        _props.set_frame_can_timing_type(self._handle, value.value)

    @property
    def can_tx_time(self):
        return _props.get_frame_can_tx_time(self._handle)

    @can_tx_time.setter
    def can_tx_time(self, value):
        _props.set_frame_can_tx_time(self._handle, value)

    @property
    def lin_checksum(self):
        return _props.get_frame_lin_checksum(self._handle)

    @property
    def mux_is_muxed(self):
        return _props.get_frame_mux_is_muxed(self._handle)

    @property
    def mux_data_mux_sig_ref(self):
        return _props.get_frame_mux_data_mux_sig_ref(self._handle)

    @property
    def mux_static_sig_refs(self):
        return _props.get_frame_mux_static_sig_refs(self._handle)

    @property
    def mux_subframe_refs(self):
        return _props.get_frame_mux_subframe_refs(self._handle)

    @property
    def pdu_refs(self):
        return _props.get_frame_pdu_refs(self._handle)

    @pdu_refs.setter
    def pdu_refs(self, value):
        _props.set_frame_pdu_refs(self._handle, value)

    @property
    def pdu_start_bits(self):
        return _props.get_frame_pdu_start_bits(self._handle)

    @pdu_start_bits.setter
    def pdu_start_bits(self, value):
        _props.set_frame_pdu_start_bits(self._handle, value)

    @property
    def pdu_update_bits(self):
        return _props.get_frame_pdu_update_bits(self._handle)

    @pdu_update_bits.setter
    def pdu_update_bits(self, value):
        _props.set_frame_pdu_update_bits(self._handle, value)

    @property
    def variable_payload(self):
        return _props.get_frame_variable_payload(self._handle)

    @variable_payload.setter
    def variable_payload(self, value):
        _props.set_frame_variable_payload(self._handle, value)

    @property
    def can_io_mode(self):
        return constants.CanIoMode(_props.get_frame_can_io_mode(self._handle))

    @can_io_mode.setter
    def can_io_mode(self, value):
        _props.set_frame_can_io_mode(self._handle, value.value)
