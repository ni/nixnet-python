from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _cprops


def get_session_application_protocol(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_APPLICATION_PROTOCOL,
    )


def get_session_auto_start(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_AUTO_START,
    )


def set_session_auto_start(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_AUTO_START,
        value,
    )


def get_session_cluster_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_session_string(
        ref,
        _cconsts.NX_PROP_SESSION_CLUSTER_NAME,
    )


def get_session_database_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_session_string(
        ref,
        _cconsts.NX_PROP_SESSION_DATABASE_NAME,
    )


def get_session_list(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_session_string_array(
        ref,
        _cconsts.NX_PROP_SESSION_LIST,
    )


def get_session_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_MODE,
    )


def get_session_num_frames(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_NUM_FRAMES,
    )


def get_session_num_in_list(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_NUM_IN_LIST,
    )


def get_session_num_pend(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_NUM_PEND,
    )


def get_session_num_unused(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_NUM_UNUSED,
    )


def get_session_payld_len_max(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_PAYLD_LEN_MAX,
    )


def get_session_protocol(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_PROTOCOL,
    )


def get_session_queue_size(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_QUEUE_SIZE,
    )


def set_session_queue_size(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_QUEUE_SIZE,
        value,
    )


def get_session_resamp_rate(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_RESAMP_RATE,
    )


def set_session_resamp_rate(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_RESAMP_RATE,
        value,
    )


def get_session_intf_baud_rate(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_BAUD_RATE,
    )


def set_session_intf_baud_rate(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_BAUD_RATE,
        value,
    )


def get_session_intf_baud_rate64(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_BAUD_RATE64,
    )


def set_session_intf_baud_rate64(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_BAUD_RATE64,
        value,
    )


def get_session_intf_bus_err_to_in_strm(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_BUS_ERR_TO_IN_STRM,
    )


def set_session_intf_bus_err_to_in_strm(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_BUS_ERR_TO_IN_STRM,
        value,
    )


def get_session_intf_echo_tx(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_ECHO_TX,
    )


def set_session_intf_echo_tx(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_ECHO_TX,
        value,
    )


def get_session_intf_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_session_string(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_NAME,
    )


def get_session_intf_out_strm_list(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_OUT_STRM_LIST,
    )


def set_session_intf_out_strm_list(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_session_ref_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_OUT_STRM_LIST,
        value,
    )


def get_session_intf_out_strm_timng(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_OUT_STRM_TIMNG,
    )


def set_session_intf_out_strm_timng(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_OUT_STRM_TIMNG,
        value,
    )


def get_session_intf_start_trig_to_in_strm(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_START_TRIG_TO_IN_STRM,
    )


def set_session_intf_start_trig_to_in_strm(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_START_TRIG_TO_IN_STRM,
        value,
    )


def set_session_intf_can_ext_tcvr_config(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_EXT_TCVR_CONFIG,
        value,
    )


def get_session_intf_can_lstn_only(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_LSTN_ONLY,
    )


def set_session_intf_can_lstn_only(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_LSTN_ONLY,
        value,
    )


def get_session_intf_can_pend_tx_order(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_PEND_TX_ORDER,
    )


def set_session_intf_can_pend_tx_order(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_PEND_TX_ORDER,
        value,
    )


def get_session_intf_can_sing_shot(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_SING_SHOT,
    )


def set_session_intf_can_sing_shot(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_SING_SHOT,
        value,
    )


def get_session_intf_can_term(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TERM,
    )


def set_session_intf_can_term(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TERM,
        value,
    )


def get_session_intf_can_tcvr_state(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TCVR_STATE,
    )


def set_session_intf_can_tcvr_state(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TCVR_STATE,
        value,
    )


def get_session_intf_can_tcvr_type(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TCVR_TYPE,
    )


def set_session_intf_can_tcvr_type(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TCVR_TYPE,
        value,
    )


def get_session_intf_can_out_strm_list_by_id(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_OUT_STRM_LIST_BY_ID,
    )


def set_session_intf_can_out_strm_list_by_id(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_OUT_STRM_LIST_BY_ID,
        value,
    )


def get_session_intf_can_io_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_IO_MODE,
    )


def get_session_intf_can_fd_baud_rate(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_FD_BAUD_RATE,
    )


def set_session_intf_can_fd_baud_rate(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_FD_BAUD_RATE,
        value,
    )


def get_session_intf_can_fd_baud_rate64(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_FD_BAUD_RATE64,
    )


def set_session_intf_can_fd_baud_rate64(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_FD_BAUD_RATE64,
        value,
    )


def get_session_intf_can_tx_io_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TX_IO_MODE,
    )


def set_session_intf_can_tx_io_mode(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TX_IO_MODE,
        value,
    )


def get_session_intf_can_fd_iso_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_FD_ISO_MODE,
    )


def set_session_intf_can_fd_iso_mode(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_FD_ISO_MODE,
        value,
    )


def get_session_intf_flex_ray_acc_start_rng(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_ACC_START_RNG,
    )


def set_session_intf_flex_ray_acc_start_rng(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_ACC_START_RNG,
        value,
    )


def get_session_intf_flex_ray_alw_hlt_clk(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_ALW_HLT_CLK,
    )


def set_session_intf_flex_ray_alw_hlt_clk(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_ALW_HLT_CLK,
        value,
    )


def get_session_intf_flex_ray_alw_pass_act(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_ALW_PASS_ACT,
    )


def set_session_intf_flex_ray_alw_pass_act(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_ALW_PASS_ACT,
        value,
    )


def get_session_intf_flex_ray_auto_aslp_whn_stp(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_AUTO_ASLP_WHN_STP,
    )


def set_session_intf_flex_ray_auto_aslp_whn_stp(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_AUTO_ASLP_WHN_STP,
        value,
    )


def get_session_intf_flex_ray_clst_drift_dmp(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_CLST_DRIFT_DMP,
    )


def set_session_intf_flex_ray_clst_drift_dmp(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_CLST_DRIFT_DMP,
        value,
    )


