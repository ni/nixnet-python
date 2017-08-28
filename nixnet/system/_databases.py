from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import typing  # NOQA: F401

import six

from nixnet import _funcs


class Databases(collections.Mapping):
    """Database aliases."""

    def __init__(self, handle):
        self._handle = handle

    def __repr__(self):
        return 'System.Databases(handle={0})'.format(self._handle)

    def __get_database_list(self, ip_address):
        alias_buffer_size, filepath_buffer_size = _funcs.nxdb_get_database_list_sizes(ip_address)
        aliases, filepaths, _ = _funcs.nxdb_get_database_list(ip_address, alias_buffer_size, filepath_buffer_size)
        return list(zip(aliases.split(","), filepaths.split(",")))

    def __len__(self):
        return len(self.__get_database_list(''))

    def __iter__(self):
        return self.keys()

    def __getitem__(self, index):
        # type: (str) -> Database
        """Return the Database object associated with the specified alias.

            Args:
                index(str): The value of the index (alias name).
        """
        if isinstance(index, six.string_types):
            for alias, filepath in self.__get_database_list(''):
                if alias == index:
                    return self._create_item(alias, filepath)
            else:
                raise KeyError('Database alias %s not found in the system' % index)
        else:
            raise TypeError(index)

    def __delitem__(self, index):
        # type: (str) -> None
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

    def _create_item(self, database_alias, database_filepath):
        return Database(database_alias, database_filepath)

    def keys(self):
        """Return all keys (alias names) used in the Databases object.

            Yields:
                An iterator to all the keys in the Database object.
        """
        for alias, _ in self.__get_database_list(''):
            yield alias

    def values(self):
        """Return all Database objects in the system.

            Yields:
                An iterator to all the values in the Databases object.
        """
        for alias, filepath in self.__get_database_list(''):
            yield self._create_item(alias, filepath)

    def items(self):
        """Return all aliases and database objects associated with those aliases in the system.

            Yields:
                An iterator to tuple pairs of alias and database objects in the system.
        """
        for alias, filepath in self.__get_database_list(''):
            yield alias, self._create_item(alias, filepath)

    def add_alias(self, database_alias, database_filepath, default_baud_rate):
        # type: (str, str, int) -> None
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
        _funcs.nxdb_add_alias64(database_alias, database_filepath, default_baud_rate)


class Database(object):
    """Database alias."""

    def __init__(
            self,
            database_alias,
            database_filepath,
    ):
        self._database_alias = database_alias
        self._database_filepath = database_filepath

    def __repr__(self):
        return 'System.Database(alias={}, filepath={})'.format(self._database_alias, self._database_filepath)

    @property
    def filepath(self):
        # type: () -> str
        """str: Get the filepath associated with the Database object"""
        return self._database_filepath
