from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _funcs
from nixnet import _props
from nixnet import constants

from nixnet.database import _collection
from nixnet.database import _dbc_attributes
from nixnet.database import _signal


class Cluster(object):
    """Database cluster"""

    def __init__(self, handle):
        # type: (int) -> None
        from nixnet.database import _ecu
        from nixnet.database import _frame
        from nixnet.database import _lin_sched
        from nixnet.database import _pdu
        self._handle = handle
        self._dbc_attributes = None  # type: typing.Optional[_dbc_attributes.DbcAttributeCollection]
        self._ecus = _collection.DbCollection(
            self._handle, constants.ObjectClass.ECU, _cconsts.NX_PROP_CLST_ECU_REFS, _ecu.Ecu)
        self._frames = _collection.DbCollection(
            self._handle, constants.ObjectClass.FRAME, _cconsts.NX_PROP_CLST_FRM_REFS, _frame.Frame)
        self._lin_sched = _collection.DbCollection(
            self._handle, constants.ObjectClass.LIN_SCHED, _cconsts.NX_PROP_CLST_LIN_SCHEDULES, _lin_sched.LinSched)
        self._pdus = _collection.DbCollection(
            self._handle, constants.ObjectClass.PDU, _cconsts.NX_PROP_CLST_PDU_REFS, _pdu.Pdu)

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
        """Check this cluster's configuration status.

        By default, incorrectly configured clusters in the database are not returned from
        :any:`Database.clusters` because they cannot be used in the bus communication.
        You can change this behavior by setting :any:`Database.show_invalid_from_open` to `True`.
        When a cluster configuration status becomes invalid after the database is opened,
        the cluster still is returned from :any:`Database.clusters`
        even if :any:`Database.show_invalid_from_open` is `False`.

        Raises:
            XnetError: The cluster is incorrectly configured.
        """
        status_code = _props.get_cluster_config_status(self._handle)
        _errors.check_for_error(status_code)

    def export(self, db_filepath):
        # type: (typing.Text) -> None
        """Exports this cluster to a CANdb++ or LIN database file format.

        A CAN cluster is exported as a CANdb++ database file (.dbc).
        A LIN cluster is exported as a LIN database file (.ldf).
        If the target file exists, it is overwritten.

        Exporting a cluster is not supported under Real-Time (RT).

        Args:
            db_filepath(str): Contains the pathname to the database file.
        """
        _funcs.nxdb_save_database(self._handle, db_filepath)

    def merge(
            self,
            source_obj,
            copy_mode,
            prefix,
            wait_for_complete):
        # type: (typing.Any, constants.Merge, typing.Text, bool) -> int
        """Merges database objects and related subobjects from the source to this cluster.

        The source can be any of the following objects:

        *   :any:`Frame<_frame.Frame>`
        *   :any:`Pdu`
        *   :any:`Ecu`
        *   :any:`LinSched`
        *   :any:`Cluster`

        All listed objects must have unique names in the cluster.
        They are referenced here as objects,
        as opposed to child objects (for example, a signal is a child of a frame).

        If the source object name is not used in the target cluster,
        this function copies the source objects with the child objects to the target.
        If an object with the same name exists in this cluster,
        you can avoid name collisions by specifying the prefix to be added to the name.

        If an object with the same name exists in this cluster,
        the merge behavior depends on the ``copy_mode`` input.

        **Example**

        Target frame F1(v1) has signals S1 and S2(v1). Source frame F1(v2) has signals S2(v2) and S3.

        (v1) and (v2) are two versions of one object with same name, but with different properties.

        *   Result when ``copy_mode`` is ``COPY_USE_SOURCE``: F1(v2), S2(v2), S3.
        *   Result when ``copy_mode`` is ``COPY_USE_TARGET``: F1(v1), S1, S2(v1).
        *   Result when ``copy_mode`` is ``MERGE_USE_SOURCE``: F1(v2), S1, S2(v2), S3.
        *   Result when ``copy_mode`` is ``MERGE_USE_TARGET``: F1(v1), S1, S2(v1), S3.

        If the source object is a cluster,
        this function copies all contained PDUs, ECUs, and LIN schedules
        with their child objects to this cluster.

        Depending on the number of contained objects in the source and destination clusters,
        the execution can take a longer time.
        If ``wait_for_complete`` is ``True``, this function waits until the merging process gets completed.
        If the execution completes without errors,
        ``perecent_complete`` returns ``100``.
        If ``wait_for_complete`` is ``False``,
        the function returns quickly,
        and ``perecent_complete`` returns values less than ``100``.
        You must call :any:`Cluster.merge` repeatedly until ``perecent_complete`` returns ``100``.
        You can use the time between calls to perform asynchronous tasks.

        Args:
            source_obj(object): The object to be merged into this cluster.
            copy_mode(:any:`Merge`): Defines the merging behavior if this cluster
                already contains an object with the same name.
            prefix(str): The prefix to be added to the source object name if an
                object with the same name and type exists in this cluster.
            wait_for_complete(bool): Determines whether the function returns directly
                or waits until the entire transmission is completed.
        Returns:
            int: A value which indicates the merging progress as a percentage. ``100`` indicates completion.
        """
        return _funcs.nxdb_merge(self._handle, source_obj._handle, copy_mode.value, prefix, wait_for_complete)

    @property
    def baud_rate(self):
        # type: (...) -> int
        """int: Get or set the buad rate all custer nodes use.

        This baud rate represents the rate from the database,
        so it is read-only from the session.
        Use a session interface property (for example, :any:`Interface.baud_rate`)
        to override the database baud rate with an application-specific baud rate.

        **CAN**

        For CAN, this rate can be 33333, 40000, 50000, 62500, 80000, 83333,
        100000, 125000, 160000, 200000, 250000, 400000, 500000, 800000, or
        1000000. Some transceivers may support only a subset of these values.

        **LIN**

        For LIN, this rate can be 2400-20000 inclusive.

        If you need values other than these,
        use the custom settings as described in :any:`Interface.baud_rate`.
        """
        return _props.get_cluster_baud_rate64(self._handle)

    @baud_rate.setter
    def baud_rate(self, value):
        # type: (int) -> None
        _props.set_cluster_baud_rate64(self._handle, value)

    @property
    def comment(self):
        # type: () -> typing.Text
        """str: Get or set a comment describing the cluster object.

        A comment is a string containing up to 65535 characters.
        """
        return _props.get_cluster_comment(self._handle)

    @comment.setter
    def comment(self, value):
        # type: (typing.Text) -> None
        _props.set_cluster_comment(self._handle, value)

    @property
    def database_ref(self):
        # type: () -> int
        # todo: return a Database object here
        handle = _props.get_cluster_database_ref(self._handle)
        return handle

    @property
    def dbc_attributes(self):
        # type: () -> _dbc_attributes.DbcAttributeCollection
        """:any:`DbcAttributeCollection`: Access the cluster's DBC attributes."""
        if self._dbc_attributes is None:
            self._dbc_attributes = _dbc_attributes.DbcAttributeCollection(self._handle)
        return self._dbc_attributes

    @property
    def ecus(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Returns a collection of :any:`Ecu` objects in this cluster.

        An ECU is assigned to a cluster when the ECU object is created.
        You cannot change this assignment afterwards.
        """
        return self._ecus

    @property
    def frames(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Returns a collection of :any:`Frame<_frame.Frame>` objects in this cluster.

        A frame is assigned to a cluster when the frame object is created.
        You cannot change this assignment afterwards.
        """
        return self._frames

    @property
    def name(self):
        # type: () -> typing.Text
        """str: Get or set the name of the cluster object.

        Lowercase letters, uppercase letters, numbers,
        and the underscore (_) are valid characters for the short name.
        The space ( ), period (.), and other special characters are not supported within the name.
        The short name must begin with a letter (uppercase or lowercase) or underscore, and not a number.
        The short name is limited to 128 characters.

        If you use a FIBEX file, the short name comes from the file.
        If you use a CANdb (.dbc), LDF (.ldf),
        or NI-CAN (.ncd) file,
        no cluster name is stored in the file,
        so NI-XNET uses the name Cluster.
        If you create the cluster yourself,
        the name that you provide is used.

        A cluster name must be unique for all clusters in a database.

        This short name does not include qualifiers to ensure that it is unique,
        such as the database name. It is for display purposes.
        """
        return _props.get_cluster_name(self._handle)

    @name.setter
    def name(self, value):
        # type: (typing.Text) -> None
        _props.set_cluster_name(self._handle, value)

    @property
    def pdus(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Returns a collection of :any:`Pdu<_pdu.Pdu>` objects in this cluster.

        A PDU is assigned to a cluster when the PDU object is created.
        You cannot change this assignment afterwards.
        """
        return self._pdus

    @property
    def pdus_reqd(self):
        # type: () -> bool
        """bool: Returns whether using :any:`PDUs<Pdu>` in the database API is required for this cluster.

        If this property returns ``False``,
        it is safe to use signals as child objects of a frame without PDUs.
        This behavior is compatible with NI-XNET 1.1 or earlier.
        Clusters from .dbc, .ncd, or FIBEX 2 files always return ``False`` for this property,
        so using PDUs from those files is not required.

        If this property returns ``True``,
        the cluster contains PDU configuration,
        which requires reading the PDUs as frame child objects and then signals as PDU child objects,
        as shown in the following figure.

        Internally, the database always uses PDUs,
        but shows the same signal objects also as children of a frame.

        .. image:: pdusrequired.gif

        |

        For this property to return ``False``,
        the following conditions must be fulfilled for all frames in the cluster:

        *   Only one PDU is mapped to the frame.
        *   This PDU is not mapped to other frames.
        *   The PDU Start Bit in the frame is 0.
        *   The PDU Update Bit is not used.

        If the conditions are not fulfilled for a given frame,
        signals from the frame are still returned,
        but reading the property returns a warning.
        """
        return _props.get_cluster_pdus_reqd(self._handle)

    @property
    def protocol(self):
        # type: () -> constants.Protocol
        """:any:`Protocol`: Get or set the cluster protocol."""
        return constants.Protocol(_props.get_cluster_protocol(self._handle))

    @protocol.setter
    def protocol(self, value):
        # type: (constants.Protocol) -> None
        _props.set_cluster_protocol(self._handle, value.value)

    @property
    def sigs(self):
        # type: () -> typing.Iterable[_signal.Signal]
        """list of :any:`Signal<_signal.Signal>`: Returns a list of all :any:`Signal<_signal.Signal>` objects in this cluster."""  # NOQA: E501
        for handle in _props.get_cluster_sig_refs(self._handle):
            yield _signal.Signal(handle)

    @property
    def can_io_mode(self):
        # type: () -> constants.CanIoMode
        """:any:`CanIoMode`: Get or set the CAN I/O Mode of the cluster."""
        return constants.CanIoMode(_props.get_cluster_can_io_mode(self._handle))

    @can_io_mode.setter
    def can_io_mode(self, value):
        # type: (constants.CanIoMode) -> None
        _props.set_cluster_can_io_mode(self._handle, value.value)

    @property
    def can_fd_baud_rate(self):
        # type: () -> int
        """int: Get or set the fast data baud rate when :any:`Cluster.can_io_mode` is ``CanIoMode.CAN_FD_BRS``.

        Refer to the :any:`CanIoMode` for a description of ``CanIoMode.CAN_FD_BRS``.
        Use a session interface property (for example, :any:`Interface.can_fd_baud_rate`)
        to override the database fast baud rate with an application-specific fast baud rate.

        NI-XNET CAN hardware currently accepts the following numeric baud rates:
        200000, 250000, 400000, 500000, 800000, 1000000, 1250000, 1600000,
        2000000, 2500000, 4000000, 5000000, and 8000000.
        Some transceivers may support only a subset of these values.

        If you need values other than these,
        use the custom settings as described in :any:`Interface.can_fd_baud_rate`.
        """
        return _props.get_cluster_can_fd_baud_rate64(self._handle)

    @can_fd_baud_rate.setter
    def can_fd_baud_rate(self, value):
        # type: (int) -> None
        _props.set_cluster_can_fd_baud_rate64(self._handle, value)

    @property
    def flex_ray_act_pt_off(self):
        return _props.get_cluster_flex_ray_act_pt_off(self._handle)

    @flex_ray_act_pt_off.setter
    def flex_ray_act_pt_off(self, value):
        _props.set_cluster_flex_ray_act_pt_off(self._handle, value)

    @property
    def flex_ray_cas_rx_l_max(self):
        return _props.get_cluster_flex_ray_cas_rx_l_max(self._handle)

    @flex_ray_cas_rx_l_max.setter
    def flex_ray_cas_rx_l_max(self, value):
        _props.set_cluster_flex_ray_cas_rx_l_max(self._handle, value)

    @property
    def flex_ray_channels(self):
        return _props.get_cluster_flex_ray_channels(self._handle)

    @flex_ray_channels.setter
    def flex_ray_channels(self, value):
        _props.set_cluster_flex_ray_channels(self._handle, value)

    @property
    def flex_ray_clst_drift_dmp(self):
        return _props.get_cluster_flex_ray_clst_drift_dmp(self._handle)

    @flex_ray_clst_drift_dmp.setter
    def flex_ray_clst_drift_dmp(self, value):
        _props.set_cluster_flex_ray_clst_drift_dmp(self._handle, value)

    @property
    def flex_ray_cold_st_ats(self):
        return _props.get_cluster_flex_ray_cold_st_ats(self._handle)

    @flex_ray_cold_st_ats.setter
    def flex_ray_cold_st_ats(self, value):
        _props.set_cluster_flex_ray_cold_st_ats(self._handle, value)

    @property
    def flex_ray_cycle(self):
        return _props.get_cluster_flex_ray_cycle(self._handle)

    @flex_ray_cycle.setter
    def flex_ray_cycle(self, value):
        _props.set_cluster_flex_ray_cycle(self._handle, value)

    @property
    def flex_ray_dyn_seg_start(self):
        return _props.get_cluster_flex_ray_dyn_seg_start(self._handle)

    @property
    def flex_ray_dyn_slot_idl_ph(self):
        return _props.get_cluster_flex_ray_dyn_slot_idl_ph(self._handle)

    @flex_ray_dyn_slot_idl_ph.setter
    def flex_ray_dyn_slot_idl_ph(self, value):
        _props.set_cluster_flex_ray_dyn_slot_idl_ph(self._handle, value)

    @property
    def flex_ray_latest_usable_dyn(self):
        return _props.get_cluster_flex_ray_latest_usable_dyn(self._handle)

    @property
    def flex_ray_latest_guar_dyn(self):
        return _props.get_cluster_flex_ray_latest_guar_dyn(self._handle)

    @property
    def flex_ray_lis_noise(self):
        return _props.get_cluster_flex_ray_lis_noise(self._handle)

    @flex_ray_lis_noise.setter
    def flex_ray_lis_noise(self, value):
        _props.set_cluster_flex_ray_lis_noise(self._handle, value)

    @property
    def flex_ray_macro_per_cycle(self):
        return _props.get_cluster_flex_ray_macro_per_cycle(self._handle)

    @flex_ray_macro_per_cycle.setter
    def flex_ray_macro_per_cycle(self, value):
        _props.set_cluster_flex_ray_macro_per_cycle(self._handle, value)

    @property
    def flex_ray_macrotick(self):
        return _props.get_cluster_flex_ray_macrotick(self._handle)

    @property
    def flex_ray_max_wo_clk_cor_fat(self):
        return _props.get_cluster_flex_ray_max_wo_clk_cor_fat(self._handle)

    @flex_ray_max_wo_clk_cor_fat.setter
    def flex_ray_max_wo_clk_cor_fat(self, value):
        _props.set_cluster_flex_ray_max_wo_clk_cor_fat(self._handle, value)

    @property
    def flex_ray_max_wo_clk_cor_pas(self):
        return _props.get_cluster_flex_ray_max_wo_clk_cor_pas(self._handle)

    @flex_ray_max_wo_clk_cor_pas.setter
    def flex_ray_max_wo_clk_cor_pas(self, value):
        _props.set_cluster_flex_ray_max_wo_clk_cor_pas(self._handle, value)

    @property
    def flex_ray_minislot_act_pt(self):
        return _props.get_cluster_flex_ray_minislot_act_pt(self._handle)

    @flex_ray_minislot_act_pt.setter
    def flex_ray_minislot_act_pt(self, value):
        _props.set_cluster_flex_ray_minislot_act_pt(self._handle, value)

    @property
    def flex_ray_minislot(self):
        return _props.get_cluster_flex_ray_minislot(self._handle)

    @flex_ray_minislot.setter
    def flex_ray_minislot(self, value):
        _props.set_cluster_flex_ray_minislot(self._handle, value)

    @property
    def flex_ray_nm_vec_len(self):
        return _props.get_cluster_flex_ray_nm_vec_len(self._handle)

    @flex_ray_nm_vec_len.setter
    def flex_ray_nm_vec_len(self, value):
        _props.set_cluster_flex_ray_nm_vec_len(self._handle, value)

    @property
    def flex_ray_nit(self):
        return _props.get_cluster_flex_ray_nit(self._handle)

    @flex_ray_nit.setter
    def flex_ray_nit(self, value):
        _props.set_cluster_flex_ray_nit(self._handle, value)

    @property
    def flex_ray_nit_start(self):
        return _props.get_cluster_flex_ray_nit_start(self._handle)

    @property
    def flex_ray_num_minislt(self):
        return _props.get_cluster_flex_ray_num_minislt(self._handle)

    @flex_ray_num_minislt.setter
    def flex_ray_num_minislt(self, value):
        _props.set_cluster_flex_ray_num_minislt(self._handle, value)

    @property
    def flex_ray_num_stat_slt(self):
        return _props.get_cluster_flex_ray_num_stat_slt(self._handle)

    @flex_ray_num_stat_slt.setter
    def flex_ray_num_stat_slt(self, value):
        _props.set_cluster_flex_ray_num_stat_slt(self._handle, value)

    @property
    def flex_ray_off_cor_st(self):
        return _props.get_cluster_flex_ray_off_cor_st(self._handle)

    @flex_ray_off_cor_st.setter
    def flex_ray_off_cor_st(self, value):
        _props.set_cluster_flex_ray_off_cor_st(self._handle, value)

    @property
    def flex_ray_payld_len_dyn_max(self):
        return _props.get_cluster_flex_ray_payld_len_dyn_max(self._handle)

    @flex_ray_payld_len_dyn_max.setter
    def flex_ray_payld_len_dyn_max(self, value):
        _props.set_cluster_flex_ray_payld_len_dyn_max(self._handle, value)

    @property
    def flex_ray_payld_len_max(self):
        return _props.get_cluster_flex_ray_payld_len_max(self._handle)

    @property
    def flex_ray_payld_len_st(self):
        return _props.get_cluster_flex_ray_payld_len_st(self._handle)

    @flex_ray_payld_len_st.setter
    def flex_ray_payld_len_st(self, value):
        _props.set_cluster_flex_ray_payld_len_st(self._handle, value)

    @property
    def flex_ray_stat_slot(self):
        return _props.get_cluster_flex_ray_stat_slot(self._handle)

    @flex_ray_stat_slot.setter
    def flex_ray_stat_slot(self, value):
        _props.set_cluster_flex_ray_stat_slot(self._handle, value)

    @property
    def flex_ray_sym_win(self):
        return _props.get_cluster_flex_ray_sym_win(self._handle)

    @flex_ray_sym_win.setter
    def flex_ray_sym_win(self, value):
        _props.set_cluster_flex_ray_sym_win(self._handle, value)

    @property
    def flex_ray_sym_win_start(self):
        return _props.get_cluster_flex_ray_sym_win_start(self._handle)

    @property
    def flex_ray_sync_node_max(self):
        return _props.get_cluster_flex_ray_sync_node_max(self._handle)

    @flex_ray_sync_node_max.setter
    def flex_ray_sync_node_max(self, value):
        _props.set_cluster_flex_ray_sync_node_max(self._handle, value)

    @property
    def flex_ray_tss_tx(self):
        return _props.get_cluster_flex_ray_tss_tx(self._handle)

    @flex_ray_tss_tx.setter
    def flex_ray_tss_tx(self, value):
        _props.set_cluster_flex_ray_tss_tx(self._handle, value)

    @property
    def flex_ray_wake_sym_rx_idl(self):
        return _props.get_cluster_flex_ray_wake_sym_rx_idl(self._handle)

    @flex_ray_wake_sym_rx_idl.setter
    def flex_ray_wake_sym_rx_idl(self, value):
        _props.set_cluster_flex_ray_wake_sym_rx_idl(self._handle, value)

    @property
    def flex_ray_wake_sym_rx_low(self):
        return _props.get_cluster_flex_ray_wake_sym_rx_low(self._handle)

    @flex_ray_wake_sym_rx_low.setter
    def flex_ray_wake_sym_rx_low(self, value):
        _props.set_cluster_flex_ray_wake_sym_rx_low(self._handle, value)

    @property
    def flex_ray_wake_sym_rx_win(self):
        return _props.get_cluster_flex_ray_wake_sym_rx_win(self._handle)

    @flex_ray_wake_sym_rx_win.setter
    def flex_ray_wake_sym_rx_win(self, value):
        _props.set_cluster_flex_ray_wake_sym_rx_win(self._handle, value)

    @property
    def flex_ray_wake_sym_tx_idl(self):
        return _props.get_cluster_flex_ray_wake_sym_tx_idl(self._handle)

    @flex_ray_wake_sym_tx_idl.setter
    def flex_ray_wake_sym_tx_idl(self, value):
        _props.set_cluster_flex_ray_wake_sym_tx_idl(self._handle, value)

    @property
    def flex_ray_wake_sym_tx_low(self):
        return _props.get_cluster_flex_ray_wake_sym_tx_low(self._handle)

    @flex_ray_wake_sym_tx_low.setter
    def flex_ray_wake_sym_tx_low(self, value):
        _props.set_cluster_flex_ray_wake_sym_tx_low(self._handle, value)

    @property
    def flex_ray_use_wakeup(self):
        return _props.get_cluster_flex_ray_use_wakeup(self._handle)

    @flex_ray_use_wakeup.setter
    def flex_ray_use_wakeup(self, value):
        _props.set_cluster_flex_ray_use_wakeup(self._handle, value)

    @property
    def lin_schedules(self):
        # type: () -> _collection.DbCollection
        """:any:`DbCollection`: Returns a collection of :any:`LinSched` defined in this cluster.

        You assign a LIN schedule to a cluster when you create the LIN schedule object.
        You cannot change this assignment afterwards.
        The schedules in this collection are sorted alphabetically by schedule name.
        """
        return self._lin_sched

    @property
    def lin_tick(self):
        # type: () -> float
        """float: Returns the relative time between LIN ticks (relative f64 in seconds).

        The :any:`LinSchedEntry.delay` property must be a multiple of this tick.

        This tick is referred to as the "timebase" in the LIN specification.

        The :any:`Ecu.lin_master` property defines the Tick property in this cluster.
        You cannot use the Tick property when there is no LIN Master property defined in this cluster.
        """
        return _props.get_cluster_lin_tick(self._handle)

    @lin_tick.setter
    def lin_tick(self, value):
        # type: (float) -> None
        _props.set_cluster_lin_tick(self._handle, value)

    @property
    def flex_ray_alw_pass_act(self):
        return _props.get_cluster_flex_ray_alw_pass_act(self._handle)

    @flex_ray_alw_pass_act.setter
    def flex_ray_alw_pass_act(self, value):
        _props.set_cluster_flex_ray_alw_pass_act(self._handle, value)

    @property
    def application_protocol(self):
        # type: () -> constants.AppProtocol
        """:any:`AppProtocol`: Get or set the application protocol."""
        return constants.AppProtocol(_props.get_cluster_application_protocol(self._handle))

    @application_protocol.setter
    def application_protocol(self, value):
        # type: (constants.AppProtocol) -> None
        _props.set_cluster_application_protocol(self._handle, value.value)

    @property
    def can_fd_iso_mode(self):
        # type: () -> constants.CanFdIsoMode
        """:any:`CanFdIsoMode`: Returns the mode of a CAN FD cluster.

        The default is ``CanFdIsoMode.ISO``.
        You define the value in a dialog box that appears when you define an alias for the database.
        """
        return constants.CanFdIsoMode(_props.get_cluster_can_fd_iso_mode(self._handle))