def get_session_intf_flex_ray_coldstart(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_COLDSTART,
    )


def get_session_intf_flex_ray_dec_corr(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_DEC_CORR,
    )


def set_session_intf_flex_ray_dec_corr(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_DEC_CORR,
        value,
    )


def get_session_intf_flex_ray_delay_comp_a(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_DELAY_COMP_A,
    )


def set_session_intf_flex_ray_delay_comp_a(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_DELAY_COMP_A,
        value,
    )


def get_session_intf_flex_ray_delay_comp_b(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_DELAY_COMP_B,
    )


def set_session_intf_flex_ray_delay_comp_b(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_DELAY_COMP_B,
        value,
    )


def get_session_intf_flex_ray_key_slot_id(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_KEY_SLOT_ID,
    )


def set_session_intf_flex_ray_key_slot_id(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_KEY_SLOT_ID,
        value,
    )


def get_session_intf_flex_ray_latest_tx(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_LATEST_TX,
    )


def get_session_intf_flex_ray_list_timo(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_LIST_TIMO,
    )


def set_session_intf_flex_ray_list_timo(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_LIST_TIMO,
        value,
    )


def get_session_intf_flex_ray_mac_init_off_a(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MAC_INIT_OFF_A,
    )


def set_session_intf_flex_ray_mac_init_off_a(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MAC_INIT_OFF_A,
        value,
    )


def get_session_intf_flex_ray_mac_init_off_b(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MAC_INIT_OFF_B,
    )


def set_session_intf_flex_ray_mac_init_off_b(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MAC_INIT_OFF_B,
        value,
    )


def get_session_intf_flex_ray_mic_init_off_a(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MIC_INIT_OFF_A,
    )


def set_session_intf_flex_ray_mic_init_off_a(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MIC_INIT_OFF_A,
        value,
    )


def get_session_intf_flex_ray_mic_init_off_b(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MIC_INIT_OFF_B,
    )


def set_session_intf_flex_ray_mic_init_off_b(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MIC_INIT_OFF_B,
        value,
    )


def get_session_intf_flex_ray_max_drift(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MAX_DRIFT,
    )


def set_session_intf_flex_ray_max_drift(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MAX_DRIFT,
        value,
    )


def get_session_intf_flex_ray_microtick(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_MICROTICK,
    )


def get_session_intf_flex_ray_null_to_in_strm(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_NULL_TO_IN_STRM,
    )


def set_session_intf_flex_ray_null_to_in_strm(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_NULL_TO_IN_STRM,
        value,
    )


def get_session_intf_flex_ray_off_corr(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_OFF_CORR,
    )


def get_session_intf_flex_ray_off_corr_out(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_OFF_CORR_OUT,
    )


def set_session_intf_flex_ray_off_corr_out(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_OFF_CORR_OUT,
        value,
    )


def get_session_intf_flex_ray_rate_corr(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_RATE_CORR,
    )


def get_session_intf_flex_ray_rate_corr_out(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_RATE_CORR_OUT,
    )


def set_session_intf_flex_ray_rate_corr_out(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_RATE_CORR_OUT,
        value,
    )


def get_session_intf_flex_ray_samp_per_micro(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SAMP_PER_MICRO,
    )


def set_session_intf_flex_ray_samp_per_micro(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SAMP_PER_MICRO,
        value,
    )


def get_session_intf_flex_ray_sing_slot_en(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SING_SLOT_EN,
    )


def set_session_intf_flex_ray_sing_slot_en(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SING_SLOT_EN,
        value,
    )


def get_session_intf_flex_ray_statistics_en(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_STATISTICS_EN,
    )


def set_session_intf_flex_ray_statistics_en(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_STATISTICS_EN,
        value,
    )


def get_session_intf_flex_ray_sym_to_in_strm(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SYM_TO_IN_STRM,
    )


def set_session_intf_flex_ray_sym_to_in_strm(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SYM_TO_IN_STRM,
        value,
    )


def get_session_intf_flex_ray_sync_ch_a_even(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_CH_A_EVEN,
    )


def get_session_intf_flex_ray_sync_ch_a_odd(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_CH_A_ODD,
    )


def get_session_intf_flex_ray_sync_ch_b_even(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_CH_B_EVEN,
    )


def get_session_intf_flex_ray_sync_ch_b_odd(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_CH_B_ODD,
    )


def get_session_intf_flex_ray_sync_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SYNC_STATUS,
    )


def get_session_intf_flex_ray_term(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_TERM,
    )


def set_session_intf_flex_ray_term(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_TERM,
        value,
    )


def get_session_intf_flex_ray_wakeup_ch(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_WAKEUP_CH,
    )


def set_session_intf_flex_ray_wakeup_ch(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_WAKEUP_CH,
        value,
    )


def get_session_intf_flex_ray_wakeup_ptrn(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_WAKEUP_PTRN,
    )


def set_session_intf_flex_ray_wakeup_ptrn(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_WAKEUP_PTRN,
        value,
    )


def set_session_intf_flex_ray_sleep(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_SLEEP,
        value,
    )


def get_session_intf_flex_ray_connected_chs(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_CONNECTED_CHS,
    )


def set_session_intf_flex_ray_connected_chs(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_FLEX_RAY_CONNECTED_CHS,
        value,
    )


def get_session_intf_lin_break_length(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_BREAK_LENGTH,
    )


def set_session_intf_lin_break_length(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_BREAK_LENGTH,
        value,
    )


def get_session_intf_lin_master(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_MASTER,
    )


def set_session_intf_lin_master(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_MASTER,
        value,
    )


def get_session_intf_lin_sched_names(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_session_string_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_SCHED_NAMES,
    )


def set_session_intf_lin_sleep(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_SLEEP,
        value,
    )


def get_session_intf_lin_term(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_TERM,
    )


def set_session_intf_lin_term(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_TERM,
        value,
    )


def get_session_intf_lin_diag_p_2min(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_DIAG_P_2MIN,
    )


