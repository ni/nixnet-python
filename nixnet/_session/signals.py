from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools
import typing  # NOQA: F401

import six

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
        # type: () -> typing.Iterable[typing.Tuple[int, float]]
        """Read data from a Signal Input Single-Point session.

        Yields:
            tuple of int and float: Timestamp and signal
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
            signals):
        # type: (typing.Iterable[float]) -> None
        """Write data to a Signal Output Single-Point session.

        Args:
            signals(list of float): A list of signal values (float).
        """
        _funcs.nx_write_signal_single_point(self._handle, list(signals))


class XYInSignals(Signals):
    """Writeable signals in a session."""

    def __repr__(self):
        return 'Session.XYInSignals(handle={0})'.format(self._handle)

    def read(
            self,
            num_values_per_signal,
            time_limit=None):
        # type: (int, int) -> typing.List[typing.List[typing.Tuple[int, float]]]
        """Read data from a Signal Input X-Y session.

        Args:
            num_values_per_signal(int): Number of values to read per signal in
                the session.
            time_limit(int): The timestamp to wait for before returning signal values.

                ``read`` waits for the timestamp to occur, then returns
                available values (up to number to read).  If you increment
                ``time_limit`` by a fixed number of seconds for each call to
                ``read``, you effectively obtain a moving window of signal
                values.

                If ``time_limit`` is ``None``, then returns immediately all
                available values up to the current time (up to
                ``num_values_per_signal``).

                This is in contrast to other ``read`` functions which take a ``timeout`` (maximum
                amount time to wait).
        Returns:
            list of list of tuple int and float: Timestamp and signal

                Each timestamp/value pair represents a value from a received
                frame. When signals exist in different frames, the array size
                may be different from one signal to another.
        """
        num_signals = len(self)
        value_buffer, timestamp_buffer, value_length_buffer = _funcs.nx_read_signal_xy(
            self._handle,
            time_limit,
            num_signals,
            num_values_per_signal)
        signals = self._unflatten_signals(value_length_buffer, time_limit, value_length_buffer)
        return signals

    @staticmethod
    def _unflatten_signals(value_buffer, timestamp_buffer, value_length_buffer):
        num_signals = len(value_length_buffer)
        num_values_returned_per_signal = (
            length_ctype.value
            for length_ctype in value_length_buffer
        )
        ranges = (
            (si * num_signals, si * num_signals + num_values_returned)
            for si, num_values_returned in enumerate(num_values_returned_per_signal)
        )
        signals = [
            [
                (signal_ctype.value, timestamp_ctype.value)
                for (signal_ctype, timestamp_ctype) in six.moves.zip(
                    value_buffer[start:end],
                    timestamp_buffer[start:end])
            ]
            for start, end in ranges
        ]
        return signals


class XYOutSignals(Signals):
    """Writeable signals in a session."""

    def __repr__(self):
        return 'Session.XYOutSignals(handle={0})'.format(self._handle)

    def write(
            self,
            signals,
            timeout=10):
        # type: (typing.List[typing.List[float]], float) -> None
        """Write data to a Signal Output X-Y session.

        Args:
            signals(list of list of floats): A list of signal values.

                Each signal value is mapped to a frame for transmit. Therefore,
                the array of signal values is mapped to an array of frames to
                transmit.  When signals exist in the same frame, signals at the
                same index in the arrays are mapped to the same frame. When
                signals exist in different frames, the array size may be
                different from one cluster (signal) to another.
            timeout(float): The time in seconds to wait for the data to be
                queued for transmit.

                If 'timeout' is positive, this function waits up to that 'timeout'
                for space to become available in queues. If the space is not
                available prior to the 'timeout', a 'timeout' error is returned.

                If 'timeout' is 'constants.TIMEOUT_INFINITE', this functions
                waits indefinitely for space to become available in queues.

                If 'timeout' is 'constants.TIMEOUT_NONE', this function does not
                wait and immediately returns with a 'timeout' error if all data
                cannot be queued. Regardless of the 'timeout' used, if a 'timeout'
                error occurs, none of the data is queued, so you can attempt to
                call this function again at a later time with the same data.
        """
        value_lengths = [len(values) for values in signals]
        max_length = max(value_lengths)
        flattened_signals = self._flatten_signals(signals, max_length)
        _funcs.nx_write_signal_xy(self._handle, timeout, flattened_signals, [], value_lengths)

    @staticmethod
    def _flatten_signals(signals, max_length, default=0):
        """Flatten uneven lists of signals.

        >>> XYOutSignals._flatten_signals([[], [1, 2]], 2)
        [0, 0, 1, 2]
        >>> XYOutSignals._flatten_signals([[1], [1, 2]], 2)
        [1, 0, 1, 2]
        """
        padded = (
            itertools.chain(
                values,
                itertools.repeat(default, max(max_length - len(values), 0))
            )
            for values in signals
        )
        return list(itertools.chain.from_iterable(padded))


class Signal(collection.Item):
    """Signal configuration for a session."""

    def __repr__(self):
        return 'Session.Signal(handle={0}, index={0})'.format(self._handle, self._index)
