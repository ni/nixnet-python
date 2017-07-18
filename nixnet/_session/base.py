from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import warnings

from nixnet import _funcs
from nixnet import _props
from nixnet import constants
from nixnet import errors

from nixnet._session import intf
from nixnet._session import j1939


class SessionBase(object):
    """Session base object."""

    def __init__(
            self,
            database_name,
            cluster_name,
            list,
            interface_name,
            mode):
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
        self._intf = intf.Interface(self._handle)
        self._j1939 = j1939.J1939(self._handle)

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
            return self._handle == other._handle
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._handle)

    def __repr__(self):
        return 'Session(handle={0})'.format(self._handle)

    def close(self):
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
            scope: Describes the impact of this operation on the underlying
                state models for the session and its interface.
                See :any:`nixnet._enums.StartStopScope`.
        """
        _funcs.nx_start(self._handle, scope)

    def stop(self, scope=constants.StartStopScope.NORMAL):
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
            scope: Describes the impact of this operation on the underlying
                state models for the session and its interface.
                See :any:`nixnet._enums.StartStopScope`.
        """
        _funcs.nx_stop(self._handle, scope)

    def flush(self):
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
        """Wait for transmition to complete.

        All frames written for the session have been transmitted on the bus.
        This condition applies to CAN, LIN, and FlexRay. This condition is state
        based, and the state is Boolean (true/false).

        Args:
            timeout: A float representing the maximum amount of time to wait in
                seconds.
        """
        _funcs.nx_wait(self._handle, constants.Condition.TRANSMIT_COMPLETE, 0, timeout)

    def wait_for_intf_communicating(self, timeout=10):
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
            timeout: A float representing the maximum amount of time to wait in
                seconds.
        """
        _funcs.nx_wait(self._handle, constants.Condition.INTF_COMMUNICATING, 0, timeout)

    def wait_for_intf_remote_wakeup(self, timeout=10):
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
            timeout: A float representing the maximum amount of time to wait in
                seconds.
        """
        _funcs.nx_wait(self._handle, constants.Condition.INTF_REMOTE_WAKEUP, 0, timeout)

    def connect_terminals(self, source, destination):
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
            source: A string representing the connection source name.
            destination: A string representing the connection destination name.
        """
        _funcs.nx_connect_terminals(self._handle, source, destination)

    def disconnect_terminals(self, source, destination):
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
            source: A string representing the connection source name.
            destination: A string representing the connection destination name.
        """
        _funcs.nx_disconnect_terminals(self._handle, source, destination)

    @property
    def intf(self):
        """:any:`nixnet._session.intf.Interface`: Returns the Interface configuration object for the session."""
        return self._intf

    @property
    def j1939(self):
        """:any:`nixnet._session.j1939.J1939`: Returns the J1939 configuration object for the session."""
        return self._j1939

    @property
    def application_protocol(self):
        """:any:`nixnet._enums.AppProtocol`: This property returns the application protocol that the session uses.

        The database used with the session determines the application protocol.
        """
        return constants.AppProtocol(_props.get_session_application_protocol(self._handle))

    @property
    def auto_start(self):
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
        _props.set_session_auto_start(self._handle, value)

    @property
    def cluster_name(self):
        """str: This property returns the cluster (network) name used with the session."""
        return _props.get_session_cluster_name(self._handle)

    @property
    def database_name(self):
        """str: This property returns the database name used with the session."""
        return _props.get_session_database_name(self._handle)

    @property
    def mode(self):
        """:any:`nixnet._enums.CreateSessionMode`: This property returns the mode associated with the session.

        For more information, refer to :any:`nixnet._enums.CreateSessionMode`.
        """
        return constants.CreateSessionMode(_props.get_session_mode(self._handle))

    @property
    def num_pend(self):
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
    def payld_len_max(self):
        """int: Returns the maximum payload length of all frames in this session, expressed as bytes (0-254).

        This property does not apply to Signal sessions (only Frame sessions).

        For CAN Stream (Input and Output), this property depends on the XNET
        Cluster CAN I/O Mode property. If the I/O mode is CAN, this property is
        8 bytes. If the I/O mode is 'constants.CaNioMode.CANFD' or
        'constants.CaNioMode.CANFD', this property is 64 bytes.

        For LIN Stream (Input and Output), this property always is 8 bytes. For
        FlexRay Stream (Input and Output), this property is the same as the XNET
        Cluster FlexRay Payload Length Maximum property value. For Queued and
        Single-Point (Input and Output), this is the maximum payload of all
        frames specified in the List property.
        """
        return _props.get_session_payld_len_max(self._handle)

    @property
    def protocol(self):
        """:any:`nixnet._enums.Protocol`: This property returns the protocol that the interface in the session uses."""
        return constants.Protocol(_props.get_session_protocol(self._handle))

    @property
    def queue_size(self):
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
        _props.set_session_queue_size(self._handle, value)

    @property
    def resamp_rate(self):
        """float: Rate used to resample frame data to/from signal data in waveforms.

        This property applies only when the session mode is Signal Input
        Waveform or Signal Output Waveform. This property is ignored for all
        other modes.

        The data type is 64-bit floating point. The units are in Hertz (samples per second).
        """
        return _props.get_session_resamp_rate(self._handle)

    @resamp_rate.setter
    def resamp_rate(self, value):
        _props.set_session_resamp_rate(self._handle, value)
