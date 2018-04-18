from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import typing  # NOQA: F401

from nixnet import _errors
from nixnet import _props
from nixnet import constants

from nixnet.database import _cluster
from nixnet.database import _dbc_attributes
from nixnet.database import _frame


class Ecu(object):
    """Database ECU"""

    def __init__(self, handle):
        # type: (int) -> None
        self._handle = handle
        self._dbc_attributes = None  # type: typing.Optional[_dbc_attributes.DbcAttributeCollection]

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
        """Check this ECU's configuration status.

        By default, incorrectly configured ECUs in the database are not returned from
        :any:`Cluster.ecus` because they cannot be used in the bus communication.
        You can change this behavior by setting :any:`Database.show_invalid_from_open` to `True`.
        When an ECU configuration status becomes invalid after the database is opened,
        the ECU still is returned from :any:`Cluster.ecus`
        even if :any:`Database.show_invalid_from_open` is `False`.

        Raises:
            XnetError: The ECU is incorrectly configured.
        """
        status_code = _props.get_ecu_config_status(self._handle)
        _errors.check_for_error(status_code)

    @property
    def clst(self):
        # type: () -> _cluster.Cluster
        """:any:`Cluster`: Returns the parent cluster to which the ECU is connected.

        The parent cluster is determined when the ECU object is created.
        You cannot change it afterwards.
        """
        handle = _props.get_ecu_clst_ref(self._handle)
        return _cluster.Cluster(handle)

    @property
    def comment(self):
        # type: () -> typing.Text
        """str: Get or set a comment describing the ECU object.

        A comment is a string containing up to 65535 characters.
        """
        return _props.get_ecu_comment(self._handle)

    @comment.setter
    def comment(self, value):
        # type: (typing.Text) -> None
        _props.set_ecu_comment(self._handle, value)

    @property
    def dbc_attributes(self):
        # type: () -> _dbc_attributes.DbcAttributeCollection
        """:any:`DbcAttributeCollection`: Access the ECU's DBC attributes."""
        if self._dbc_attributes is None:
            self._dbc_attributes = _dbc_attributes.DbcAttributeCollection(self._handle)
        return self._dbc_attributes

    @property
    def name(self):
        # type: () -> typing.Text
        """str: Get or set the name of the ECU object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.), and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        An ECU name must be unique for all ECUs in a cluster.

        This short name does not include qualifiers to ensure that it is unique,
        such as the database and cluster name.
        It is for display purposes.
        """
        return _props.get_ecu_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_ecu_name(self._handle, value)

    @property
    def rx_frms(self):
        # type: () -> typing.Iterable[_frame.Frame]
        """list of :any:`Frame<_frame.Frame>`: Get or set a list of frames the ECU receives.

        This property defines all frames the ECU receives.
        All frames an ECU receives in a given cluster must be defined in the same cluster.
        """
        for ref in _props.get_ecu_rx_frm_refs(self._handle):
            yield _frame.Frame(ref)

    @rx_frms.setter
    def rx_frms(self, value):
        # type: (typing.Iterable[_frame.Frame]) -> None
        handle_list = [frame._handle for frame in value]
        _props.set_ecu_rx_frm_refs(self._handle, handle_list)

    @property
    def tx_frms(self):
        # type: () -> typing.Iterable[_frame.Frame]
        """list of :any:`Frame<_frame.Frame>`: Get or set a list of frames the ECU transmits.

        This property defines all frames the ECU transmits.
        All frames an ECU transmits in a given cluster must be defined in the same cluster.
        """
        for ref in _props.get_ecu_tx_frm_refs(self._handle):
            yield _frame.Frame(ref)

    @tx_frms.setter
    def tx_frms(self, value):
        # type: (typing.Iterable[_frame.Frame]) -> None
        frame_handles = [frame._handle for frame in value]
        _props.set_ecu_tx_frm_refs(self._handle, frame_handles)

    @property
    def flex_ray_is_coldstart(self):
        return _props.get_ecu_flex_ray_is_coldstart(self._handle)

    @property
    def flex_ray_startup_frame_ref(self):
        return _props.get_ecu_flex_ray_startup_frame_ref(self._handle)

    @property
    def flex_ray_wakeup_ptrn(self):
        return _props.get_ecu_flex_ray_wakeup_ptrn(self._handle)

    @flex_ray_wakeup_ptrn.setter
    def flex_ray_wakeup_ptrn(self, value):
        _props.set_ecu_flex_ray_wakeup_ptrn(self._handle, value)

    @property
    def flex_ray_wakeup_chs(self):
        return _props.get_ecu_flex_ray_wakeup_chs(self._handle)

    @flex_ray_wakeup_chs.setter
    def flex_ray_wakeup_chs(self, value):
        _props.set_ecu_flex_ray_wakeup_chs(self._handle, value)

    @property
    def flex_ray_connected_chs(self):
        return _props.get_ecu_flex_ray_connected_chs(self._handle)

    @flex_ray_connected_chs.setter
    def flex_ray_connected_chs(self, value):
        _props.set_ecu_flex_ray_connected_chs(self._handle, value)

    @property
    def lin_master(self):
        # type: () -> bool
        """bool: Get or set whether the ECU is a LIN master (``True``) or LIN slave (``False``)."""
        return _props.get_ecu_lin_master(self._handle)

    @lin_master.setter
    def lin_master(self, value):
        # type: (bool) -> None
        _props.set_ecu_lin_master(self._handle, value)

    @property
    def lin_protocol_ver(self):
        # type: () -> constants.LinProtocolVer
        """:any:`LinProtocolVer`: Get or set the version of the LIN standard this ECU uses."""
        return constants.LinProtocolVer(_props.get_ecu_lin_protocol_ver(self._handle))

    @lin_protocol_ver.setter
    def lin_protocol_ver(self, value):
        # type: (constants.LinProtocolVer) -> None
        _props.set_ecu_lin_protocol_ver(self._handle, value.value)

    @property
    def lin_initial_nad(self):
        # type: () -> int
        """int: Get or set the initial NAD of a LIN slave node.

        NAD is the address of a slave node and is used in diagnostic services.
        Initial NAD is replaced by configured NAD with node configuration services.

        .. warning:: This property is not saved in the FIBEX database.
            You can import it only from an LDF file.
        """
        return _props.get_ecu_lin_initial_nad(self._handle)

    @lin_initial_nad.setter
    def lin_initial_nad(self, value):
        # type: (int) -> None
        _props.set_ecu_lin_initial_nad(self._handle, value)

    @property
    def lin_config_nad(self):
        # type: () -> int
        """int: Get or set the configured NAD of a LIN slave node.

        NAD is the address of a slave node and is used in diagnostic services.
        Initial NAD is replaced by configured NAD with node configuration services.

        .. warning:: This property is not saved in the FIBEX database.
            You can import it only from an LDF file.
        """
        return _props.get_ecu_lin_config_nad(self._handle)

    @lin_config_nad.setter
    def lin_config_nad(self, value):
        # type: (int) -> None
        _props.set_ecu_lin_config_nad(self._handle, value)

    @property
    def lin_supplier_id(self):
        # type: () -> int
        """int: Get or set the supplier ID.

        Supplier ID is a 16-bit value identifying the supplier of the LIN node (ECU).

        .. warning:: This property is not saved in the FIBEX database.
            You can import it only from an LDF file.
        """
        return _props.get_ecu_lin_supplier_id(self._handle)

    @lin_supplier_id.setter
    def lin_supplier_id(self, value):
        # type: (int) -> None
        _props.set_ecu_lin_supplier_id(self._handle, value)

    @property
    def lin_function_id(self):
        # type: () -> int
        """int: Get or set the function ID.

        Function ID is a 16-bit value identifying the function of the LIN node (ECU).

        .. warning:: This property is not saved in the FIBEX database.
            You can import it only from an LDF file.
        """
        return _props.get_ecu_lin_function_id(self._handle)

    @lin_function_id.setter
    def lin_function_id(self, value):
        # type: (int) -> None
        _props.set_ecu_lin_function_id(self._handle, value)

    @property
    def lin_p2_min(self):
        # type: () -> float
        """float: Get or set the minimum time in seconds between frame reception and node response.

        This is the minimum time between reception of the last frame
        of the diagnostic request and the response sent by the node.

        .. warning:: This property is not saved in the FIBEX database.
            You can import it only from an LDF file.
        """
        return _props.get_ecu_lin_p2_min(self._handle)

    @lin_p2_min.setter
    def lin_p2_min(self, value):
        # type (float) -> None
        _props.set_ecu_lin_p2_min(self._handle, value)

    @property
    def lin_st_min(self):
        # type: () -> float
        """float: Get or set the minimum time in seconds for node preparation.

        This is the minimum time the node requires to prepare
        for the next frame of the diagnostic service.

        .. warning:: This property is not saved in the FIBEX database.
            You can import it only from an LDF file.
        """
        return _props.get_ecu_lin_st_min(self._handle)

    @lin_st_min.setter
    def lin_st_min(self, value):
        # type (float) -> None
        _props.set_ecu_lin_st_min(self._handle, value)

    @property
    def j1939_preferred_address(self):
        # type: () -> int
        """int: Get or set the preferred J1939 node address to be used when simulating this ECU.

        If you assign this ECU to an XNET session (`j1939.set_ecu`),
        XNET will start address claiming for this address using
        :any:`Ecu.j1939_node_name` and use the address for the session when the address is granted.
        """
        return _props.get_ecu_j1939_preferred_address(self._handle)

    @j1939_preferred_address.setter
    def j1939_preferred_address(self, value):
        # type: (int) -> None
        _props.set_ecu_j1939_preferred_address(self._handle, value)

    @property
    def j1939_node_name(self):
        # type: () -> int
        """int: Get or set the preferred J1939 node address to be used when simulating this ECU.

        If you assign this ECU to an XNET session (`j1939.set_ecu`),
        XNET will start address claiming for this address using
        this node name and :any:`Ecu.j1939_preferred_address`.
        """
        return _props.get_ecu_j1939_node_name(self._handle)

    @j1939_node_name.setter
    def j1939_node_name(self, value):
        # type: (int) -> None
        _props.set_ecu_j1939_node_name(self._handle, value)
