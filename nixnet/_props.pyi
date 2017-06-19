from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes

from nixnet import _cconsts
from nixnet import _cprops
from nixnet import _errors


def get_session_application_protocol(
        ref):
    ...


def get_session_auto_start(
        ref):
    ...


def set_session_auto_start(
        ref
        value) -> None:
    ...


def get_session_cluster_name(
        ref):
    ...


def get_session_database_name(
        ref):
    ...


def get_session_list(
        ref):
    ...


def get_session_mode(
        ref):
    ...


def get_session_num_frames(
        ref):
    ...


def get_session_num_in_list(
        ref):
    ...


def get_session_num_pend(
        ref):
    ...


def get_session_num_unused(
        ref):
    ...


def get_session_payld_len_max(
        ref):
    ...


def get_session_protocol(
        ref):
    ...


def get_session_queue_size(
        ref):
    ...


def set_session_queue_size(
        ref
        value) -> None:
    ...


def get_session_resamp_rate(
        ref):
    ...


def set_session_resamp_rate(
        ref
        value) -> None:
    ...


def get_session_intf_baud_rate(
        ref):
    ...


def set_session_intf_baud_rate(
        ref
        value) -> None:
    ...


def get_session_intf_baud_rate64(
        ref):
    ...


def set_session_intf_baud_rate64(
        ref
        value) -> None:
    ...


def get_session_intf_bus_err_to_in_strm(
        ref):
    ...


def set_session_intf_bus_err_to_in_strm(
        ref
        value) -> None:
    ...


def get_session_intf_echo_tx(
        ref):
    ...


def set_session_intf_echo_tx(
        ref
        value) -> None:
    ...


def get_session_intf_name(
        ref):
    ...


def get_session_intf_out_strm_list(
        ref):
    ...


def set_session_intf_out_strm_list(
        ref
        value) -> None:
    ...


def get_session_intf_out_strm_timng(
        ref):
    ...


def set_session_intf_out_strm_timng(
        ref
        value) -> None:
    ...


def get_session_intf_start_trig_to_in_strm(
        ref):
    ...


def set_session_intf_start_trig_to_in_strm(
        ref
        value) -> None:
    ...


def set_session_intf_can_ext_tcvr_config(
        ref
        value) -> None:
    ...


def get_session_intf_can_lstn_only(
        ref):
    ...


def set_session_intf_can_lstn_only(
        ref
        value) -> None:
    ...


def get_session_intf_can_pend_tx_order(
        ref):
    ...


def set_session_intf_can_pend_tx_order(
        ref
        value) -> None:
    ...


def get_session_intf_can_sing_shot(
        ref):
    ...


def set_session_intf_can_sing_shot(
        ref
        value) -> None:
    ...


def get_session_intf_can_term(
        ref):
    ...


def set_session_intf_can_term(
        ref
        value) -> None:
    ...


def get_session_intf_can_tcvr_state(
        ref):
    ...


def set_session_intf_can_tcvr_state(
        ref
        value) -> None:
    ...


def get_session_intf_can_tcvr_type(
        ref):
    ...


def set_session_intf_can_tcvr_type(
        ref
        value) -> None:
    ...


def get_session_intf_can_out_strm_list_by_id(
        ref):
    ...


def set_session_intf_can_out_strm_list_by_id(
        ref
        value) -> None:
    ...


def get_session_intf_can_io_mode(
        ref):
    ...


def get_session_intf_can_fd_baud_rate(
        ref):
    ...


def set_session_intf_can_fd_baud_rate(
        ref
        value) -> None:
    ...


def get_session_intf_can_fd_baud_rate64(
        ref):
    ...


def set_session_intf_can_fd_baud_rate64(
        ref
        value) -> None:
    ...


def get_session_intf_can_tx_io_mode(
        ref):
    ...


def set_session_intf_can_tx_io_mode(
        ref
        value) -> None:
    ...


def get_session_intf_can_fd_iso_mode(
        ref):
    ...