def set_session_intf_lin_diag_p_2min(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_DIAG_P_2MIN,
        value,
    )


def get_session_intf_lin_diag_s_tmin(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_DIAG_S_TMIN,
    )


def set_session_intf_lin_diag_s_tmin(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_DIAG_S_TMIN,
        value,
    )


def get_session_intf_lin_alw_start_wo_bus_pwr(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_ALW_START_WO_BUS_PWR,
    )


def set_session_intf_lin_alw_start_wo_bus_pwr(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_ALW_START_WO_BUS_PWR,
        value,
    )


def get_session_intf_lino_str_slv_rsp_lst_by_nad(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LINO_STR_SLV_RSP_LST_BY_NAD,
    )


def set_session_intf_lino_str_slv_rsp_lst_by_nad(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_session_u32_array(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LINO_STR_SLV_RSP_LST_BY_NAD,
        value,
    )


def get_session_intf_lin_no_response_to_in_strm(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_NO_RESPONSE_TO_IN_STRM,
    )


def set_session_intf_lin_no_response_to_in_strm(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_LIN_NO_RESPONSE_TO_IN_STRM,
        value,
    )


def get_session_intf_src_term_start_trigger(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_session_string(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_SRC_TERM_START_TRIGGER,
    )


def set_session_intf_src_term_start_trigger(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_session_string(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_SRC_TERM_START_TRIGGER,
        value,
    )


def get_session_j1939_address(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_ADDRESS,
    )


def set_session_j1939_address(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_ADDRESS,
        value,
    )


def get_session_j1939_name(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_NAME,
    )


def set_session_j1939_name(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_NAME,
        value,
    )


def set_session_j1939ecu(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_ref(
        ref,
        _cconsts.NX_PROP_SESSION_J1939ECU,
        value,
    )


def get_session_j1939_timeout_t1(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T1,
    )


def set_session_j1939_timeout_t1(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T1,
        value,
    )


def get_session_j1939_timeout_t2(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T2,
    )


def set_session_j1939_timeout_t2(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T2,
        value,
    )


def get_session_j1939_timeout_t3(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T3,
    )


def set_session_j1939_timeout_t3(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T3,
        value,
    )


def get_session_j1939_timeout_t4(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T4,
    )


def set_session_j1939_timeout_t4(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_TIMEOUT_T4,
        value,
    )


def get_session_j1939_response_time_tr_sd(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_RESPONSE_TIME_TR_SD,
    )


def set_session_j1939_response_time_tr_sd(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_RESPONSE_TIME_TR_SD,
        value,
    )


def get_session_j1939_response_time_tr_gd(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_RESPONSE_TIME_TR_GD,
    )


def set_session_j1939_response_time_tr_gd(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_RESPONSE_TIME_TR_GD,
        value,
    )


def get_session_j1939_hold_time_th(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_HOLD_TIME_TH,
    )


def set_session_j1939_hold_time_th(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_HOLD_TIME_TH,
        value,
    )


def get_session_j1939_num_packets_recv(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_NUM_PACKETS_RECV,
    )


def set_session_j1939_num_packets_recv(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_NUM_PACKETS_RECV,
        value,
    )


def get_session_j1939_num_packets_resp(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_NUM_PACKETS_RESP,
    )


def set_session_j1939_num_packets_resp(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_NUM_PACKETS_RESP,
        value,
    )


def get_session_j1939_max_repeat_cts(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_MAX_REPEAT_CTS,
    )


def set_session_j1939_max_repeat_cts(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_MAX_REPEAT_CTS,
        value,
    )


def get_session_j1939_fill_byte(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_FILL_BYTE,
    )


def set_session_j1939_fill_byte(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_FILL_BYTE,
        value,
    )


def get_session_j1939_write_queue_size(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_WRITE_QUEUE_SIZE,
    )


def set_session_j1939_write_queue_size(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_u32(
        ref,
        _cconsts.NX_PROP_SESSION_J1939_WRITE_QUEUE_SIZE,
        value,
    )


def get_session_j1939ecu_busy(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_J1939ECU_BUSY,
    )


def set_session_j1939ecu_busy(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_J1939ECU_BUSY,
        value,
    )


def get_session_intf_can_edge_filter(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_EDGE_FILTER,
    )


def set_session_intf_can_edge_filter(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_EDGE_FILTER,
        value,
    )


def get_session_intf_can_transmit_pause(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TRANSMIT_PAUSE,
    )


def set_session_intf_can_transmit_pause(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_TRANSMIT_PAUSE,
        value,
    )


def get_session_intf_can_disable_prot_exception_handling(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_DISABLE_PROT_EXCEPTION_HANDLING,
    )


def set_session_intf_can_disable_prot_exception_handling(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_session_bool(
        ref,
        _cconsts.NX_PROP_SESSION_INTF_CAN_DISABLE_PROT_EXCEPTION_HANDLING,
        value,
    )


def set_session_can_start_time_off(
    ref,  # type: int
    sub,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_sub_f64(
        ref,
        sub,
        _cconsts.NX_PROP_SESSION_SUB_CAN_START_TIME_OFF,
        value,
    )


def set_session_can_tx_time(
    ref,  # type: int
    sub,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_sub_f64(
        ref,
        sub,
        _cconsts.NX_PROP_SESSION_SUB_CAN_TX_TIME,
        value,
    )


def set_session_skip_n_cyclic_frames(
    ref,  # type: int
    sub,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_sub_u32(
        ref,
        sub,
        _cconsts.NX_PROP_SESSION_SUB_SKIP_N_CYCLIC_FRAMES,
        value,
    )


def set_session_output_queue_update_freq(
    ref,  # type: int
    sub,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_sub_u32(
        ref,
        sub,
        _cconsts.NX_PROP_SESSION_SUB_OUTPUT_QUEUE_UPDATE_FREQ,
        value,
    )


def set_session_lin_tx_n_corrupted_chksums(
    ref,  # type: int
    sub,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_session_sub_u32(
        ref,
        sub,
        _cconsts.NX_PROP_SESSION_SUB_LIN_TX_N_CORRUPTED_CHKSUMS,
        value,
    )


def set_session_j1939_addr_filter(
    ref,  # type: int
    sub,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_session_sub_string(
        ref,
        sub,
        _cconsts.NX_PROP_SESSION_SUB_J1939_ADDR_FILTER,
        value,
    )


def get_system_dev_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_SYS_DEV_REFS,
    )


def get_system_intf_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_SYS_INTF_REFS,
    )


def get_system_intf_refs_can(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_SYS_INTF_REFS_CAN,
    )


def get_system_intf_refs_flex_ray(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_SYS_INTF_REFS_FLEX_RAY,
    )


def get_system_intf_refs_lin(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_SYS_INTF_REFS_LIN,
    )


def get_system_ver_build(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SYS_VER_BUILD,
    )


def get_system_ver_major(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SYS_VER_MAJOR,
    )


def get_system_ver_minor(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SYS_VER_MINOR,
    )


def get_system_ver_phase(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SYS_VER_PHASE,
    )


def get_system_ver_update(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_SYS_VER_UPDATE,
    )


def get_system_cdaq_pkt_time(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_session_f64(
        ref,
        _cconsts.NX_PROP_SYS_CDAQ_PKT_TIME,
    )


def set_system_cdaq_pkt_time(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_session_f64(
        ref,
        _cconsts.NX_PROP_SYS_CDAQ_PKT_TIME,
        value,
    )


def get_system_intf_refs_all(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_SYS_INTF_REFS_ALL,
    )


def get_device_form_fac(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_DEV_FORM_FAC,
    )


def get_device_intf_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_DEV_INTF_REFS,
    )


def get_device_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_session_string(
        ref,
        _cconsts.NX_PROP_DEV_NAME,
    )


def get_device_num_ports(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_DEV_NUM_PORTS,
    )


def get_device_product_num(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_DEV_PRODUCT_NUM,
    )


def get_device_ser_num(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_DEV_SER_NUM,
    )


def get_device_slot_num(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_DEV_SLOT_NUM,
    )


def get_device_num_ports_all(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_DEV_NUM_PORTS_ALL,
    )


def get_device_intf_refs_all(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_session_ref_array(
        ref,
        _cconsts.NX_PROP_DEV_INTF_REFS_ALL,
    )


def get_interface_dev_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_ref(
        ref,
        _cconsts.NX_PROP_INTF_DEV_REF,
    )


def get_interface_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_session_string(
        ref,
        _cconsts.NX_PROP_INTF_NAME,
    )


def get_interface_num(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_NUM,
    )


def get_interface_port_num(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_PORT_NUM,
    )


def get_interface_protocol(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_PROTOCOL,
    )


def get_interface_can_term_cap(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_CAN_TERM_CAP,
    )


def get_interface_can_tcvr_cap(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_CAN_TCVR_CAP,
    )


def get_interface_dongle_state(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_DONGLE_STATE,
    )


def get_interface_dongle_id(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_DONGLE_ID,
    )


def get_interface_dongle_revision(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_DONGLE_REVISION,
    )


def get_interface_dongle_firmware_version(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_DONGLE_FIRMWARE_VERSION,
    )


def get_interface_dongle_compatible_revision(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_DONGLE_COMPATIBLE_REVISION,
    )


def get_interface_dongle_compatible_firmware_version(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_session_u32(
        ref,
        _cconsts.NX_PROP_INTF_DONGLE_COMPATIBLE_FIRMWARE_VERSION,
    )


def get_database_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_DATABASE_NAME,
    )


def get_database_clst_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_DATABASE_CLST_REFS,
    )


def get_database_show_invalid_from_open(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_DATABASE_SHOW_INVALID_FROM_OPEN,
    )


def set_database_show_invalid_from_open(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_DATABASE_SHOW_INVALID_FROM_OPEN,
        value,
    )


def get_cluster_baud_rate(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_BAUD_RATE,
    )


def set_cluster_baud_rate(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_BAUD_RATE,
        value,
    )


def get_cluster_baud_rate64(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u64(
        ref,
        _cconsts.NX_PROP_CLST_BAUD_RATE64,
    )


def set_cluster_baud_rate64(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u64(
        ref,
        _cconsts.NX_PROP_CLST_BAUD_RATE64,
        value,
    )


def get_cluster_comment(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_CLST_COMMENT,
    )


def set_cluster_comment(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_CLST_COMMENT,
        value,
    )


def get_cluster_config_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_CONFIG_STATUS,
    )


def get_cluster_database_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_CLST_DATABASE_REF,
    )


def get_cluster_ecu_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_CLST_ECU_REFS,
    )


def get_cluster_frm_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_CLST_FRM_REFS,
    )


def get_cluster_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_CLST_NAME,
    )


def set_cluster_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_CLST_NAME,
        value,
    )


def get_cluster_pdu_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_CLST_PDU_REFS,
    )


def get_cluster_pd_us_reqd(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_CLST_PD_US_REQD,
    )


def get_cluster_protocol(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_PROTOCOL,
    )


def set_cluster_protocol(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_PROTOCOL,
        value,
    )


def get_cluster_sig_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_CLST_SIG_REFS,
    )


def get_cluster_can_io_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_CAN_IO_MODE,
    )


def set_cluster_can_io_mode(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_CAN_IO_MODE,
        value,
    )


def get_cluster_can_fd_baud_rate(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_CAN_FD_BAUD_RATE,
    )


def set_cluster_can_fd_baud_rate(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_CAN_FD_BAUD_RATE,
        value,
    )


def get_cluster_can_fd_baud_rate64(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u64(
        ref,
        _cconsts.NX_PROP_CLST_CAN_FD_BAUD_RATE64,
    )


def set_cluster_can_fd_baud_rate64(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u64(
        ref,
        _cconsts.NX_PROP_CLST_CAN_FD_BAUD_RATE64,
        value,
    )


def get_cluster_flex_ray_act_pt_off(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_ACT_PT_OFF,
    )


def set_cluster_flex_ray_act_pt_off(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_ACT_PT_OFF,
        value,
    )


def get_cluster_flex_ray_cas_rx_l_max(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CAS_RX_L_MAX,
    )


def set_cluster_flex_ray_cas_rx_l_max(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CAS_RX_L_MAX,
        value,
    )


def get_cluster_flex_ray_channels(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CHANNELS,
    )


def set_cluster_flex_ray_channels(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CHANNELS,
        value,
    )


def get_cluster_flex_ray_clst_drift_dmp(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CLST_DRIFT_DMP,
    )


def set_cluster_flex_ray_clst_drift_dmp(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CLST_DRIFT_DMP,
        value,
    )


def get_cluster_flex_ray_cold_st_ats(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_COLD_ST_ATS,
    )


def set_cluster_flex_ray_cold_st_ats(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_COLD_ST_ATS,
        value,
    )


def get_cluster_flex_ray_cycle(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CYCLE,
    )


def set_cluster_flex_ray_cycle(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_CYCLE,
        value,
    )


def get_cluster_flex_ray_dyn_seg_start(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_DYN_SEG_START,
    )


def get_cluster_flex_ray_dyn_slot_idl_ph(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_DYN_SLOT_IDL_PH,
    )


def set_cluster_flex_ray_dyn_slot_idl_ph(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_DYN_SLOT_IDL_PH,
        value,
    )


def get_cluster_flex_ray_latest_usable_dyn(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_LATEST_USABLE_DYN,
    )


def get_cluster_flex_ray_latest_guar_dyn(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_LATEST_GUAR_DYN,
    )


def get_cluster_flex_ray_lis_noise(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_LIS_NOISE,
    )


def set_cluster_flex_ray_lis_noise(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_LIS_NOISE,
        value,
    )


def get_cluster_flex_ray_macro_per_cycle(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MACRO_PER_CYCLE,
    )


def set_cluster_flex_ray_macro_per_cycle(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MACRO_PER_CYCLE,
        value,
    )


def get_cluster_flex_ray_macrotick(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MACROTICK,
    )


def get_cluster_flex_ray_max_wo_clk_cor_fat(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MAX_WO_CLK_COR_FAT,
    )


def set_cluster_flex_ray_max_wo_clk_cor_fat(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MAX_WO_CLK_COR_FAT,
        value,
    )


def get_cluster_flex_ray_max_wo_clk_cor_pas(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MAX_WO_CLK_COR_PAS,
    )


def set_cluster_flex_ray_max_wo_clk_cor_pas(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MAX_WO_CLK_COR_PAS,
        value,
    )


def get_cluster_flex_ray_minislot_act_pt(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MINISLOT_ACT_PT,
    )


def set_cluster_flex_ray_minislot_act_pt(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MINISLOT_ACT_PT,
        value,
    )


def get_cluster_flex_ray_minislot(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MINISLOT,
    )


def set_cluster_flex_ray_minislot(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_MINISLOT,
        value,
    )


def get_cluster_flex_ray_nm_vec_len(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NM_VEC_LEN,
    )


def set_cluster_flex_ray_nm_vec_len(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NM_VEC_LEN,
        value,
    )


def get_cluster_flex_ray_nit(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NIT,
    )


def set_cluster_flex_ray_nit(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NIT,
        value,
    )


def get_cluster_flex_ray_nit_start(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NIT_START,
    )


def get_cluster_flex_ray_num_minislt(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NUM_MINISLT,
    )


def set_cluster_flex_ray_num_minislt(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NUM_MINISLT,
        value,
    )


def get_cluster_flex_ray_num_stat_slt(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NUM_STAT_SLT,
    )


def set_cluster_flex_ray_num_stat_slt(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_NUM_STAT_SLT,
        value,
    )


def get_cluster_flex_ray_off_cor_st(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_OFF_COR_ST,
    )


def set_cluster_flex_ray_off_cor_st(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_OFF_COR_ST,
        value,
    )


def get_cluster_flex_ray_payld_len_dyn_max(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_PAYLD_LEN_DYN_MAX,
    )


def set_cluster_flex_ray_payld_len_dyn_max(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_PAYLD_LEN_DYN_MAX,
        value,
    )


def get_cluster_flex_ray_payld_len_max(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_PAYLD_LEN_MAX,
    )


def get_cluster_flex_ray_payld_len_st(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_PAYLD_LEN_ST,
    )


def set_cluster_flex_ray_payld_len_st(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_PAYLD_LEN_ST,
        value,
    )


def get_cluster_flex_ray_stat_slot(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_STAT_SLOT,
    )


def set_cluster_flex_ray_stat_slot(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_STAT_SLOT,
        value,
    )


def get_cluster_flex_ray_sym_win(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_SYM_WIN,
    )


def set_cluster_flex_ray_sym_win(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_SYM_WIN,
        value,
    )


def get_cluster_flex_ray_sym_win_start(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_SYM_WIN_START,
    )


def get_cluster_flex_ray_sync_node_max(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_SYNC_NODE_MAX,
    )


def set_cluster_flex_ray_sync_node_max(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_SYNC_NODE_MAX,
        value,
    )


def get_cluster_flex_ray_tss_tx(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_TSS_TX,
    )


def set_cluster_flex_ray_tss_tx(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_TSS_TX,
        value,
    )


def get_cluster_flex_ray_wake_sym_rx_idl(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_IDL,
    )


def set_cluster_flex_ray_wake_sym_rx_idl(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_IDL,
        value,
    )


def get_cluster_flex_ray_wake_sym_rx_low(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_LOW,
    )


def set_cluster_flex_ray_wake_sym_rx_low(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_LOW,
        value,
    )


def get_cluster_flex_ray_wake_sym_rx_win(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_WIN,
    )


def set_cluster_flex_ray_wake_sym_rx_win(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_RX_WIN,
        value,
    )


def get_cluster_flex_ray_wake_sym_tx_idl(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_TX_IDL,
    )


def set_cluster_flex_ray_wake_sym_tx_idl(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_TX_IDL,
        value,
    )


def get_cluster_flex_ray_wake_sym_tx_low(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_TX_LOW,
    )


def set_cluster_flex_ray_wake_sym_tx_low(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_WAKE_SYM_TX_LOW,
        value,
    )


def get_cluster_flex_ray_use_wakeup(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_USE_WAKEUP,
    )


def set_cluster_flex_ray_use_wakeup(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_USE_WAKEUP,
        value,
    )


def get_cluster_lin_schedules(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_CLST_LIN_SCHEDULES,
    )


def get_cluster_lin_tick(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_CLST_LIN_TICK,
    )


def set_cluster_lin_tick(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_CLST_LIN_TICK,
        value,
    )


def get_cluster_flex_ray_alw_pass_act(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_ALW_PASS_ACT,
    )


def set_cluster_flex_ray_alw_pass_act(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_FLEX_RAY_ALW_PASS_ACT,
        value,
    )


def get_cluster_application_protocol(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_APPLICATION_PROTOCOL,
    )


def set_cluster_application_protocol(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_APPLICATION_PROTOCOL,
        value,
    )


def get_cluster_can_fd_iso_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_CLST_CAN_FD_ISO_MODE,
    )


def get_frame_application_protocol(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_APPLICATION_PROTOCOL,
    )


def set_frame_application_protocol(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_APPLICATION_PROTOCOL,
        value,
    )


def get_frame_cluster_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_FRM_CLUSTER_REF,
    )


def get_frame_comment(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_FRM_COMMENT,
    )


def set_frame_comment(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_FRM_COMMENT,
        value,
    )


def get_frame_config_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_CONFIG_STATUS,
    )


def get_frame_default_payload(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_u8_array(
        ref,
        _cconsts.NX_PROP_FRM_DEFAULT_PAYLOAD,
    )


def set_frame_default_payload(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_u8_array(
        ref,
        _cconsts.NX_PROP_FRM_DEFAULT_PAYLOAD,
        value,
    )


def get_frame_id(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_ID,
    )


def set_frame_id(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_ID,
        value,
    )


def get_frame_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_FRM_NAME,
    )


def set_frame_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_FRM_NAME,
        value,
    )


def get_frame_payload_len(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_PAYLOAD_LEN,
    )


def set_frame_payload_len(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_PAYLOAD_LEN,
        value,
    )


def get_frame_sig_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_FRM_SIG_REFS,
    )


def get_frame_can_ext_id(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_CAN_EXT_ID,
    )


def set_frame_can_ext_id(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_CAN_EXT_ID,
        value,
    )


def get_frame_can_timing_type(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_CAN_TIMING_TYPE,
    )


def set_frame_can_timing_type(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_CAN_TIMING_TYPE,
        value,
    )


def get_frame_can_tx_time(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_FRM_CAN_TX_TIME,
    )


def set_frame_can_tx_time(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_FRM_CAN_TX_TIME,
        value,
    )


def get_frame_flex_ray_base_cycle(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_BASE_CYCLE,
    )


def set_frame_flex_ray_base_cycle(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_BASE_CYCLE,
        value,
    )


def get_frame_flex_ray_ch_assign(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_CH_ASSIGN,
    )


def set_frame_flex_ray_ch_assign(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_CH_ASSIGN,
        value,
    )


def get_frame_flex_ray_cycle_rep(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_CYCLE_REP,
    )


def set_frame_flex_ray_cycle_rep(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_CYCLE_REP,
        value,
    )


def get_frame_flex_ray_preamble(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_PREAMBLE,
    )


def set_frame_flex_ray_preamble(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_PREAMBLE,
        value,
    )


def get_frame_flex_ray_startup(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_STARTUP,
    )


def set_frame_flex_ray_startup(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_STARTUP,
        value,
    )


def get_frame_flex_ray_sync(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_SYNC,
    )


def set_frame_flex_ray_sync(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_SYNC,
        value,
    )


def get_frame_flex_ray_timing_type(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_TIMING_TYPE,
    )


def set_frame_flex_ray_timing_type(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_TIMING_TYPE,
        value,
    )


def get_frame_flex_ray_in_cyc_rep_enabled(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_IN_CYC_REP_ENABLED,
    )


def get_frame_flex_ray_in_cyc_rep_i_ds(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_IN_CYC_REP_I_DS,
    )


def set_frame_flex_ray_in_cyc_rep_i_ds(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_IN_CYC_REP_I_DS,
        value,
    )


def get_frame_flex_ray_in_cyc_rep_ch_assigns(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_IN_CYC_REP_CH_ASSIGNS,
    )


def set_frame_flex_ray_in_cyc_rep_ch_assigns(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_FLEX_RAY_IN_CYC_REP_CH_ASSIGNS,
        value,
    )


def get_frame_lin_checksum(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_LIN_CHECKSUM,
    )


def get_frame_mux_is_muxed(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_MUX_IS_MUXED,
    )


def get_frame_mux_data_mux_sig_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_FRM_MUX_DATA_MUX_SIG_REF,
    )


def get_frame_mux_static_sig_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_FRM_MUX_STATIC_SIG_REFS,
    )


