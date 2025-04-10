﻿from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
try:
    # Python 3.3+
    from collections.abc import Sequence
except ImportError:
    # Python 2.7
    from collections import Sequence  # type: ignore
import typing  # NOQA: F401

import six

from nixnet import _props


@six.add_metaclass(abc.ABCMeta)
class Collection(Sequence):
    """Collection of items in a session."""

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle
        self.__list_cache = None  # type: typing.Optional[typing.List[typing.Text]]

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def __len__(self):
        # type: () -> int
        return _props.get_session_num_in_list(self._handle)

    def __iter__(self):
        item_count = len(self)
        item_names = self._list_cache
        assert item_count == len(item_names), \
            "Frame count ({}) is out of sync with items ({})".format(item_count, item_names)
        for index, name in enumerate(item_names):
            yield self._create_item(self._handle, index, name)

    def __contains__(self, index):
        if isinstance(index, six.integer_types):
            return 0 <= index and index < len(self._list_cache)
        elif isinstance(index, six.string_types):
            name = index
            return name in self._list_cache
        else:
            raise TypeError(index)

    def __getitem__(self, index):
        if isinstance(index, six.integer_types):
            name = self._list_cache[index]
        elif isinstance(index, six.string_types):
            name = index
            item_names = self._list_cache
            try:
                index = item_names.index(name)
            except ValueError:
                raise KeyError(name)
        else:
            raise TypeError(index)

        return self._create_item(self._handle, index, name)

    def get(self, index, default=None):
        # type: (typing.Union[int, typing.Text], typing.Any) -> Item
        """Access an item, returning ``default`` on failure.

        Args:
            index(str or int): Item name or index
            default: Value to return when lookup fails
        """
        if isinstance(index, six.integer_types):
            try:
                name = self._list_cache[index]
            except IndexError:
                return default
        elif isinstance(index, six.string_types):
            name = index
            item_names = self._list_cache
            try:
                index = item_names.index(name)
            except ValueError:
                return default
        else:
            raise TypeError(index)

        return self._create_item(self._handle, index, name)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_collection = typing.cast(Collection, other)
            return (
                self._handle == other_collection._handle
                and self._list_cache == other_collection._list_cache
            )
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    @property
    def _list_cache(self):
        # type: () -> typing.List[typing.Text]
        if self.__list_cache is None:
            self.__list_cache = list(_props.get_session_list(self._handle))
        return self.__list_cache

    @abc.abstractmethod
    def _create_item(self, handle, index, name):
        # type: (int, int, typing.Text) -> Item
        pass


class Item(object):
    """Item configuration for a session."""

    def __init__(self, handle, index, name):
        # type: (int, int, typing.Text) -> None
        self._handle = handle
        self._index = index
        self._name = name

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_item = typing.cast(Item, other)
            return (
                self._handle == other_item._handle
                and self._index == other_item._index
            )
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __int__(self):
        # type: () -> int
        return self._index

    def __str__(self):
        # type: () -> typing.Text
        return self._name