def set_session_intf_can_fd_iso_mode(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_acc_start_rng(
        ref):
    ...


def set_session_intf_flex_ray_acc_start_rng(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_alw_hlt_clk(
        ref):
    ...


def set_session_intf_flex_ray_alw_hlt_clk(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_alw_pass_act(
        ref):
    ...


def set_session_intf_flex_ray_alw_pass_act(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_auto_aslp_whn_stp(
        ref):
    ...


def set_session_intf_flex_ray_auto_aslp_whn_stp(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_clst_drift_dmp(
        ref):
    ...


def set_session_intf_flex_ray_clst_drift_dmp(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_coldstart(
        ref):
    ...


def get_session_intf_flex_ray_dec_corr(
        ref):
    ...


def set_session_intf_flex_ray_dec_corr(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_delay_comp_a(
        ref):
    ...


def set_session_intf_flex_ray_delay_comp_a(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_delay_comp_b(
        ref):
    ...


def set_session_intf_flex_ray_delay_comp_b(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_key_slot_id(
        ref):
    ...


def set_session_intf_flex_ray_key_slot_id(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_latest_tx(
        ref):
    ...


def get_session_intf_flex_ray_list_timo(
        ref):
    ...


def set_session_intf_flex_ray_list_timo(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_mac_init_off_a(
        ref):
    ...


def set_session_intf_flex_ray_mac_init_off_a(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_mac_init_off_b(
        ref):
    ...


def set_session_intf_flex_ray_mac_init_off_b(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_mic_init_off_a(
        ref):
    ...


def set_session_intf_flex_ray_mic_init_off_a(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_mic_init_off_b(
        ref):
    ...


def set_session_intf_flex_ray_mic_init_off_b(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_max_drift(
        ref):
    ...


def set_session_intf_flex_ray_max_drift(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_microtick(
        ref):
    ...


def get_session_intf_flex_ray_null_to_in_strm(
        ref):
    ...


def set_session_intf_flex_ray_null_to_in_strm(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_off_corr(
        ref):
    ...


def get_session_intf_flex_ray_off_corr_out(
        ref):
    ...


def set_session_intf_flex_ray_off_corr_out(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_rate_corr(
        ref):
    ...


def get_session_intf_flex_ray_rate_corr_out(
        ref):
    ...


def set_session_intf_flex_ray_rate_corr_out(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_samp_per_micro(
        ref):
    ...


def set_session_intf_flex_ray_samp_per_micro(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_sing_slot_en(
        ref):
    ...


def set_session_intf_flex_ray_sing_slot_en(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_statistics_en(
        ref):
    ...


def set_session_intf_flex_ray_statistics_en(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_sym_to_in_strm(
        ref):
    ...


def set_session_intf_flex_ray_sym_to_in_strm(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_sync_ch_a_even(
        ref):
    ...


def get_session_intf_flex_ray_sync_ch_a_odd(
        ref):
    ...


def get_session_intf_flex_ray_sync_ch_b_even(
        ref):
    ...


def get_session_intf_flex_ray_sync_ch_b_odd(
        ref):
    ...


def get_session_intf_flex_ray_sync_status(
        ref):
    ...


def get_session_intf_flex_ray_term(
        ref):
    ...


def set_session_intf_flex_ray_term(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_wakeup_ch(
        ref):
    ...


def set_session_intf_flex_ray_wakeup_ch(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_wakeup_ptrn(
        ref):
    ...


def set_session_intf_flex_ray_wakeup_ptrn(
        ref
        value) -> None:
    ...


def set_session_intf_flex_ray_sleep(
        ref
        value) -> None:
    ...


def get_session_intf_flex_ray_connected_chs(
        ref):
    ...


def set_session_intf_flex_ray_connected_chs(
        ref
        value) -> None:
    ...


def get_session_intf_lin_break_length(
        ref):
    ...


def set_session_intf_lin_break_length(
        ref
        value) -> None:
    ...


def get_session_intf_lin_master(
        ref):
    ...


def set_session_intf_lin_master(
        ref
        value) -> None:
    ...


def get_session_intf_lin_sched_names(
        ref):
    ...


def set_session_intf_lin_sleep(
        ref
        value) -> None:
    ...


def get_session_intf_lin_term(
        ref):
    ...


def set_session_intf_lin_term(
        ref
        value) -> None:
    ...


def get_session_intf_lin_diag_p_2min(
        ref):
    ...


def set_session_intf_lin_diag_p_2min(
        ref
        value) -> None:
    ...


def get_session_intf_lin_diag_s_tmin(
        ref):
    ...


def set_session_intf_lin_diag_s_tmin(
        ref
        value) -> None:
    ...


def get_session_intf_lin_alw_start_wo_bus_pwr(
        ref):
    ...


def set_session_intf_lin_alw_start_wo_bus_pwr(
        ref
        value) -> None:
    ...


def get_session_intf_lino_str_slv_rsp_lst_by_nad(
        ref):
    ...


def set_session_intf_lino_str_slv_rsp_lst_by_nad(
        ref
        value) -> None:
    ...


def get_session_intf_lin_no_response_to_in_strm(
        ref):
    ...


def set_session_intf_lin_no_response_to_in_strm(
        ref
        value) -> None:
    ...


def get_session_intf_src_term_start_trigger(
        ref):
    ...


def set_session_intf_src_term_start_trigger(
        ref
        value) -> None:
    ...


def get_session_j1939_address(
        ref):
    ...


def set_session_j1939_address(
        ref
        value) -> None:
    ...


def get_session_j1939_name(
        ref):
    ...


def set_session_j1939_name(
        ref
        value) -> None:
    ...


def set_session_j1939ecu(
        ref
        value) -> None:
    ...


def get_session_j1939_timeout_t1(
        ref):
    ...


def set_session_j1939_timeout_t1(
        ref
        value) -> None:
    ...


def get_session_j1939_timeout_t2(
        ref):
    ...


def set_session_j1939_timeout_t2(
        ref
        value) -> None:
    ...


def get_session_j1939_timeout_t3(
        ref):
    ...


def set_session_j1939_timeout_t3(
        ref
        value) -> None:
    ...


def get_session_j1939_timeout_t4(
        ref):
    ...


def set_session_j1939_timeout_t4(
        ref
        value) -> None:
    ...


def get_session_j1939_response_time_tr_sd(
        ref):
    ...


def set_session_j1939_response_time_tr_sd(
        ref
        value) -> None:
    ...


def get_session_j1939_response_time_tr_gd(
        ref):
    ...


def set_session_j1939_response_time_tr_gd(
        ref
        value) -> None:
    ...


def get_session_j1939_hold_time_th(
        ref):
    ...


def set_session_j1939_hold_time_th(
        ref
        value) -> None:
    ...


def get_session_j1939_num_packets_recv(
        ref):
    ...


def set_session_j1939_num_packets_recv(
        ref
        value) -> None:
    ...


def get_session_j1939_num_packets_resp(
        ref):
    ...


def set_session_j1939_num_packets_resp(
        ref
        value) -> None:
    ...


def get_session_j1939_max_repeat_cts(
        ref):
    ...


def set_session_j1939_max_repeat_cts(
        ref
        value) -> None:
    ...


def get_session_j1939_fill_byte(
        ref):
    ...


def set_session_j1939_fill_byte(
        ref
        value) -> None:
    ...


def get_session_j1939_write_queue_size(
        ref):
    ...


def set_session_j1939_write_queue_size(
        ref
        value) -> None:
    ...


def get_session_j1939ecu_busy(
        ref):
    ...


def set_session_j1939ecu_busy(
        ref
        value) -> None:
    ...


def get_session_intf_can_edge_filter(
        ref):
    ...


def set_session_intf_can_edge_filter(
        ref
        value) -> None:
    ...


def get_session_intf_can_transmit_pause(
        ref):
    ...


def set_session_intf_can_transmit_pause(
        ref
        value) -> None:
    ...


def get_session_intf_can_disable_prot_exception_handling(
        ref):
    ...


def set_session_intf_can_disable_prot_exception_handling(
        ref
        value) -> None:
    ...


def set_session_can_start_time_off(
        ref
        sub,
        value) -> None:
    ...


def set_session_can_tx_time(
        ref
        sub,
        value) -> None:
    ...


def set_session_skip_n_cyclic_frames(
        ref
        sub,
        value) -> None:
    ...


def set_session_output_queue_update_freq(
        ref
        sub,
        value) -> None:
    ...


def set_session_lin_tx_n_corrupted_chksums(
        ref
        sub,
        value) -> None:
    ...


def set_session_j1939_addr_filter(
        ref
        sub,
        value) -> None:
    ...


def get_system_dev_refs(
        ref):
    ...


def get_system_intf_refs(
        ref):
    ...


def get_system_intf_refs_can(
        ref):
    ...


def get_system_intf_refs_flex_ray(
        ref):
    ...


def get_system_intf_refs_lin(
        ref):
    ...


def get_system_ver_build(
        ref):
    ...


def get_system_ver_major(
        ref):
    ...


def get_system_ver_minor(
        ref):
    ...


def get_system_ver_phase(
        ref):
    ...


def get_system_ver_update(
        ref):
    ...


def get_system_cdaq_pkt_time(
        ref):
    ...


def set_system_cdaq_pkt_time(
        ref
        value) -> None:
    ...


def get_system_intf_refs_all(
        ref):
    ...


def get_device_form_fac(
        ref):
    ...


def get_device_intf_refs(
        ref):
    ...


def get_device_name(
        ref):
    ...


def get_device_num_ports(
        ref):
    ...


def get_device_product_num(
        ref):
    ...


def get_device_ser_num(
        ref):
    ...


def get_device_slot_num(
        ref):
    ...


def get_device_num_ports_all(
        ref):
    ...


def get_device_intf_refs_all(
        ref):
    ...


def get_interface_dev_ref(
        ref):
    ...


def get_interface_name(
        ref):
    ...


def get_interface_num(
        ref):
    ...


def get_interface_port_num(
        ref):
    ...


def get_interface_protocol(
        ref):
    ...


def get_interface_can_term_cap(
        ref):
    ...


def get_interface_can_tcvr_cap(
        ref):
    ...


def get_interface_dongle_state(
        ref):
    ...


def get_interface_dongle_id(
        ref):
    ...


def get_interface_dongle_revision(
        ref):
    ...


def get_interface_dongle_firmware_version(
        ref):
    ...


def get_interface_dongle_compatible_revision(
        ref):
    ...


def get_interface_dongle_compatible_firmware_version(
        ref):
    ...


def get_database_name(
        ref):
    ...


def get_database_clst_refs(
        ref):
    ...


def get_database_show_invalid_from_open(
        ref):
    ...


def set_database_show_invalid_from_open(
        ref
        value) -> None:
    ...


def get_cluster_baud_rate(
        ref):
    ...


def set_cluster_baud_rate(
        ref
        value) -> None:
    ...


def get_cluster_baud_rate64(
        ref):
    ...


def set_cluster_baud_rate64(
        ref
        value) -> None:
    ...


def get_cluster_comment(
        ref):
    ...


def set_cluster_comment(
        ref
        value) -> None:
    ...


def get_cluster_config_status(
        ref):
    ...


def get_cluster_database_ref(
        ref):
    ...


def get_cluster_ecu_refs(
        ref):
    ...


def get_cluster_frm_refs(
        ref):
    ...


def get_cluster_name(
        ref):
    ...


def set_cluster_name(
        ref
        value) -> None:
    ...


def get_cluster_pdu_refs(
        ref):
    ...


def get_cluster_pd_us_reqd(
        ref):
    ...


def get_cluster_protocol(
        ref):
    ...


def set_cluster_protocol(
        ref
        value) -> None:
    ...


def get_cluster_sig_refs(
        ref):
    ...


def get_cluster_can_io_mode(
        ref):
    ...


def set_cluster_can_io_mode(
        ref
        value) -> None:
    ...


def get_cluster_can_fd_baud_rate(
        ref):
    ...


def set_cluster_can_fd_baud_rate(
        ref
        value) -> None:
    ...


def get_cluster_can_fd_baud_rate64(
        ref):
    ...


def set_cluster_can_fd_baud_rate64(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_act_pt_off(
        ref):
    ...


def set_cluster_flex_ray_act_pt_off(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_cas_rx_l_max(
        ref):
    ...


def set_cluster_flex_ray_cas_rx_l_max(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_channels(
        ref):
    ...


def set_cluster_flex_ray_channels(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_clst_drift_dmp(
        ref):
    ...


def set_cluster_flex_ray_clst_drift_dmp(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_cold_st_ats(
        ref):
    ...


def set_cluster_flex_ray_cold_st_ats(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_cycle(
        ref):
    ...


def set_cluster_flex_ray_cycle(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_dyn_seg_start(
        ref):
    ...


def get_cluster_flex_ray_dyn_slot_idl_ph(
        ref):
    ...


def set_cluster_flex_ray_dyn_slot_idl_ph(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_latest_usable_dyn(
        ref):
    ...


def get_cluster_flex_ray_latest_guar_dyn(
        ref):
    ...


def get_cluster_flex_ray_lis_noise(
        ref):
    ...


def set_cluster_flex_ray_lis_noise(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_macro_per_cycle(
        ref):
    ...


def set_cluster_flex_ray_macro_per_cycle(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_macrotick(
        ref):
    ...


def get_cluster_flex_ray_max_wo_clk_cor_fat(
        ref):
    ...


def set_cluster_flex_ray_max_wo_clk_cor_fat(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_max_wo_clk_cor_pas(
        ref):
    ...


def set_cluster_flex_ray_max_wo_clk_cor_pas(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_minislot_act_pt(
        ref):
    ...


def set_cluster_flex_ray_minislot_act_pt(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_minislot(
        ref):
    ...


def set_cluster_flex_ray_minislot(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_nm_vec_len(
        ref):
    ...


def set_cluster_flex_ray_nm_vec_len(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_nit(
        ref):
    ...


def set_cluster_flex_ray_nit(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_nit_start(
        ref):
    ...


def get_cluster_flex_ray_num_minislt(
        ref):
    ...


def set_cluster_flex_ray_num_minislt(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_num_stat_slt(
        ref):
    ...


def set_cluster_flex_ray_num_stat_slt(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_off_cor_st(
        ref):
    ...


def set_cluster_flex_ray_off_cor_st(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_payld_len_dyn_max(
        ref):
    ...


def set_cluster_flex_ray_payld_len_dyn_max(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_payld_len_max(
        ref):
    ...


def get_cluster_flex_ray_payld_len_st(
        ref):
    ...


def set_cluster_flex_ray_payld_len_st(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_stat_slot(
        ref):
    ...


def set_cluster_flex_ray_stat_slot(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_sym_win(
        ref):
    ...


def set_cluster_flex_ray_sym_win(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_sym_win_start(
        ref):
    ...


def get_cluster_flex_ray_sync_node_max(
        ref):
    ...


def set_cluster_flex_ray_sync_node_max(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_tss_tx(
        ref):
    ...


def set_cluster_flex_ray_tss_tx(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_wake_sym_rx_idl(
        ref):
    ...


def set_cluster_flex_ray_wake_sym_rx_idl(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_wake_sym_rx_low(
        ref):
    ...


def set_cluster_flex_ray_wake_sym_rx_low(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_wake_sym_rx_win(
        ref):
    ...


def set_cluster_flex_ray_wake_sym_rx_win(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_wake_sym_tx_idl(
        ref):
    ...


def set_cluster_flex_ray_wake_sym_tx_idl(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_wake_sym_tx_low(
        ref):
    ...


def set_cluster_flex_ray_wake_sym_tx_low(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_use_wakeup(
        ref):
    ...


def set_cluster_flex_ray_use_wakeup(
        ref
        value) -> None:
    ...


def get_cluster_lin_schedules(
        ref):
    ...


def get_cluster_lin_tick(
        ref):
    ...


def set_cluster_lin_tick(
        ref
        value) -> None:
    ...


def get_cluster_flex_ray_alw_pass_act(
        ref):
    ...


def set_cluster_flex_ray_alw_pass_act(
        ref
        value) -> None:
    ...


def get_cluster_application_protocol(
        ref):
    ...


def set_cluster_application_protocol(
        ref
        value) -> None:
    ...


def get_cluster_can_fd_iso_mode(
        ref):
    ...


def get_frame_application_protocol(
        ref):
    ...


def set_frame_application_protocol(
        ref
        value) -> None:
    ...


def get_frame_cluster_ref(
        ref):
    ...


def get_frame_comment(
        ref):
    ...


def set_frame_comment(
        ref
        value) -> None:
    ...


def get_frame_config_status(
        ref):
    ...


def get_frame_default_payload(
        ref):
    ...


def set_frame_default_payload(
        ref
        value) -> None:
    ...


def get_frame_id(
        ref):
    ...


def set_frame_id(
        ref
        value) -> None:
    ...


def get_frame_name(
        ref):
    ...


def set_frame_name(
        ref
        value) -> None:
    ...


def get_frame_payload_len(
        ref):
    ...


def set_frame_payload_len(
        ref
        value) -> None:
    ...


def get_frame_sig_refs(
        ref):
    ...


def get_frame_can_ext_id(
        ref):
    ...


def set_frame_can_ext_id(
        ref
        value) -> None:
    ...


def get_frame_can_timing_type(
        ref):
    ...


def set_frame_can_timing_type(
        ref
        value) -> None:
    ...


def get_frame_can_tx_time(
        ref):
    ...


def set_frame_can_tx_time(
        ref
        value) -> None:
    ...


def get_frame_flex_ray_base_cycle(
        ref):
    ...


def set_frame_flex_ray_base_cycle(
        ref
        value) -> None:
    ...


def get_frame_flex_ray_ch_assign(
        ref):
    ...


def set_frame_flex_ray_ch_assign(
        ref
        value) -> None:
    ...


def get_frame_flex_ray_cycle_rep(
        ref):
    ...


def set_frame_flex_ray_cycle_rep(
        ref
        value) -> None:
    ...


def get_frame_flex_ray_preamble(
        ref):
    ...


def set_frame_flex_ray_preamble(
        ref
        value) -> None:
    ...


def get_frame_flex_ray_startup(
        ref):
    ...


def set_frame_flex_ray_startup(
        ref
        value) -> None:
    ...


def get_frame_flex_ray_sync(
        ref):
    ...


def set_frame_flex_ray_sync(
        ref
        value) -> None:
    ...


def get_frame_flex_ray_timing_type(
        ref):
    ...


def set_frame_flex_ray_timing_type(
        ref
        value) -> None:
    ...


def get_frame_flex_ray_in_cyc_rep_enabled(
        ref):
    ...


def get_frame_flex_ray_in_cyc_rep_i_ds(
        ref):
    ...


def set_frame_flex_ray_in_cyc_rep_i_ds(
        ref
        value) -> None:
    ...


def get_frame_flex_ray_in_cyc_rep_ch_assigns(
        ref):
    ...


def set_frame_flex_ray_in_cyc_rep_ch_assigns(
        ref
        value) -> None:
    ...


def get_frame_lin_checksum(
        ref):
    ...


def get_frame_mux_is_muxed(
        ref):
    ...


def get_frame_mux_data_mux_sig_ref(
        ref):
    ...


def get_frame_mux_static_sig_refs(
        ref):
    ...


def get_frame_mux_subframe_refs(
        ref):
    ...


def get_frame_pdu_refs(
        ref):
    ...


def set_frame_pdu_refs(
        ref
        value) -> None:
    ...


def get_frame_pdu_start_bits(
        ref):
    ...


def set_frame_pdu_start_bits(
        ref
        value) -> None:
    ...


def get_frame_pdu_update_bits(
        ref):
    ...


def set_frame_pdu_update_bits(
        ref
        value) -> None:
    ...


def get_frame_variable_payload(
        ref):
    ...


def set_frame_variable_payload(
        ref
        value) -> None:
    ...


def get_frame_ca_nio_mode(
        ref):
    ...


def set_frame_ca_nio_mode(
        ref
        value) -> None:
    ...


def get_pdu_cluster_ref(
        ref):
    ...


def get_pdu_default_payload(
        ref):
    ...


def set_pdu_default_payload(
        ref
        value) -> None:
    ...


def get_pdu_comment(
        ref):
    ...


def set_pdu_comment(
        ref
        value) -> None:
    ...


def get_pdu_config_status(
        ref):
    ...


def get_pdu_frm_refs(
        ref):
    ...


def get_pdu_name(
        ref):
    ...


def set_pdu_name(
        ref
        value) -> None:
    ...


def get_pdu_payload_len(
        ref):
    ...


def set_pdu_payload_len(
        ref
        value) -> None:
    ...


def get_pdu_sig_refs(
        ref):
    ...


def get_pdu_mux_is_muxed(
        ref):
    ...


def get_pdu_mux_data_mux_sig_ref(
        ref):
    ...


def get_pdu_mux_static_sig_refs(
        ref):
    ...


def get_pdu_mux_subframe_refs(
        ref):
    ...


def get_signal_byte_ordr(
        ref):
    ...


def set_signal_byte_ordr(
        ref
        value) -> None:
    ...


def get_signal_comment(
        ref):
    ...


def set_signal_comment(
        ref
        value) -> None:
    ...


def get_signal_config_status(
        ref):
    ...


def get_signal_data_type(
        ref):
    ...


def set_signal_data_type(
        ref
        value) -> None:
    ...


def get_signal_default(
        ref):
    ...


def set_signal_default(
        ref
        value) -> None:
    ...


def get_signal_frame_ref(
        ref):
    ...


def get_signal_max(
        ref):
    ...


def set_signal_max(
        ref
        value) -> None:
    ...


def get_signal_min(
        ref):
    ...


def set_signal_min(
        ref
        value) -> None:
    ...


def get_signal_name(
        ref):
    ...


def set_signal_name(
        ref
        value) -> None:
    ...


def get_signal_name_unique_to_cluster(
        ref):
    ...


def get_signal_num_bits(
        ref):
    ...


def set_signal_num_bits(
        ref
        value) -> None:
    ...


def get_signal_pdu_ref(
        ref):
    ...


def get_signal_scale_fac(
        ref):
    ...


def set_signal_scale_fac(
        ref
        value) -> None:
    ...


def get_signal_scale_off(
        ref):
    ...


def set_signal_scale_off(
        ref
        value) -> None:
    ...


def get_signal_start_bit(
        ref):
    ...


def set_signal_start_bit(
        ref
        value) -> None:
    ...


def get_signal_unit(
        ref):
    ...


def set_signal_unit(
        ref
        value) -> None:
    ...


def get_signal_mux_is_data_mux(
        ref):
    ...


def set_signal_mux_is_data_mux(
        ref
        value) -> None:
    ...


def get_signal_mux_is_dynamic(
        ref):
    ...


def get_signal_mux_value(
        ref):
    ...


def get_signal_mux_subfrm_ref(
        ref):
    ...


def get_subframe_config_status(
        ref):
    ...


def get_subframe_dyn_sig_refs(
        ref):
    ...


def get_subframe_frm_ref(
        ref):
    ...


def get_subframe_mux_value(
        ref):
    ...


def set_subframe_mux_value(
        ref
        value) -> None:
    ...


def get_subframe_name(
        ref):
    ...


def set_subframe_name(
        ref
        value) -> None:
    ...


def get_subframe_pdu_ref(
        ref):
    ...


def get_subframe_name_unique_to_cluster(
        ref):
    ...


def get_ecu_clst_ref(
        ref):
    ...


def get_ecu_comment(
        ref):
    ...


def set_ecu_comment(
        ref
        value) -> None:
    ...


def get_ecu_config_status(
        ref):
    ...


def get_ecu_name(
        ref):
    ...


def set_ecu_name(
        ref
        value) -> None:
    ...


def get_ecu_rx_frm_refs(
        ref):
    ...


def set_ecu_rx_frm_refs(
        ref
        value) -> None:
    ...


def get_ecu_tx_frm_refs(
        ref):
    ...


def set_ecu_tx_frm_refs(
        ref
        value) -> None:
    ...


def get_ecu_flex_ray_is_coldstart(
        ref):
    ...


def get_ecu_flex_ray_startup_frame_ref(
        ref):
    ...


def get_ecu_flex_ray_wakeup_ptrn(
        ref):
    ...


def set_ecu_flex_ray_wakeup_ptrn(
        ref
        value) -> None:
    ...


def get_ecu_flex_ray_wakeup_chs(
        ref):
    ...


def set_ecu_flex_ray_wakeup_chs(
        ref
        value) -> None:
    ...


def get_ecu_flex_ray_connected_chs(
        ref):
    ...


def set_ecu_flex_ray_connected_chs(
        ref
        value) -> None:
    ...


def get_ecu_lin_master(
        ref):
    ...


def set_ecu_lin_master(
        ref
        value) -> None:
    ...


def get_ecu_lin_protocol_ver(
        ref):
    ...


def set_ecu_lin_protocol_ver(
        ref
        value) -> None:
    ...


def get_ecu_lin_initial_nad(
        ref):
    ...


def set_ecu_lin_initial_nad(
        ref
        value) -> None:
    ...


def get_ecu_lin_config_nad(
        ref):
    ...


def set_ecu_lin_config_nad(
        ref
        value) -> None:
    ...


def get_ecu_lin_supplier_id(
        ref):
    ...


def set_ecu_lin_supplier_id(
        ref
        value) -> None:
    ...


def get_ecu_lin_function_id(
        ref):
    ...


def set_ecu_lin_function_id(
        ref
        value) -> None:
    ...


def get_ecu_linp_2min(
        ref):
    ...


def set_ecu_linp_2min(
        ref
        value) -> None:
    ...


def get_ecu_lins_tmin(
        ref):
    ...


def set_ecu_lins_tmin(
        ref
        value) -> None:
    ...


def get_ecu_j1939_preferred_address(
        ref):
    ...


def set_ecu_j1939_preferred_address(
        ref
        value) -> None:
    ...


def get_ecu_j1939_node_name(
        ref):
    ...


def set_ecu_j1939_node_name(
        ref
        value) -> None:
    ...


def get_lin_sched_clst_ref(
        ref):
    ...


def get_lin_sched_comment(
        ref):
    ...


def set_lin_sched_comment(
        ref
        value) -> None:
    ...


def get_lin_sched_config_status(
        ref):
    ...


def get_lin_sched_entries(
        ref):
    ...


def get_lin_sched_name(
        ref):
    ...


def set_lin_sched_name(
        ref
        value) -> None:
    ...


def get_lin_sched_priority(
        ref):
    ...


def set_lin_sched_priority(
        ref
        value) -> None:
    ...


def get_lin_sched_run_mode(
        ref):
    ...


def set_lin_sched_run_mode(
        ref
        value) -> None:
    ...


def get_lin_sched_entry_collision_res_sched(
        ref):
    ...


def set_lin_sched_entry_collision_res_sched(
        ref
        value) -> None:
    ...


def get_lin_sched_entry_delay(
        ref):
    ...


def set_lin_sched_entry_delay(
        ref
        value) -> None:
    ...


def get_lin_sched_entry_event_id(
        ref):
    ...


def set_lin_sched_entry_event_id(
        ref
        value) -> None:
    ...


def get_lin_sched_entry_frames(
        ref):
    ...


def set_lin_sched_entry_frames(
        ref
        value) -> None:
    ...


def get_lin_sched_entry_name(
        ref):
    ...


def set_lin_sched_entry_name(
        ref
        value) -> None:
    ...


def get_lin_sched_entry_name_unique_to_cluster(
        ref):
    ...


def get_lin_sched_entry_sched(
        ref):
    ...


def get_lin_sched_entry_type(
        ref):
    ...


def set_lin_sched_entry_type(
        ref
        value) -> None:
    ...


def get_lin_sched_entry_nc_ff_data_bytes(
        ref):
    ...


def set_lin_sched_entry_nc_ff_data_bytes(
        ref
        value) -> None:
    ...