def get_frame_mux_subframe_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_FRM_MUX_SUBFRAME_REFS,
    )


def get_frame_pdu_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_FRM_PDU_REFS,
    )


def set_frame_pdu_refs(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_ref_array(
        ref,
        _cconsts.NX_PROP_FRM_PDU_REFS,
        value,
    )


def get_frame_pdu_start_bits(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_PDU_START_BITS,
    )


def set_frame_pdu_start_bits(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_PDU_START_BITS,
        value,
    )


def get_frame_pdu_update_bits(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_PDU_UPDATE_BITS,
    )


def set_frame_pdu_update_bits(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_u32_array(
        ref,
        _cconsts.NX_PROP_FRM_PDU_UPDATE_BITS,
        value,
    )


def get_frame_variable_payload(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_VARIABLE_PAYLOAD,
    )


def set_frame_variable_payload(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_FRM_VARIABLE_PAYLOAD,
        value,
    )


def get_frame_ca_nio_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_CA_NIO_MODE,
    )


def set_frame_ca_nio_mode(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_FRM_CA_NIO_MODE,
        value,
    )


def get_pdu_cluster_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_PDU_CLUSTER_REF,
    )


def get_pdu_default_payload(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_u8_array(
        ref,
        _cconsts.NX_PROP_PDU_DEFAULT_PAYLOAD,
    )


def set_pdu_default_payload(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_u8_array(
        ref,
        _cconsts.NX_PROP_PDU_DEFAULT_PAYLOAD,
        value,
    )


def get_pdu_comment(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_PDU_COMMENT,
    )


def set_pdu_comment(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_PDU_COMMENT,
        value,
    )


def get_pdu_config_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_PDU_CONFIG_STATUS,
    )


def get_pdu_frm_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_PDU_FRM_REFS,
    )


