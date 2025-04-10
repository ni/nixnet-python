from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

try:
    # Python 3.3+
    from collections.abc import Mapping
except ImportError:
    # Python 2.7
    from collections import Mapping  # type: ignore
import typing  # NOQA: F401

import six

from nixnet import _cprops
from nixnet import _funcs
from nixnet import constants  # NOQA: F401

from nixnet.database import _database_object  # NOQA: F401


class DbCollection(Mapping):
    """Collection of database objects."""

    def __init__(self, handle, db_type, prop_id, factory):
        # type: (int, constants.ObjectClass, int, typing.Any) -> None
        self._handle = handle
        self._type = db_type
        self._prop_id = prop_id
        self._factory = factory

    def __repr__(self):
        return '{}(handle={}, db_type={})'.format(type(self).__name__, self._handle, self._type)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            sys_other = typing.cast(DbCollection, other)
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
        return _cprops.get_database_ref_array_len(self._handle, self._prop_id)

    def __iter__(self):
        return self.keys()

    def __getitem__(self, index):
        """Return the database object.

        Args:
            Name of database object
        Returns:
            index(str): Name of database object.
        """
        if isinstance(index, six.string_types):
            ref = _funcs.nxdb_find_object(self._handle, self._type, index)
            return self._factory(_handle=ref)
        else:
            raise TypeError(index)

    def __delitem__(self, index):
        ref = _funcs.nxdb_find_object(self._handle, self._type, index)
        _funcs.nxdb_delete_object(ref)

    def keys(self):
        """Return database object names in the collection.

        Yields:
            An iterator to database object names in the collection.
        """
        for child in self._get_children():
            yield child.name

    def values(self):
        """Return database objects in the collection.

        Yields:
            An iterator to database objects in the collection.
        """
        return self._get_children()

    def items(self):
        """Return all database object names and objects in the collection.

        Yields:
            An iterator to tuple pairs of database object names and objects in the collection
        """
        for child in self._get_children():
            yield child.name, child

    def add(self, name):
        # type: (typing.Text) -> _database_object.DatabaseObject
        """Add a new database object to the collection.

        Args:
            name(str): Name of the new database object.
        Returns:
            ``DatabaseObject``: An instance of the new database object.
        """
        ref = _funcs.nxdb_create_object(self._handle, self._type, name)
        return self._factory(_handle=ref)

    def _get_children(self):
        for ref in _cprops.get_database_ref_array(self._handle, self._prop_id):
            yield self._factory(_handle=ref)
