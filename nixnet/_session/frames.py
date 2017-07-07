from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _props

from nixnet._session import collection


class Frames(collection.Collection):
    """Frames in a session."""

    def __repr__(self):
        return 'Session.Frames(handle={0})'.format(self._handle)


class Frame(collection.Item):
    """Frame configuration for a session."""

    def __repr__(self):
        return 'Session.Frame(handle={0}, index={0})'.format(self._handle, self._index)

    def set_can_start_time_off(self, value):
        _props.set_session_can_start_time_off(self._handle, self._index, value)

    def set_can_tx_time(self, value):
        _props.set_session_can_tx_time(self._handle, self._index, value)

    def set_skip_n_cyclic_frames(self, value):
        _props.set_session_skip_n_cyclic_frames(self._handle, self._index, value)

    def set_output_queue_update_freq(self, value):
        _props.set_session_output_queue_update_freq(self._handle, self._index, value)

    def set_lin_tx_n_corrupted_chksums(self, value):
        _props.set_session_lin_tx_n_corrupted_chksums(self._handle, self._index, value)

    def set_j1939_addr_filter(self, value):
        _props.set_session_j1939_addr_filter(self._handle, self._index, value)