def get_pdu_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_PDU_NAME,
    )


def set_pdu_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_PDU_NAME,
        value,
    )


def get_pdu_payload_len(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_PDU_PAYLOAD_LEN,
    )


def set_pdu_payload_len(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_PDU_PAYLOAD_LEN,
        value,
    )


def get_pdu_sig_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_PDU_SIG_REFS,
    )


def get_pdu_mux_is_muxed(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_PDU_MUX_IS_MUXED,
    )


def get_pdu_mux_data_mux_sig_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_PDU_MUX_DATA_MUX_SIG_REF,
    )


def get_pdu_mux_static_sig_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_PDU_MUX_STATIC_SIG_REFS,
    )


def get_pdu_mux_subframe_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_PDU_MUX_SUBFRAME_REFS,
    )


def get_signal_byte_ordr(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_BYTE_ORDR,
    )


def set_signal_byte_ordr(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_BYTE_ORDR,
        value,
    )


def get_signal_comment(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_SIG_COMMENT,
    )


def set_signal_comment(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_SIG_COMMENT,
        value,
    )


def get_signal_config_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_CONFIG_STATUS,
    )


def get_signal_data_type(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_DATA_TYPE,
    )


def set_signal_data_type(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_DATA_TYPE,
        value,
    )


def get_signal_default(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_DEFAULT,
    )


