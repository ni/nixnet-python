from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import warnings

from nixnet import _funcs
from nixnet import _props
from nixnet import constants
from nixnet import errors


class Session(object):

    def __init__(
            self,
            database_name,
            cluster_name,
            list,
            interface,
            mode):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesession/"
        self._handle = _funcs.nx_create_session(database_name, cluster_name, list, interface, mode)

    def __del__(self):
        if self._handle is not None:
            warnings.warn(
                'Session was not explicitly closed before it was destructed. '
                'Resources on the device may still be reserved.',
                errors.XnetResourceWarning)

    def __enter__(self):
        return self

    def __exit__(self):
        self.close()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        return 'Session(handle={0})'.format(self._handle)

    def close(self):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxclear/"
        if self._handle is None:
            warnings.warn(
                'Attempting to close NI-XNET session but session was already '
                'closed', errors.XnetResourceWarning)
            return

        _funcs.nx_clear(self._handle)

        self._handle = None

    def start(self, scope):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxstart/"
        _funcs.nx_start(self, scope)

    def read_frame(
            self,
            number_to_read=constants.READ_ALL_AVAILABLE,
            timeout=constants.TIMEOUT_NONE):
        """Read frames.

        Valid modes
        - Frame Input Stream Mode
        - Frame Input Queued Mode
        - Frame Input Single-Point Mode
        Frame: one or more
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadframe/
        """
        raise NotImplementedError("Placeholder")

    def write_frame(
            self,
            frames,
            timeout=10):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwriteframe/"
        raise NotImplementedError("Placeholder")

    @property
    def application_protocol(self):
        return constants.AppProtocol(_props.get_session_application_protocol(self._handle))

    @property
    def auto_start(self):
        return _props.get_session_auto_start(self._handle)

    @auto_start.setter
    def auto_start(self, value):
        _props.set_session_auto_start(self._handle, value)

    @property
    def cluster_name(self):
        return _props.get_session_cluster_name(self._handle)

    @property
    def database_name(self):
        return _props.get_session_database_name(self._handle)

    @property
    def list(self):
        return _props.get_session_list(self._handle)

    @property
    def mode(self):
        return constants.CreateSessionMode(_props.get_session_mode(self._handle))

    @property
    def num_frames(self):
        return _props.get_session_num_frames(self._handle)

    @property
    def num_in_list(self):
        return _props.get_session_num_in_list(self._handle)

    @property
    def num_pend(self):
        return _props.get_session_num_pend(self._handle)

    @property
    def num_unused(self):
        return _props.get_session_num_unused(self._handle)

    @property
    def payld_len_max(self):
        return _props.get_session_payld_len_max(self._handle)

    @property
    def protocol(self):
        return constants.Protocol(_props.get_session_protocol(self._handle))

    @property
    def queue_size(self):
        return _props.get_session_queue_size(self._handle)

    @queue_size.setter
    def queue_size(self, value):
        _props.set_session_queue_size(self._handle, value)

    @property
    def resamp_rate(self):
        return _props.get_session_resamp_rate(self._handle)

    @resamp_rate.setter
    def resamp_rate(self, value):
        _props.set_session_resamp_rate(self._handle, value)

    @property
    def intf_baud_rate(self):
        return _props.get_session_intf_baud_rate(self._handle)

    @intf_baud_rate.setter
    def intf_baud_rate(self, value):
        _props.set_session_intf_baud_rate(self._handle, value)

    @property
    def intf_baud_rate64(self):
        return _props.get_session_intf_baud_rate64(self._handle)

    @intf_baud_rate64.setter
    def intf_baud_rate64(self, value):
        _props.set_session_intf_baud_rate64(self._handle, value)

    @property
    def intf_bus_err_to_in_strm(self):
        return _props.get_session_intf_bus_err_to_in_strm(self._handle)

    @intf_bus_err_to_in_strm.setter
    def intf_bus_err_to_in_strm(self, value):
        _props.set_session_intf_bus_err_to_in_strm(self._handle, value)

    @property
    def intf_echo_tx(self):
        return _props.get_session_intf_echo_tx(self._handle)

    @intf_echo_tx.setter
    def intf_echo_tx(self, value):
        _props.set_session_intf_echo_tx(self._handle, value)

    @property
    def intf_name(self):
        return _props.get_session_intf_name(self._handle)

    @property
    def intf_out_strm_list(self):
        return _props.get_session_intf_out_strm_list(self._handle)

    @intf_out_strm_list.setter
    def intf_out_strm_list(self, value):
        _props.set_session_intf_out_strm_list(self._handle, value)

    @property
    def intf_out_strm_timng(self):
        return constants.OutStrmTimng(_props.get_session_intf_out_strm_timng(self._handle))

    @intf_out_strm_timng.setter
    def intf_out_strm_timng(self, value):
        _props.set_session_intf_out_strm_timng(self._handle, value.value)

    @property
    def intf_start_trig_to_in_strm(self):
        return _props.get_session_intf_start_trig_to_in_strm(self._handle)

    @intf_start_trig_to_in_strm.setter
    def intf_start_trig_to_in_strm(self, value):
        _props.set_session_intf_start_trig_to_in_strm(self._handle, value)

    def set_intf_can_ext_tcvr_config(self, value):
        _props.set_session_intf_can_ext_tcvr_config(self._handle, value)

    @property
    def intf_can_lstn_only(self):
        return _props.get_session_intf_can_lstn_only(self._handle)

    @intf_can_lstn_only.setter
    def intf_can_lstn_only(self, value):
        _props.set_session_intf_can_lstn_only(self._handle, value)

    @property
    def intf_can_pend_tx_order(self):
        return constants.CanPendTxOrder(_props.get_session_intf_can_pend_tx_order(self._handle))

    @intf_can_pend_tx_order.setter
    def intf_can_pend_tx_order(self, value):
        _props.set_session_intf_can_pend_tx_order(self._handle, value.value)

    @property
    def intf_can_sing_shot(self):
        return _props.get_session_intf_can_sing_shot(self._handle)

    @intf_can_sing_shot.setter
    def intf_can_sing_shot(self, value):
        _props.set_session_intf_can_sing_shot(self._handle, value)

    @property
    def intf_can_term(self):
        return constants.CanTerm(_props.get_session_intf_can_term(self._handle))

    @intf_can_term.setter
    def intf_can_term(self, value):
        _props.set_session_intf_can_term(self._handle, value.value)

    @property
    def intf_can_tcvr_state(self):
        return constants.CanTcvrState(_props.get_session_intf_can_tcvr_state(self._handle))

    @intf_can_tcvr_state.setter
    def intf_can_tcvr_state(self, value):
        _props.set_session_intf_can_tcvr_state(self._handle, value.value)

    @property
    def intf_can_tcvr_type(self):
        return constants.CanTcvrType(_props.get_session_intf_can_tcvr_type(self._handle))

    @intf_can_tcvr_type.setter
    def intf_can_tcvr_type(self, value):
        _props.set_session_intf_can_tcvr_type(self._handle, value.value)

    @property
    def intf_can_out_strm_list_by_id(self):
        return _props.get_session_intf_can_out_strm_list_by_id(self._handle)

    @intf_can_out_strm_list_by_id.setter
    def intf_can_out_strm_list_by_id(self, value):
        _props.set_session_intf_can_out_strm_list_by_id(self._handle, value)

    @property
    def intf_can_io_mode(self):
        return constants.CaNioMode(_props.get_session_intf_can_io_mode(self._handle))

    @property
    def intf_can_fd_baud_rate(self):
        return _props.get_session_intf_can_fd_baud_rate(self._handle)

    @intf_can_fd_baud_rate.setter
    def intf_can_fd_baud_rate(self, value):
        _props.set_session_intf_can_fd_baud_rate(self._handle, value)

    @property
    def intf_can_fd_baud_rate64(self):
        return _props.get_session_intf_can_fd_baud_rate64(self._handle)

    @intf_can_fd_baud_rate64.setter
    def intf_can_fd_baud_rate64(self, value):
        _props.set_session_intf_can_fd_baud_rate64(self._handle, value)

    @property
    def intf_can_tx_io_mode(self):
        return constants.CaNioMode(_props.get_session_intf_can_tx_io_mode(self._handle))

    @intf_can_tx_io_mode.setter
    def intf_can_tx_io_mode(self, value):
        _props.set_session_intf_can_tx_io_mode(self._handle, value.value)

    @property
    def intf_can_fd_iso_mode(self):
        return constants.CanFdIsoMode(_props.get_session_intf_can_fd_iso_mode(self._handle))

    @intf_can_fd_iso_mode.setter
    def intf_can_fd_iso_mode(self, value):
        _props.set_session_intf_can_fd_iso_mode(self._handle, value.value)

    @property
    def intf_flex_ray_acc_start_rng(self):
        return _props.get_session_intf_flex_ray_acc_start_rng(self._handle)

    @intf_flex_ray_acc_start_rng.setter
    def intf_flex_ray_acc_start_rng(self, value):
        _props.set_session_intf_flex_ray_acc_start_rng(self._handle, value)

    @property
    def intf_flex_ray_alw_hlt_clk(self):
        return _props.get_session_intf_flex_ray_alw_hlt_clk(self._handle)

    @intf_flex_ray_alw_hlt_clk.setter
    def intf_flex_ray_alw_hlt_clk(self, value):
        _props.set_session_intf_flex_ray_alw_hlt_clk(self._handle, value)

    @property
    def intf_flex_ray_alw_pass_act(self):
        return _props.get_session_intf_flex_ray_alw_pass_act(self._handle)

    @intf_flex_ray_alw_pass_act.setter
    def intf_flex_ray_alw_pass_act(self, value):
        _props.set_session_intf_flex_ray_alw_pass_act(self._handle, value)

    @property
    def intf_flex_ray_auto_aslp_whn_stp(self):
        return _props.get_session_intf_flex_ray_auto_aslp_whn_stp(self._handle)

    @intf_flex_ray_auto_aslp_whn_stp.setter
    def intf_flex_ray_auto_aslp_whn_stp(self, value):
        _props.set_session_intf_flex_ray_auto_aslp_whn_stp(self._handle, value)

    @property
    def intf_flex_ray_clst_drift_dmp(self):
        return _props.get_session_intf_flex_ray_clst_drift_dmp(self._handle)

    @intf_flex_ray_clst_drift_dmp.setter
    def intf_flex_ray_clst_drift_dmp(self, value):
        _props.set_session_intf_flex_ray_clst_drift_dmp(self._handle, value)

    @property
    def intf_flex_ray_coldstart(self):
        return _props.get_session_intf_flex_ray_coldstart(self._handle)

    @property
    def intf_flex_ray_dec_corr(self):
        return _props.get_session_intf_flex_ray_dec_corr(self._handle)

    @intf_flex_ray_dec_corr.setter
    def intf_flex_ray_dec_corr(self, value):
        _props.set_session_intf_flex_ray_dec_corr(self._handle, value)

    @property
    def intf_flex_ray_delay_comp_a(self):
        return _props.get_session_intf_flex_ray_delay_comp_a(self._handle)

    @intf_flex_ray_delay_comp_a.setter
    def intf_flex_ray_delay_comp_a(self, value):
        _props.set_session_intf_flex_ray_delay_comp_a(self._handle, value)

    @property
    def intf_flex_ray_delay_comp_b(self):
        return _props.get_session_intf_flex_ray_delay_comp_b(self._handle)

    @intf_flex_ray_delay_comp_b.setter
    def intf_flex_ray_delay_comp_b(self, value):
        _props.set_session_intf_flex_ray_delay_comp_b(self._handle, value)

    @property
    def intf_flex_ray_key_slot_id(self):
        return _props.get_session_intf_flex_ray_key_slot_id(self._handle)

    @intf_flex_ray_key_slot_id.setter
    def intf_flex_ray_key_slot_id(self, value):
        _props.set_session_intf_flex_ray_key_slot_id(self._handle, value)

    @property
    def intf_flex_ray_latest_tx(self):
        return _props.get_session_intf_flex_ray_latest_tx(self._handle)

    @property
    def intf_flex_ray_list_timo(self):
        return _props.get_session_intf_flex_ray_list_timo(self._handle)

    @intf_flex_ray_list_timo.setter
    def intf_flex_ray_list_timo(self, value):
        _props.set_session_intf_flex_ray_list_timo(self._handle, value)

    @property
    def intf_flex_ray_mac_init_off_a(self):
        return _props.get_session_intf_flex_ray_mac_init_off_a(self._handle)

    @intf_flex_ray_mac_init_off_a.setter
    def intf_flex_ray_mac_init_off_a(self, value):
        _props.set_session_intf_flex_ray_mac_init_off_a(self._handle, value)

    @property
    def intf_flex_ray_mac_init_off_b(self):
        return _props.get_session_intf_flex_ray_mac_init_off_b(self._handle)

    @intf_flex_ray_mac_init_off_b.setter
    def intf_flex_ray_mac_init_off_b(self, value):
        _props.set_session_intf_flex_ray_mac_init_off_b(self._handle, value)

    @property
    def intf_flex_ray_mic_init_off_a(self):
        return _props.get_session_intf_flex_ray_mic_init_off_a(self._handle)

    @intf_flex_ray_mic_init_off_a.setter
    def intf_flex_ray_mic_init_off_a(self, value):
        _props.set_session_intf_flex_ray_mic_init_off_a(self._handle, value)

    @property
    def intf_flex_ray_mic_init_off_b(self):
        return _props.get_session_intf_flex_ray_mic_init_off_b(self._handle)

    @intf_flex_ray_mic_init_off_b.setter
    def intf_flex_ray_mic_init_off_b(self, value):
        _props.set_session_intf_flex_ray_mic_init_off_b(self._handle, value)

    @property
    def intf_flex_ray_max_drift(self):
        return _props.get_session_intf_flex_ray_max_drift(self._handle)

    @intf_flex_ray_max_drift.setter
    def intf_flex_ray_max_drift(self, value):
        _props.set_session_intf_flex_ray_max_drift(self._handle, value)

    @property
    def intf_flex_ray_microtick(self):
        return _props.get_session_intf_flex_ray_microtick(self._handle)

    @property
    def intf_flex_ray_null_to_in_strm(self):
        return _props.get_session_intf_flex_ray_null_to_in_strm(self._handle)

    @intf_flex_ray_null_to_in_strm.setter
    def intf_flex_ray_null_to_in_strm(self, value):
        _props.set_session_intf_flex_ray_null_to_in_strm(self._handle, value)

    @property
    def intf_flex_ray_off_corr(self):
        return _props.get_session_intf_flex_ray_off_corr(self._handle)

    @property
    def intf_flex_ray_off_corr_out(self):
        return _props.get_session_intf_flex_ray_off_corr_out(self._handle)

    @intf_flex_ray_off_corr_out.setter
    def intf_flex_ray_off_corr_out(self, value):
        _props.set_session_intf_flex_ray_off_corr_out(self._handle, value)

    @property
    def intf_flex_ray_rate_corr(self):
        return _props.get_session_intf_flex_ray_rate_corr(self._handle)

    @property
    def intf_flex_ray_rate_corr_out(self):
        return _props.get_session_intf_flex_ray_rate_corr_out(self._handle)

    @intf_flex_ray_rate_corr_out.setter
    def intf_flex_ray_rate_corr_out(self, value):
        _props.set_session_intf_flex_ray_rate_corr_out(self._handle, value)

    @property
    def intf_flex_ray_samp_per_micro(self):
        return _props.get_session_intf_flex_ray_samp_per_micro(self._handle)

    @intf_flex_ray_samp_per_micro.setter
    def intf_flex_ray_samp_per_micro(self, value):
        _props.set_session_intf_flex_ray_samp_per_micro(self._handle, value)

    @property
    def intf_flex_ray_sing_slot_en(self):
        return _props.get_session_intf_flex_ray_sing_slot_en(self._handle)

    @intf_flex_ray_sing_slot_en.setter
    def intf_flex_ray_sing_slot_en(self, value):
        _props.set_session_intf_flex_ray_sing_slot_en(self._handle, value)

    @property
    def intf_flex_ray_statistics_en(self):
        return _props.get_session_intf_flex_ray_statistics_en(self._handle)

    @intf_flex_ray_statistics_en.setter
    def intf_flex_ray_statistics_en(self, value):
        _props.set_session_intf_flex_ray_statistics_en(self._handle, value)

    @property
    def intf_flex_ray_sym_to_in_strm(self):
        return _props.get_session_intf_flex_ray_sym_to_in_strm(self._handle)

    @intf_flex_ray_sym_to_in_strm.setter
    def intf_flex_ray_sym_to_in_strm(self, value):
        _props.set_session_intf_flex_ray_sym_to_in_strm(self._handle, value)

    @property
    def intf_flex_ray_sync_ch_a_even(self):
        return _props.get_session_intf_flex_ray_sync_ch_a_even(self._handle)

    @property
    def intf_flex_ray_sync_ch_a_odd(self):
        return _props.get_session_intf_flex_ray_sync_ch_a_odd(self._handle)

    @property
    def intf_flex_ray_sync_ch_b_even(self):
        return _props.get_session_intf_flex_ray_sync_ch_b_even(self._handle)

    @property
    def intf_flex_ray_sync_ch_b_odd(self):
        return _props.get_session_intf_flex_ray_sync_ch_b_odd(self._handle)

    @property
    def intf_flex_ray_sync_status(self):
        return _props.get_session_intf_flex_ray_sync_status(self._handle)

    @property
    def intf_flex_ray_term(self):
        return _props.get_session_intf_flex_ray_term(self._handle)

    @intf_flex_ray_term.setter
    def intf_flex_ray_term(self, value):
        _props.set_session_intf_flex_ray_term(self._handle, value)

    @property
    def intf_flex_ray_wakeup_ch(self):
        return _props.get_session_intf_flex_ray_wakeup_ch(self._handle)

    @intf_flex_ray_wakeup_ch.setter
    def intf_flex_ray_wakeup_ch(self, value):
        _props.set_session_intf_flex_ray_wakeup_ch(self._handle, value)

    @property
    def intf_flex_ray_wakeup_ptrn(self):
        return _props.get_session_intf_flex_ray_wakeup_ptrn(self._handle)

    @intf_flex_ray_wakeup_ptrn.setter
    def intf_flex_ray_wakeup_ptrn(self, value):
        _props.set_session_intf_flex_ray_wakeup_ptrn(self._handle, value)

    def set_intf_flex_ray_sleep(self, value):
        _props.set_session_intf_flex_ray_sleep(self._handle, value)

    @property
    def intf_flex_ray_connected_chs(self):
        return _props.get_session_intf_flex_ray_connected_chs(self._handle)

    @intf_flex_ray_connected_chs.setter
    def intf_flex_ray_connected_chs(self, value):
        _props.set_session_intf_flex_ray_connected_chs(self._handle, value)

    @property
    def intf_lin_break_length(self):
        return _props.get_session_intf_lin_break_length(self._handle)

    @intf_lin_break_length.setter
    def intf_lin_break_length(self, value):
        _props.set_session_intf_lin_break_length(self._handle, value)

    @property
    def intf_lin_master(self):
        return _props.get_session_intf_lin_master(self._handle)

    @intf_lin_master.setter
    def intf_lin_master(self, value):
        _props.set_session_intf_lin_master(self._handle, value)

    @property
    def intf_lin_sched_names(self):
        return _props.get_session_intf_lin_sched_names(self._handle)

    def set_intf_lin_sleep(self, value):
        _props.set_session_intf_lin_sleep(self._handle, value.value)

    @property
    def intf_lin_term(self):
        return constants.LinTerm(_props.get_session_intf_lin_term(self._handle))

    @intf_lin_term.setter
    def intf_lin_term(self, value):
        _props.set_session_intf_lin_term(self._handle, value.value)

    @property
    def intf_lin_diag_p_2min(self):
        return _props.get_session_intf_lin_diag_p_2min(self._handle)

    @intf_lin_diag_p_2min.setter
    def intf_lin_diag_p_2min(self, value):
        _props.set_session_intf_lin_diag_p_2min(self._handle, value)

    @property
    def intf_lin_diag_s_tmin(self):
        return _props.get_session_intf_lin_diag_s_tmin(self._handle)

    @intf_lin_diag_s_tmin.setter
    def intf_lin_diag_s_tmin(self, value):
        _props.set_session_intf_lin_diag_s_tmin(self._handle, value)

    @property
    def intf_lin_alw_start_wo_bus_pwr(self):
        return _props.get_session_intf_lin_alw_start_wo_bus_pwr(self._handle)

    @intf_lin_alw_start_wo_bus_pwr.setter
    def intf_lin_alw_start_wo_bus_pwr(self, value):
        _props.set_session_intf_lin_alw_start_wo_bus_pwr(self._handle, value)

    @property
    def intf_lino_str_slv_rsp_lst_by_nad(self):
        return _props.get_session_intf_lino_str_slv_rsp_lst_by_nad(self._handle)

    @intf_lino_str_slv_rsp_lst_by_nad.setter
    def intf_lino_str_slv_rsp_lst_by_nad(self, value):
        _props.set_session_intf_lino_str_slv_rsp_lst_by_nad(self._handle, value)

    @property
    def intf_lin_no_response_to_in_strm(self):
        return _props.get_session_intf_lin_no_response_to_in_strm(self._handle)

    @intf_lin_no_response_to_in_strm.setter
    def intf_lin_no_response_to_in_strm(self, value):
        _props.set_session_intf_lin_no_response_to_in_strm(self._handle, value)

    @property
    def intf_src_term_start_trigger(self):
        return _props.get_session_intf_src_term_start_trigger(self._handle)

    @intf_src_term_start_trigger.setter
    def intf_src_term_start_trigger(self, value):
        _props.set_session_intf_src_term_start_trigger(self._handle, value)

    @property
    def j1939_address(self):
        return _props.get_session_j1939_address(self._handle)

    @j1939_address.setter
    def j1939_address(self, value):
        _props.set_session_j1939_address(self._handle, value)

    @property
    def j1939_name(self):
        return _props.get_session_j1939_name(self._handle)

    @j1939_name.setter
    def j1939_name(self, value):
        _props.set_session_j1939_name(self._handle, value)

    def set_j1939ecu(self, value):
        _props.set_session_j1939ecu(self._handle, value)

    @property
    def j1939_timeout_t1(self):
        return _props.get_session_j1939_timeout_t1(self._handle)

    @j1939_timeout_t1.setter
    def j1939_timeout_t1(self, value):
        _props.set_session_j1939_timeout_t1(self._handle, value)

    @property
    def j1939_timeout_t2(self):
        return _props.get_session_j1939_timeout_t2(self._handle)

    @j1939_timeout_t2.setter
    def j1939_timeout_t2(self, value):
        _props.set_session_j1939_timeout_t2(self._handle, value)

    @property
    def j1939_timeout_t3(self):
        return _props.get_session_j1939_timeout_t3(self._handle)

    @j1939_timeout_t3.setter
    def j1939_timeout_t3(self, value):
        _props.set_session_j1939_timeout_t3(self._handle, value)

    @property
    def j1939_timeout_t4(self):
        return _props.get_session_j1939_timeout_t4(self._handle)

    @j1939_timeout_t4.setter
    def j1939_timeout_t4(self, value):
        _props.set_session_j1939_timeout_t4(self._handle, value)

    @property
    def j1939_response_time_tr_sd(self):
        return _props.get_session_j1939_response_time_tr_sd(self._handle)

    @j1939_response_time_tr_sd.setter
    def j1939_response_time_tr_sd(self, value):
        _props.set_session_j1939_response_time_tr_sd(self._handle, value)

    @property
    def j1939_response_time_tr_gd(self):
        return _props.get_session_j1939_response_time_tr_gd(self._handle)

    @j1939_response_time_tr_gd.setter
    def j1939_response_time_tr_gd(self, value):
        _props.set_session_j1939_response_time_tr_gd(self._handle, value)

    @property
    def j1939_hold_time_th(self):
        return _props.get_session_j1939_hold_time_th(self._handle)

    @j1939_hold_time_th.setter
    def j1939_hold_time_th(self, value):
        _props.set_session_j1939_hold_time_th(self._handle, value)

    @property
    def j1939_num_packets_recv(self):
        return _props.get_session_j1939_num_packets_recv(self._handle)

    @j1939_num_packets_recv.setter
    def j1939_num_packets_recv(self, value):
        _props.set_session_j1939_num_packets_recv(self._handle, value)

    @property
    def j1939_num_packets_resp(self):
        return _props.get_session_j1939_num_packets_resp(self._handle)

    @j1939_num_packets_resp.setter
    def j1939_num_packets_resp(self, value):
        _props.set_session_j1939_num_packets_resp(self._handle, value)

    @property
    def j1939_max_repeat_cts(self):
        return _props.get_session_j1939_max_repeat_cts(self._handle)

    @j1939_max_repeat_cts.setter
    def j1939_max_repeat_cts(self, value):
        _props.set_session_j1939_max_repeat_cts(self._handle, value)

    @property
    def j1939_fill_byte(self):
        return _props.get_session_j1939_fill_byte(self._handle)

    @j1939_fill_byte.setter
    def j1939_fill_byte(self, value):
        _props.set_session_j1939_fill_byte(self._handle, value)

    @property
    def j1939_write_queue_size(self):
        return _props.get_session_j1939_write_queue_size(self._handle)

    @j1939_write_queue_size.setter
    def j1939_write_queue_size(self, value):
        _props.set_session_j1939_write_queue_size(self._handle, value)

    @property
    def j1939ecu_busy(self):
        return _props.get_session_j1939ecu_busy(self._handle)

    @j1939ecu_busy.setter
    def j1939ecu_busy(self, value):
        _props.set_session_j1939ecu_busy(self._handle, value)

    @property
    def intf_can_edge_filter(self):
        return _props.get_session_intf_can_edge_filter(self._handle)

    @intf_can_edge_filter.setter
    def intf_can_edge_filter(self, value):
        _props.set_session_intf_can_edge_filter(self._handle, value)

    @property
    def intf_can_transmit_pause(self):
        return _props.get_session_intf_can_transmit_pause(self._handle)

    @intf_can_transmit_pause.setter
    def intf_can_transmit_pause(self, value):
        _props.set_session_intf_can_transmit_pause(self._handle, value)

    @property
    def intf_can_disable_prot_exception_handling(self):
        return _props.get_session_intf_can_disable_prot_exception_handling(self._handle)

    @intf_can_disable_prot_exception_handling.setter
    def intf_can_disable_prot_exception_handling(self, value):
        _props.set_session_intf_can_disable_prot_exception_handling(self._handle, value)


