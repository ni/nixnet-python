﻿from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

try:
    from collections.abc import Iterable  # python 3.3+
    from collections.abc import Sized  # python 3.3+
except ImportError:
    from collections import Iterable  # python 2.7
    from collections import Sized  # python 2.7
import typing  # NOQA: F401

from nixnet import _cprops


class SystemCollection(Iterable, Sized):
    """Collection of System related objects."""

    def __init__(self, handle, prop_id, factory):
        # type: (int, int, typing.Any) -> None
        self._handle = handle
        self._prop_id = prop_id
        self._factory = factory

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            sys_other = typing.cast(SystemCollection, other)
            return self._handle == sys_other._handle and self._prop_id == sys_other._prop_id
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self._handle)

    def __len__(self):
        return _cprops.get_session_ref_array_len(self._handle, self._prop_id)

    def __iter__(self):
        for ref in _cprops.get_session_ref_array(self._handle, self._prop_id):
            yield self._factory(ref)
