from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import six

from nixnet import _props
from nixnet import constants


class Interface(object):
    """Interface configuration for a session"""

    def __init__(self, handle):
        self._handle = handle

    def __repr__(self):
        return 'Session.Interface(handle={0})'.format(self._handle)

    def __str__(self):
        return self._name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._name == other._name
        elif isinstance(other, six.string_types):
            return self._name == other
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def baud_rate(self):
        return _props.get_session_intf_baud_rate(self._handle)

    @baud_rate.setter
    def baud_rate(self, value):
        _props.set_session_intf_baud_rate(self._handle, value)

    @property
    def baud_rate64(self):
        return _props.get_session_intf_baud_rate64(self._handle)

    @baud_rate64.setter
    def baud_rate64(self, value):
        _props.set_session_intf_baud_rate64(self._handle, value)

    @property
    def bus_err_to_in_strm(self):
        return _props.get_session_intf_bus_err_to_in_strm(self._handle)

    @bus_err_to_in_strm.setter
    def bus_err_to_in_strm(self, value):
        _props.set_session_intf_bus_err_to_in_strm(self._handle, value)

    @property
    def echo_tx(self):
        return _props.get_session_intf_echo_tx(self._handle)

    @echo_tx.setter
    def echo_tx(self, value):
        _props.set_session_intf_echo_tx(self._handle, value)

    @property
    def out_strm_list(self):
        return _props.get_session_intf_out_strm_list(self._handle)

    @out_strm_list.setter
    def out_strm_list(self, value):
        _props.set_session_intf_out_strm_list(self._handle, value)

    @property
    def out_strm_timng(self):
        return constants.OutStrmTimng(_props.get_session_intf_out_strm_timng(self._handle))

    @out_strm_timng.setter
    def out_strm_timng(self, value):
        _props.set_session_intf_out_strm_timng(self._handle, value.value)

    @property
    def start_trig_to_in_strm(self):
        return _props.get_session_intf_start_trig_to_in_strm(self._handle)

    @start_trig_to_in_strm.setter
    def start_trig_to_in_strm(self, value):
        _props.set_session_intf_start_trig_to_in_strm(self._handle, value)

    def set_can_ext_tcvr_config(self, value):
        _props.set_session_intf_can_ext_tcvr_config(self._handle, value)

    @property
    def can_lstn_only(self):
        return _props.get_session_intf_can_lstn_only(self._handle)

    @can_lstn_only.setter
    def can_lstn_only(self, value):
        _props.set_session_intf_can_lstn_only(self._handle, value)

    @property
    def can_pend_tx_order(self):
        return constants.CanPendTxOrder(_props.get_session_intf_can_pend_tx_order(self._handle))

    @can_pend_tx_order.setter
    def can_pend_tx_order(self, value):
        _props.set_session_intf_can_pend_tx_order(self._handle, value.value)

    @property
    def can_sing_shot(self):
        return _props.get_session_intf_can_sing_shot(self._handle)

    @can_sing_shot.setter
    def can_sing_shot(self, value):
        _props.set_session_intf_can_sing_shot(self._handle, value)

    @property
    def can_term(self):
        return constants.CanTerm(_props.get_session_intf_can_term(self._handle))

    @can_term.setter
    def can_term(self, value):
        _props.set_session_intf_can_term(self._handle, value.value)

    @property
    def can_tcvr_state(self):
        return constants.CanTcvrState(_props.get_session_intf_can_tcvr_state(self._handle))

    @can_tcvr_state.setter
    def can_tcvr_state(self, value):
        _props.set_session_intf_can_tcvr_state(self._handle, value.value)

    @property
    def can_tcvr_type(self):
        return constants.CanTcvrType(_props.get_session_intf_can_tcvr_type(self._handle))

    @can_tcvr_type.setter
    def can_tcvr_type(self, value):
        _props.set_session_intf_can_tcvr_type(self._handle, value.value)

    @property
    def can_out_strm_list_by_id(self):
        return _props.get_session_intf_can_out_strm_list_by_id(self._handle)

    @can_out_strm_list_by_id.setter
    def can_out_strm_list_by_id(self, value):
        _props.set_session_intf_can_out_strm_list_by_id(self._handle, value)

    @property
    def can_io_mode(self):
        return constants.CaNioMode(_props.get_session_intf_can_io_mode(self._handle))

    @property
    def can_fd_baud_rate(self):
        return _props.get_session_intf_can_fd_baud_rate(self._handle)

    @can_fd_baud_rate.setter
    def can_fd_baud_rate(self, value):
        _props.set_session_intf_can_fd_baud_rate(self._handle, value)

    @property
    def can_fd_baud_rate64(self):
        return _props.get_session_intf_can_fd_baud_rate64(self._handle)

    @can_fd_baud_rate64.setter
    def can_fd_baud_rate64(self, value):
        _props.set_session_intf_can_fd_baud_rate64(self._handle, value)

    @property
    def can_tx_io_mode(self):
        return constants.CaNioMode(_props.get_session_intf_can_tx_io_mode(self._handle))

    @can_tx_io_mode.setter
    def can_tx_io_mode(self, value):
        _props.set_session_intf_can_tx_io_mode(self._handle, value.value)

    @property
    def can_fd_iso_mode(self):
        return constants.CanFdIsoMode(_props.get_session_intf_can_fd_iso_mode(self._handle))

    @can_fd_iso_mode.setter
    def can_fd_iso_mode(self, value):
        _props.set_session_intf_can_fd_iso_mode(self._handle, value.value)

    @property
    def can_edge_filter(self):
        return _props.get_session_intf_can_edge_filter(self._handle)

    @can_edge_filter.setter
    def can_edge_filter(self, value):
        _props.set_session_intf_can_edge_filter(self._handle, value)

    @property
    def can_transmit_pause(self):
        return _props.get_session_intf_can_transmit_pause(self._handle)

    @can_transmit_pause.setter
    def can_transmit_pause(self, value):
        _props.set_session_intf_can_transmit_pause(self._handle, value)

    @property
    def can_disable_prot_exception_handling(self):
        return _props.get_session_intf_can_disable_prot_exception_handling(self._handle)

    @can_disable_prot_exception_handling.setter
    def can_disable_prot_exception_handling(self, value):
        _props.set_session_intf_can_disable_prot_exception_handling(self._handle, value)

    @property
    def flex_ray_acc_start_rng(self):
        return _props.get_session_intf_flex_ray_acc_start_rng(self._handle)

    @flex_ray_acc_start_rng.setter
    def flex_ray_acc_start_rng(self, value):
        _props.set_session_intf_flex_ray_acc_start_rng(self._handle, value)

    @property
    def flex_ray_alw_hlt_clk(self):
        return _props.get_session_intf_flex_ray_alw_hlt_clk(self._handle)

    @flex_ray_alw_hlt_clk.setter
    def flex_ray_alw_hlt_clk(self, value):
        _props.set_session_intf_flex_ray_alw_hlt_clk(self._handle, value)

    @property
    def flex_ray_alw_pass_act(self):
        return _props.get_session_intf_flex_ray_alw_pass_act(self._handle)

    @flex_ray_alw_pass_act.setter
    def flex_ray_alw_pass_act(self, value):
        _props.set_session_intf_flex_ray_alw_pass_act(self._handle, value)

    @property
    def flex_ray_auto_aslp_whn_stp(self):
        return _props.get_session_intf_flex_ray_auto_aslp_whn_stp(self._handle)

    @flex_ray_auto_aslp_whn_stp.setter
    def flex_ray_auto_aslp_whn_stp(self, value):
        _props.set_session_intf_flex_ray_auto_aslp_whn_stp(self._handle, value)

    @property
    def flex_ray_clst_drift_dmp(self):
        return _props.get_session_intf_flex_ray_clst_drift_dmp(self._handle)

    @flex_ray_clst_drift_dmp.setter
    def flex_ray_clst_drift_dmp(self, value):
        _props.set_session_intf_flex_ray_clst_drift_dmp(self._handle, value)

    @property
    def flex_ray_coldstart(self):
        return _props.get_session_intf_flex_ray_coldstart(self._handle)

    @property
    def flex_ray_dec_corr(self):
        return _props.get_session_intf_flex_ray_dec_corr(self._handle)

    @flex_ray_dec_corr.setter
    def flex_ray_dec_corr(self, value):
        _props.set_session_intf_flex_ray_dec_corr(self._handle, value)

    @property
    def flex_ray_delay_comp_a(self):
        return _props.get_session_intf_flex_ray_delay_comp_a(self._handle)

    @flex_ray_delay_comp_a.setter
    def flex_ray_delay_comp_a(self, value):
        _props.set_session_intf_flex_ray_delay_comp_a(self._handle, value)

    @property
    def flex_ray_delay_comp_b(self):
        return _props.get_session_intf_flex_ray_delay_comp_b(self._handle)

    @flex_ray_delay_comp_b.setter
    def flex_ray_delay_comp_b(self, value):
        _props.set_session_intf_flex_ray_delay_comp_b(self._handle, value)

    @property
    def flex_ray_key_slot_id(self):
        return _props.get_session_intf_flex_ray_key_slot_id(self._handle)

    @flex_ray_key_slot_id.setter
    def flex_ray_key_slot_id(self, value):
        _props.set_session_intf_flex_ray_key_slot_id(self._handle, value)

    @property
    def flex_ray_latest_tx(self):
        return _props.get_session_intf_flex_ray_latest_tx(self._handle)

    @property
    def flex_ray_list_timo(self):
        return _props.get_session_intf_flex_ray_list_timo(self._handle)

    @flex_ray_list_timo.setter
    def flex_ray_list_timo(self, value):
        _props.set_session_intf_flex_ray_list_timo(self._handle, value)

    @property
    def flex_ray_mac_init_off_a(self):
        return _props.get_session_intf_flex_ray_mac_init_off_a(self._handle)

    @flex_ray_mac_init_off_a.setter
    def flex_ray_mac_init_off_a(self, value):
        _props.set_session_intf_flex_ray_mac_init_off_a(self._handle, value)

    @property
    def flex_ray_mac_init_off_b(self):
        return _props.get_session_intf_flex_ray_mac_init_off_b(self._handle)

    @flex_ray_mac_init_off_b.setter
    def flex_ray_mac_init_off_b(self, value):
        _props.set_session_intf_flex_ray_mac_init_off_b(self._handle, value)

    @property
    def flex_ray_mic_init_off_a(self):
        return _props.get_session_intf_flex_ray_mic_init_off_a(self._handle)

    @flex_ray_mic_init_off_a.setter
    def flex_ray_mic_init_off_a(self, value):
        _props.set_session_intf_flex_ray_mic_init_off_a(self._handle, value)

    @property
    def flex_ray_mic_init_off_b(self):
        return _props.get_session_intf_flex_ray_mic_init_off_b(self._handle)

    @flex_ray_mic_init_off_b.setter
    def flex_ray_mic_init_off_b(self, value):
        _props.set_session_intf_flex_ray_mic_init_off_b(self._handle, value)

    @property
    def flex_ray_max_drift(self):
        return _props.get_session_intf_flex_ray_max_drift(self._handle)

    @flex_ray_max_drift.setter
    def flex_ray_max_drift(self, value):
        _props.set_session_intf_flex_ray_max_drift(self._handle, value)

    @property
    def flex_ray_microtick(self):
        return _props.get_session_intf_flex_ray_microtick(self._handle)

    @property
    def flex_ray_null_to_in_strm(self):
        return _props.get_session_intf_flex_ray_null_to_in_strm(self._handle)

    @flex_ray_null_to_in_strm.setter
    def flex_ray_null_to_in_strm(self, value):
        _props.set_session_intf_flex_ray_null_to_in_strm(self._handle, value)

    @property
    def flex_ray_off_corr(self):
        return _props.get_session_intf_flex_ray_off_corr(self._handle)

    @property
    def flex_ray_off_corr_out(self):
        return _props.get_session_intf_flex_ray_off_corr_out(self._handle)

    @flex_ray_off_corr_out.setter
    def flex_ray_off_corr_out(self, value):
        _props.set_session_intf_flex_ray_off_corr_out(self._handle, value)

    @property
    def flex_ray_rate_corr(self):
        return _props.get_session_intf_flex_ray_rate_corr(self._handle)

    @property
    def flex_ray_rate_corr_out(self):
        return _props.get_session_intf_flex_ray_rate_corr_out(self._handle)

    @flex_ray_rate_corr_out.setter
    def flex_ray_rate_corr_out(self, value):
        _props.set_session_intf_flex_ray_rate_corr_out(self._handle, value)

    @property
    def flex_ray_samp_per_micro(self):
        return _props.get_session_intf_flex_ray_samp_per_micro(self._handle)

    @flex_ray_samp_per_micro.setter
    def flex_ray_samp_per_micro(self, value):
        _props.set_session_intf_flex_ray_samp_per_micro(self._handle, value)

    @property
    def flex_ray_sing_slot_en(self):
        return _props.get_session_intf_flex_ray_sing_slot_en(self._handle)

    @flex_ray_sing_slot_en.setter
    def flex_ray_sing_slot_en(self, value):
        _props.set_session_intf_flex_ray_sing_slot_en(self._handle, value)

    @property
    def flex_ray_statistics_en(self):
        return _props.get_session_intf_flex_ray_statistics_en(self._handle)

    @flex_ray_statistics_en.setter
    def flex_ray_statistics_en(self, value):
        _props.set_session_intf_flex_ray_statistics_en(self._handle, value)

    @property
    def flex_ray_sym_to_in_strm(self):
        return _props.get_session_intf_flex_ray_sym_to_in_strm(self._handle)

    @flex_ray_sym_to_in_strm.setter
    def flex_ray_sym_to_in_strm(self, value):
        _props.set_session_intf_flex_ray_sym_to_in_strm(self._handle, value)

    @property
    def flex_ray_sync_ch_a_even(self):
        return _props.get_session_intf_flex_ray_sync_ch_a_even(self._handle)

    @property
    def flex_ray_sync_ch_a_odd(self):
        return _props.get_session_intf_flex_ray_sync_ch_a_odd(self._handle)

    @property
    def flex_ray_sync_ch_b_even(self):
        return _props.get_session_intf_flex_ray_sync_ch_b_even(self._handle)

    @property
    def flex_ray_sync_ch_b_odd(self):
        return _props.get_session_intf_flex_ray_sync_ch_b_odd(self._handle)

    @property
    def flex_ray_sync_status(self):
        return _props.get_session_intf_flex_ray_sync_status(self._handle)

    @property
    def flex_ray_term(self):
        return _props.get_session_intf_flex_ray_term(self._handle)

    @flex_ray_term.setter
    def flex_ray_term(self, value):
        _props.set_session_intf_flex_ray_term(self._handle, value)

    @property
    def flex_ray_wakeup_ch(self):
        return _props.get_session_intf_flex_ray_wakeup_ch(self._handle)

    @flex_ray_wakeup_ch.setter
    def flex_ray_wakeup_ch(self, value):
        _props.set_session_intf_flex_ray_wakeup_ch(self._handle, value)

    @property
    def flex_ray_wakeup_ptrn(self):
        return _props.get_session_intf_flex_ray_wakeup_ptrn(self._handle)

    @flex_ray_wakeup_ptrn.setter
    def flex_ray_wakeup_ptrn(self, value):
        _props.set_session_intf_flex_ray_wakeup_ptrn(self._handle, value)

    def set_flex_ray_sleep(self, value):
        _props.set_session_intf_flex_ray_sleep(self._handle, value)

    @property
    def flex_ray_connected_chs(self):
        return _props.get_session_intf_flex_ray_connected_chs(self._handle)

    @flex_ray_connected_chs.setter
    def flex_ray_connected_chs(self, value):
        _props.set_session_intf_flex_ray_connected_chs(self._handle, value)

    @property
    def lin_break_length(self):
        return _props.get_session_intf_lin_break_length(self._handle)

    @lin_break_length.setter
    def lin_break_length(self, value):
        _props.set_session_intf_lin_break_length(self._handle, value)

    @property
    def lin_master(self):
        return _props.get_session_intf_lin_master(self._handle)

    @lin_master.setter
    def lin_master(self, value):
        _props.set_session_intf_lin_master(self._handle, value)

    @property
    def lin_sched_names(self):
        return _props.get_session_intf_lin_sched_names(self._handle)

    def set_lin_sleep(self, value):
        _props.set_session_intf_lin_sleep(self._handle, value.value)

    @property
    def lin_term(self):
        return constants.LinTerm(_props.get_session_intf_lin_term(self._handle))

    @lin_term.setter
    def lin_term(self, value):
        _props.set_session_intf_lin_term(self._handle, value.value)

    @property
    def lin_diag_p_2min(self):
        return _props.get_session_intf_lin_diag_p_2min(self._handle)

    @lin_diag_p_2min.setter
    def lin_diag_p_2min(self, value):
        _props.set_session_intf_lin_diag_p_2min(self._handle, value)

    @property
    def lin_diag_s_tmin(self):
        return _props.get_session_intf_lin_diag_s_tmin(self._handle)

    @lin_diag_s_tmin.setter
    def lin_diag_s_tmin(self, value):
        _props.set_session_intf_lin_diag_s_tmin(self._handle, value)

    @property
    def lin_alw_start_wo_bus_pwr(self):
        return _props.get_session_intf_lin_alw_start_wo_bus_pwr(self._handle)

    @lin_alw_start_wo_bus_pwr.setter
    def lin_alw_start_wo_bus_pwr(self, value):
        _props.set_session_intf_lin_alw_start_wo_bus_pwr(self._handle, value)

    @property
    def lino_str_slv_rsp_lst_by_nad(self):
        return _props.get_session_intf_lino_str_slv_rsp_lst_by_nad(self._handle)

    @lino_str_slv_rsp_lst_by_nad.setter
    def lino_str_slv_rsp_lst_by_nad(self, value):
        _props.set_session_intf_lino_str_slv_rsp_lst_by_nad(self._handle, value)

    @property
    def lin_no_response_to_in_strm(self):
        return _props.get_session_intf_lin_no_response_to_in_strm(self._handle)

    @lin_no_response_to_in_strm.setter
    def lin_no_response_to_in_strm(self, value):
        _props.set_session_intf_lin_no_response_to_in_strm(self._handle, value)

    @property
    def src_term_start_trigger(self):
        return _props.get_session_intf_src_term_start_trigger(self._handle)

    @src_term_start_trigger.setter
    def src_term_start_trigger(self, value):
        _props.set_session_intf_src_term_start_trigger(self._handle, value)

    @property
    def _name(self):
        return _props.get_session_intf_name(self._handle)
