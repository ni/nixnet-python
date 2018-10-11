from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from nixnet import _props


class J1939(object):
    """J1939 configuration for a session"""

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

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
        _props.set_session_j1939_ecu(self._handle, value)

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
        return _props.get_session_j1939_ecu_busy(self._handle)

    @ecu_busy.setter
    def ecu_busy(self, value):
        _props.set_session_j1939_ecu_busy(self._handle, value)

    @property
    def include_dest_addr_in_pgn(self):
        # type: () -> bool
        """bool: SAE J1939 Include Destination Address in PGN

        Incoming J1939 frames are matched to an XNET database by the Parameter Group Number (PGN) of the frame.
        When receiving PDU1 frames,
        the destination address of the frame (J1939 PS field) is ignored when calculating the PGN,
        in accordance to the J1939 specification.
        This causes an XNET session to receive all frames that share the same PGN,
        making it difficult to distinguish destinations for traffic.

        When set to ``True``,
        this property instructs NI-XNET to include the destination address when extracting the PGN from the frame.
        This allows the same PGN sent to different destination addresses to be handled by separate input sessions.

        This property may be set at any time.
        When set after session start,
        it will not affect frames already received.

        This property is valid only for input sessions.
        It is not valid for stream sessions.
        This property affects all frames in a session.
        """
        return _props.get_session_j1939_include_dest_addr_in_pgn(self._handle)

    @include_dest_addr_in_pgn.setter
    def include_dest_addr_in_pgn(self, value):
        # type: (bool) -> None
        _props.set_session_j1939_include_dest_addr_in_pgn(self._handle, value)
