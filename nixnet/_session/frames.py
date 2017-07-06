from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import six

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _props


class Frames(object):
    """Frames in a session."""

    def __init__(self, handle):
        self._handle = handle

    def __len__(self):
        return _props.get_session_num_in_list(self._handle)

    def __iter__(self):
        for index in range(len(self)):
            yield Frame(self._handle, index)

    def __getitem__(self, index):
        if isinstance(index, six.integer_types):
            pass
        else:
            _errors.check_error(_cconsts.NX_ERR_INVALID_ACTIVE_FRAME_INDEX)

        return Frame(self._handle, index)

    def __repr__(self):
        return 'Session.Frames(handle={0})'.format(self._handle)


class Frame(object):
    """Frame configuration for a session."""

    def __init__(self, handle, index):
        self._handle = handle
        self._index = index

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle and self._index == self._index
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

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