def set_signal_default(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_DEFAULT,
        value,
    )


def get_signal_frame_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_SIG_FRAME_REF,
    )


def get_signal_max(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_MAX,
    )


def set_signal_max(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_MAX,
        value,
    )


def get_signal_min(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_MIN,
    )


def set_signal_min(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_MIN,
        value,
    )


def get_signal_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_SIG_NAME,
    )


def set_signal_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_SIG_NAME,
        value,
    )


def get_signal_name_unique_to_cluster(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_SIG_NAME_UNIQUE_TO_CLUSTER,
    )


def get_signal_num_bits(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_NUM_BITS,
    )


def set_signal_num_bits(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_NUM_BITS,
        value,
    )


def get_signal_pdu_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_SIG_PDU_REF,
    )


def get_signal_scale_fac(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_SCALE_FAC,
    )


def set_signal_scale_fac(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_SCALE_FAC,
        value,
    )


def get_signal_scale_off(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_SCALE_OFF,
    )


def set_signal_scale_off(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_SIG_SCALE_OFF,
        value,
    )


def get_signal_start_bit(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_START_BIT,
    )


def set_signal_start_bit(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_START_BIT,
        value,
    )


def get_signal_unit(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_SIG_UNIT,
    )


def set_signal_unit(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_SIG_UNIT,
        value,
    )


