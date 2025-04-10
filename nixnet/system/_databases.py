﻿from __future__ import absolute_import
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

from nixnet import _funcs


class AliasCollection(Mapping):
    """Alias aliases."""

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle

    def __repr__(self):
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(AliasCollection, other)._handle
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
        return self._get_database_len('')

    def __iter__(self):
        return self.keys()

    def __getitem__(self, index):
        # type: (typing.Text) -> Alias
        """Return the Alias object associated with the specified alias.

            Args:
                index(str): The value of the index (alias name).
        """
        if isinstance(index, six.string_types):
            for alias, filepath in self._get_database_list(''):
                if alias == index:
                    return self._create_item(alias, filepath)
            else:
                raise KeyError('Alias alias %s not found in the system' % index)
        else:
            raise TypeError(index)

    def __delitem__(self, index):
        # type: (typing.Text) -> None
        """Delete/Remove a database alias from the system.

        This function removes the alias from NI-XNET, but does not affect the
        database text file. It just removes the alias association to the
        database file path.

        This function is supported on Windows only, and the alias is removed
        from Windows only (not RT targets). Use 'undeploy' to remove an alias
        from a Real-Time (RT) target.

        Args:
            index(str): The name of the alias to delete.
        """
        _funcs.nxdb_remove_alias(index)

    def keys(self):
        """Return all keys (alias names) used in the AliasCollection object.

            Yields:
                An iterator to all the keys in the Alias object.
        """
        for alias, _ in self._get_database_list(''):
            yield alias

    def values(self):
        """Return all Alias objects in the system.

            Yields:
                An iterator to all the values in the AliasCollection object.
        """
        for alias, filepath in self._get_database_list(''):
            yield self._create_item(alias, filepath)

    def items(self):
        """Return all aliases and database objects associated with those aliases in the system.

            Yields:
                An iterator to tuple pairs of alias and database objects in the system.
        """
        for alias, filepath in self._get_database_list(''):
            yield alias, self._create_item(alias, filepath)

    def add_alias(self, database_alias, database_filepath, default_baud_rate=None):
        # type: (typing.Text, typing.Text, typing.Optional[int]) -> None
        """Add a new alias with baud rate size of up to 64 bits to a database file.

        NI-XNET uses alias names for database files. The alias names provide a
        shorter name for display, allow for changes to the file system without
        changing the application.

        This function is supported on Windows only.

        Args:
            database_alias(str): Provides the desired alias name. Unlike the names of
                other XNET database objects, the alias name can use special
                characters such as space and dash. Commas are not allowed in the
                alias name. If the alias name already exists, this function
                changes the previous filepath to the specified filepath.
            database_filepath(str): Provides the path to the CANdb, FIBEX, or LDF
                file. Commas are not allowed in the filepath name.
            default_baud_rate(int): Provides the default baud rate, used when
                filepath refers to a CANdb database (.dbc) or an NI-CAN database
                (.ncd). These database formats are specific to CAN and do not
                specify a cluster baud rate. Use this default baud rate to
                specify a default CAN baud rate to use with this alias. If
                database_filepath refers to a FIBEX database (.xml) or LIN LDF
                file, the default_baud_rate parameter is ignored. The FIBEX and
                LDF database formats require a valid baud rate for every
                cluster, and NI-XNET uses that baud rate as the default.
        """
        if default_baud_rate is None:
            default_baud_rate = 0

        _funcs.nxdb_add_alias64(database_alias, database_filepath, default_baud_rate)

    def _create_item(self, database_alias, database_filepath):
        # type: (typing.Text, typing.Text) -> Alias
        return Alias(database_alias, database_filepath)

    @staticmethod
    def _get_database_len(ip_address):
        # type: (typing.Text) -> int
        alias_buffer_size, filepath_buffer_size = _funcs.nxdb_get_database_list_sizes(ip_address)
        _, _, number_of_databases = _funcs.nxdb_get_database_list(ip_address, alias_buffer_size, filepath_buffer_size)
        return number_of_databases

    @staticmethod
    def _get_database_list(ip_address):
        # type: (typing.Text) -> typing.List[typing.Tuple[typing.Text, typing.Text]]
        alias_buffer_size, filepath_buffer_size = _funcs.nxdb_get_database_list_sizes(ip_address)
        aliases, filepaths, _ = _funcs.nxdb_get_database_list(ip_address, alias_buffer_size, filepath_buffer_size)
        return list(zip(aliases.split(","), filepaths.split(",")))


class Alias(object):
    """Alias alias."""

    def __init__(
            self,
            database_alias,
            database_filepath,
    ):
        # type: (typing.Text, typing.Text) -> None
        self._database_alias = database_alias
        self._database_filepath = database_filepath

    def __repr__(self):
        return '{}(alias={}, filepath={})'.format(
            type(self).__name__, self._database_alias, self._database_filepath)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_db = typing.cast(Alias, other)
            return self.alias == other_db.alias and self.filepath == other_db.filepath
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        else:
            return not result

    def __hash__(self):
        return hash(self.alias)

    @property
    def alias(self):
        return self._database_alias

    @property
    def filepath(self):
        # type: () -> typing.Text
        """str: Get the filepath associated with the Alias object"""
        return self._database_filepath
