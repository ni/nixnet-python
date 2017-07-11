from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import collections

import six

from nixnet import _cconsts
from nixnet import _errors


def flatten_items(list):
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
