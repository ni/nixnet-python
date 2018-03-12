from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _props
from nixnet import constants

from nixnet.database import _collection
from nixnet.database import _frame


class SubFrame(object):
    """Database subframe"""

    def __init__(self, handle):
        # type: (int) -> None
        from nixnet.database import _signal
        self._handle = handle
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

    @property
    def config_status(self):
        # type: () -> int
        """int: Returns the subframe object configuration status.

        Configuration Status returns an NI-XNET error code.
        You can pass the value to the `nxStatusToString` function to
        convert the value to a text description of the configuration problem.

        By default, incorrectly configured subframes in the database are not returned from
        :any:`Frame.mux_subframes` because they cannot be used in the bus communication.
        You can change this behavior by setting :any:`Database.show_invalid_from_open` to ``True``.
        When the configuration status of a subframe becomes invalid after opening the database,
        the subframe still is returned from :any:`Frame.mux_subframes`
        even if :any:`Database.show_invalid_from_open` is ``False``.
        """
        return _props.get_subframe_config_status(self._handle)

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
        return _frame.Frame(handle)

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
        # actually returns _pdu.Pdu, but avoiding a circular import
        # type: () -> typing.Any
        """:any:`Pdu`: Returns the subframe's parent PDU.

        This property returns the reference to the subframe's parent PDU.
        The parent PDU is defined when the subframe object is created.
        You cannot change it afterwards.
        """
        from nixnet.database import _pdu
        handle = _props.get_subframe_pdu_ref(self._handle)
        return _pdu.Pdu(handle)

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
