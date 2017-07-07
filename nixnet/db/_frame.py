from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _props
from nixnet import constants


class Frame(object):

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
    def flex_ray_base_cycle(self):
        return _props.get_frame_flex_ray_base_cycle(self._handle)

    @flex_ray_base_cycle.setter
    def flex_ray_base_cycle(self, value):
        _props.set_frame_flex_ray_base_cycle(self._handle, value)

    @property
    def flex_ray_ch_assign(self):
        return _props.get_frame_flex_ray_ch_assign(self._handle)

    @flex_ray_ch_assign.setter
    def flex_ray_ch_assign(self, value):
        _props.set_frame_flex_ray_ch_assign(self._handle, value)

    @property
    def flex_ray_cycle_rep(self):
        return _props.get_frame_flex_ray_cycle_rep(self._handle)

    @flex_ray_cycle_rep.setter
    def flex_ray_cycle_rep(self, value):
        _props.set_frame_flex_ray_cycle_rep(self._handle, value)

    @property
    def flex_ray_preamble(self):
        return _props.get_frame_flex_ray_preamble(self._handle)

    @flex_ray_preamble.setter
    def flex_ray_preamble(self, value):
        _props.set_frame_flex_ray_preamble(self._handle, value)

    @property
    def flex_ray_startup(self):
        return _props.get_frame_flex_ray_startup(self._handle)

    @flex_ray_startup.setter
    def flex_ray_startup(self, value):
        _props.set_frame_flex_ray_startup(self._handle, value)

    @property
    def flex_ray_sync(self):
        return _props.get_frame_flex_ray_sync(self._handle)

    @flex_ray_sync.setter
    def flex_ray_sync(self, value):
        _props.set_frame_flex_ray_sync(self._handle, value)

    @property
    def flex_ray_timing_type(self):
        return _props.get_frame_flex_ray_timing_type(self._handle)

    @flex_ray_timing_type.setter
    def flex_ray_timing_type(self, value):
        _props.set_frame_flex_ray_timing_type(self._handle, value)

    @property
    def flex_ray_in_cyc_rep_enabled(self):
        return _props.get_frame_flex_ray_in_cyc_rep_enabled(self._handle)

    @property
    def flex_ray_in_cyc_rep_i_ds(self):
        return _props.get_frame_flex_ray_in_cyc_rep_i_ds(self._handle)

    @flex_ray_in_cyc_rep_i_ds.setter
    def flex_ray_in_cyc_rep_i_ds(self, value):
        _props.set_frame_flex_ray_in_cyc_rep_i_ds(self._handle, value)

    @property
    def flex_ray_in_cyc_rep_ch_assigns(self):
        return _props.get_frame_flex_ray_in_cyc_rep_ch_assigns(self._handle)

    @flex_ray_in_cyc_rep_ch_assigns.setter
    def flex_ray_in_cyc_rep_ch_assigns(self, value):
        _props.set_frame_flex_ray_in_cyc_rep_ch_assigns(self._handle, value)

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
    def ca_nio_mode(self):
        return constants.CaNioMode(_props.get_frame_ca_nio_mode(self._handle))

    @ca_nio_mode.setter
    def ca_nio_mode(self, value):
        _props.set_frame_ca_nio_mode(self._handle, value.value)
