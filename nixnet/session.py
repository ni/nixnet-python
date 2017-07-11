from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import warnings

from nixnet import _funcs
from nixnet import _props
from nixnet import _utils
from nixnet import constants
from nixnet import errors

from nixnet._session import frames as session_frames
from nixnet._session import intf
from nixnet._session import j1939
from nixnet._session import signals as session_signals


__all__ = [
    "FrameInStreamSession",
    "FrameOutStreamSession",
    "FrameInQueuedSession",
    "FrameOutQueuedSession",
    "SignalInSinglePointSession",
    "SignalOutSinglePointSession"]


class SessionBase(object):

    def __init__(
            self,
            database_name,
            cluster_name,
            list,
            interface,
            mode):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesession/"
        self._handle = None  # To satisfy `__del__` in case nx_create_session throws
        self._handle = _funcs.nx_create_session(database_name, cluster_name, list, interface, mode)
        self._intf = intf.Interface(self._handle)
        self._j1939 = j1939.J1939(self._handle)

    def __del__(self):
        if self._handle is not None:
            warnings.warn(
                'Session was not explicitly closed before it was destructed. '
                'Resources on the device may still be reserved.',
                errors.XnetResourceWarning)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
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

    def start(self, scope=constants.StartStopScope.NORMAL):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxstart/"
        _funcs.nx_start(self._handle, scope)

    def stop(self, scope=constants.StartStopScope.NORMAL):
        _funcs.nx_stop(self._handle, scope)

    def flush(self):
        _funcs.nx_flush(self._handle)

    def wait_for_transmit_complete(self, timeout=10):
        _funcs.nx_wait(self._handle, constants.Condition.TRANSMIT_COMPLETE, 0, timeout)

    def wait_for_intf_communicating(self, timeout=10):
        _funcs.nx_wait(self._handle, constants.Condition.INTF_COMMUNICATING, 0, timeout)

    def wait_for_intf_remote_wakeup(self, timeout=10):
        _funcs.nx_wait(self._handle, constants.Condition.INTF_REMOTE_WAKEUP, 0, timeout)

    def connect_terminals(self, source, destination):
        _funcs.nx_connect_terminals(self._handle, source, destination)

    def disconnect_terminals(self, source, destination):
        _funcs.nx_disconnect_terminals(self._handle, source, destination)

    @property
    def intf(self):
        return self._intf

    @property
    def j1939(self):
        return self._j1939

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
    def mode(self):
        return constants.CreateSessionMode(_props.get_session_mode(self._handle))

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


class FrameInStreamSession(SessionBase):

    def __init__(
            self,
            interface,
            database_name=':memory:',
            cluster_name=''):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesession/"
        flattened_list = _utils.flatten_items(None)
        SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface,
            constants.CreateSessionMode.FRAME_IN_STREAM)
        self._frames = session_frames.InFrames(self._handle)

    @property
    def frames(self):
        return self._frames


class FrameOutStreamSession(SessionBase):

    def __init__(
            self,
            interface,
            database_name=':memory:',
            cluster_name=''):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesession/"
        flattened_list = _utils.flatten_items(None)
        SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface,
            constants.CreateSessionMode.FRAME_OUT_STREAM)
        self._frames = session_frames.OutFrames(self._handle)

    @property
    def frames(self):
        return self._frames


class FrameInQueuedSession(SessionBase):

    def __init__(
            self,
            interface,
            database_name,
            cluster_name,
            frame):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesession/"
        flattened_list = _utils.flatten_items(frame)
        SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface,
            constants.CreateSessionMode.FRAME_IN_QUEUED)
        self._frames = session_frames.InFrames(self._handle)

    @property
    def frames(self):
        return self._frames


class FrameOutQueuedSession(SessionBase):

    def __init__(
            self,
            interface,
            database_name,
            cluster_name,
            frame):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesession/"
        flattened_list = _utils.flatten_items(frame)
        SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface,
            constants.CreateSessionMode.FRAME_OUT_QUEUED)
        self._frames = session_frames.OutFrames(self._handle)

    @property
    def frames(self):
        return self._frames


class FrameInSinglePointSession(SessionBase):

    def __init__(
            self,
            interface,
            database_name,
            cluster_name,
            frames):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesession/"
        flattened_list = _utils.flatten_items(frames)
        SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface,
            constants.CreateSessionMode.FRAME_IN_SINGLE_POINT)
        self._frames = session_frames.SinglePointInFrames(self._handle)

    @property
    def frames(self):
        return self._frames


class FrameOutSinglePointSession(SessionBase):

    def __init__(
            self,
            interface,
            database_name,
            cluster_name,
            frames):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesession/"
        flattened_list = _utils.flatten_items(frames)
        SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface,
            constants.CreateSessionMode.FRAME_OUT_SINGLE_POINT)
        self._frames = session_frames.OutFrames(self._handle)

    @property
    def frames(self):
        return self._frames


class SignalInSinglePointSession(SessionBase):

    def __init__(
            self,
            interface,
            database_name,
            cluster_name,
            signals):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesession/"
        flattened_list = _utils.flatten_items(signals)
        SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface,
            constants.CreateSessionMode.SIGNAL_IN_SINGLE_POINT)
        self._signals = session_signals.SinglePointInSignals(self._handle)

    @property
    def signals(self):
        return self._signals


class SignalOutSinglePointSession(SessionBase):

    def __init__(
            self,
            interface,
            database_name,
            cluster_name,
            signals):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesession/"
        flattened_list = _utils.flatten_items(signals)
        SessionBase.__init__(
            self,
            database_name,
            cluster_name,
            flattened_list,
            interface,
            constants.CreateSessionMode.SIGNAL_OUT_SINGLE_POINT)
        self._signals = session_signals.SinglePointOutSignals(self._handle)

    @property
    def signals(self):
        return self._signals


def create_session_by_ref(
        database_refs,
        interface,
        mode):
    return _funcs.nx_create_session_by_ref(database_refs, interface, mode)


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
