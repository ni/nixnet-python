from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _props


class J1939(object):
    """J1939 configuration for a session"""

    def __init__(self, handle):
        self._handle = handle

    def __repr__(self):
        return 'Session.J1939(handle={0})'.format(self._handle)

    def __str__(self):
        return self.name

    @property
    def address(self):
        return _props.get_session_j1939_address(self._handle)

    @address.setter
    def address(self, value):
        _props.set_session_j1939_address(self._handle, value)

    @property
    def name(self):
        return _props.get_session_j1939_name(self._handle)

    @name.setter
    def name(self, value):
        _props.set_session_j1939_name(self._handle, value)

    def set_ecu(self, value):
        _props.set_session_j1939ecu(self._handle, value)

    @property
    def timeout_t1(self):
        return _props.get_session_j1939_timeout_t1(self._handle)

    @timeout_t1.setter
    def timeout_t1(self, value):
        _props.set_session_j1939_timeout_t1(self._handle, value)

    @property
    def timeout_t2(self):
        return _props.get_session_j1939_timeout_t2(self._handle)

    @timeout_t2.setter
    def timeout_t2(self, value):
        _props.set_session_j1939_timeout_t2(self._handle, value)

    @property
    def timeout_t3(self):
        return _props.get_session_j1939_timeout_t3(self._handle)

    @timeout_t3.setter
    def timeout_t3(self, value):
        _props.set_session_j1939_timeout_t3(self._handle, value)

    @property
    def timeout_t4(self):
        return _props.get_session_j1939_timeout_t4(self._handle)

    @timeout_t4.setter
    def timeout_t4(self, value):
        _props.set_session_j1939_timeout_t4(self._handle, value)

    @property
    def response_time_tr_sd(self):
        return _props.get_session_j1939_response_time_tr_sd(self._handle)

    @response_time_tr_sd.setter
    def response_time_tr_sd(self, value):
        _props.set_session_j1939_response_time_tr_sd(self._handle, value)

    @property
    def response_time_tr_gd(self):
        return _props.get_session_j1939_response_time_tr_gd(self._handle)

    @response_time_tr_gd.setter
    def response_time_tr_gd(self, value):
        _props.set_session_j1939_response_time_tr_gd(self._handle, value)

    @property
    def hold_time_th(self):
        return _props.get_session_j1939_hold_time_th(self._handle)

    @hold_time_th.setter
    def hold_time_th(self, value):
        _props.set_session_j1939_hold_time_th(self._handle, value)

    @property
    def num_packets_recv(self):
        return _props.get_session_j1939_num_packets_recv(self._handle)

    @num_packets_recv.setter
    def num_packets_recv(self, value):
        _props.set_session_j1939_num_packets_recv(self._handle, value)

    @property
    def num_packets_resp(self):
        return _props.get_session_j1939_num_packets_resp(self._handle)

    @num_packets_resp.setter
    def num_packets_resp(self, value):
        _props.set_session_j1939_num_packets_resp(self._handle, value)

    @property
    def max_repeat_cts(self):
        return _props.get_session_j1939_max_repeat_cts(self._handle)

    @max_repeat_cts.setter
    def max_repeat_cts(self, value):
        _props.set_session_j1939_max_repeat_cts(self._handle, value)

    @property
    def fill_byte(self):
        return _props.get_session_j1939_fill_byte(self._handle)

    @fill_byte.setter
    def fill_byte(self, value):
        _props.set_session_j1939_fill_byte(self._handle, value)

    @property
    def write_queue_size(self):
        return _props.get_session_j1939_write_queue_size(self._handle)

    @write_queue_size.setter
    def write_queue_size(self, value):
        _props.set_session_j1939_write_queue_size(self._handle, value)

    @property
    def ecu_busy(self):
        return _props.get_session_j1939ecu_busy(self._handle)

    @ecu_busy.setter
    def ecu_busy(self, value):
        _props.set_session_j1939ecu_busy(self._handle, value)
