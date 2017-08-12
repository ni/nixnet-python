from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import typing  # NOQA: F401

import six

from nixnet import _cconsts
from nixnet import _errors
from nixnet import constants
from nixnet import types


def flatten_items(list):
    # (typing.Union[typing.Text, typing.List[typing.Text]]) -> typing.Text
    """Flatten an item list to a string

    >>> str(flatten_items('Item'))
    'Item'
    >>> str(flatten_items(['A', 'B']))
    'A,B'
    >>> str(flatten_items(None))
    ''
    """
    if isinstance(list, six.string_types):
        # For FRAME_IN_QUEUED / FRAME_OUT_QUEUED
        # Convenience for everything else
        if ',' in list:
            # A bit of an abuse of an error code
            _errors.check_for_error(_cconsts.NX_ERR_INVALID_PROPERTY_VALUE)
        flattened = list
    elif isinstance(list, collections.Iterable):
        flattened = ",".join(list)
    elif list is None:
        # For FRAME_IN_STREAM / FRAME_OUT_STREAM
        flattened = ''
    else:
        # A bit of an abuse of an error code
        _errors.check_for_error(_cconsts.NX_ERR_INVALID_PROPERTY_VALUE)

    return flattened


def parse_can_comm_bitfield(bitfield):
    # (int) -> types.CanComm
    """Parse a CAN Comm bitfield."""
    state = constants.CanCommState(bitfield & 0x0F)
    tcvr_err = ((bitfield >> 4) & 0x01) != 0
    sleep = ((bitfield >> 5) & 0x01) != 0
    last_err = constants.CanLastErr((bitfield >> 8) & 0x0F)
    tx_err_count = ((bitfield >> 16) & 0x0FF)
    rx_err_count = ((bitfield >> 24) & 0x0FF)
    return types.CanComm(state, tcvr_err, sleep, last_err, tx_err_count, rx_err_count)


def parse_lin_comm_bitfield(first, second):
    # (int) -> types.CanComm
    """Parse a LIN Comm first."""
    sleep = ((first >> 1) & 0x01) != 0
    state = constants.LinCommState((first >> 2) & 0x03)
    last_err = constants.LinLastErr((first >> 4) & 0x0F)
    last_err_received = (first >> 8) & 0x0FF
    last_err_expected = (first >> 16) & 0x0FF
    last_err_id = (first >> 24) & 0x03F
    tcvr_rdy = ((first >> 32) & 0x01) != 0

    sched_index = second & 0x0FF

    return types.LinComm(
        sleep,
        state,
        last_err,
        last_err_received,
        last_err_expected,
        last_err_id,
        tcvr_rdy,
        sched_index)
