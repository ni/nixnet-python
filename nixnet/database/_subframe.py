from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _props
from nixnet import constants

from nixnet.database import _collection
from nixnet.database import _database_object
from nixnet.database import _find_object
from nixnet.database import _frame

# workaround to avoid circular imports caused by mypy type annotations
MYPY = False
if MYPY:
    from nixnet.database import _pdu  # NOQA: F401


class SubFrame(_database_object.DatabaseObject):
    """Database subframe"""

    def __init__(
            self,
            **kwargs  # type: int
    ):
        # type: (...) -> None
        if not kwargs or '_handle' not in kwargs:
            raise TypeError()

        self._handle = kwargs['_handle']

        from nixnet.database import _signal
        self._dyn_signals = _collection.DbCollection(
            self._handle, constants.ObjectClass.SIGNAL, _cconsts.NX_PROP_SUBFRM_DYN_SIG_REFS, _signal.Signal)

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
        """Check this subframe's configuration status.


        By default, incorrectly configured subframes in the database are not returned from
        :any:`Frame.mux_subframes` because they cannot be used in the bus communication.
        You can change this behavior by setting :any:`Database.show_invalid_from_open` to `True`.
        When a subframe configuration status becomes invalid after the database is opened,
        the subframe still is returned from :any:`Frame.mux_subframes`
        even if :any:`Database.show_invalid_from_open` is `False`.

        Raises:
            :any:`XnetError`: The subframe is incorrectly configured.
        """
        status_code = _props.get_subframe_config_status(self._handle)
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
    def dyn_signals(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Returns a collection of dynamic :any:`Signal<_signal.Signal>` objects in the subframe.

        Those signals are transmitted when the multiplexer signal
        in the frame has the multiplexer value defined in the subframe.
        """
        return self._dyn_signals

    @property
    def frm(self):
        # type: () -> _frame.Frame
        """:any:`Frame<_frame.Frame>`: Returns the reference to the parent frame.

        The parent frame is defined when the subframe is created,
        and you cannot change it afterwards.
        """
        handle = _props.get_subframe_frm_ref(self._handle)
        return _frame.Frame(_handle=handle)

    @property
    def mux_value(self):
        # type: () -> int
        """int: Get or set the multiplexer value for this subframe.

        This property specifies the multiplexer signal value used when the
        dynamic signals in this subframe are transmitted in the frame.
        Only one subframe is transmitted at a time in the frame.

        There also is a multiplexer value for a signal object as a read-only property.
        It reflects the value set on the parent subframe object.

        This property is required. If the property does not contain a valid value,
        and you create an XNET session that uses this subframe,
        the session returns an error.
        To ensure that the property contains a valid value,
        you can do one of the following:

        *   Use a database file (or alias) to create the session.

            The file formats require a valid value in the text for this property.

        *   Set a value at runtime using this property.

            This is needed when you create your own in-memory database (*:memory:*) rather than use a file.
            The property does not contain a default in this case,
            so you must set a valid value prior to creating a session.
        """
        return _props.get_subframe_mux_value(self._handle)

    @mux_value.setter
    def mux_value(self, value):
        # type: (int) -> None
        _props.set_subframe_mux_value(self._handle, value)

    @property
    def name(self):
        # type: () -> typing.Text
        """str: Get or set the name of the subframe object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.), and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        A subframe name must be unique for all subframes in a frame.

        This short name does not include qualifiers to ensure that it is unique,
        such as the database, cluster, and frame name. It is for display purposes.
        """
        return _props.get_subframe_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_subframe_name(self._handle, value)

    @property
    def pdu(self):
        # type: () -> _pdu.Pdu
        """:any:`Pdu`: Returns the subframe's parent PDU.

        This property returns the reference to the subframe's parent PDU.
        The parent PDU is defined when the subframe object is created.
        You cannot change it afterwards.
        """
        from nixnet.database import _pdu  # NOQA: F811
        handle = _props.get_subframe_pdu_ref(self._handle)
        return _pdu.Pdu(_handle=handle)

    @property
    def name_unique_to_cluster(self):
        # type: () -> typing.Text
        """str: Returns a subframe name unique to the cluster that contains the subframe.

        If the single name is not unique within the cluster, the name is <frame-name>.<subframe-name>.

        You can pass the name to the `find` function to retrieve the reference to the object,
        while the single name is not guaranteed success in `find`
        because it may be not unique in the cluster.
        """
        return _props.get_subframe_name_unique_to_cluster(self._handle)
