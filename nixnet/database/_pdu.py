from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _props
from nixnet import constants

from nixnet.database import _cluster
from nixnet.database import _collection
from nixnet.database import _frame
from nixnet.database import _signal


class Pdu(object):
    """Database PDU"""

    def __init__(self, handle):
        # type: (int) -> None
        from nixnet.database import _signal
        from nixnet.database import _subframe
        self._handle = handle
        self._signals = _collection.DbCollection(
            self._handle, constants.ObjectClass.SIGNAL, _cconsts.NX_PROP_PDU_SIG_REFS, _signal.Signal)
        self._mux_subframes = _collection.DbCollection(
            self._handle, constants.ObjectClass.SUBFRAME, _cconsts.NX_PROP_PDU_MUX_SUBFRAME_REFS, _subframe.SubFrame)

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
    def cluster(self):
        # type: () -> _cluster.Cluster
        """:any:`Cluster`: Get the parent cluster in which the PDU has been created.

        You cannot change the parent cluster after creating the PDU object.
        """
        handle = _props.get_pdu_cluster_ref(self._handle)
        return _cluster.Cluster(handle)

    @property
    def default_payload(self):
        return _props.get_pdu_default_payload(self._handle)

    @default_payload.setter
    def default_payload(self, value):
        _props.set_pdu_default_payload(self._handle, value)

    @property
    def comment(self):
        # type: () -> typing.Text
        """str: Get or set a comment describing the PDU object.

        A comment is a string containing up to 65535 characters.
        """
        return _props.get_pdu_comment(self._handle)

    @comment.setter
    def comment(self, value):
        # type: (typing.Text) -> None
        _props.set_pdu_comment(self._handle, value)

    @property
    def config_status(self):
        # type: () -> int
        """int: Returns the PDU object configuration status.

        Configuration Status returns an NI-XNET error code.
        You can pass the value to the `nxStatusToString` function to
        convert the value to a text description of the configuration problem.

        By default, incorrectly configured frames in the database are not returned from
        :any:`Cluster.frames` because they cannot be used in the bus communication.
        You can change this behavior by setting :any:`Database.show_invalid_from_open` to ``True``.
        When the configuration status of a frames becomes invalid after opening the database,
        the frame still is returned from :any:`Cluster.frames`
        even if :any:`Database.show_invalid_from_open` is ``False``.
        """
        return _props.get_pdu_config_status(self._handle)

    @property
    def frms(self):
        # type: () -> typing.Iterable[_frame.Frame]
        """list of :any:`Frame<_frame.Frame>`: Returns a list of all frames to which the PDU is mapped.

        A PDU is transmitted within the frames to which it is mapped.

        To map a PDU to a frame,
        use the :any:`Frame.pdu_properties` property.
        You can map one PDU to multiple frames.
        """
        for handle in _props.get_pdu_frm_refs(self._handle):
            yield _frame.Frame(handle)

    @property
    def name(self):
        # type: () -> typing.Text
        """str: Get or set the name of the PDU object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.), and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        A PDU name must be unique for all PDUs in a cluster.
        """
        return _props.get_pdu_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_pdu_name(self._handle, value)

    @property
    def payload_len(self):
        # type: () -> int
        """int: Get or set the size of the PDU data in bytes.

        This property is required.
        If the property does not contain a valid value,
        and you create an XNET session that uses this PDU,
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
        return _props.get_pdu_payload_len(self._handle)

    @payload_len.setter
    def payload_len(self, value):
        # type: (int) -> None
        _props.set_pdu_payload_len(self._handle, value)

    @property
    def signals(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Collection of all :any:`Signal<_signal.Signal>` objects in this PDU.

        The collection includes all signals in the PDU,
        including static and dynamic signals and the multiplexer signal.
        """
        return self._signals

    @property
    def mux_is_muxed(self):
        # type: () -> bool
        """bool: Returns ``True`` if the PDU contains a multiplexer signal.

        PDUs containing a multiplexer contain subframes that allow
        using bits of the payload for different information (signals),
        depending on the value of the :any:`SubFrame.mux_value` property.
        """
        return _props.get_pdu_mux_is_muxed(self._handle)

    @property
    def mux_data_mux_sig(self):
        # type: () -> _signal.Signal
        """:any:`Signal<_signal.Signal>`: Data multiplexer signal in the PDU.

        This property returns the reference to the data multiplexer signal.
        If data multiplexer is not defined in the PDU, the property raises an XnetError exception.
        Use the :any:`Pdu.mux_is_muxed` property to determine whether the PDU contains a multiplexer signal.

        You can create a data multiplexer signal by creating a signal
        and then setting the :any:`Signal.mux_is_data_mux` property to ``True``.

        A PDU can contain only one data multiplexer signal.

        Raises:
            XnetError: The data multiplexer is not defined in the PDU.
        """
        handle = _props.get_pdu_mux_data_mux_sig_ref(self._handle)
        if handle == 0:
            # A bit of an abuse of errors
            _errors.check_for_error(_cconsts.NX_ERR_SIGNAL_NOT_FOUND)
        return _signal.Signal(handle)

    @property
    def mux_static_sigs(self):
        # type: () -> typing.Iterable[_signal.Signal]
        """list of :any:`Signal<_signal.Signal>`: Returns a list of static signals in the PDU.

        Returns an list of signal objects in the PDU that do not depend
        on value of the :any:`SubFrame.mux_value` property.
        Static signals are contained in every PDU transmitted,
        as opposed to dynamic signals,
        which are transmitted depending on the value of the :any:`SubFrame.mux_value` property.

        You can create static signals by specifying the PDU as the parent object.
        You can create dynamic signals by specifying a subframe as the parent.

        If the PDU is not multiplexed,
        this property returns the same list as the :any:`Pdu.signals` property.
        """
        for handle in _props.get_pdu_mux_static_sig_refs(self._handle):
            yield _signal.Signal(handle)

    @property
    def mux_subframes(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Collection of :any:`SubFrame` objects in this PDU.

        A subframe defines a group of signals transmitted using the same value of the :any:`SubFrame.mux_value`.
        Only one subframe is transmitted in the PDU at a time.
        """
        return self._mux_subframes
