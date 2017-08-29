from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from nixnet import _funcs
from nixnet import _props
from nixnet import constants


class Cluster(object):

    def __init__(self, handle):
        self._handle = handle

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

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
        return _props.get_cluster_baud_rate64(self._handle)

    @baud_rate.setter
    def baud_rate(self, value):
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
        return constants.CanIoMode(_props.get_cluster_can_io_mode(self._handle))

    @can_io_mode.setter
    def can_io_mode(self, value):
        _props.set_cluster_can_io_mode(self._handle, value.value)

    @property
    def can_fd_baud_rate(self):
        return _props.get_cluster_can_fd_baud_rate64(self._handle)

    @can_fd_baud_rate.setter
    def can_fd_baud_rate(self, value):
        _props.set_cluster_can_fd_baud_rate64(self._handle, value)

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
    def application_protocol(self):
        return constants.AppProtocol(_props.get_cluster_application_protocol(self._handle))

    @application_protocol.setter
    def application_protocol(self, value):
        _props.set_cluster_application_protocol(self._handle, value.value)

    @property
    def can_fd_iso_mode(self):
        return constants.CanFdIsoMode(_props.get_cluster_can_fd_iso_mode(self._handle))
