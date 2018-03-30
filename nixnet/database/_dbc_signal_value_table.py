from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import six
import typing  # NOQA: F401

from nixnet import _funcs
from nixnet import constants


class DbcSignalValueTable(collections.Mapping):
    """Collection for accessing a DBC signal value table."""

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(DbcSignalValueTable, other)._handle
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
        return len(self._value_table)

    def __iter__(self):
        return self.keys()

    def __getitem__(self, key):
        # type: (typing.Text) -> int
        """Return the value.

            Args:
                Value description.
            Returns:
                Value
        """
        if isinstance(key, six.string_types):
            return self._value_table[key]
        else:
            raise TypeError(key)

    def keys(self):
        """Return all value descriptions in the collection.

            Yields:
                An iterator to all value descriptions in the collection.
        """
        return iter(self._value_table.keys())

    def values(self):
        """Return all values in the collection.

            Yields:
                An iterator to all values in the collection.
        """
        return iter(self._value_table.values())

    def items(self):
        """Return all value descriptions and values in the collection.

            Yields:
                An iterator to tuple pairs of value descriptions and values in the collection.
        """
        return iter(self._value_table.items())

    @property
    def _value_table(self):
        # type: () -> typing.Dict[typing.Text, int]
        mode = constants.GetDbcAttributeMode.VALUE_TABLE_LIST
        attribute_size = _funcs.nxdb_get_dbc_attribute_size(self._handle, mode, '')
        attribute_info = _funcs.nxdb_get_dbc_attribute(self._handle, mode, '', attribute_size)
        table_string = attribute_info[0]
        if not table_string:
            return {}

        table_list = table_string.split(',')
        if len(table_list) % 2:
            raise ValueError('Value tables require an even number of items: %s' % table_list)

        # table_string is of the format 'value1, key1, value2, key2, ...'
        # convert to a dict: { 'key1': int('value1'), 'key2': int('value2'), ... }
        table_dict = dict(
            (key, int(value))
            for value, key in zip(table_list[0::2], table_list[1::2]))
        return table_dict