def create_session_by_ref(
        database_refs,
        interface,
        mode):
    return _funcs.nx_create_session_by_ref(database_refs, interface, mode)


def read_signal_single_point(
        session_ref,
        value_buffer,
        size_of_value_buffer,
        timestamp_buffer,
        size_of_timestamp_buffer):
    raise NotImplementedError("Placeholder")


def read_signal_waveform(
        session_ref,
        timeout,
        start_time,
        delta_time,
        value_buffer,
        size_of_value_buffer,
        number_of_values_returned):
    raise NotImplementedError("Placeholder")


def read_signal_xy(
        session_ref,
        time_limit,
        value_buffer,
        size_of_value_buffer,
        timestamp_buffer,
        size_of_timestamp_buffer,
        num_pairs_buffer,
        size_of_num_pairs_buffer):
    raise NotImplementedError("Placeholder")


def read_state(
        session_ref,
        state_id,
        state_size,
        state_value,
        fault):
    raise NotImplementedError("Placeholder")


def write_signal_single_point(
        session_ref,
        value_buffer):
    _funcs.nx_write_signal_single_point(session_ref, value_buffer)


def write_state(
        session_ref,
        state_id,
        state_size,
        state_value):
    raise NotImplementedError("Placeholder")


def write_signal_waveform(
        session_ref,
        timeout,
        value_buffer):
    _funcs.nx_write_signal_waveform(session_ref, timeout, value_buffer)


