from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import typing  # NOQA: F401
import warnings

from nixnet import _cconsts
from nixnet import _funcs
from nixnet import _props
from nixnet import constants
from nixnet import errors

from nixnet.db import _cluster
from nixnet.db import _collection


class Database(object):

    def __init__(self, database_name):
        self._handle = None  # To satisfy `__del__` in case nxdb_open_database throws
        self._handle = _funcs.nxdb_open_database(database_name)
        self._clusters = _collection.DbCollection(
            self._handle, constants.ObjectClass.CLUSTER, _cconsts.NX_PROP_DATABASE_CLST_REFS, _cluster.Cluster)

    def __del__(self):
        if self._handle is not None:
            warnings.warn(
                'Database was not explicitly closed before it was destructed. '
                'Resources on the device may still be reserved.',
                errors.XnetResourceWarning)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
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

    def __repr__(self):
        return 'Database(handle={0})'.format(self._handle)

    def close(self, close_all_refs=False):
        if self._handle is None:
            warnings.warn(
                'Attempting to close NI-XNET system but system was already '
                'closed', errors.XnetResourceWarning)
            return

        _funcs.nxdb_close_database(self._handle, close_all_refs)

        self._handle = None

    def save(self, db_filepath=""):
        # type: (typing.Text) -> None
        _funcs.nxdb_save_database(self._handle, db_filepath)

    @property
    def name(self):
        return _props.get_database_name(self._handle)

    @property
    def clusters(self):
        return self._clusters

    @property
    def show_invalid_from_open(self):
        return _props.get_database_show_invalid_from_open(self._handle)

    @show_invalid_from_open.setter
    def show_invalid_from_open(self, value):
        _props.set_database_show_invalid_from_open(self._handle, value)
