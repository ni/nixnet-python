from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class CanFrame(object):
    """CAN Frame.

    Attributes:
        identifier (int): CAN frame arbitration identifier
        extended (bool): identifier uses extended format
        echo (bool): Frame is an echo of a successful transmit rather than being received from the network.
        type (consants.FrameType): Frame Type
        timestamp (Optional[datetime]): Absolute time the XNET interface received the end-of-frame.
        payload (bytearray): Data bytes.
    """

    __slots__ = [
        "identifier",
        "extended",
        "echo",
        "type",
        "timestamp",
        "payload"]

    def __init__(self, identifier, extended, type, payload=bytearray()):
        self.identifier = identifier
        self.extended = extended
        self.echo = False  # Used only for Read
        self.type = type
        self.timestamp = None  # Used only for Read
        self.payload = payload
