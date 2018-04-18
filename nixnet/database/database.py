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

from nixnet.database import _collection


class Database(object):
    """Opens a database file.

    When an already open database is opened,
    this class grants access to the same database and increases an internal reference counter.
    A multiple referenced (open) database must be closed as many times as it has been opened.
    Until it is completely closed, the access to this database remains granted,
    and the database uses computer resources (memory and handles).
    For more information, refer to :any:`Database.close`.

    Args:
        database_name(str): The database alias or file pathname to open.
    """
    def __init__(self, database_name):
        # type: (typing.Text) -> None
        self._handle = None  # To satisfy `__del__` in case nxdb_open_database throws
        self._handle = _funcs.nxdb_open_database(database_name)

        from nixnet.database import _cluster
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

    def __exit__(self, exception_type, exception_value, traceback):
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
        return '{}(handle={})'.format(type(self).__name__, self._handle)

    def close(self, close_all_refs=False):
        # type: (bool) -> None
        """Closes the database.

        For the case that different threads of an application are using the same database,
        :any:`Database` and :any:`Database.close`
        maintain a reference counter indicating how many times the database is open.
        Every thread can open the database, work with it,
        and close the database independently using ``close_all_refs`` set to ``False``.
        Only the last call to :any:`Database.close` actually closes access to the database.

        .. note:: ``Database.__exit__`` calls :any:`Database.close` with ``close_all_refs`` set to ``False``.
            See examples of this in :ref:`can_dynamic_database_creation_label`
            and :ref:`lin_dynamic_database_creation_label`.

        Another option is that only one thread executes :any:`Database.close` once,
        using ``close_all_refs`` set to ``True``, which closes access for all other threads.
        This may be convenient when, for example,
        the main program needs to stop all running threads
        and be sure the database is closed properly,
        even if some threads could not execute :any:`Database.close`.

        Args:
            close_all_refs(bool): Indicates that a database open multiple times
                (refer to :any:`Database`) should be closed completely
                (``close_all_refs`` is ``True``),
                or just the reference counter should be decremented
                (``close_all_refs`` is ``False``),
                and the database remains open.
                When the database is closed completely,
                all references to objects in this database become invalid.
        """
        if self._handle is None:
            warnings.warn(
                'Attempting to close NI-XNET database but database was already '
                'closed', errors.XnetResourceWarning)
            return

        _funcs.nxdb_close_database(self._handle, close_all_refs)
        self._handle = None

    def save(self, db_filepath=""):
        # type: (typing.Text) -> None
        """Saves the open database to a FIBEX 3.1.0 file.

        The file extension must be .xml. If the target file exists, it is overwritten.

        XNET saves to the FIBEX file only features that XNET sessions use to communicate on the network.
        If the original file was created using non-XNET software,
        the target file may be missing details from the original file.
        For example, NI-XNET supports only linear scaling.
        If the original FIBEX file used a rational equation that cannot be expressed as a linear scaling,
        XNET converts this to a linear scaling with factor 1.0 and offset 0.0.

        If ``db_filepath`` is empty, the file is saved to the same FIBEX file specified when opened.
        If opened as a file path, it uses that file path.
        If opened as an alias, it uses the file path registered for that alias.

        Saving a database is not supported under Real-Time (RT),
        but you can deploy and use a database saved on Windows on a Real-Time (RT) target (refer to `Database.deploy`).

        Args:
            db_filepath(str): Contains the pathname to the database file or is
                empty (saves to the original filepath).
        """
        _funcs.nxdb_save_database(self._handle, db_filepath)

    @property
    def name(self):
        # type: () -> typing.Text
        return _props.get_database_name(self._handle)

    @property
    def clusters(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Returns a collection of :any:`Cluster` objects in this database.

        A cluster is assigned to a database when the cluster object is created.
        You cannot change this assignment afterwards.

        FIBEX and AUTOSAR files can contain any number of clusters,
        and each cluster uses a unique name.

        For CANdb (.dbc), LDF (.ldf), or NI-CAN (.ncd) files,
        the file contains only one cluster, and no cluster name is stored in the file.
        For these database formats, NI-XNET uses the name Cluster for the single cluster.
        """
        return self._clusters

    @property
    def show_invalid_from_open(self):
        # type: () -> bool
        """bool: Show or hide :any:`Frame<_frame.Frame>` and :any:`Signal<_signal.Signal>` objects that are invalid.

        After opening a database, this property always is set to ``False``,
        meaning that invalid :any:`Cluster`, :any:`Frame<_frame.Frame>`,
        and :any:`Signal<_signal.Signal>` objects
        are not returned in properties that return a :any:`DbCollection` for the database
        (for example, :any:`Cluster.frames` and :any:`Frame.mux_static_signals`).
        Invalid :any:`Cluster`, :any:`Frame<_frame.Frame>`,
        and :any:`Signal<_signal.Signal>` objects are incorrectly defined
        and therefore cannot be used in the bus communication.
        The ``False`` setting is recommended when you use the database to create XNET sessions.

        In case the database was opened to correct invalid configuration
        (for example, in a database editor),
        you must set the property to ``True`` prior to reading properties that return
        a :any:`DbCollection` for the database
        (for example, :any:`Cluster.frames` and :any:`Frame.mux_static_signals`).

        For invalid objects,
        the :any:`Cluster.check_config_status`,
        :any:`Frame.check_config_status`,
        and :any:`Signal.check_config_status` methods raise an exception if there is a problem.
        For valid objects, no error is raised.

        :any:`Cluster`, :any:`Frame<_frame.Frame>`, and :any:`Signal<_signal.Signal>` objects that became
        invalid after the database is opened are still returned from the
        :any:`Database.clusters`, :any:`Cluster.frames`, and :any:`Frame.mux_static_signals`,
        even if :any:`Database.show_invalid_from_open` is ``False``
        and Configuration Status returns an error code.
        For example, if you open a :any:`Frame<_frame.Frame>` with valid properties,
        then you set :any:`Signal.start_bit` beyond the :any:`Frame.payload_len`,
        :any:`Frame.check_config_status` raises an exception,
        but the frame is returned from :any:`Cluster.frames`.
        """
        return _props.get_database_show_invalid_from_open(self._handle)

    @show_invalid_from_open.setter
    def show_invalid_from_open(self, value):
        # type: (bool) -> None
        _props.set_database_show_invalid_from_open(self._handle, value)
