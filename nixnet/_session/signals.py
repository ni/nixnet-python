from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools
import typing  # NOQA: F401

from nixnet import _funcs
from nixnet import _props
from nixnet import constants

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


class WaveformInSignals(Signals):
    """Writeable signals in a session."""

    def __repr__(self):
        return 'Session.WaveformInSignals(handle={0})'.format(self._handle)

    @property
    def resamp_rate(self):
        # type: () -> float
        """float: Rate used to resample frame data to/from signal data in waveforms.

        The units are in Hertz (samples per second).
        """
        return _props.get_session_resamp_rate(self._handle)

    @resamp_rate.setter
    def resamp_rate(self, value):
        # type: (float) -> None
        _props.set_session_resamp_rate(self._handle, value)

    def read(
            self,
            num_values_per_signal,
            timeout=constants.TIMEOUT_NONE):
        # type: (int, float) -> typing.Tuple[int, float, typing.List[typing.List[float]]]
        """Read data from a Signal Input Waveform session.

        Returns:
            tuple of int, float, and list of list of float: t0, dt, and a list
                of signal waveforms.  A signal waveform is a list of signal
                values.
        """
        num_signals = len(self)
        t0, dt, flattened_signals, num_values_returned = _funcs.nx_read_signal_waveform(
            self._handle,
            timeout,
            num_signals,
            num_values_per_signal)
        signals = self._unflatten_signals(flattened_signals, num_values_returned, num_signals)
        return t0, dt, signals

    @staticmethod
    def _unflatten_signals(flattened_signals, num_values_returned, num_signals):
        ranges = (
            (si * num_signals, si * num_signals + num_values_returned)
            for si in range(num_signals)
        )
        signals = [
            [
                signal_ctype.value
                for signal_ctype in flattened_signals[start:end]
            ]
            for start, end in ranges
        ]
        return signals


class WaveformOutSignals(Signals):
    """Writeable signals in a session."""

    def __repr__(self):
        return 'Session.WaveformOutSignals(handle={0})'.format(self._handle)

    @property
    def resamp_rate(self):
        # type: () -> float
        """float: Rate used to resample frame data to/from signal data in waveforms.

        The units are in Hertz (samples per second).
        """
        return _props.get_session_resamp_rate(self._handle)

    @resamp_rate.setter
    def resamp_rate(self, value):
        # type: (float) -> None
        _props.set_session_resamp_rate(self._handle, value)

    def write(
            self,
            signals,
            timeout=10):
        # type: (typing.List[typing.List[float]], float) -> None
        """Write data to a Signal Output Waveform session.

        Args:
            signals(list of list of float): A list of signal waveforms.  A
                signal waveform is a list of signal values (float)). Each
                waveform must be the same length.

                The data you write is queued for transmit on the network. Using
                the default queue configuration for this mode, and assuming a
                1000 Hz resample rate, you can safely write 64 elements if you
                have a sufficiently long timeout. To write more data, refer to
                the XNET Session Number of Values Unused property to determine
                the actual amount of queue space available for writing.
            timeout(float): The time in seconds to wait for the data to be
                queued for transmit. The timeout does not wait for frames to be
                transmitted on the network (see
                :any:`nixnet._session.base.SessionBase.wait_for_transmit_complete`).

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
        flattened_signals = self._flatten_signals(signals)
        _funcs.nx_write_signal_waveform(self._handle, timeout, flattened_signals)

    @staticmethod
    def _flatten_signals(signals):
        """Flatten even lists of signals.

        >>> WaveformOutSignals._flatten_signals([])
        []
        >>> WaveformOutSignals._flatten_signals([[1, 2], [3, 4]])
        [1, 2, 3, 4]
        """
        flattened_signals = list(itertools.chain.from_iterable(signals))
        return flattened_signals


class Signal(collection.Item):
    """Signal configuration for a session."""

    def __repr__(self):
        return 'Session.Signal(handle={0}, index={0})'.format(self._handle, self._index)
