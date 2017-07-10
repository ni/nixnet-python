from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import collections

from nixnet import _cconsts
from nixnet import _errors
from nixnet import constants

__all__ = ['DriverVersion', 'RawFrame', 'CanFrame']


DriverVersion = collections.namedtuple(
    'DriverVersion',
    ['major', 'minor', 'update', 'phase', 'build'])


class RawFrame(object):
    """Raw Frame.

    Attributes:
        timestamp: Absolute time the XNET interface received the end-of-frame.
        identifier (int): CAN frame arbitration identifier.
        type (consants.FrameType): Frame Type.
        flags (int): Flags that qualify the type.
        info (int): Info that qualify the type.
        payload (byte string): Data bytes.
    """

    __slots__ = [
        "timestamp",
        "identifier",
        "type",
        "flags",
        "info",
        "payload"]

    def __init__(self, timestamp, identifier, type, flags, info, payload=b""):
        self.timestamp = timestamp
        self.identifier = identifier
        self.type = type
        self.flags = flags
        self.info = info
        self.payload = payload

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return all((
                self.timestamp == other.timestamp,
                self.identifier == other.identifier,
                self.type == other.type,
                self.flags == other.flags,
                self.info == other.info,
                self.payload == other.payload))
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
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
        identifier (int): CAN frame arbitration identifier.
        extended (bool): identifier uses extended format.
        echo (bool): Frame is an echo of a successful transmit rather than being received from the network.
        type (consants.FrameType): Frame Type.
        timestamp (Optional[datetime]): Absolute time the XNET interface received the end-of-frame.
        payload (byte string): Data bytes.
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
        self.identifier = identifier
        self.extended = extended
        self.echo = False  # Used only for Read
        self.type = type
        self.timestamp = 0  # Used only for Read
        self.payload = payload

    @classmethod
    def from_raw(cls, frame):
        """Convert from RawFrame

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
        """Convert to RawFrame

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
            return all((
                self.identifier == other.identifier,
                self.extended == other.extended,
                self.echo == other.echo,
                self.type == other.type,
                self.timestamp == other.timestamp,
                self.payload == other.payload))
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        """CanFrame debug representation.

        >>> CanFrame(1, True, constants.FrameType.CAN_DATA)
        CanFrame(identifier=0x1, echo=False, type=FrameType.CAN_DATA, timestamp=0x0, payload=...)
        """
        return "CanFrame(identifier=0x{:x}, echo={}, type={}, timestamp=0x{:x}, payload=...)".format(
            self.identifier,
            self.echo,
            self.type,
            self.timestamp)
