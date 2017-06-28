from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _funcs
from nixnet import _props
from nixnet import constants


class Cluster(object):

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
        return 'Cluster(handle={0})'.format(self._handle)

    def merge(
            self,
            source_obj,
            copy_mode,
            prefix,
            wait_for_complete):
        return _funcs.nxdb_merge(self._handle, source_obj._handle, copy_mode, prefix, wait_for_complete)

    @property
    def baud_rate(self):
        return _props.get_cluster_baud_rate(self._handle)

    @baud_rate.setter
    def baud_rate(self, value):
        _props.set_cluster_baud_rate(self._handle, value)

    @property
    def baud_rate64(self):
        return _props.get_cluster_baud_rate64(self._handle)

    @baud_rate64.setter
    def baud_rate64(self, value):
        _props.set_cluster_baud_rate64(self._handle, value)

    @property
    def comment(self):
        return _props.get_cluster_comment(self._handle)

    @comment.setter
    def comment(self, value):
        _props.set_cluster_comment(self._handle, value)

    @property
    def config_status(self):
        return _props.get_cluster_config_status(self._handle)

    @property
    def database_ref(self):
        return _props.get_cluster_database_ref(self._handle)

    @property
    def ecu_refs(self):
        return _props.get_cluster_ecu_refs(self._handle)

    @property
    def frm_refs(self):
        return _props.get_cluster_frm_refs(self._handle)

    @property
    def name(self):
        return _props.get_cluster_name(self._handle)

    @name.setter
    def name(self, value):
        _props.set_cluster_name(self._handle, value)

    @property
    def pdu_refs(self):
        return _props.get_cluster_pdu_refs(self._handle)

    @property
    def pd_us_reqd(self):
        return _props.get_cluster_pd_us_reqd(self._handle)

    @property
    def protocol(self):
        return constants.Protocol(_props.get_cluster_protocol(self._handle))

    @protocol.setter
    def protocol(self, value):
        _props.set_cluster_protocol(self._handle, value.value)

    @property
    def sig_refs(self):
        return _props.get_cluster_sig_refs(self._handle)

    @property
    def can_io_mode(self):
        return constants.CaNioMode(_props.get_cluster_can_io_mode(self._handle))

    @can_io_mode.setter
    def can_io_mode(self, value):
        _props.set_cluster_can_io_mode(self._handle, value.value)

    @property
    def can_fd_baud_rate(self):
        return _props.get_cluster_can_fd_baud_rate(self._handle)

    @can_fd_baud_rate.setter
    def can_fd_baud_rate(self, value):
        _props.set_cluster_can_fd_baud_rate(self._handle, value)

    @property
    def can_fd_baud_rate64(self):
        return _props.get_cluster_can_fd_baud_rate64(self._handle)

    @can_fd_baud_rate64.setter
    def can_fd_baud_rate64(self, value):
        _props.set_cluster_can_fd_baud_rate64(self._handle, value)

    @property
    def flex_ray_act_pt_off(self):
        return _props.get_cluster_flex_ray_act_pt_off(self._handle)

    @flex_ray_act_pt_off.setter
    def flex_ray_act_pt_off(self, value):
        _props.set_cluster_flex_ray_act_pt_off(self._handle, value)

    @property
    def flex_ray_cas_rx_l_max(self):
        return _props.get_cluster_flex_ray_cas_rx_l_max(self._handle)

    @flex_ray_cas_rx_l_max.setter
    def flex_ray_cas_rx_l_max(self, value):
        _props.set_cluster_flex_ray_cas_rx_l_max(self._handle, value)

    @property
    def flex_ray_channels(self):
        return _props.get_cluster_flex_ray_channels(self._handle)

    @flex_ray_channels.setter
    def flex_ray_channels(self, value):
        _props.set_cluster_flex_ray_channels(self._handle, value)

    @property
    def flex_ray_clst_drift_dmp(self):
        return _props.get_cluster_flex_ray_clst_drift_dmp(self._handle)

    @flex_ray_clst_drift_dmp.setter
    def flex_ray_clst_drift_dmp(self, value):
        _props.set_cluster_flex_ray_clst_drift_dmp(self._handle, value)

    @property
    def flex_ray_cold_st_ats(self):
        return _props.get_cluster_flex_ray_cold_st_ats(self._handle)

    @flex_ray_cold_st_ats.setter
    def flex_ray_cold_st_ats(self, value):
        _props.set_cluster_flex_ray_cold_st_ats(self._handle, value)

    @property
    def flex_ray_cycle(self):
        return _props.get_cluster_flex_ray_cycle(self._handle)

    @flex_ray_cycle.setter
    def flex_ray_cycle(self, value):
        _props.set_cluster_flex_ray_cycle(self._handle, value)

    @property
    def flex_ray_dyn_seg_start(self):
        return _props.get_cluster_flex_ray_dyn_seg_start(self._handle)

    @property
    def flex_ray_dyn_slot_idl_ph(self):
        return _props.get_cluster_flex_ray_dyn_slot_idl_ph(self._handle)

    @flex_ray_dyn_slot_idl_ph.setter
    def flex_ray_dyn_slot_idl_ph(self, value):
        _props.set_cluster_flex_ray_dyn_slot_idl_ph(self._handle, value)

    @property
    def flex_ray_latest_usable_dyn(self):
        return _props.get_cluster_flex_ray_latest_usable_dyn(self._handle)

    @property
    def flex_ray_latest_guar_dyn(self):
        return _props.get_cluster_flex_ray_latest_guar_dyn(self._handle)

    @property
    def flex_ray_lis_noise(self):
        return _props.get_cluster_flex_ray_lis_noise(self._handle)

    @flex_ray_lis_noise.setter
    def flex_ray_lis_noise(self, value):
        _props.set_cluster_flex_ray_lis_noise(self._handle, value)

    @property
    def flex_ray_macro_per_cycle(self):
        return _props.get_cluster_flex_ray_macro_per_cycle(self._handle)

    @flex_ray_macro_per_cycle.setter
    def flex_ray_macro_per_cycle(self, value):
        _props.set_cluster_flex_ray_macro_per_cycle(self._handle, value)

    @property
    def flex_ray_macrotick(self):
        return _props.get_cluster_flex_ray_macrotick(self._handle)

    @property
    def flex_ray_max_wo_clk_cor_fat(self):
        return _props.get_cluster_flex_ray_max_wo_clk_cor_fat(self._handle)

    @flex_ray_max_wo_clk_cor_fat.setter
    def flex_ray_max_wo_clk_cor_fat(self, value):
        _props.set_cluster_flex_ray_max_wo_clk_cor_fat(self._handle, value)

    @property
    def flex_ray_max_wo_clk_cor_pas(self):
        return _props.get_cluster_flex_ray_max_wo_clk_cor_pas(self._handle)

    @flex_ray_max_wo_clk_cor_pas.setter
    def flex_ray_max_wo_clk_cor_pas(self, value):
        _props.set_cluster_flex_ray_max_wo_clk_cor_pas(self._handle, value)

    @property
    def flex_ray_minislot_act_pt(self):
        return _props.get_cluster_flex_ray_minislot_act_pt(self._handle)

    @flex_ray_minislot_act_pt.setter
    def flex_ray_minislot_act_pt(self, value):
        _props.set_cluster_flex_ray_minislot_act_pt(self._handle, value)

    @property
    def flex_ray_minislot(self):
        return _props.get_cluster_flex_ray_minislot(self._handle)

    @flex_ray_minislot.setter
    def flex_ray_minislot(self, value):
        _props.set_cluster_flex_ray_minislot(self._handle, value)

    @property
    def flex_ray_nm_vec_len(self):
        return _props.get_cluster_flex_ray_nm_vec_len(self._handle)

    @flex_ray_nm_vec_len.setter
    def flex_ray_nm_vec_len(self, value):
        _props.set_cluster_flex_ray_nm_vec_len(self._handle, value)

    @property
    def flex_ray_nit(self):
        return _props.get_cluster_flex_ray_nit(self._handle)

    @flex_ray_nit.setter
    def flex_ray_nit(self, value):
        _props.set_cluster_flex_ray_nit(self._handle, value)

    @property
    def flex_ray_nit_start(self):
        return _props.get_cluster_flex_ray_nit_start(self._handle)

    @property
    def flex_ray_num_minislt(self):
        return _props.get_cluster_flex_ray_num_minislt(self._handle)

    @flex_ray_num_minislt.setter
    def flex_ray_num_minislt(self, value):
        _props.set_cluster_flex_ray_num_minislt(self._handle, value)

    @property
    def flex_ray_num_stat_slt(self):
        return _props.get_cluster_flex_ray_num_stat_slt(self._handle)

    @flex_ray_num_stat_slt.setter
    def flex_ray_num_stat_slt(self, value):
        _props.set_cluster_flex_ray_num_stat_slt(self._handle, value)

    @property
    def flex_ray_off_cor_st(self):
        return _props.get_cluster_flex_ray_off_cor_st(self._handle)

    @flex_ray_off_cor_st.setter
    def flex_ray_off_cor_st(self, value):
        _props.set_cluster_flex_ray_off_cor_st(self._handle, value)

    @property
    def flex_ray_payld_len_dyn_max(self):
        return _props.get_cluster_flex_ray_payld_len_dyn_max(self._handle)

    @flex_ray_payld_len_dyn_max.setter
    def flex_ray_payld_len_dyn_max(self, value):
        _props.set_cluster_flex_ray_payld_len_dyn_max(self._handle, value)

    @property
    def flex_ray_payld_len_max(self):
        return _props.get_cluster_flex_ray_payld_len_max(self._handle)

    @property
    def flex_ray_payld_len_st(self):
        return _props.get_cluster_flex_ray_payld_len_st(self._handle)

    @flex_ray_payld_len_st.setter
    def flex_ray_payld_len_st(self, value):
        _props.set_cluster_flex_ray_payld_len_st(self._handle, value)

    @property
    def flex_ray_stat_slot(self):
        return _props.get_cluster_flex_ray_stat_slot(self._handle)

    @flex_ray_stat_slot.setter
    def flex_ray_stat_slot(self, value):
        _props.set_cluster_flex_ray_stat_slot(self._handle, value)

    @property
    def flex_ray_sym_win(self):
        return _props.get_cluster_flex_ray_sym_win(self._handle)

    @flex_ray_sym_win.setter
    def flex_ray_sym_win(self, value):
        _props.set_cluster_flex_ray_sym_win(self._handle, value)

    @property
    def flex_ray_sym_win_start(self):
        return _props.get_cluster_flex_ray_sym_win_start(self._handle)

    @property
    def flex_ray_sync_node_max(self):
        return _props.get_cluster_flex_ray_sync_node_max(self._handle)

    @flex_ray_sync_node_max.setter
    def flex_ray_sync_node_max(self, value):
        _props.set_cluster_flex_ray_sync_node_max(self._handle, value)

    @property
    def flex_ray_tss_tx(self):
        return _props.get_cluster_flex_ray_tss_tx(self._handle)

    @flex_ray_tss_tx.setter
    def flex_ray_tss_tx(self, value):
        _props.set_cluster_flex_ray_tss_tx(self._handle, value)

    @property
    def flex_ray_wake_sym_rx_idl(self):
        return _props.get_cluster_flex_ray_wake_sym_rx_idl(self._handle)

    @flex_ray_wake_sym_rx_idl.setter
    def flex_ray_wake_sym_rx_idl(self, value):
        _props.set_cluster_flex_ray_wake_sym_rx_idl(self._handle, value)

    @property
    def flex_ray_wake_sym_rx_low(self):
        return _props.get_cluster_flex_ray_wake_sym_rx_low(self._handle)

    @flex_ray_wake_sym_rx_low.setter
    def flex_ray_wake_sym_rx_low(self, value):
        _props.set_cluster_flex_ray_wake_sym_rx_low(self._handle, value)

    @property
    def flex_ray_wake_sym_rx_win(self):
        return _props.get_cluster_flex_ray_wake_sym_rx_win(self._handle)

    @flex_ray_wake_sym_rx_win.setter
    def flex_ray_wake_sym_rx_win(self, value):
        _props.set_cluster_flex_ray_wake_sym_rx_win(self._handle, value)

    @property
    def flex_ray_wake_sym_tx_idl(self):
        return _props.get_cluster_flex_ray_wake_sym_tx_idl(self._handle)

    @flex_ray_wake_sym_tx_idl.setter
    def flex_ray_wake_sym_tx_idl(self, value):
        _props.set_cluster_flex_ray_wake_sym_tx_idl(self._handle, value)

    @property
    def flex_ray_wake_sym_tx_low(self):
        return _props.get_cluster_flex_ray_wake_sym_tx_low(self._handle)

    @flex_ray_wake_sym_tx_low.setter
    def flex_ray_wake_sym_tx_low(self, value):
        _props.set_cluster_flex_ray_wake_sym_tx_low(self._handle, value)

    @property
    def flex_ray_use_wakeup(self):
        return _props.get_cluster_flex_ray_use_wakeup(self._handle)

    @flex_ray_use_wakeup.setter
    def flex_ray_use_wakeup(self, value):
        _props.set_cluster_flex_ray_use_wakeup(self._handle, value)

    @property
    def lin_schedules(self):
        return _props.get_cluster_lin_schedules(self._handle)

    @property
    def lin_tick(self):
        return _props.get_cluster_lin_tick(self._handle)

    @lin_tick.setter
    def lin_tick(self, value):
        _props.set_cluster_lin_tick(self._handle, value)

    @property
    def flex_ray_alw_pass_act(self):
        return _props.get_cluster_flex_ray_alw_pass_act(self._handle)

    @flex_ray_alw_pass_act.setter
    def flex_ray_alw_pass_act(self, value):
        _props.set_cluster_flex_ray_alw_pass_act(self._handle, value)

    @property
    def application_protocol(self):
        return constants.AppProtocol(_props.get_cluster_application_protocol(self._handle))

    @application_protocol.setter
    def application_protocol(self, value):
        _props.set_cluster_application_protocol(self._handle, value.value)

    @property
    def can_fd_iso_mode(self):
        return constants.CanFdIsoMode(_props.get_cluster_can_fd_iso_mode(self._handle))