def get_signal_mux_is_data_mux(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_SIG_MUX_IS_DATA_MUX,
    )


def set_signal_mux_is_data_mux(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_SIG_MUX_IS_DATA_MUX,
        value,
    )


def get_signal_mux_is_dynamic(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_SIG_MUX_IS_DYNAMIC,
    )


def get_signal_mux_value(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SIG_MUX_VALUE,
    )


def get_signal_mux_subfrm_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_SIG_MUX_SUBFRM_REF,
    )


def get_subframe_config_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SUBFRM_CONFIG_STATUS,
    )


def get_subframe_dyn_sig_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_SUBFRM_DYN_SIG_REFS,
    )


def get_subframe_frm_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_SUBFRM_FRM_REF,
    )


def get_subframe_mux_value(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_SUBFRM_MUX_VALUE,
    )


def set_subframe_mux_value(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_SUBFRM_MUX_VALUE,
        value,
    )


def get_subframe_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_SUBFRM_NAME,
    )


def set_subframe_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_SUBFRM_NAME,
        value,
    )


def get_subframe_pdu_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_SUBFRM_PDU_REF,
    )


def get_subframe_name_unique_to_cluster(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_SUBFRM_NAME_UNIQUE_TO_CLUSTER,
    )


def get_ecu_clst_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_ECU_CLST_REF,
    )


def get_ecu_comment(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_ECU_COMMENT,
    )


def set_ecu_comment(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_ECU_COMMENT,
        value,
    )


def get_ecu_config_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_CONFIG_STATUS,
    )


def get_ecu_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_ECU_NAME,
    )


def set_ecu_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_ECU_NAME,
        value,
    )


def get_ecu_rx_frm_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_ECU_RX_FRM_REFS,
    )


