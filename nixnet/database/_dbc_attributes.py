from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from collections.abc import Mapping
import six
import typing  # NOQA: F401

from nixnet import _funcs
from nixnet import constants


class DbcAttributeCollection(Mapping):
    """Collection for accessing DBC attributes."""

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle

        # Here, we are caching the attribute names and enums to work around a driver issue.
        # The issue results in an empty attribute value after intermixing calls to get attribute values and enums.
        # We can avoid this issue if we get all attribute enums first, before getting any attribute values.
        self._cache = dict(
            (name, self._get_enums(name))
            for name in self._get_names()
        )

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(DbcAttributeCollection, other)._handle
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
        return len(list(self.keys()))

    def __iter__(self):
        return self.keys()

    def __getitem__(self, key):
        # type: (typing.Text) -> typing.Tuple[typing.Text, bool]
        """Return the attribute value and whether it's the default value.

            Args:
                key(str): attribute name.
            Returns:
                tuple(str, bool): attribute value and whether it's the default value.
        """
        if isinstance(key, six.string_types):
            return self._get_value(key)
        else:
            raise TypeError(key)

    def keys(self):
        """Return all attribute names in the collection.

            Yields:
                An iterator to all attribute names in the collection.
        """
        for name in self._cache:
            yield name

    def values(self):
        """Return all attribute values in the collection.

            Yields:
                An iterator to all attribute values in the collection.
        """
        for name in self._cache:
            yield self._get_value(name)

    def items(self):
        """Return all attribute names and values in the collection.

            Yields:
                An iterator to tuple pairs of attribute names and values in the collection.
        """
        for name in self._cache:
            yield name, self._get_value(name)

    def _get_names(self):
        # type: () -> typing.List[typing.Text]
        mode = constants.GetDbcAttributeMode.ATTRIBUTE_LIST
        attribute_size = _funcs.nxdb_get_dbc_attribute_size(self._handle, mode, '')
        attribute_info = _funcs.nxdb_get_dbc_attribute(self._handle, mode, '', attribute_size)
        name_string = attribute_info[0]
        name_list = [
            name
            for name in name_string.split(',')
            if name.strip()
        ]
        return name_list

    def _get_enums(self, name):
        # type: (typing.Text) -> typing.List[typing.Text]
        mode = constants.GetDbcAttributeMode.ENUMERATION_LIST
        attribute_size = _funcs.nxdb_get_dbc_attribute_size(self._handle, mode, name)
        attribute_info = _funcs.nxdb_get_dbc_attribute(self._handle, mode, name, attribute_size)
        enum_string = attribute_info[0]
        enum_list = [
            enum
            for enum in enum_string.split(',')
            if enum.strip()
        ]
        return enum_list

    def _get_value(self, name):
        # type: (typing.Text) -> typing.Tuple[typing.Text, bool]
        if name not in self._cache:
            raise KeyError('Attribute name %s not found in DBC attributes' % name)

        mode = constants.GetDbcAttributeMode.ATTRIBUTE
        attribute_size = _funcs.nxdb_get_dbc_attribute_size(self._handle, mode, name)
        attribute_info = _funcs.nxdb_get_dbc_attribute(self._handle, mode, name, attribute_size)
        enums = self._cache[name]
        if not enums:
            return attribute_info

        # This attribute is an enum. Replace the enum index with the enum string.
        index = int(attribute_info[0])
        attribute_info = (enums[index], attribute_info[1])
        return attribute_info
