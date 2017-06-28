from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _props


class Ecu(object):

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
        return 'Ecu(handle={0})'.format(self._handle)

    @property
    def clst_ref(self):
        return _props.get_ecu_clst_ref(self._handle)

    @property
    def comment(self):
        return _props.get_ecu_comment(self._handle)

    @comment.setter
    def comment(self, value):
        _props.set_ecu_comment(self._handle, value)

    @property
    def config_status(self):
        return _props.get_ecu_config_status(self._handle)

    @property
    def name(self):
        return _props.get_ecu_name(self._handle)

    @name.setter
    def name(self, value):
        _props.set_ecu_name(self._handle, value)

    @property
    def rx_frm_refs(self):
        return _props.get_ecu_rx_frm_refs(self._handle)

    @rx_frm_refs.setter
    def rx_frm_refs(self, value):
        _props.set_ecu_rx_frm_refs(self._handle, value)

    @property
    def tx_frm_refs(self):
        return _props.get_ecu_tx_frm_refs(self._handle)

    @tx_frm_refs.setter
    def tx_frm_refs(self, value):
        _props.set_ecu_tx_frm_refs(self._handle, value)

    @property
    def flex_ray_is_coldstart(self):
        return _props.get_ecu_flex_ray_is_coldstart(self._handle)

    @property
    def flex_ray_startup_frame_ref(self):
        return _props.get_ecu_flex_ray_startup_frame_ref(self._handle)

    @property
    def flex_ray_wakeup_ptrn(self):
        return _props.get_ecu_flex_ray_wakeup_ptrn(self._handle)

    @flex_ray_wakeup_ptrn.setter
    def flex_ray_wakeup_ptrn(self, value):
        _props.set_ecu_flex_ray_wakeup_ptrn(self._handle, value)

    @property
    def flex_ray_wakeup_chs(self):
        return _props.get_ecu_flex_ray_wakeup_chs(self._handle)

    @flex_ray_wakeup_chs.setter
    def flex_ray_wakeup_chs(self, value):
        _props.set_ecu_flex_ray_wakeup_chs(self._handle, value)

    @property
    def flex_ray_connected_chs(self):
        return _props.get_ecu_flex_ray_connected_chs(self._handle)

    @flex_ray_connected_chs.setter
    def flex_ray_connected_chs(self, value):
        _props.set_ecu_flex_ray_connected_chs(self._handle, value)

    @property
    def lin_master(self):
        return _props.get_ecu_lin_master(self._handle)

    @lin_master.setter
    def lin_master(self, value):
        _props.set_ecu_lin_master(self._handle, value)

    @property
    def lin_protocol_ver(self):
        return _props.get_ecu_lin_protocol_ver(self._handle)

    @lin_protocol_ver.setter
    def lin_protocol_ver(self, value):
        _props.set_ecu_lin_protocol_ver(self._handle, value)

    @property
    def lin_initial_nad(self):
        return _props.get_ecu_lin_initial_nad(self._handle)

    @lin_initial_nad.setter
    def lin_initial_nad(self, value):
        _props.set_ecu_lin_initial_nad(self._handle, value)

    @property
    def lin_config_nad(self):
        return _props.get_ecu_lin_config_nad(self._handle)

    @lin_config_nad.setter
    def lin_config_nad(self, value):
        _props.set_ecu_lin_config_nad(self._handle, value)

    @property
    def lin_supplier_id(self):
        return _props.get_ecu_lin_supplier_id(self._handle)

    @lin_supplier_id.setter
    def lin_supplier_id(self, value):
        _props.set_ecu_lin_supplier_id(self._handle, value)

    @property
    def lin_function_id(self):
        return _props.get_ecu_lin_function_id(self._handle)

    @lin_function_id.setter
    def lin_function_id(self, value):
        _props.set_ecu_lin_function_id(self._handle, value)

    @property
    def linp_2min(self):
        return _props.get_ecu_linp_2min(self._handle)

    @linp_2min.setter
    def linp_2min(self, value):
        _props.set_ecu_linp_2min(self._handle, value)

    @property
    def lins_tmin(self):
        return _props.get_ecu_lins_tmin(self._handle)

    @lins_tmin.setter
    def lins_tmin(self, value):
        _props.set_ecu_lins_tmin(self._handle, value)

    @property
    def j1939_preferred_address(self):
        return _props.get_ecu_j1939_preferred_address(self._handle)

    @j1939_preferred_address.setter
    def j1939_preferred_address(self, value):
        _props.set_ecu_j1939_preferred_address(self._handle, value)

    @property
    def j1939_node_name(self):
        return _props.get_ecu_j1939_node_name(self._handle)

    @j1939_node_name.setter
    def j1939_node_name(self, value):
        _props.set_ecu_j1939_node_name(self._handle, value)
