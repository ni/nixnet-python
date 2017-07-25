from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import constants

__all__ = ['DriverVersion', 'CanComm', 'RawFrame', 'CanFrame']


DriverVersion = collections.namedtuple(
    'DriverVersion',
    ['major', 'minor', 'update', 'phase', 'build'])


CanComm_ = collections.namedtuple(
    'CanComm_',
    ['state', 'tcvr_err', 'sleep', 'last_err', 'tx_err_count', 'rx_err_count'])


class CanComm(CanComm_):
    """CAN Communication State.

    Attributes:
        state (:any:`nixnet._enums.CanCommState`): Communication State
        tcvr_err (bool): Transceiver Error.
            Transceiver error indicates whether an error condition exists on
            the physical transceiver. This is typically referred to as the
            transceiver chip NERR pin.  False indicates normal operation (no
            error), and true indicates an error.
        sleep (bool): Sleep.
            Sleep indicates whether the transceiver and communication
            controller are in their sleep state. False indicates normal
            operation (awake), and true indicates sleep.
        last_err (:any:`nixnet._enums.CanLastErr`): Last Error.
            Last error specifies the status of the last attempt to receive or
            transmit a frame
        tx_err_count (int): Transmit Error Counter.
            The transmit error counter begins at 0 when communication starts on
            the CAN interface. The counter increments when an error is detected
            for a transmitted frame and decrements when a frame transmits
            successfully. The counter increases more for an error than it is
            decreased for success. This ensures that the counter generally
            increases when a certain ratio of frames (roughly 1/8) encounter
            errors.
            When communication state transitions to Bus Off, the transmit error
            counter no longer is valid.
        rx_err_count (int): Receive Error Counter.
            The receive error counter begins at 0 when communication starts on
            the CAN interface. The counter increments when an error is detected
            for a received frame and decrements when a frame is received
            successfully. The counter increases more for an error than it is
            decreased for success. This ensures that the counter generally
            increases when a certain ratio of frames (roughly 1/8) encounter
            errors.
    """

    pass


class RawFrame(object):
    """Raw Frame.

    Attributes:
        timestamp(int): Absolute time the XNET interface received the end-of-frame.
        identifier(int): CAN frame arbitration identifier.
        type(:any:`nixnet._enums.FrameType`): Frame type.
        flags(int): Flags that qualify the type.
        info(int): Info that qualify the type.
        payload(bytes): Payload.
    """

    __slots__ = [
        "timestamp",
        "identifier",
        "type",
        "flags",
        "info",
        "payload"]

    def __init__(self, timestamp, identifier, type, flags, info, payload=b""):
        # type: (int, int, constants.FrameType, int, int, bytes) -> None
        self.timestamp = timestamp
        self.identifier = identifier
        self.type = type
        self.flags = flags
        self.info = info
        self.payload = payload

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_frame = typing.cast(RawFrame, other)
            return all((
                self.timestamp == other_frame.timestamp,
                self.identifier == other_frame.identifier,
                self.type == other_frame.type,
                self.flags == other_frame.flags,
                self.info == other_frame.info,
                self.payload == other_frame.payload))
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        # type: () -> typing.Text
        """RawFrame debug representation.

        >>> RawFrame(1, 2, constants.FrameType.CAN_DATA, 3, 4)
        RawFrame(timestamp=0x1, identifier=0x2, type=FrameType.CAN_DATA, flags=0x3, info=0x4, payload=...)
        """
        return "RawFrame(timestamp=0x{:x}, identifier=0x{:x}, type={}, flags=0x{:x}, info=0x{:x}, payload=...)".format(
            self.timestamp,
            self.identifier,
            self.type,
            self.flags,
            self.info)


class CanFrame(object):
    """CAN Frame.

    Attributes:
        identifier(int): CAN frame arbitration identifier.
        extended(bool): If the identifier uses an extended format.
        echo(bool): If the frame is an echo of a successful
            transmit rather than being received from the network.
        type(:any:`nixnet._enums.FrameType`): Frame type.
        timestamp(int): Absolute time the XNET interface received the end-of-frame.
        payload(bytes): Payload.
    """

    __slots__ = [
        "identifier",
        "extended",
        "echo",
        "type",
        "timestamp",
        "payload"]

    _FRAME_ID_MASK = 0x000003FF
    _EXTENDED_FRAME_ID_MASK = 0x1FFFFFFF

    def __init__(self, identifier, extended, type, payload=b""):
        # type: (int, bool, constants.FrameType, bytes) -> None
        self.identifier = identifier
        self.extended = extended
        self.echo = False  # Used only for Read
        self.type = type
        self.timestamp = 0  # Used only for Read
        self.payload = payload

    @classmethod
    def from_raw(cls, frame):
        # type: (RawFrame) -> CanFrame
        """Convert from RawFrame.

        >>> raw = RawFrame(5, 0x20000001, constants.FrameType.CAN_DATA, _cconsts.NX_FRAME_FLAGS_TRANSMIT_ECHO, 0, b'')
        >>> CanFrame.from_raw(raw)
        CanFrame(identifier=0x1, echo=True, type=FrameType.CAN_DATA, timestamp=0x5, payload=...)
        """
        extended = bool(frame.identifier & _cconsts.NX_FRAME_ID_CAN_IS_EXTENDED)
        if extended:
            identifier = frame.identifier & cls._EXTENDED_FRAME_ID_MASK
        else:
            identifier = frame.identifier & cls._FRAME_ID_MASK
        can_frame = CanFrame(identifier, extended, constants.FrameType(frame.type), frame.payload)
        can_frame.timestamp = frame.timestamp
        can_frame.echo = bool(frame.flags & _cconsts.NX_FRAME_FLAGS_TRANSMIT_ECHO)
        return can_frame

    def to_raw(self):
        # type: () -> RawFrame
        """Convert to RawFrame.

        >>> CanFrame(1, True, constants.FrameType.CAN_DATA).to_raw()
        RawFrame(timestamp=0x0, identifier=0x20000001, type=FrameType.CAN_DATA, flags=0x0, info=0x0, payload=...)
        """
        identifier = self.identifier
        if self.extended:
            if identifier != (identifier & self._EXTENDED_FRAME_ID_MASK):
                _errors.check_for_error(_cconsts.NX_ERR_UNDEFINED_FRAME_ID)
            identifier |= _cconsts.NX_FRAME_ID_CAN_IS_EXTENDED
        else:
            if identifier != (identifier & self._FRAME_ID_MASK):
                _errors.check_for_error(_cconsts.NX_ERR_UNDEFINED_FRAME_ID)
        flags = 0
        if self.echo:
            flags |= _cconsts.NX_FRAME_FLAGS_TRANSMIT_ECHO
        return RawFrame(self.timestamp, identifier, self.type, flags, 0, self.payload)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_frame = typing.cast(CanFrame, other)
            return all((
                self.identifier == other_frame.identifier,
                self.extended == other_frame.extended,
                self.echo == other_frame.echo,
                self.type == other_frame.type,
                self.timestamp == other_frame.timestamp,
                self.payload == other_frame.payload))
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        # type: () -> typing.Text
        """CanFrame debug representation.

        >>> CanFrame(1, True, constants.FrameType.CAN_DATA)
        CanFrame(identifier=0x1, echo=False, type=FrameType.CAN_DATA, timestamp=0x0, payload=...)
        """
        return "CanFrame(identifier=0x{:x}, echo={}, type={}, timestamp=0x{:x}, payload=...)".format(
            self.identifier,
            self.echo,
            self.type,
            self.timestamp)
