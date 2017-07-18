from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _funcs

from nixnet._session import collection


class Signals(collection.Collection):
    """Signals in a session."""

    def __repr__(self):
        return 'Session.Signals(handle={0})'.format(self._handle)

    def _create_item(self, handle, index, name):
        return Signal(handle, index, name)


class SinglePointInSignals(Signals):
    """Writeable signals in a session."""

    def __repr__(self):
        return 'Session.SinglePointInSignals(handle={0})'.format(self._handle)

    def read(self):
        """Read data from a Signal Input Single-Point session.

        Yields:
            A tuple of timestamp (internal NI-XNET ctype around u64) and signal
            values (float).
        """
        num_signals = len(self)
        timestamps, values = _funcs.nx_read_signal_single_point(self._handle, num_signals)
        for timestamp, value in zip(timestamps, values):
            yield timestamp.value, value.value


class SinglePointOutSignals(Signals):
    """Writeable signals in a session."""

    def __repr__(self):
        return 'Session.SinglePointOutSignals(handle={0})'.format(self._handle)

    def write(
            self,
            value_buffer):
        """Write data to a Signal Output Single-Point session.

        Args:
            value_buffer: A list of singal values (float).
        """
        _funcs.nx_write_signal_single_point(self._handle, value_buffer)


class Signal(collection.Item):
    """Signal configuration for a session."""

    def __repr__(self):
        return 'Session.Signal(handle={0}, index={0})'.format(self._handle, self._index)
