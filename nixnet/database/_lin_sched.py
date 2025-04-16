import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _props
from nixnet import constants

from nixnet.database import _cluster
from nixnet.database import _collection
from nixnet.database import _database_object
from nixnet.database import _find_object


class LinSched(_database_object.DatabaseObject):
    """Database LIN schedule"""

    def __init__(
            self,
            **kwargs  # type: int
    ):
        # type: (...) -> None
        if not kwargs or '_handle' not in kwargs:
            raise TypeError()

        self._handle = kwargs['_handle']

        from nixnet.database import _lin_sched_entry
        self._entries = _collection.DbCollection(
            self._handle,
            constants.ObjectClass.LIN_SCHED_ENTRY,
            _cconsts.NX_PROP_LIN_SCHED_ENTRIES,
            _lin_sched_entry.LinSchedEntry)

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

    def check_config_status(self):
        # type: () -> None
        """Check this LIN schedule's configuration status.

        By default, incorrectly configured schedules in the database are not returned from
        :any:`Cluster.lin_schedules` because they cannot be used in the bus communication.
        You can change this behavior by setting :any:`Database.show_invalid_from_open` to `True`.
        When a schedule configuration status becomes invalid after the database is opened,
        the schedule still is returned from :any:`Cluster.lin_schedules`
        even if :any:`Database.show_invalid_from_open` is `False`.

        Raises:
            :any:`XnetError`: The LIN schedule is incorrectly configured.
        """
        status_code = _props.get_lin_sched_config_status(self._handle)
        _errors.check_for_error(status_code)

    def find(
            self,
            object_class,  # type: typing.Type[_database_object.DatabaseObject]
            object_name,  # type: typing.Text
    ):
        # type: (...) -> _database_object.DatabaseObject
        """Finds an object in the database.

        This function finds a database object relative to this parent object.
        This object may be a grandparent or great-grandparent.

        If this object is a direct parent
        (for example, :any:`Frame<_frame.Frame>` for :any:`Signal<_signal.Signal>`),
        the ``object_name`` to search for can be short, and the search proceeds quickly.

        If this object is not a direct parent
        (for example, :any:`Database` for :any:`Signal<_signal.Signal>`),
        the ``object_name`` to search for must be qualified such
        that it is unique within the scope of this object.

        For example, if the class of this object is :any:`Cluster`,
        and ``object_class`` is :any:`Signal<_signal.Signal>`,
        you can specify ``object_name`` of ``mySignal``,
        assuming that signal name is unique to the cluster.
        If not, you must include the :any:`Frame<_frame.Frame>` name as a prefix,
        such as ``myFrameA.mySignal``.

        NI-XNET supports the following subclasses of ``DatabaseObject`` as arguments for ``object_class``:

        *   :any:`nixnet.database.Cluster<Cluster>`
        *   :any:`nixnet.database.Frame<_frame.Frame>`
        *   :any:`nixnet.database.Pdu<Pdu>`
        *   :any:`nixnet.database.Signal<_signal.Signal>`
        *   :any:`nixnet.database.SubFrame<SubFrame>`
        *   :any:`nixnet.database.Ecu<Ecu>`
        *   :any:`nixnet.database.LinSched<LinSched>`
        *   :any:`nixnet.database.LinSchedEntry<LinSchedEntry>`

        Args:
            object_class(``DatabaseObject``): The class of the object to find.
            object_name(str): The name of the object to find.
        Returns:
            An instance of the found object.
        Raises:
            ValueError: Unsupported value provided for argument ``object_class``.
            :any:`XnetError`: The object is not found.
        """
        return _find_object.find_object(self._handle, object_class, object_name)

    @property
    def clst(self):
        # type: () -> _cluster.Cluster
        """:any:`Cluster`: Get the parent cluster in which the you created the schedule.

        You cannot change the parent cluster after creating the schedule object.
        """
        handle = _props.get_lin_sched_clst_ref(self._handle)
        return _cluster.Cluster(_handle=handle)

    @property
    def comment(self):
        # type: () -> typing.Text
        """str: Get or set a comment describing the schedule object.

        A comment is a string containing up to 65535 characters.
        """
        return _props.get_lin_sched_comment(self._handle)

    @comment.setter
    def comment(self, value):
        # type: (typing.Text) -> None
        _props.set_lin_sched_comment(self._handle, value)

    @property
    def entries(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Collection of :any:`LinSchedEntry` for this LIN schedule.

        The position of each entry in this collection specifies the position in the schedule.
        The database file and/or the order that you create entries at runtime determine the position.
        """
        return self._entries

    @property
    def name(self):
        # type: () -> typing.Text
        """str: Get or set the name of the LIN schedule object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.),
        and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        A schedule name must be unique for all schedules in a cluster.
        """
        return _props.get_lin_sched_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_lin_sched_name(self._handle, value)

    @property
    def priority(self):
        # type: () -> int
        """int: Get or set the priority of a run-once LIN schedule.

        This priority applies when multiple run-once schedules are pending for execution.

        The valid range for this property is 1-254.
        Lower values correspond to higher priority.

        This property applies only when the :any:`LinSched.run_mode` property is ``ONCE``.
        Run-once schedule requests are queued for execution based on this property.
        When all run-once schedules have completed,
        the master returns to the previously running continuous schedule (or null).

        Run-continuous schedule requests are not queued.
        Only the most recent run-continuous schedule is used,
        and it executes only if no run-once schedule is pending.
        Therefore, a run-continuous schedule has an effective priority of ``255``,
        but this property is not used.

        Null schedule requests take effect immediately
        and supercede any running run-once or run-continuous schedule.
        The queue of pending run-once schedule requests
        is flushed (emptied without running them).
        Therefore, a null schedule has an effective priority of ``0``,
        but this property is not used.

        This property is not read from the database,
        but is handled like a database property.
        After opening the database, the default value is returned,
        and you can change the property.
        But similar to database properties,
        you cannot change it after a session is created.
        """
        return _props.get_lin_sched_priority(self._handle)

    @priority.setter
    def priority(self, value):
        # type: (int) -> None
        _props.set_lin_sched_priority(self._handle, value)

    @property
    def run_mode(self):
        # type: () -> constants.LinSchedRunMode
        """:any:`LinSchedRunMode`: Get or set how the master runs this schedule.

        This property is not read from the database,
        but is handled like a database property.
        After opening the database, the default value is returned,
        and you can change the property.
        But similar to database properties,
        you cannot change it after a session is created.

        Usually, the default value for the run mode is ``CONTINUOUS``.
        If the schedule is configured to be a collision resolving table
        for an event-triggered entry, the default is ``ONCE``.
        """
        return constants.LinSchedRunMode(_props.get_lin_sched_run_mode(self._handle))

    @run_mode.setter
    def run_mode(self, value):
        # type: (constants.LinSchedRunMode) -> None
        _props.set_lin_sched_run_mode(self._handle, value.value)
