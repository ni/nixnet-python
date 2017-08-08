from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import ctypes  # type: ignore
import typing  # NOQA: F401
import warnings

from nixnet import _ctypedefs
from nixnet import _errors
from nixnet import _funcs
from nixnet import _props
from nixnet import _utils
from nixnet import constants
from nixnet import errors
from nixnet import types  # NOQA: F401

from nixnet._session import intf as session_intf
from nixnet._session import j1939 as session_j1939


class SessionBase(object):
    """Session base object."""

    def __init__(
            self,
            database_name,  # type: typing.Text
            cluster_name,  # type: typing.Text
            list,  # type: typing.Text
            interface_name,  # type: typing.Text
            mode,  # type: constants.CreateSessionMode
    ):
        # type: (...) -> None
        """Create an XNET session at run time using named references to database objects.

        This function creates a session using the named database objects
        specified in 'list' from the database named in 'database_name'.

        This function is intended to be used by session classes that derive from
        SessionBase; therefore, it is not public.

        Args:
            database_name: A string representing the XNET database to use for
                interface configuration. The database name must use the <alias>
                or <filepath> syntax (refer to Databases).
            cluster_name: A string representing the XNET cluster to use for
                interface configuration. The name must specify a cluster from
                the database given in the database_name parameter. If it is left
                blank, the cluster is extracted from the list parameter; this is
                not allowed for modes of 'constants.CreateSessionMode.FRAME_IN_STREAM'
                or 'constants.CreateSessionMode.FRAME_OUT_STREAM'.
            list: A list of strings describing signals or frames for the session.
                The list syntax depends on the mode. Refer to mode spefic
                session classes defined below for 'list' syntax.
            interface_name: A string representing the XNET Interface to use for
                this session. If Mode is
                'constants.CreateSessionMode.SIGNAL_CONVERSION_SINGLE_POINT',
                this input is ignored. You can set it to an empty string.
            mode: The session mode. See :any:`nixnet._enums.CreateSessionMode`.

        Returns:
            A session base object.
        """
        self._handle = None  # To satisfy `__del__` in case nx_create_session throws
        self._handle = _funcs.nx_create_session(database_name, cluster_name, list, interface_name, mode)
        self._intf = session_intf.Interface(self._handle)
        self._j1939 = session_j1939.J1939(self._handle)

    def __del__(self):
        if self._handle is not None:
            warnings.warn(
                'Session was not explicitly closed before it was destructed. '
                'Resources on the device may still be reserved.',
                errors.XnetResourceWarning)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == typing.cast(SessionBase, other._handle)
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
        # type: () -> typing.Text
        return 'Session(handle={0})'.format(self._handle)

    def close(self):
        # type: () -> None
        """Close (clear) the XNET session.

        This function stops communication for the session and releases all
        resources the session uses. It internally calls
        :any:`nixnet._session.base.SessionBase.stop` with normal scope, so if
        this is the last session using the interface, communication stops.

        You typically use 'close' when you need to close the existing session to
        create a new session that uses the same objects. For example, if you
        create a session for a frame named frame_a using Frame Output
        Single-Point mode, then you create a second session for frame_a using
        Frame Output Queued mode, the second call to the session constructor
        returns an error, because frame_a can be accessed using only one output
        mode. If you call 'close' before the second constructor call, you can
        close the previous use of frame_a to create the new session.
        """
        if self._handle is None:
            warnings.warn(
                'Attempting to close NI-XNET session but session was already '
                'closed', errors.XnetResourceWarning)
            return

        _funcs.nx_clear(self._handle)

        self._handle = None

    def start(self, scope=constants.StartStopScope.NORMAL):
        # type: (constants.StartStopScope) -> None
        """Start communication for the XNET session.

        Because the session is started automatically by default, this function
        is optional. This function is for more advanced applications to start
        multiple sessions in a specific order. For more information about the
        automatic start feature, refer to the
        :any:`nixnet._session.base.SessionBase.auto_start` property.

        For each physical interface, the NI-XNET hardware is divided into two logical units:

            Sessions: You can create one or more sessions, each of which contains
            frames or signals to be transmitted (or received) on the bus.

            Interface: The interface physically connects to the bus and transmits
            (or receives) data for the sessions.

        You can start each logical unit separately. When a session is started,
        all contained frames or signals are placed in a state where they are
        ready to communicate. When the interface is started, it takes data from
        all started sessions to communicate with other nodes on the bus. For a
        specification of the state models for the session and interface, refer
        to State Models.

        If an output session starts before you write data, or you read an input
        session before it receives a frame, default data is used. For more
        information, refer to the XNET Frame Default Payload and XNET Signal
        Default Value properties.

        Args:
            scope(:any:`nixnet._enums.StartStopScope`): Describes the impact of
                this operation on the underlying state models for the session
                and its interface.
        """
        _funcs.nx_start(self._handle, scope)

    def stop(self, scope=constants.StartStopScope.NORMAL):
        # type: (constants.StartStopScope) -> None
        """Stop communication for the XNET session.

        Because the session is stopped automatically when closed (cleared),
        this function is optional.

        For each physical interface, the NI-XNET hardware is divided into two logical units:

            Sessions: You can create one or more sessions, each of which contains
            frames or signals to be transmitted (or received) on the bus.

            Interface: The interface physically connects to the bus and transmits
            (or receives) data for the sessions.

        You can stop each logical unit separately. When a session is stopped,
        all contained frames or signals are placed in a state where they are no
        longer ready to communicate. When the interface is stopped, it no longer
        takes data from sessions to communicate with other nodes on the bus. For
        a specification of the state models for the session and interface, refer
        to State Models.

        Args:
            scope(:any:`nixnet._enums.StartStopScope`): Describes the impact of
                this operation on the underlying state models for the session
                and its interface.
        """
        _funcs.nx_stop(self._handle, scope)

    def flush(self):
        # type: () -> None
        """Flushes (empties) all XNET session queues.

        With the exception of single-point modes, all sessions use queues to
        store frames. For input modes, the queues store frame values (or
        corresponding signal values) that have been received, but not obtained
        by calling the read function. For output sessions, the queues store
        frame values provided to write function, but not transmitted successfully.

        :any:`nixnet._session.base.SessionBase.start` and
        :any:`nixnet._session.base.SessionBase.stop` have no effect on these
        queues. Use 'flush' to discard all values in the session's queues.

        For example, if you call a write function to write three frames, then
        immediately call :any:`nixnet._session.base.SessionBase.stop`, then
        call :any:`nixnet._session.base.SessionBase.start` a few seconds
        later, the three frames transmit. If you call 'flush' between
        :any:`nixnet._session.base.SessionBase.stop` and
        :any:`nixnet._session.base.SessionBase.start`, no frames transmit.

        As another example, if you receive three frames, then call
        :any:`nixnet._session.base.SessionBase.stop`, the three frames remains
        in the queue. If you call :any:`nixnet._session.base.SessionBase.start`
        a few seconds later, then call a read function, you obtain the three
        frames received earlier, potentially followed by other frames received
        after calling :any:`nixnet._session.base.SessionBase.start`. If you
        call 'flush' between :any:`nixnet._session.base.SessionBase.stop` and
        :any:`nixnet._session.base.SessionBase.start`, read function returns
        only frames received after the calling
        :any:`nixnet._session.base.SessionBase.start`.
        """
        _funcs.nx_flush(self._handle)

    def wait_for_transmit_complete(self, timeout=10):
        # type: (float) -> None
        """Wait for transmition to complete.

        All frames written for the session have been transmitted on the bus.
        This condition applies to CAN, LIN, and FlexRay. This condition is state
        based, and the state is Boolean (true/false).

        Args:
            timeout(float): The maximum amount of time to wait in seconds.
        """
        _funcs.nx_wait(self._handle, constants.Condition.TRANSMIT_COMPLETE, 0, timeout)

    def wait_for_intf_communicating(self, timeout=10):
        # type: (float) -> None
        """Wait for the interface to begin communication on the network.

        If a start trigger is configured for the interface, this first waits for
        the trigger. Once the interface is started, this waits for the
        protocol's communication state to transition to a value that indicates
        communication with remote nodes.

        After this wait succeeds, calls to 'read_state' will return:

            :any:`nixnet._enums.CanCommState`: 'constants.CAN_COMM.ERROR_ACTIVE'

            :any:`nixnet._enums.CanCommState`: 'constants.CAN_COMM.ERROR_PASSIVE'

            'constants.ReadState.TIME_COMMUNICATING': Valid time for
            communication (invalid time of 0 prior)

        Args:
            timeout(float): The maximum amount of time to wait in seconds.
        """
        _funcs.nx_wait(self._handle, constants.Condition.INTF_COMMUNICATING, 0, timeout)

    def wait_for_intf_remote_wakeup(self, timeout=10):
        # type: (float) -> None
        """Wait for interface remote wakeup.

        Wait for the interface to wakeup due to activity by a remote node on the
        network. This wait is used for CAN, when you set the 'can_tcvr_state'
        property to 'constants.CanTcvrState.SLEEP'. Although the interface
        itself is ready to communicate, this places the transceiver into a sleep
        state. When a remote CAN node transmits a frame, the transceiver wakes
        up, and communication is restored. This wait detects that remote wakeup.

        This wait is used for LIN when you set 'lin_sleep' property to
        'constants.LinSleep.REMOTE_SLEEP' or 'constants.LinSleep.LOCAL_SLEEP'.
        When asleep, if a remote LIN ECU transmits the wakeup pattern (break),
        the XNET LIN interface detects this transmission and wakes up. This wait
        detects that remote wakeup.

        Args:
            timeout(float): The maximum amount of time to wait in seconds.
        """
        _funcs.nx_wait(self._handle, constants.Condition.INTF_REMOTE_WAKEUP, 0, timeout)

    def connect_terminals(self, source, destination):
        # type: (typing.Text, typing.Text) -> None
        """Connect terminals on the XNET interface.

        This function connects a source terminal to a destination terminal on
        the interface hardware. The XNET terminal represents an external or
        internal hardware connection point on a National Instruments XNET
        hardware product. External terminals include PXI Trigger lines for a PXI
        card, RTSI terminals for a PCI card, or the single external terminal for
        a C Series module. Internal terminals include timebases (clocks) and
        logical entities such as a start trigger.

        The terminal inputs use the Terminal I/O names. Typically, one of the
        pair is an internal and the other an external.

        Args:
            source(str): Connection source name.
            destination(str): Connection destination name.
        """
        _funcs.nx_connect_terminals(self._handle, source, destination)

    def disconnect_terminals(self, source, destination):
        # type: (typing.Text, typing.Text) -> None
        """Disconnect terminals on the XNET interface.

        This function disconnects a specific pair of source/destination terminals
        previously connected with :any:`nixnet._session.base.SessionBase.connect_terminals`.

        When the final session for a given interface is cleared, NI-XNET
        automatically disconnects all terminal connections for that interface.
        Therefore, 'disconnect_terminals' is not required for most applications.

        This function typically is used to change terminal connections
        dynamically while an application is running. To disconnect a terminal,
        you first must stop the interface using
        :any:`nixnet._session.base.SessionBase.stop` with the Interface Only
        scope. Then you can call 'disconnect_terminals' and
        :any:`nixnet._session.base.SessionBase.connect_terminals` to adjust
        terminal connections. Finally, you can call
        :any:`nixnet._session.base.SessionBase.start` with the Interface Only
        scope to restart the interface.

        You can disconnect only a terminal that has been previously connected.
        Attempting to disconnect a nonconnected terminal results in an error.

        Args:
            source(str): Connection source name.
            destination(str): Connection destination name.
        """
        _funcs.nx_disconnect_terminals(self._handle, source, destination)

    def change_lin_schedule(self, sched_index):
        # type: (int) -> None
        """Writes communication states of an XNET session.

        This function writes a request for the LIN interface to change
        the running schedule.

        According to the LIN protocol, only the master executes schedules,
        not slaves. If the
        :any:`nixnet._session.intf.Interface.lin_master` property is false (slave),
        this write function implicitly sets that property to true (master). If the
        interface currently is running as a slave, this write returns an error,
        because it cannot change to master while running.

        Args:
            sched_index(int): Index to the schedule table that the LIN master executes.

            The schedule tables are sorted the way they are returned from the database
            with the `nixnet.db._cluster.Cluster.lin_schedules` property.
        """
        _funcs.nx_write_state(self._handle, constants.WriteState.LIN_SCHEDULE_CHANGE, _ctypedefs.u32(sched_index))

    def change_lin_diagnostic_schedule(self, schedule):
        # type: (constants.LinDiagnosticSchedule) -> None
        """Writes communication states of an XNET session.

        This function writes a request for the LIN interface to change
        the diagnostic schedule.

        Args:
            schedule(:any:`nixnet._enums.LinDiagnosticSchedule`): Diagnostic schedule
                that the LIN master executes.
        """
        _funcs.nx_write_state(self._handle, constants.WriteState.LIN_DIAGNOSTIC_SCHEDULE_CHANGE, _ctypedefs.u32(schedule.value))  # NOQA: E501

    @property
    def time_current(self):
        # type: () -> int
        """int: Current interface time."""
        state_value_ctypes = _ctypedefs.nxTimestamp_t()
        _funcs.nx_read_state(
            self._handle,
            constants.ReadState.TIME_CURRENT,
            ctypes.pointer(state_value_ctypes))
        time = state_value_ctypes.value
        return time

    @property
    def time_start(self):
        # type: () -> int
        """int: Time the interface was started."""
        state_value_ctypes = _ctypedefs.nxTimestamp_t()
        _funcs.nx_read_state(
            self._handle,
            constants.ReadState.TIME_START,
            ctypes.pointer(state_value_ctypes))
        time = state_value_ctypes.value
        if time == 0:
            # The interface is not communicating.
            _errors.check_for_error(constants.Err.SESSION_NOT_STARTED.value)
        return time

    @property
    def time_communicating(self):
        # type: () -> int
        """int: Time the interface started communicating.

        The time is usually later than ``time_start`` because the interface
        must undergo a communication startup procedure.
        """
        state_value_ctypes = _ctypedefs.nxTimestamp_t()
        _funcs.nx_read_state(
            self._handle,
            constants.ReadState.TIME_COMMUNICATING,
            ctypes.pointer(state_value_ctypes))
        time = state_value_ctypes.value
        if time == 0:
            # The interface is not communicating.
            _errors.check_for_error(constants.Err.SESSION_NOT_STARTED.value)
        return time

    @property
    def state(self):
        # type: () -> constants.SessionInfoState
        """:any:`nixnet._enums.SessionInfoState`: Session running state."""
        state_value_ctypes = _ctypedefs.u32()
        _funcs.nx_read_state(
            self._handle,
            constants.ReadState.SESSION_INFO,
            ctypes.pointer(state_value_ctypes))
        state = state_value_ctypes.value
        return constants.SessionInfoState(state)

    @property
    def can_comm(self):
        # type: () -> types.CanComm
        """:any:`nixnet.types.CanComm`: CAN Communication state"""
        state_value_ctypes = _ctypedefs.u32()
        _funcs.nx_read_state(
            self._handle,
            constants.ReadState.CAN_COMM,
            ctypes.pointer(state_value_ctypes))
        bitfield = state_value_ctypes.value
        return _utils.parse_can_comm_bitfield(bitfield)

    @property
    def lin_comm(self):
        # type: () -> types.LinComm
        """:any:`nixnet.types.LinComm`: LIN Communication state"""
        state_value_ctypes = (_ctypedefs.u32 * 2)()  # type: ignore
        _funcs.nx_read_state(
            self._handle,
            constants.ReadState.LIN_COMM,
            ctypes.pointer(state_value_ctypes))
        first = state_value_ctypes[0].value
        second = state_value_ctypes[1].value
        return _utils.parse_lin_comm_bitfield(first, second)

    def check_fault(self):
        # type: () -> None
        """Check for an asynchronous fault.

        A fault is an error that occurs asynchronously to the NI-XNET
        application calls. The fault cause may be related to network
        communication, but it also can be related to XNET hardware, such as a
        fault in the onboard processor. Although faults are extremely rare,
        nxReadState provides a detection method distinct from the status of
        NI-XNET function calls, yet easy to use alongside the common practice
        of checking the communication state.
        """
        state_value_ctypes = _ctypedefs.u32()
        fault = _funcs.nx_read_state(
            self._handle,
            constants.ReadState.SESSION_INFO,
            ctypes.pointer(state_value_ctypes))
        _errors.check_for_error(fault)

    @property
    def intf(self):
        # type: () -> session_intf.Interface
        """:any:`nixnet._session.intf.Interface`: Returns the Interface configuration object for the session."""
        return self._intf

    @property
    def j1939(self):
        # type: () -> session_j1939.J1939
        """:any:`nixnet._session.j1939.J1939`: Returns the J1939 configuration object for the session."""
        return self._j1939

    @property
    def application_protocol(self):
        # type: () -> constants.AppProtocol
        """:any:`nixnet._enums.AppProtocol`: This property returns the application protocol that the session uses.

        The database used with the session determines the application protocol.
        """
        return constants.AppProtocol(_props.get_session_application_protocol(self._handle))

    @property
    def auto_start(self):
        # type: () -> bool
        """bool: Automatically starts the output session on the first call to the appropriate write function.

        For input sessions, start always is performed within the first call to
        the appropriate read function (if not already started using
        :any:`nixnet._session.base.SessionBase.start`). This is done
        because there is no known use case for reading a stopped input session.

        For output sessions, as long as the first call to the appropriate write
        function contains valid data, you can leave this property at its default
        value of true. If you need to call the appropriate write function
        multiple times prior to starting the session, or if you are starting
        multiple sessions simultaneously, you can set this property to false.
        After calling the appropriate write function as desired, you can call
        :any:`nixnet._session.base.SessionBase.start` to start the session(s).

        When automatic start is performed, it is equivalent to
        :any:`nixnet._session.base.SessionBase.start` with scope set to Normal.
        This starts the session itself, and if the interface is not already
        started, it starts the interface also.
        """
        return _props.get_session_auto_start(self._handle)

    @auto_start.setter
    def auto_start(self, value):
        # type: (bool) -> None
        _props.set_session_auto_start(self._handle, value)

    @property
    def cluster_name(self):
        # type: () -> typing.Text
        """str: This property returns the cluster (network) name used with the session."""
        return _props.get_session_cluster_name(self._handle)

    @property
    def database_name(self):
        # type: () -> typing.Text
        """str: This property returns the database name used with the session."""
        return _props.get_session_database_name(self._handle)

    @property
    def mode(self):
        # type: () -> constants.CreateSessionMode
        """:any:`nixnet._enums.CreateSessionMode`: This property returns the mode associated with the session.

        For more information, refer to :any:`nixnet._enums.CreateSessionMode`.
        """
        return constants.CreateSessionMode(_props.get_session_mode(self._handle))

    @property
    def num_pend(self):
        # type: () -> int
        """int: This property returns the number of values (frames or signals) pending for the session.

        For input sessions, this is the number of frame/signal values available
        to the appropriate read function. If you call the appropriate read
        function with number to read of this number and timeout of 0.0, the
        appropriate read function should return this number of values successfully.

        For output sessions, this is the number of frames/signal values provided
        to the appropriate write function but not yet transmitted onto the network.

        Stream frame sessions using FlexRay or CAN FD protocol may use a
        variable size of frames. In these cases, this property assumes the
        largest possible frame size. If you use smaller frames, the real number
        of pending values might be higher.

        The largest possible frames sizes are:

            CAN FD: 64 byte payload.

            FlexRay: The higher value of the frame size in the static segment
            and the maximum frame size in the dynamic segment. The XNET Cluster
            FlexRay Payload Length Maximum property provides this value.
        """
        return _props.get_session_num_pend(self._handle)

    @property
    def num_unused(self):
        # type: () -> int
        """int: This property returns the number of values (frames or signals) unused for the session.

        If you get this property prior to starting the session, it provides the
        size of the underlying queue(s). Contrary to the Queue Size property,
        this value is in number of frames for Frame I/O, not number of bytes;
        for Signal I/O, it is the number of signal values in both cases. After
        start, this property returns the queue size minus the
        :any:`Number of Values Pending <nixnet._session.base.SessionBase.num_pend>`
        property.

        For input sessions, this is the number of frame/signal values unused in
        the underlying queue(s).

        For output sessions, this is the number of frame/signal values you can
        provide to a subsequent call to the appropriate write function. If you
        call the appropriate write function with this number of values and
        timeout of 0.0, it should return success.

        Stream frame sessions using FlexRay or CAN FD protocol may use a
        variable size of frames. In these cases, this property assumes the
        largest possible frame size. If you use smaller frames, the real number
        of pending values might be higher.

        The largest possible frames sizes are:

            CAN FD: 64 byte payload.

            FlexRay: The higher value of the frame size in the static segment
            and the maximum frame size in the dynamic segment. The XNET Cluster
            FlexRay Payload Length Maximum property provides this value.
        """
        return _props.get_session_num_unused(self._handle)

    @property
    def protocol(self):
        # type: () -> constants.Protocol
        """:any:`nixnet._enums.Protocol`: This property returns the protocol that the interface in the session uses."""
        return constants.Protocol(_props.get_session_protocol(self._handle))

    @property
    def queue_size(self):
        # type: () -> int
        """int: Get or set queue size.

        For output sessions, queues store data passed to the appropriate
        write function and not yet transmitted onto the network. For input
        sessions, queues store data received from the network and not yet
        obtained using the appropriate read function.

        For most applications, the default queue sizes are sufficient. You can
        write to this property to override the default. When you write (set)
        this property, you must do so prior to the first session start. You
        cannot set this property again after calling
        :any:`nixnet._session.base.SessionBase.stop`.

        For signal I/O sessions, this property is the number of signal values
        stored. This is analogous to the number of values you use with the
        appropriate read or write function.

        For frame I/O sessions, this property is the number of bytes of frame
        data stored.

        For standard CAN or LIN frame I/O sessions, each frame uses exactly 24
        bytes. You can use this number to convert the Queue Size (in bytes)
        to/from the number of frame values.

        For CAN FD and FlexRay frame I/O sessions, each frame value size can
        vary depending on the payload length. For more information, refer to
        Raw Frame Format.

        For Signal I/O XY sessions, you can use signals from more than one frame.
        Within the implementation, each frame uses a dedicated queue. According
        to the formulas below, the default queue sizes can be different for each
        frame. If you read the default Queue Size property for a Signal Input XY
        session, the largest queue size is returned, so that a call to the
        appropriate read function of that size can empty all queues. If you
        read the default Queue Size property for a Signal Output XY session, the
        smallest queue size is returned, so that a call to the appropriate write
        function of that size can succeed when all queues are empty. If you
        write the Queue Size property for a Signal I/O XY session, that size is
        used for all frames, so you must ensure that it is sufficient for the
        frame with the fastest transmit time.

        For Signal I/O Waveform sessions, you can use signals from more than one
        frame. Within the implementation, each frame uses a dedicated queue. The
        Queue Size property does not represent the memory in these queues, but
        rather the amount of time stored. The default queue allocations store
        Application Time worth of resampled signal values. If you read the
        default Queue Size property for a Signal I/O Waveform session, it
        returns Application Time multiplied by the time Resample Rate. If you
        write the Queue Size property for a Signal I/O Waveform session, that
        value is translated from a number of samples to a time, and that time is
        used to allocate memory for each queue.

        For Single-Point sessions (signal or frame), this property is ignored.
        Single-Point sessions always use a value of 1 as the effective queue size.
        """
        return _props.get_session_queue_size(self._handle)

    @queue_size.setter
    def queue_size(self, value):
        # type: (int) -> None
        _props.set_session_queue_size(self._handle, value)
