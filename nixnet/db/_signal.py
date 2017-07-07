from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _props
from nixnet import constants


class Signal(object):

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
        return 'Signal(handle={0})'.format(self._handle)

    @property
    def byte_ordr(self):
        return constants.SigByteOrdr(_props.get_signal_byte_ordr(self._handle))

    @byte_ordr.setter
    def byte_ordr(self, value):
        _props.set_signal_byte_ordr(self._handle, value.value)

    @property
    def comment(self):
        return _props.get_signal_comment(self._handle)

    @comment.setter
    def comment(self, value):
        _props.set_signal_comment(self._handle, value)

    @property
    def config_status(self):
        return _props.get_signal_config_status(self._handle)

    @property
    def data_type(self):
        return constants.SigDataType(_props.get_signal_data_type(self._handle))

    @data_type.setter
    def data_type(self, value):
        _props.set_signal_data_type(self._handle, value.value)

    @property
    def default(self):
        return _props.get_signal_default(self._handle)

    @default.setter
    def default(self, value):
        _props.set_signal_default(self._handle, value)

    @property
    def frame_ref(self):
        return _props.get_signal_frame_ref(self._handle)

    @property
    def max(self):
        return _props.get_signal_max(self._handle)

    @max.setter
    def max(self, value):
        _props.set_signal_max(self._handle, value)

    @property
    def min(self):
        return _props.get_signal_min(self._handle)

    @min.setter
    def min(self, value):
        _props.set_signal_min(self._handle, value)

    @property
    def name(self):
        return _props.get_signal_name(self._handle)

    @name.setter
    def name(self, value):
        _props.set_signal_name(self._handle, value)

    @property
    def name_unique_to_cluster(self):
        return _props.get_signal_name_unique_to_cluster(self._handle)

    @property
    def num_bits(self):
        return _props.get_signal_num_bits(self._handle)

    @num_bits.setter
    def num_bits(self, value):
        _props.set_signal_num_bits(self._handle, value)

    @property
    def pdu_ref(self):
        return _props.get_signal_pdu_ref(self._handle)

    @property
    def scale_fac(self):
        return _props.get_signal_scale_fac(self._handle)

    @scale_fac.setter
    def scale_fac(self, value):
        _props.set_signal_scale_fac(self._handle, value)

    @property
    def scale_off(self):
        return _props.get_signal_scale_off(self._handle)

    @scale_off.setter
    def scale_off(self, value):
        _props.set_signal_scale_off(self._handle, value)

    @property
    def start_bit(self):
        return _props.get_signal_start_bit(self._handle)

    @start_bit.setter
    def start_bit(self, value):
        _props.set_signal_start_bit(self._handle, value)

    @property
    def unit(self):
        return _props.get_signal_unit(self._handle)

    @unit.setter
    def unit(self, value):
        _props.set_signal_unit(self._handle, value)

    @property
    def mux_is_data_mux(self):
        return _props.get_signal_mux_is_data_mux(self._handle)

    @mux_is_data_mux.setter
    def mux_is_data_mux(self, value):
        _props.set_signal_mux_is_data_mux(self._handle, value)

    @property
    def mux_is_dynamic(self):
        return _props.get_signal_mux_is_dynamic(self._handle)

    @property
    def mux_value(self):
        return _props.get_signal_mux_value(self._handle)

    @property
    def mux_subfrm_ref(self):
        return _props.get_signal_mux_subfrm_ref(self._handle)
