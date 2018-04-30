from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _props
from nixnet import constants

from nixnet.database import _database_object
from nixnet.database import _dbc_attributes
from nixnet.database import _dbc_signal_value_table

# workaround to avoid circular imports caused by mypy type annotations
MYPY = False
if MYPY:
    from nixnet.database import _frame  # NOQA: F401
    from nixnet.database import _pdu  # NOQA: F401
    from nixnet.database import _subframe  # NOQA: F401


class Signal(_database_object.DatabaseObject):
    """Database signal"""

    def __init__(
            self,
            **kwargs  # type: int
    ):
        # type: (...) -> None
        if not kwargs or '_handle' not in kwargs:
            raise TypeError()

        self._handle = kwargs['_handle']
        self._dbc_attributes = None  # type: typing.Optional[_dbc_attributes.DbcAttributeCollection]
        self._dbc_signal_value_table = _dbc_signal_value_table.DbcSignalValueTable(self._handle)

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
        """Check this signal's configuration status.

        By default, incorrectly configured signals in the database are not returned from
        :any:`Frame.sigs` because they cannot be used in the bus communication.
        You can change this behavior by setting :any:`Database.show_invalid_from_open` to `True`.
        When a signal configuration status becomes invalid after the database is opened,
        the signal still is returned from :any:`Frame.sigs`
        even if :any:`Database.show_invalid_from_open` is `False`.

        Examples of invalid signal configuration:

        *   The signal is specified using bits outside the frame payload.
        *   The signal overlaps another signal in the frame.
            For example,
            two multiplexed signals with the same multiplexer value are using the same bit in the frame payload.
        *   The signal with integer data type (signed or unsigned) is specified with more than 52 bits.
            This is not allowed due to internal limitation of the double data type that NI-XNET uses for signal values.
        *   The frame containing the signal is invalid
            (for example, a CAN frame is defined with more than 8 payload bytes).

        Raises:
            :any:`XnetError`: The signal is incorrectly configured.
        """
        status_code = _props.get_signal_config_status(self._handle)
        _errors.check_for_error(status_code)

    @property
    def byte_ordr(self):
        # type: () -> constants.SigByteOrdr
        """:any:`SigByteOrdr`: Signal byte order in the frame payload.

        This property defines how signal bytes are ordered in the frame payload when the frame is loaded in memory.

        This property is required.
        If the property does not contain a valid value,
        and you create an XNET session that uses this signal,
        the session returns an error.
        To ensure that the property contains a valid value,
        you can do one of the following:

        *   Use a database file (or alias) to create the session.

            The file formats require a valid value in the text for this property.
        *   Set a value using the nxdbSetProperty function.

            This is needed when you create your own in-memory database (*:memory:*) rather than use a file.
            The property does not contain a default in this case,
            so you must set a valid value prior to creating a session.
        """
        return constants.SigByteOrdr(_props.get_signal_byte_ordr(self._handle))

    @byte_ordr.setter
    def byte_ordr(self, value):
        # type: (constants.SigByteOrdr) -> None
        _props.set_signal_byte_ordr(self._handle, value.value)

    @property
    def comment(self):
        # type: () -> typing.Text
        """str: Get or set a comment describing the signal object.

        A comment is a string containing up to 65535 characters.
        """
        return _props.get_signal_comment(self._handle)

    @comment.setter
    def comment(self, value):
        # type: (typing.Text) -> None
        _props.set_signal_comment(self._handle, value)

    @property
    def data_type(self):
        # type: () -> constants.SigDataType
        """:any:`SigDataType`: Get or set the signal data type.

        This property determines how the bits of a signal in a frame must be interpreted to build a value.

        This property is required.
        If the property does not contain a valid value,
        and you create an XNET session that uses this signal,
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
        return constants.SigDataType(_props.get_signal_data_type(self._handle))

    @data_type.setter
    def data_type(self, value):
        # type: (constants.SigDataType) -> None
        _props.set_signal_data_type(self._handle, value.value)

    @property
    def dbc_attributes(self):
        # type: () -> _dbc_attributes.DbcAttributeCollection
        """:any:`DbcAttributeCollection`: Access the signal's DBC attributes."""
        if self._dbc_attributes is None:
            self._dbc_attributes = _dbc_attributes.DbcAttributeCollection(self._handle)
        return self._dbc_attributes

    @property
    def dbc_signal_value_table(self):
        # type: () -> _dbc_signal_value_table.DbcSignalValueTable
        """:any:`DbcSignalValueTable`: Access the signal's DBC value table."""
        return self._dbc_signal_value_table

    @property
    def default(self):
        # type: () -> float
        """float: Get or set the signal default value, specified as scaled floating-point units.

        The initial value of this property comes from the database.
        If the database does not provide a value, this property uses a default value of 0.0.

        For all three signal output sessions,
        this property is used when a frame transmits prior to writing to a session.
        The :any:`Frame.default_payload` property is used as the initial payload,
        then the default value of each signal is mapped into that payload using this property,
        and the result is used for the frame transmit.

        For all three signal input sessions,
        this property is returned for each signal when reading a session prior to receiving the first frame.

        For more information about when this property is used,
        refer to the discussion of read and write for each session mode.
        """
        return _props.get_signal_default(self._handle)

    @default.setter
    def default(self, value):
        # type: (float) -> None
        _props.set_signal_default(self._handle, value)

    @property
    def frame(self):
        # type: () -> _frame.Frame
        """:any:`Frame<_frame.Frame>`: Returns the signal parent frame object.

        The parent frame is defined when the signal object is created. You cannot change it afterwards.
        """
        from nixnet.database import _frame  # NOQA: F811
        ref = _props.get_signal_frame_ref(self._handle)
        return _frame.Frame(_handle=ref)

    @property
    def max(self):
        # type: () -> float
        """float: Get or set the scaled signal value maximum.

        Session read and write methods do not limit the signal value to a maximum value.
        Use this database property to set the maximum value.
        """
        return _props.get_signal_max(self._handle)

    @max.setter
    def max(self, value):
        # type: (float) -> None
        _props.set_signal_max(self._handle, value)

    @property
    def min(self):
        # type: () -> float
        """float: The scaled signal value minimum.

        Session read and write methods do not limit the signal value to a minimum value.
        Use this database property to set the minimum value.
        """
        return _props.get_signal_min(self._handle)

    @min.setter
    def min(self, value):
        # type: (float) -> None
        _props.set_signal_min(self._handle, value)

    @property
    def name(self):
        # type: () -> typing.Text
        """str: Get or set a string identifying a signal object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.), and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        A signal name must be unique for all signals in a frame.

        This short name does not include qualifiers to ensure that it is unique,
        such as the database, cluster, and frame name.
        It is for display purposes.
        """
        return _props.get_signal_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_signal_name(self._handle, value)

    @property
    def name_unique_to_cluster(self):
        # type: () -> typing.Text
        """str: Returns a signal name unique to the cluster that contains the signal.

        If the single name is not unique within the cluster,
        the name is <frame-name>.<signal-name>.

        You can pass the name to the `find` function to retrieve the reference to the object,
        while the single name is not guaranteed success in `find` because it may be not unique in the cluster.
        """
        return _props.get_signal_name_unique_to_cluster(self._handle)

    @property
    def num_bits(self):
        # type: () -> int
        """int: The number of bits the signal uses in the frame payload.

        IEEE Float numbers are limited to 32 bit or 64 bit.

        Integer (signed and unsigned) numbers are limited to 1-52 bits.
        NI-XNET converts all integers to doubles (64-bit IEEE Float).
        Integer numbers with more than 52 bits
        (the size of the mantissa in a 64-bit IEEE Float)
        cannot be converted exactly to double, and vice versa; therefore,
        NI-XNET does not support this.

        This property is required.
        If the property does not contain a valid value,
        and you create an XNET session that uses this signal,
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
        return _props.get_signal_num_bits(self._handle)

    @num_bits.setter
    def num_bits(self, value):
        # type: (int) -> None
        _props.set_signal_num_bits(self._handle, value)

    @property
    def pdu(self):
        # type: () -> _pdu.Pdu
        """:any:`Pdu`: Returns to the signal's parent PDU.

        The parent PDU is defined when the signal object is created.
        You cannot change it afterwards.
        """
        from nixnet.database import _pdu  # NOQA: F811
        ref = _props.get_signal_pdu_ref(self._handle)
        return _pdu.Pdu(_handle=ref)

    @property
    def scale_fac(self):
        # type: () -> float
        """float: Get or set factor `a` for linear scaling `ax+b`.

        Linear scaling is applied to all signals with the IEEE Float data type,
        unsigned and signed.
        For identical scaling 1.0x+0.0,
        NI-XNET optimized scaling routines do not perform the multiplication and addition
        """
        return _props.get_signal_scale_fac(self._handle)

    @scale_fac.setter
    def scale_fac(self, value):
        # type: (float) -> None
        _props.set_signal_scale_fac(self._handle, value)

    @property
    def scale_off(self):
        # type: () -> float
        """float: Get or set offset `b` for linear scaling `ax+b`.

        Linear scaling is applied to all signals with the IEEE Float data type,
        unsigned and signed.
        For identical scaling 1.0x+0.0,
        NI-XNET optimized scaling routines do not perform the multiplication and addition
        """
        return _props.get_signal_scale_off(self._handle)

    @scale_off.setter
    def scale_off(self, value):
        # type: (float) -> None
        _props.set_signal_scale_off(self._handle, value)

    @property
    def start_bit(self):
        """int: Get or set the least significant signal bit position in the frame payload.

        This property determines the signal starting point in the frame.
        For the integer data type (signed and unsigned),
        it means the binary signal representation least significant bit position.
        For IEEE Float signals, it means the mantissa least significant bit.

        The NI-XNET Database Editor shows a graphical overview of the frame.
        It enumerates the frame bytes on the left and the byte bits on top.
        The bit number in the frame is calculated as byte number x 8 + bit number.
        The maximum bit number in a CAN or LIN frame is 63 (7 x 8 + 7);
        the maximum bit number in a FlexRay frame is 2031 (253 x 8 + 7).

        .. image:: frameoverviewsignalstartingbit12.gif

        **Frame Overview in the NI-XNET Database Editor with a Signal Starting in Bit 12**

        This property is required.
        If the property does not contain a valid value,
        and you create an XNET session that uses this signal,
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
        return _props.get_signal_start_bit(self._handle)

    @start_bit.setter
    def start_bit(self, value):
        # type: (typing.Any) -> typing.Any
        _props.set_signal_start_bit(self._handle, value)

    @property
    def unit(self):
        # type: () -> typing.Text
        """str: Get or set the signal value unit.

        NI-XNET does not use the unit internally for calculations.
        You can use the string to display the signal value along with the unit.
        """
        return _props.get_signal_unit(self._handle)

    @unit.setter
    def unit(self, value):
        # type: (typing.Text) -> None
        _props.set_signal_unit(self._handle, value)

    @property
    def mux_is_data_mux(self):
        # type: () -> bool
        """bool: Get or set whether this signal is a multiplexer signal.

        A frame containing a multiplexer value is called a multiplexed frame.

        A multiplexer defines an area within the frame to contain different information
        (dynamic signals) depending on the multiplexer signal value.
        Dynamic signals with a different multiplexer value
        (defined in a different subframe)
        can share bits in the frame payload.
        The multiplexer signal value determines which dynamic signals are transmitted in the given frame.

        To define dynamic signals in the frame transmitted with a given multiplexer value,
        you first must create a subframe in this frame and set the multiplexer value in the subframe.
        Then you must create dynamic signals using
        :any:`SubFrame.dyn_signals` to create child signals of this subframe.

        Multiplexer signals may not overlap other static or dynamic signals in the frame.

        Dynamic signals may overlap other dynamic signals when they have a different multiplexer value.

        A frame may contain only one multiplexer signal.

        The multiplexer signal is not scaled.
        Scaling factor and offset do not apply.

        In NI-CAN, the multiplexer signal was called mode channel.
        """
        return _props.get_signal_mux_is_data_mux(self._handle)

    @mux_is_data_mux.setter
    def mux_is_data_mux(self, value):
        # type: (bool) -> None
        _props.set_signal_mux_is_data_mux(self._handle, value)

    @property
    def mux_is_dynamic(self):
        # type: () -> bool
        """bool: returns whether this signal is a dynamic signal.

        Use this property to determine if a signal is static or dynamic.
        Dynamic signals are transmitted in the frame when the multiplexer signal
        in the frame has a given value specified in the subframe.
        Use the :any:`Signal.mux_value` property to determine with which
        multiplexer value the dynamic signal is transmitted.

        This property is read only.
        To create a dynamic signal,
        create the signal object as a child of a subframe instead of a frame.
        The dynamic signal cannot be changed to a static signal afterwards.

        In NI-CAN, dynamic signals were called mode-dependent signals.
        """
        return _props.get_signal_mux_is_dynamic(self._handle)

    @property
    def mux_value(self):
        # type: () -> int
        """int: Returns the multiplexer value of a dynamic signal.

        The multiplexer value applies to dynamic signals only
        (when :any:`Signal.mux_is_dynamic` is ``True``).
        This property defines which multiplexer value is transmitted in the
        multiplexer signal when this dynamic signal is transmitted in the frame.

        The multiplexer value is determined in the subframe.
        All dynamic signals that are children of the same subframe object use the same multiplexer value.

        Dynamic signals with the same multiplexer value may not overlap each other,
        the multiplexer signal, or static signals.
        """
        return _props.get_signal_mux_value(self._handle)

    @property
    def mux_subfrm(self):
        # type: () -> _subframe.SubFrame
        """:any:`SubFrame`: Returns the subframe parent.

        This property is valid only for dynamic signals that have a subframe parent.
        For static signals or the multiplexer signal,
        this property raises an :any:`XnetError` exception.

        Raises:
            :any:`XnetError`: The signal does not have a subframe parent.
        """
        from nixnet.database import _subframe  # NOQA: F811
        ref = _props.get_signal_mux_subfrm_ref(self._handle)
        if ref == 0:
            _errors.raise_xnet_error(_cconsts.NX_ERR_FRAME_NOT_FOUND)

        return _subframe.SubFrame(_handle=ref)
