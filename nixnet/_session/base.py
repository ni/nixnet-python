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
                not allowed for modes of
                :class:`nixnet.constants.CreateSessionMode.FRAME_IN_STREAM`
                or :class:`nixnet.constants.CreateSessionMode.FRAME_OUT_STREAM`.
            list: A list of strings describing signals or frames for the session.
                The list syntax depends on the mode. Refer to mode spefic
                session classes defined below for 'list' syntax.
            interface_name: A string representing the XNET Interface to use for
                this session. If Mode is
                :class:`nixnet.constants.CreateSessionMode.SIGNAL_CONVERSION_SINGLE_POINT`,
                this input is ignored. You can set it to an empty string.
            mode: The session mode. See :class:`nixnet._enums.CreateSessionMode`.

        Returns:
            A Session object.
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
        :class:`nixnet.session.Session.stop` with normal scope, so if this is the
        last session using the interface, communication stops.

        You typically use 'close' when you need to close the existing session to
        create a new session that uses the same objects. For example, if you
        create a session for a frame named frame_a using Frame Output
        Single-Point mode, then you create a second session for frame_a using
        Frame Output Queued mode, the second call to the session constructor
        returns an error, because frame_a can be accessed using only one output
        mode. If you call 'close' before the second constructor call, you can
        close the previous use of frame_a to create the new session.

        Args:
            None

        Returns:
            None
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
        :class:`nixnet.session.Session.auto_start` property.

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
                See :class:`nixnet._enums.StartStopScope`.

        Returns:
            None
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
                See :class:`nixnet._enums.StartStopScope`.

        Returns:
            None
        """
        _funcs.nx_stop(self._handle, scope)

    def flush(self):
        """Flushes (empties) all XNET session queues.

        With the exception of single-point modes, all sessions use queues to
        store frames. For input modes, the queues store frame values (or
        corresponding signal values) that have been received, but not obtained
        by calling the read function. For output sessions, the queues store
        frame values provided to write function, but not transmitted successfully.

        :class:`nixnet.session.Session.start` and :class:`nixnet.session.Session.stop`
        have no effect on these queues. Use 'flush' to discard all values in the
        session's queues.

        For example, if you call a write function to write three frames, then
        immediately call :class:`nixnet.session.Session.stop`, then call
        :class:`nixnet.session.Session.start` a few seconds later, the three frames
        transmit. If you call 'flush' between :class:`nixnet.session.Session.stop` and
        :class:`nixnet.session.Session.start`, no frames transmit.

        As another example, if you receive three frames, then call
        :class:`nixnet.session.Session.stop`, the three frames remains in the queue.
        If you call :class:`nixnet.session.Session.start` a few seconds later, then
        call a read function, you obtain the three frames received earlier,
        potentially followed by other frames received after calling
        :class:`nixnet.session.Session.start`. If you call 'flush' between
        :class:`nixnet.session.Session.stop` and :class:`nixnet.session.Session.start`,
        read function returns only frames received after the calling
        :class:`nixnet.session.Session.start`.

        Args:
            None

        Returns:
            None
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

        Returns:
            None
        """
        _funcs.nx_wait(self._handle, constants.Condition.TRANSMIT_COMPLETE, 0, timeout)

    def wait_for_intf_communicating(self, timeout=10):
        """Wait for the interface to begin communication on the network.

        If a start trigger is configured for the interface, this first waits for
        the trigger. Once the interface is started, this waits for the
        protocol's communication state to transition to a value that indicates
        communication with remote nodes.

        After this wait succeeds, calls to 'read_state' will return:
            :class:`nixnet.constants.ReadState.CAN_COMM`:
                :class:`nixnet.constants.ReadState.CAN_COMM.ERROR_ACTIVE`
            :class:`nixnet.constants.ReadState.CAN_COMM`:
                :class:`nixnet.constants.ReadState.CAN_COMM.ERROR_PASSIVE`
            :class:`nixnet.constants.ReadState.TIME_COMMUNICATING`: Valid time
                for communication (invalid time of 0 prior)

        Args:
            timeout: A float representing the maximum amount of time to wait in
                seconds.

        Returns:
            None
        """
        _funcs.nx_wait(self._handle, constants.Condition.INTF_COMMUNICATING, 0, timeout)

    def wait_for_intf_remote_wakeup(self, timeout=10):
        """Wait for interface remote wakeup.

        Wait for the interface to wakeup due to activity by a remote node on the
        network. This wait is used for CAN, when you set the 'can_tcvr_state'
        property to :class:`nixnet.constants.CanTcvrState.SLEEP`. Although the
        interface itself is ready to communicate, this places the transceiver
        into a sleep state. When a remote CAN node transmits a frame, the
        transceiver wakes up, and communication is restored. This wait detects
        that remote wakeup.

        This wait is used for LIN when you set 'lin_sleep' property to
        :class:`nixnet.constants.LinSleep.REMOTE_SLEEP` or
        :class:`nixnet.constants.LinSleep.LOCAL_SLEEP`. When asleep, if a remote
        LIN ECU transmits the wakeup pattern (break), the XNET LIN interface
        detects this transmission and wakes up. This wait detects that remote wakeup.

        Args:
            timeout: A float representing the maximum amount of time to wait in
                seconds.

        Returns:
            None
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

        Returns:
            None
        """
        _funcs.nx_connect_terminals(self._handle, source, destination)

    def disconnect_terminals(self, source, destination):
        """Disconnect terminals on the XNET interface.

        This function disconnects a specific pair of source/destination terminals
        previously connected with :class:`nixnet.session.Session.connect_terminals`.

        When the final session for a given interface is cleared, NI-XNET
        automatically disconnects all terminal connections for that interface.
        Therefore, 'disconnect_terminals' is not required for most applications.

        This function typically is used to change terminal connections
        dynamically while an application is running. To disconnect a terminal,
        you first must stop the interface using :class:`nixnet.session.Session.stop`
        with the Interface Only scope. Then you can call 'disconnect_terminals'
        and :class:`nixnet.session.Session.connect_terminals` to adjust terminal
        connections. Finally, you can call :class:`nixnet.session.Session.start` with
        the Interface Only scope to restart the interface.

        You can disconnect only a terminal that has been previously connected.
        Attempting to disconnect a nonconnected terminal results in an error.

        Args:
            source: A string representing the connection source name.
            destination: A string representing the connection destination name.

        Returns:
            None
        """
        _funcs.nx_disconnect_terminals(self._handle, source, destination)

    @property
    def intf(self):
        return self._intf

    @property
    def j1939(self):
        return self._j1939

    @property
    def application_protocol(self):
        return constants.AppProtocol(_props.get_session_application_protocol(self._handle))

    @property
    def auto_start(self):
        return _props.get_session_auto_start(self._handle)

    @auto_start.setter
    def auto_start(self, value):
        _props.set_session_auto_start(self._handle, value)

    @property
    def cluster_name(self):
        return _props.get_session_cluster_name(self._handle)

    @property
    def database_name(self):
        return _props.get_session_database_name(self._handle)

    @property
    def mode(self):
        return constants.CreateSessionMode(_props.get_session_mode(self._handle))

    @property
    def num_pend(self):
        return _props.get_session_num_pend(self._handle)

    @property
    def num_unused(self):
        return _props.get_session_num_unused(self._handle)

    @property
    def payld_len_max(self):
        return _props.get_session_payld_len_max(self._handle)

    @property
    def protocol(self):
        return constants.Protocol(_props.get_session_protocol(self._handle))

    @property
    def queue_size(self):
        return _props.get_session_queue_size(self._handle)

    @queue_size.setter
    def queue_size(self, value):
        _props.set_session_queue_size(self._handle, value)

    @property
    def resamp_rate(self):
        return _props.get_session_resamp_rate(self._handle)

    @resamp_rate.setter
    def resamp_rate(self, value):
        _props.set_session_resamp_rate(self._handle, value)