def set_ecu_rx_frm_refs(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_ref_array(
        ref,
        _cconsts.NX_PROP_ECU_RX_FRM_REFS,
        value,
    )


def get_ecu_tx_frm_refs(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_ECU_TX_FRM_REFS,
    )


def set_ecu_tx_frm_refs(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_ref_array(
        ref,
        _cconsts.NX_PROP_ECU_TX_FRM_REFS,
        value,
    )


def get_ecu_flex_ray_is_coldstart(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_IS_COLDSTART,
    )


def get_ecu_flex_ray_startup_frame_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_STARTUP_FRAME_REF,
    )


def get_ecu_flex_ray_wakeup_ptrn(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_WAKEUP_PTRN,
    )


def set_ecu_flex_ray_wakeup_ptrn(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_WAKEUP_PTRN,
        value,
    )


def get_ecu_flex_ray_wakeup_chs(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_WAKEUP_CHS,
    )


def set_ecu_flex_ray_wakeup_chs(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_WAKEUP_CHS,
        value,
    )


def get_ecu_flex_ray_connected_chs(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_CONNECTED_CHS,
    )


def set_ecu_flex_ray_connected_chs(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_FLEX_RAY_CONNECTED_CHS,
        value,
    )


def get_ecu_lin_master(
    ref,  # type: int
):
    # type: (...) -> bool
    return _cprops.get_database_bool(
        ref,
        _cconsts.NX_PROP_ECU_LIN_MASTER,
    )


def set_ecu_lin_master(
    ref,  # type: int
    value,  # type: bool
):
    # type: (...) -> None
    _cprops.set_database_bool(
        ref,
        _cconsts.NX_PROP_ECU_LIN_MASTER,
        value,
    )


def get_ecu_lin_protocol_ver(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_PROTOCOL_VER,
    )


def set_ecu_lin_protocol_ver(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_PROTOCOL_VER,
        value,
    )


def get_ecu_lin_initial_nad(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_INITIAL_NAD,
    )


def set_ecu_lin_initial_nad(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_INITIAL_NAD,
        value,
    )


def get_ecu_lin_config_nad(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_CONFIG_NAD,
    )


def set_ecu_lin_config_nad(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_CONFIG_NAD,
        value,
    )


def get_ecu_lin_supplier_id(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_SUPPLIER_ID,
    )


def set_ecu_lin_supplier_id(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_SUPPLIER_ID,
        value,
    )


def get_ecu_lin_function_id(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_FUNCTION_ID,
    )


def set_ecu_lin_function_id(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_LIN_FUNCTION_ID,
        value,
    )


def get_ecu_linp_2min(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_ECU_LINP_2MIN,
    )


def set_ecu_linp_2min(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_ECU_LINP_2MIN,
        value,
    )


def get_ecu_lins_tmin(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_ECU_LINS_TMIN,
    )


def set_ecu_lins_tmin(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_ECU_LINS_TMIN,
        value,
    )


def get_ecu_j1939_preferred_address(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_J1939_PREFERRED_ADDRESS,
    )


def set_ecu_j1939_preferred_address(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_ECU_J1939_PREFERRED_ADDRESS,
        value,
    )


def get_ecu_j1939_node_name(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u64(
        ref,
        _cconsts.NX_PROP_ECU_J1939_NODE_NAME,
    )


def set_ecu_j1939_node_name(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u64(
        ref,
        _cconsts.NX_PROP_ECU_J1939_NODE_NAME,
        value,
    )


def get_lin_sched_clst_ref(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_CLST_REF,
    )


def get_lin_sched_comment(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_COMMENT,
    )


def set_lin_sched_comment(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_COMMENT,
        value,
    )


def get_lin_sched_config_status(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_CONFIG_STATUS,
    )


def get_lin_sched_entries(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRIES,
    )


def get_lin_sched_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_NAME,
    )


def set_lin_sched_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_NAME,
        value,
    )


def get_lin_sched_priority(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_PRIORITY,
    )


def set_lin_sched_priority(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_PRIORITY,
        value,
    )


def get_lin_sched_run_mode(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_RUN_MODE,
    )


def set_lin_sched_run_mode(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_RUN_MODE,
        value,
    )


def get_lin_sched_entry_collision_res_sched(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_COLLISION_RES_SCHED,
    )


def set_lin_sched_entry_collision_res_sched(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_ref(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_COLLISION_RES_SCHED,
        value,
    )


def get_lin_sched_entry_delay(
    ref,  # type: int
):
    # type: (...) -> float
    return _cprops.get_database_f64(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_DELAY,
    )


def set_lin_sched_entry_delay(
    ref,  # type: int
    value,  # type: float
):
    # type: (...) -> None
    _cprops.set_database_f64(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_DELAY,
        value,
    )


def get_lin_sched_entry_event_id(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_EVENT_ID,
    )


def set_lin_sched_entry_event_id(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_EVENT_ID,
        value,
    )


def get_lin_sched_entry_frames(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_ref_array(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_FRAMES,
    )


def set_lin_sched_entry_frames(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_ref_array(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_FRAMES,
        value,
    )


def get_lin_sched_entry_name(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_NAME,
    )


def set_lin_sched_entry_name(
    ref,  # type: int
    value,  # type: typing.Text
):
    # type: (...) -> None
    _cprops.set_database_string(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_NAME,
        value,
    )


def get_lin_sched_entry_name_unique_to_cluster(
    ref,  # type: int
):
    # type: (...) -> typing.Text
    return _cprops.get_database_string(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_NAME_UNIQUE_TO_CLUSTER,
    )


def get_lin_sched_entry_sched(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_ref(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_SCHED,
    )


def get_lin_sched_entry_type(
    ref,  # type: int
):
    # type: (...) -> int
    return _cprops.get_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_TYPE,
    )


def set_lin_sched_entry_type(
    ref,  # type: int
    value,  # type: int
):
    # type: (...) -> None
    _cprops.set_database_u32(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_TYPE,
        value,
    )


def get_lin_sched_entry_nc_ff_data_bytes(
    ref,  # type: int
):
    # type: (...) -> typing.List[int]
    return _cprops.get_database_u8_array(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_NC_FF_DATA_BYTES,
    )


def set_lin_sched_entry_nc_ff_data_bytes(
    ref,  # type: int
    value,  # type: typing.List[int]
):
    # type: (...) -> None
    _cprops.set_database_u8_array(
        ref,
        _cconsts.NX_PROP_LIN_SCHED_ENTRY_NC_FF_DATA_BYTES,
        value,
    )
