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


class SinglePointInSignals(Signals):
    """Writeable signals in a session."""

    def __repr__(self):
        return 'Session.SinglePointInSignals(handle={0})'.format(self._handle)

    def read(self):
        """Read signal single point.

        Valid modes
        - Single Input Single-Point
        Timestamps
        - Optional in C API
        - Timestamp per data point
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadsignalsinglepoint/
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
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwritesignalsinglepoint/"
        _funcs.nx_write_signal_single_point(self._handle, value_buffer)


class Signal(collection.Item):
    """Signal configuration for a session."""

    def __repr__(self):
        return 'Session.Signal(handle={0}, index={0})'.format(self._handle, self._index)
