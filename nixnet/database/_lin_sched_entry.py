from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _props
from nixnet import constants

from nixnet.database import _database_object
from nixnet.database import _frame
from nixnet.database import _lin_sched


class LinSchedEntry(_database_object.DatabaseObject):
    """Database LIN schedule entry"""

    def __init__(
            self,
            **kwargs  # type: int
    ):
        # type: (...) -> None
        if not kwargs or '_handle' not in kwargs:
            raise TypeError()

        self._handle = kwargs['_handle']

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

    @property
    def collision_res_sched(self):
        # type: () -> typing.Optional[_lin_sched.LinSched]
        """:any:`LinSched`: Get or set a LIN schedule that resolves a collision for this event-triggered entry.

        This property applies only when :any:`LinSchedEntry.type` is ``EVENT_TRIGGERED``.
        When a collision occurs for the event-triggered entry in this schedule,
        the master must switch to the collision resolving schedule to transfer the unconditional frames successfully.

        Raises:
            :any:`XnetError`: The property requires that :any:`LinSchedEntry.type` be set to ``EVENT_TRIGGERED``.
        """
        handle = _props.get_lin_sched_entry_collision_res_sched(self._handle)
        if handle == 0:
            _errors.raise_xnet_error(_cconsts.NX_ERR_DATABASE_OBJECT_NOT_FOUND)

        return _lin_sched.LinSched(_handle=handle)

    @collision_res_sched.setter
    def collision_res_sched(self, value):
        # type: (_lin_sched.LinSched) -> None
        _props.set_lin_sched_entry_collision_res_sched(self._handle, value._handle)

    @property
    def delay(self):
        # type: () -> float
        """float: Get or set the time from the start of this entry (slot) to the start of the next entry.

        The property uses a float value in seconds, with the fractional part used for milliseconds or microseconds.
        """
        return _props.get_lin_sched_entry_delay(self._handle)

    @delay.setter
    def delay(self, value):
        # type: (float) -> None
        _props.set_lin_sched_entry_delay(self._handle, value)

    @property
    def event_id(self):
        # type: () -> int
        """int: Get or set the event-triggered entry identifier.

        This identifier is unprotected (NI-XNET handles the protection).

        This property applies only when :any:`LinSchedEntry.type` is ``EVENT_TRIGGERED``.
        This identifier is for the event triggered entry itself,
        and the first payload byte is for the protected identifier of the contained unconditional frame.
        """
        return _props.get_lin_sched_entry_event_id(self._handle)

    @event_id.setter
    def event_id(self, value):
        # type: (int) -> None
        _props.set_lin_sched_entry_event_id(self._handle, value)

    @property
    def frames(self):
        # type: () -> typing.Iterable[_frame.Frame]
        """list of :any:`Frame<_frame.Frame>`: Get or set a list of frames for this LIN schedule entry.

        If :any:`LinSchedEntry.type` is ``UNCONDITIONAL``,
        this list contains one frame,
        which is the single unconditional frame for this entry.

        If :any:`LinSchedEntry.type` is ``SPORADIC``,
        this list contains one or more unconditional frames for this entry.
        When multiple frames are pending for this entry,
        the order in the list determines the priority to transmit.

        If :any:`LinSchedEntry.type` is ``EVENT_TRIGGERED``,
        this list contains one or more unconditional frames for this entry.
        When multiple frames for this entry are pending to be sent by distinct slaves,
        this property uses the :any:`LinSchedEntry.collision_res_sched` to process the frames.
        """
        for ref in _props.get_lin_sched_entry_frames(self._handle):
            yield _frame.Frame(_handle=ref)

    @frames.setter
    def frames(self, value):
        # type: (typing.Iterable[_frame.Frame]) -> None
        frame_handles = [frame._handle for frame in value]
        _props.set_lin_sched_entry_frames(self._handle, frame_handles)

    @property
    def name(self):
        # type: () -> typing.Text
        """str: Get or set the name of the LIN schedule entry object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.), and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        A schedule entry name must be unique for all entries in the same schedule.
        """
        return _props.get_lin_sched_entry_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_lin_sched_entry_name(self._handle, value)

    @property
    def name_unique_to_cluster(self):
        # type: () -> typing.Text
        """str: Returns a LIN schedule entry name unique to the cluster that contains the object.

        If the single name is not unique within the cluster,
        the name is <schedule-name>.<schedule-entry-name>.

        You can pass the name to the `find` function to retrieve the reference to the object,
        while the single name is not guaranteed success in `find`
        because it may be not unique in the cluster.
        """
        return _props.get_lin_sched_entry_name_unique_to_cluster(self._handle)

    @property
    def sched(self):
        # type: () -> _lin_sched.LinSched
        """:any:`LinSched`: Returns the LIN schedule that uses this entry.

        This LIN schedule is considered this entry's parent.
        You define the parent schedule when you create the entry object.
        You cannot change it afterwards.
        """
        handle = _props.get_lin_sched_entry_sched(self._handle)
        lin_sched = _lin_sched.LinSched(_handle=handle)
        return lin_sched

    @property
    def type(self):
        # type: () -> constants.LinSchedEntryType
        """:any:`LinSchedEntryType`: Get or set the LIN schedule entry type.

        All frames that contain a payload are ``UNCONDITIONAL``.
        The LIN schedule entry type determines the mechanism for transferring frames in this entry (slot).
        """
        return constants.LinSchedEntryType(_props.get_lin_sched_entry_type(self._handle))

    @type.setter
    def type(self, value):
        # type: (constants.LinSchedEntryType) -> None
        _props.set_lin_sched_entry_type(self._handle, value.value)

    @property
    def nc_ff_data_bytes(self):
        # type: () -> typing.Iterable[int]
        """list of int: Get or set a list of 8 ints containing raw data for LIN node configuration.

        Node configuration defines a set of services used to configure slave nodes in the cluster.
        Every service has a specific set of parameters coded in this int list.
        In the LDF, file those parameters are stored, for example, in the node (ECU) or the frame object.
        NI-XNET LDF reader composes those parameters to the byte values like they are sent on the bus.
        The LIN specification document describes the node configuration services
        and the mapping of the parameters to the free format bytes.

        The node configuration service is executed only if
        :any:`LinSchedEntry.type` is set to ``NODE_CONFIG_SERVICE``.

        .. warning:: This property is not saved to the FIBEX file.
            If you write this property, save the database, and reopen it,
            the node configuration services are not contained in the database.
            Writing this property is useful only in the NI-XNET session immediately following.
        """
        return _props.get_lin_sched_entry_nc_ff_data_bytes(self._handle)

    @nc_ff_data_bytes.setter
    def nc_ff_data_bytes(self, value):
        # type: (typing.List[int]) -> None
        _props.set_lin_sched_entry_nc_ff_data_bytes(self._handle, value)