def write_signal_xy(
        session_ref,
        timeout,
        value_buffer,
        timestamp_buffer,
        num_pairs_buffer):
    _funcs.nx_write_signal_xy(session_ref, timeout, value_buffer, timestamp_buffer, num_pairs_buffer)


def convert_frames_to_signals_single_point(
        session_ref,
        frame_buffer,
        number_of_bytes_for_frames,
        value_buffer,
        size_of_value_buffer,
        timestamp_buffer,
        size_of_timestamp_buffer):
    raise NotImplementedError("Placeholder")


def convert_signals_to_frames_single_point(
        session_ref,
        value_buffer,
        size_of_value_buffer,
        buffer,
        size_of_buffer,
        number_of_bytes_returned):
    raise NotImplementedError("Placeholder")


def clear(
        session_ref):
    _funcs.nx_clear(session_ref)


def connect_terminals(
        session_ref,
        source,
        destination):
    _funcs.nx_connect_terminals(session_ref, source, destination)


def disconnect_terminals(
        session_ref,
        source,
        destination):
    _funcs.nx_disconnect_terminals(session_ref, source, destination)


def flush(
        session_ref):
    _funcs.nx_flush(session_ref)


def stop(
        session_ref,
        scope):
    _funcs.nx_stop(session_ref, scope)


def wait(
        session_ref,
        condition,
        param_in,
        timeout):
    return _funcs.nx_wait(session_ref, condition, param_in, timeout)
