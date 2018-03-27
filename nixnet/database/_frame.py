from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import operator
import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _props
from nixnet import constants
from nixnet import types

from nixnet.database import _cluster
from nixnet.database import _collection
from nixnet.database import _dbc_attributes
from nixnet.database import _signal


class Frame(object):
    """Database frame"""

    def __init__(self, handle):
        # type: (int) -> None
        from nixnet.database import _subframe
        self._handle = handle
        self._dbc_attributes = None  # type: typing.Optional[_dbc_attributes.DbcAttributeCollection]
        self._mux_static_signals = _collection.DbCollection(
            self._handle, constants.ObjectClass.SIGNAL, _cconsts.NX_PROP_FRM_MUX_STATIC_SIG_REFS, _signal.Signal)
        self._mux_subframes = _collection.DbCollection(
            self._handle, constants.ObjectClass.SUBFRAME, _cconsts.NX_PROP_FRM_MUX_SUBFRAME_REFS, _subframe.SubFrame)

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
    def application_protocol(self):
        # type: () -> constants.AppProtocol
        """:any:`AppProtocol`: Get or set the frame's application protocol."""
        return constants.AppProtocol(_props.get_frame_application_protocol(self._handle))

    @application_protocol.setter
    def application_protocol(self, value):
        # type: (constants.AppProtocol) -> None
        _props.set_frame_application_protocol(self._handle, value.value)

    @property
    def cluster(self):
        # type: () -> _cluster.Cluster
        """:any:`Cluster`: Get the parent cluster in which the frame has been created.

        You cannot change the parent cluster after the frame object has been created.
        """
        handle = _props.get_frame_cluster_ref(self._handle)
        return _cluster.Cluster(handle)

    @property
    def comment(self):
        # type: () -> typing.Text
        """str: Get or set a comment describing the frame object.

        A comment is a string containing up to 65535 characters.
        """
        return _props.get_frame_comment(self._handle)

    @comment.setter
    def comment(self, value):
        # type: (typing.Text) -> None
        _props.set_frame_comment(self._handle, value)

    @property
    def config_status(self):
        # type: () -> int
        """int: Returns the frame object configuration status.

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
        return _props.get_frame_config_status(self._handle)

    @property
    def default_payload(self):
        # type: () -> typing.Iterable[int]
        """list of int: Get or set the frame default payload, specified as a list of ints.

        Each int in the list represents a byte (U8).
        The number of bytes in the list must match the :any:`Frame.payload_len` property.

        This property's initial value is an list of all ``0``,
        except the frame is located in a CAN cluster with J1939 application protocol,
        which uses ``0xFF`` by default.
        For the database formats NI-XNET supports,
        this property is not provided in the database file.

        When you use this frame within an NI-XNET session,
        this property's use varies depending on the session mode.
        The following sections describe this property's behavior for each session mode.

        Frame Output Single-Point and Frame Output Queued Modes:
            Use this property when a frame transmits prior to a call to write.
            This can occur when you set the :any:`SessionBase.auto_start` property to ``False``
            and start a session prior to writing.
            When :any:`SessionBase.auto_start` is ``True`` (default),
            the first frame write also starts frame transmit, so this property is not used.

            The following frame configurations potentially can transmit prior to a call to write:

            *   :any:`Frame.can_timing_type` is  ``CYCLIC_DATA``.
            *   :any:`Frame.can_timing_type` is  ``CYCLIC_REMOTE``.
                (for example, a remote frame received prior to a call to writing).
            *   :any:`Frame.can_timing_type` is  ``EVENT_REMOTE``.
                (for example, a remote frame received prior to a call to writing).
            *   :any:`Frame.can_timing_type` is  ``CYCLIC_EVENT``.
            *   LIN frame in a schedule entry where :any:`LinSchedEntry.type` is ``UNCONDITIONAL``.

            The following frame configurations cannot transmit prior to writing, so this property is not used:

            *   :any:`Frame.can_timing_type` is  ``EVENT_DATA``..
            *   LIN frame in a schedule entry where :any:`LinSchedEntry.type` is ``SPORADIC``
                or ``EVENT_TRIGGERED``.

        Frame Output Stream Mode:
            This property is not used. Transmit is limited to frames provided to write.

        Signal Output Single-Point, Signal Output Waveform, and Signal Output XY Modes:
            Use this property when a frame transmits prior to a call to write.
            Refer to Frame Output Single-Point and Frame Output Queued Modes
            for a list of applicable frame configurations.

            This property is used as the initial payload,
            then each XNET Signal Default Value is mapped into that payload,
            and the result is used for the frame transmit.

        Frame Input Stream and Frame Input Queued Modes:
            This property is not used.
            These modes do not return data prior to receiving frames.

        Frame Input Single-Point Mode:
            This property is used for frames read returns prior to receiving the first frame.

        Signal Input Single-Point, Signal Input Waveform, and Signal Input XY Modes:
            This property is not used.
            Each :any:`Signal.default` is used when
            reading from a session prior to receiving the first frame.
        """
        return _props.get_frame_default_payload(self._handle)

    @default_payload.setter
    def default_payload(self, value):
        # type: (typing.List[int]) -> None
        _props.set_frame_default_payload(self._handle, value)

    @property
    def dbc_attributes(self):
        # type: () -> _dbc_attributes.DbcAttributeCollection
        """:any:`DbcAttributeCollection`: Access the frame's DBC attributes."""
        if self._dbc_attributes is None:
            self._dbc_attributes = _dbc_attributes.DbcAttributeCollection(self._handle)
        return self._dbc_attributes

    @property
    def id(self):
        # type: () -> int
        """int: Get or set the frame identifier.

        This property is required.
        If the property does not contain a valid value,
        and you create an XNET session that uses this frame,
        the session returns an error.
        To ensure that the property contains a valid value,
        you can do one of the following:

        *   Use a database file (or alias) to create the session.

            The file formats require a valid value in the text for this property.

        *   Set a value at runtime using this property.

            This is needed when you create your own in-memory database (*:memory:*) rather than use a file.
            The property does not contain a default in this case,
            so you must set a valid value prior to creating a session.

        CAN:
            For CAN frames, this is the Arbitration ID.

            When :any:`Frame.can_ext_id` is set to ``False``,
            this is the standard CAN identifier with a size of 11 bits,
            which results in allowed range of 0-2047.
            However, the CAN standard disallows identifiers in which the first 7 bits are all recessive,
            so the working range of identifiers is 0-2031.

            When :any:`Frame.can_ext_id` is set to ``True``,
            this is the extended CAN identifier with a size of 29 bits,
            which results in allowed range of 0-536870911.
        LIN:
            For LIN frames, this is the frame's ID (unprotected).
            The valid range for a LIN frame ID is 0-63 (inclusive)
        """
        return _props.get_frame_id(self._handle)

    @id.setter
    def id(self, value):
        # type: (int) -> None
        _props.set_frame_id(self._handle, value)

    @property
    def name(self):
        # type: () -> typing.Text
        """str: String identifying a frame object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.), and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        A frame name must be unique for all frames in a cluster.

        This short name does not include qualifiers to ensure that it is unique,
        such as the database and cluster name.
        It is for display purposes.
        """
        return _props.get_frame_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_frame_name(self._handle, value)

    @property
    def payload_len(self):
        # type: () -> int
        """int: Get or set the number of bytes of data in the payload.

        For CAN and LIN, this is 0-8.

        This property is required.
        If the property does not contain a valid value,
        and you create an XNET session that uses this frame,
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
        return _props.get_frame_payload_len(self._handle)

    @payload_len.setter
    def payload_len(self, value):
        # type: (int) -> None
        _props.set_frame_payload_len(self._handle, value)

    @property
    def sigs(self):
        # type: () -> typing.Iterable[_signal.Signal]
        """list of :any:`Signal<_signal.Signal>`:Get a list of all :any:`Signal<_signal.Signal>` objects in the frame.

        This property returns a list to all :any:`Signal<_signal.Signal>` objects in the frame,
        including static and dynamic signals and the multiplexer signal.
        """
        for handle in _props.get_frame_sig_refs(self._handle):
            yield _signal.Signal(handle)

    @property
    def can_ext_id(self):
        # type: () -> bool
        """bool: Get or set whether the :any:`Frame.id` property in a CAN cluster is extended.

        The frame identifier represents a standard 11-bit (``False``) or extended 29-bit (``True``) arbitration ID.
        """
        return _props.get_frame_can_ext_id(self._handle)

    @can_ext_id.setter
    def can_ext_id(self, value):
        # type: (bool) -> None
        _props.set_frame_can_ext_id(self._handle, value)

    @property
    def can_timing_type(self):
        # type: () -> constants.FrmCanTiming
        """:any:`FrmCanTiming`: Get or set the CAN frame timing.

        Because this property specifies the behavior of the frame's transfer within the embedded system
        (for example, a vehicle),
        it describes the transfer between ECUs in the network.
        In the following description,
        transmitting ECU refers to the ECU that transmits the CAN data frame
        (and possibly receives the associated CAN remote frame).
        Receiving ECU refers to an ECU that receives the CAN data frame
        (and possibly transmits the associated CAN remote frame).

        When you use the frame within an NI-XNET session,
        an output session acts as the transmitting ECU,
        and an input session acts as a receiving ECU.
        For a description of how these CAN timing types apply to the NI-XNET session mode,
        refer to `CAN Timing Type and Session Mode`.

        If you are using a FIBEX or AUTOSAR database,
        this property is a required part of the XML schema for a frame,
        so the default (initial) value is obtained from the file.

        If you are using a CANdb (.dbc) database,
        this property is an optional attribute in the file.
        If NI-XNET finds an attribute named GenMsgSendType,
        that attribute is the default value of this property.
        If the GenMsgSendType attribute begins with cyclic,
        this property's default value is ``CYCLIC_DATA``;
        otherwise, it is ``EVENT_DATA``.
        If the CANdb file does not use the GenMsgSendType attribute,
        this property uses a default value of ``EVENT_DATA``,
        which you can change in your application.

        If you are using an .ncd database or an in-memory database,
        this property uses a default value of ``EVENT_DATA``.
        Within your application,
        change this property to the desired timing type.
        """
        return constants.FrmCanTiming(_props.get_frame_can_timing_type(self._handle))

    @can_timing_type.setter
    def can_timing_type(self, value):
        # type: (constants.FrmCanTiming) -> None
        _props.set_frame_can_timing_type(self._handle, value.value)

    @property
    def can_tx_time(self):
        # type: () -> float
        """float: Get or set the time between consecutive frames from the transmitting ECU.

        The units are in seconds.

        Although the fractional part of the float can provide resolution of picoseconds,
        the NI-XNET CAN transmit supports an accuracy of 500 microseconds.
        Therefore, when used within an NI-XNET output session,
        this property is rounded to the nearest 500 microsecond increment (0.0005).

        For a :any:`Frame.can_timing_type` of ``CYCLIC_DATA`` or ``CYCLIC_REMOTE``,
        this property specifies the time between consecutive data/remote frames.
        A time of 0.0 is invalid.

        For a :any:`Frame.can_timing_type` of ``EVENT_DATA`` or ``EVENT_REMOTE``,
        this property specifies the minimum time between consecutive
        data/remote frames when the event occurs quickly.
        This is also known as the debounce time or minimum interval.
        The time is measured from the end of previous frame (acknowledgment) to the start of the next frame.
        A time of 0.0 specifies no minimum (back to back frames allowed).

        If you are using a FIBEX or AUTOSAR database,
        this property is a required part of the XML schema for a frame,
        so the default (initial) value is obtained from the file.

        If you are using a CANdb (.dbc) database,
        this property is an optional attribute in the file.
        If NI-XNET finds an attribute named GenMsgCycleTime,
        that attribute is interpreted as a number of milliseconds and used as the default value of this property.
        If the CANdb file does not use the GenMsgCycleTime attribute,
        this property uses a default value of 0.1 (100 ms),
        which you can change in your application.

        If you are using a .ncd database or an in-memory database,
        this property uses a default value of 0.1 (100 ms).
        Within your application, change this property to the desired time.
        """
        return _props.get_frame_can_tx_time(self._handle)

    @can_tx_time.setter
    def can_tx_time(self, value):
        # type: (float) -> None
        _props.set_frame_can_tx_time(self._handle, value)

    @property
    def flex_ray_base_cycle(self):
        return _props.get_frame_flex_ray_base_cycle(self._handle)

    @flex_ray_base_cycle.setter
    def flex_ray_base_cycle(self, value):
        _props.set_frame_flex_ray_base_cycle(self._handle, value)

    @property
    def flex_ray_ch_assign(self):
        return _props.get_frame_flex_ray_ch_assign(self._handle)

    @flex_ray_ch_assign.setter
    def flex_ray_ch_assign(self, value):
        _props.set_frame_flex_ray_ch_assign(self._handle, value)

    @property
    def flex_ray_cycle_rep(self):
        return _props.get_frame_flex_ray_cycle_rep(self._handle)

    @flex_ray_cycle_rep.setter
    def flex_ray_cycle_rep(self, value):
        _props.set_frame_flex_ray_cycle_rep(self._handle, value)

    @property
    def flex_ray_preamble(self):
        return _props.get_frame_flex_ray_preamble(self._handle)

    @flex_ray_preamble.setter
    def flex_ray_preamble(self, value):
        _props.set_frame_flex_ray_preamble(self._handle, value)

    @property
    def flex_ray_startup(self):
        return _props.get_frame_flex_ray_startup(self._handle)

    @flex_ray_startup.setter
    def flex_ray_startup(self, value):
        _props.set_frame_flex_ray_startup(self._handle, value)

    @property
    def flex_ray_sync(self):
        return _props.get_frame_flex_ray_sync(self._handle)

    @flex_ray_sync.setter
    def flex_ray_sync(self, value):
        _props.set_frame_flex_ray_sync(self._handle, value)

    @property
    def flex_ray_timing_type(self):
        return _props.get_frame_flex_ray_timing_type(self._handle)

    @flex_ray_timing_type.setter
    def flex_ray_timing_type(self, value):
        _props.set_frame_flex_ray_timing_type(self._handle, value)

    @property
    def flex_ray_in_cyc_rep_enabled(self):
        return _props.get_frame_flex_ray_in_cyc_rep_enabled(self._handle)

    @property
    def flex_ray_in_cyc_rep_i_ds(self):
        return _props.get_frame_flex_ray_in_cyc_rep_i_ds(self._handle)

    @flex_ray_in_cyc_rep_i_ds.setter
    def flex_ray_in_cyc_rep_i_ds(self, value):
        _props.set_frame_flex_ray_in_cyc_rep_i_ds(self._handle, value)

    @property
    def flex_ray_in_cyc_rep_ch_assigns(self):
        return _props.get_frame_flex_ray_in_cyc_rep_ch_assigns(self._handle)

    @flex_ray_in_cyc_rep_ch_assigns.setter
    def flex_ray_in_cyc_rep_ch_assigns(self, value):
        _props.set_frame_flex_ray_in_cyc_rep_ch_assigns(self._handle, value)

    @property
    def lin_checksum(self):
        # type: () -> constants.FrmLinChecksum
        """:any:`FrmLinChecksum`: Returns whether the LIN frame transmitted checksum is classic or enhanced.

        The enhanced checksum considers the protected identifier when it is generated.

        The checksum is determined from the :any:`Ecu.lin_protocol_ver` properties
        of the transmitting and receiving the frame.
        The lower version of both ECUs is significant.
        If the LIN version of both ECUs is 2.0 or higher,
        the checksum type is enhanced;
        otherwise, the checksum type is classic.

        Diagnostic frames (with decimal identifier 60 or 61) always use classic checksum,
        even on LIN 2.x.
        """
        return constants.FrmLinChecksum(_props.get_frame_lin_checksum(self._handle))

    @property
    def mux_is_muxed(self):
        # type: () -> bool
        """bool: Returns whether this frame is data multiplexed.

        This property returns ``True`` if the frame contains a multiplexer signal.
        Frames containing a multiplexer contain subframes that allow using bits
        of the frame payload for different information (signals) depending on
        the multiplexer value.
        """
        return _props.get_frame_mux_is_muxed(self._handle)

    @property
    def mux_data_mux_sig(self):
        # type: () -> _signal.Signal
        """:any:`Signal<_signal.Signal>`: Returns a data multiplexer signal object in the frame.

        Use the :any:`Frame.mux_is_muxed` property to determine whether the frame contains a multiplexer signal.

        You can create a data multiplexer signal by creating a signal
        and then setting the :any:`Signal.mux_is_data_mux` property to ``True``.

        A frame can contain only one data multiplexer signal.

        Raises:
            XnetError: The data multiplexer signal is not defined in the frame
        """
        ref = _props.get_frame_mux_data_mux_sig_ref(self._handle)
        if ref == 0:
            # A bit of an abuse of errors
            _errors.check_for_error(_cconsts.NX_ERR_SIGNAL_NOT_FOUND)
        return _signal.Signal(ref)

    @property
    def mux_static_signals(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Collection of static :any:`Signal<_signal.Signal>` objects in this frame.

        Static signals are contained in every frame transmitted,
        as opposed to dynamic signals,
        which are transmitted depending on the multiplexer value.

        If the frame is not multiplexed,
        this property returns the same objects as :any:`Frame.sigs`.
        """
        return self._mux_static_signals

    @property
    def mux_subframes(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Collection of :any:`SubFrame` objects in this frame.

        A subframe defines a group of signals transmitted using the same multiplexer value.
        Only one subframe at a time is transmitted in the frame.

        A subframe is defined by creating a subframe object as a child of a frame.
        """
        return self._mux_subframes

    @property
    def pdu_properties(self):
        # type: () -> typing.Iterable[types.PduProperties]
        """list of :any:`PduProperties`: Get or set a list that maps existing PDUs to a frame.

        A mapped PDU is transmitted inside the frame payload when the frame is transmitted.
        You can map one or more PDUs to a frame and one PDU to multiple frames.

        Mapping PDUs to a frame requires setting pdu_properties with a list of PduProperties tuples.
        Each tuple contains the following properties:

        *   :any:`PduProperties.pdu`: Defines the sequence of values for the other two properties.
        *   :any:`PduProperties.start_bit`: Defines the start bit of the PDU inside the frame.
        *   :any:`PduProperties.update_bit`: Defines the update bit for the PDU inside the frame.
            If the update bit is not used, set the value to ``-1``.

        Databases imported from FIBEX prior to version 3.0,
        from DBC, NCD, or LDF files have a strong one-to-one relationship between frames and PDUs.
        Every frame has exactly one PDU mapped, and every PDU is mapped to exactly one frame.

        To unmap PDUs from a frame, set this property to an empty list.
        A frame without mapped PDUs contains no signals.

        For CAN and LIN, NI-XNET supports only a one-to-one relationship between frames and PDUs.
        For those interfaces, advanced PDU configuration returns
        an error from the :any:`Frame.config_status` property and when creating a session.
        If you do not use advanced PDU configuration,
        you can avoid using PDUs in the database API
        and create signals and subframes directly on a frame.
        """
        handles = _props.get_frame_pdu_refs(self._handle)
        pdu_tuples = zip(*(handles,
                           _props.get_frame_pdu_start_bits(self._handle),
                           _props.get_frame_pdu_update_bits(self._handle)))
        for (ref, start_bit, update_bit) in pdu_tuples:
            yield types.PduProperties(ref, start_bit, update_bit)

    @pdu_properties.setter
    def pdu_properties(self, pdus):
        # type: (typing.Iterable[types.PduProperties]) -> None
        _props.set_frame_pdu_refs(self._handle,
                                  list(map(lambda p: p.pdu._handle, pdus)))
        _props.set_frame_pdu_start_bits(self._handle,
                                        list(map(operator.attrgetter('start_bit'), pdus)))
        _props.set_frame_pdu_update_bits(self._handle,
                                         list(map(operator.attrgetter('update_bit'), pdus)))

    @property
    def variable_payload(self):
        # type: () -> bool
        # This property is currently not documented in the C API.
        # If/when we have C API documentation, we should add it here too.
        return _props.get_frame_variable_payload(self._handle)

    @variable_payload.setter
    def variable_payload(self, value):
        # type: (bool) -> None
        _props.set_frame_variable_payload(self._handle, value)

    @property
    def can_io_mode(self):
        # type: () -> constants.CanIoMode
        """:any:`CanIoMode`: Get or set the frame's I/O mode.

        This property is used in ISO CAN FD+BRS mode only.
        In this mode,
        you can specify every frame to be transmitted in CAN 2.0, CAN FD, or CAN FD+BRS mode.
        CAN FD+BRS frames require the interface to be in CAN FD+BRS mode;
        otherwise, it is transmitted in CAN FD mode.

        When the interface is in Non-ISO CAN FD or Legacy ISO CAN FD mode,
        this property is disregarded.
        In Non-ISO CAN FD and Legacy ISO CAN FD mode,
        you must use :any:`Interface.can_tx_io_mode` to switch the transmit mode.

        When the assigned database does not define the property in ISO CAN FD mode,
        the frames are transmitted with :any:`Interface.can_io_mode`.
        """
        return constants.CanIoMode(_props.get_frame_can_io_mode(self._handle))

    @can_io_mode.setter
    def can_io_mode(self, value):
        # type: (constants.CanIoMode) -> None
        _props.set_frame_can_io_mode(self._handle, value.value)
