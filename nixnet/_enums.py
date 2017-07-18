from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import enum

from nixnet import _cconsts


class Err(enum.Enum):
    # An internal error occurred in the NI-XNET driver. Please contact National
    # Instruments and provide the information from the file
    # %LOCALAPPDATA%\\National Instruments\\NI-XNET\\log\\niXntErr.log. On Windows XP,
    # the file can be found at %USERPROFILE%\\Local Settings\\Application
    # Data\\National Instruments\\NI-XNET\\log\\niXntErr.log. Please note that this
    # location may be hidden on your computer.
    INTERNAL_ERROR = _cconsts.NX_ERR_INTERNAL_ERROR
    # Board self test failed(code 2). Solution: try reinstalling the driver or
    # switching the slot(s) of the board(s). If the error persists,contact
    # National Instruments.
    SELF_TEST_ERROR1 = _cconsts.NX_ERR_SELF_TEST_ERROR1
    # Board self test failed(code 3). Solution: try reinstalling the driver or
    # switching the slot(s) of the board(s). If the error persists,contact
    # National Instruments.
    SELF_TEST_ERROR2 = _cconsts.NX_ERR_SELF_TEST_ERROR2
    # Board self test failed(code 4). Solution: try reinstalling the driver or
    # switching the slot(s) of the board(s). If the error persists,contact
    # National Instruments.
    SELF_TEST_ERROR3 = _cconsts.NX_ERR_SELF_TEST_ERROR3
    # Board self test failed(code 5). Solution: try reinstalling the driver or
    # switching the slot(s) of the board(s). If the error persists,contact
    # National Instruments.
    SELF_TEST_ERROR4 = _cconsts.NX_ERR_SELF_TEST_ERROR4
    # Board self test failed(code 6). Solution: try reinstalling the driver or
    # switching the slot(s) of the board(s). If the error persists,contact
    # National Instruments.
    SELF_TEST_ERROR5 = _cconsts.NX_ERR_SELF_TEST_ERROR5
    # Computer went to hibernation mode and the board lost power. Solution:
    # prevent the computer from going to hibernation mode in the control panel.
    POWER_SUSPENDED = _cconsts.NX_ERR_POWER_SUSPENDED
    # A write queue overflowed. Solution: wait until queue space becomes available
    # and retry.
    OUTPUT_QUEUE_OVERFLOW = _cconsts.NX_ERR_OUTPUT_QUEUE_OVERFLOW
    # The board's firmware did not answer a command. Solution: Stop your
    # application and execute a self test. Try deactivating/reactivating the
    # driver in the Device Manager. If the problem persists, contact National
    # Instruments.
    FIRMWARE_NO_RESPONSE = _cconsts.NX_ERR_FIRMWARE_NO_RESPONSE
    # The operation timed out. Solution: specify a timeout long enough to complete
    # the operation, or change the operation in a way that it can get completed in
    # less time (e.g. read less data).
    EVENT_TIMEOUT = _cconsts.NX_ERR_EVENT_TIMEOUT
    # A read queue overflowed. Solution: reduce your data rate or call Read more
    # frequently.
    INPUT_QUEUE_OVERFLOW = _cconsts.NX_ERR_INPUT_QUEUE_OVERFLOW
    # The Read buffer is too small to hold a single frame. Solution: provide a
    # buffer large enough.
    INPUT_QUEUE_READ_SIZE = _cconsts.NX_ERR_INPUT_QUEUE_READ_SIZE
    # You tried to open the same frame twice. This is not permitted. Solution:
    # open each frame only once.
    DUPLICATE_FRAME_OBJECT = _cconsts.NX_ERR_DUPLICATE_FRAME_OBJECT
    # You tried to open the same stream object twice. This is not permitted.
    # Solution: open each stream object only once.
    DUPLICATE_STREAM_OBJECT = _cconsts.NX_ERR_DUPLICATE_STREAM_OBJECT
    # Self test is not possible since the board is in use by an application.
    # Solution: stop all NI-XNET applications before executing a self test.
    SELF_TEST_NOT_POSSIBLE = _cconsts.NX_ERR_SELF_TEST_NOT_POSSIBLE
    # Allocation of memory failed. You do not have sufficient memory in the
    # LabVIEW target. Solution: add more RAM or try to use fewer resources in your
    # applications (arrays, XNET sessions, etc).
    MEMORY_FULL = _cconsts.NX_ERR_MEMORY_FULL
    # The maximum number of sessions was exceeded. Solution: use fewer sessions.
    MAX_SESSIONS = _cconsts.NX_ERR_MAX_SESSIONS
    # The maximum number of frames has been exceeded. Solution: Use fewer frames
    # in your sessions.
    MAX_FRAMES = _cconsts.NX_ERR_MAX_FRAMES
    # The maximum number of devices has been detected. Solution: use fewer
    # devices.
    MAX_DEVICES = _cconsts.NX_ERR_MAX_DEVICES
    # A driver support file is missing. Solution: try reinstalling the driver. If
    # the error persists, contact National Instruments.
    MISSING_FILE = _cconsts.NX_ERR_MISSING_FILE
    # This indicates that a NULL pointer or an empty string was passed to a
    # function. The user should verify that the parameters passed in make sense
    # for the given function.
    PARAMETER_NULL_OR_EMPTY = _cconsts.NX_ERR_PARAMETER_NULL_OR_EMPTY
    # The maximum number of schedules has been detected. Solution: Use fewer
    # schedules.
    MAX_SCHEDULES = _cconsts.NX_ERR_MAX_SCHEDULES
    # Board self test failed (code 17). Solution: Try reinstalling the driver or
    # switching the slot(s) of the board(s). If the error persists, contact
    # National Instruments.
    SELF_TEST_ERROR6 = _cconsts.NX_ERR_SELF_TEST_ERROR6
    # You cannot start an NI-XNET application while a self test is in progress.
    # Solution: Complete the self test before starting any NI-XNET applications.
    SELF_TEST_IN_PROGRESS = _cconsts.NX_ERR_SELF_TEST_IN_PROGRESS
    # An invalid reference has been passed to a NI-XNET session function.
    # Solution: Only pass reference retrieved from Create Session, or from an IO
    # name of a session in LabVIEW project.
    INVALID_SESSION_HANDLE = _cconsts.NX_ERR_INVALID_SESSION_HANDLE
    # An invalid reference has been passed to a NI-XNET system function. Solution:
    # Only pass a valid system reference.
    INVALID_SYSTEM_HANDLE = _cconsts.NX_ERR_INVALID_SYSTEM_HANDLE
    # A device reference was expected for a NI-XNET session function. Solution:
    # Only pass a device reference.
    DEVICE_HANDLE_EXPECTED = _cconsts.NX_ERR_DEVICE_HANDLE_EXPECTED
    # An interface reference was expected for a NI-XNET session function.
    # Solution: Only pass an interface reference.
    INTF_HANDLE_EXPECTED = _cconsts.NX_ERR_INTF_HANDLE_EXPECTED
    # You have configured a property that conflicts with the current mode of the
    # session. For example, you have created a CAN output session with a frame
    # configured with a Timing Type = Cyclic and a Transmit Time of 0.
    PROPERTY_MODE_CONFLICTING = _cconsts.NX_ERR_PROPERTY_MODE_CONFLICTING
    # XNET Create Timing Source VI is not supported on Windows. This VI is
    # supported on LabVIEW Real-Time targets only.
    TIMING_SOURCE_NOT_SUPPORTED = _cconsts.NX_ERR_TIMING_SOURCE_NOT_SUPPORTED
    # You tried to create more than one LabVIEW timing source for a single
    # interface. Only one timing source per interface is supported. The timing
    # source remains until the top-level VI is idle (no longer running). Solution:
    # Call the XNET Create Timing Source VI only once per interface. You can use
    # the timing source with multiple timed structures (e.g. timed loops).
    MULTIPLE_TIMING_SOURCE = _cconsts.NX_ERR_MULTIPLE_TIMING_SOURCE
    # You invoked two or more VIs simultaneously for the same session, and those
    # VIs do not support overlap. For example, you attempted to invoke two Read
    # VIs at the same time for the same session. Solution: Wire the error cluster
    # from one VI to another, to enforce sequential execution for the session.
    OVERLAPPING_IO = _cconsts.NX_ERR_OVERLAPPING_IO
    # You are trying to start an interface that is missing bus power for the
    # transceiver. Some physical layers on NI-XNET hardware are internally
    # powered, but others require external power for the port to operate. This
    # error occurs when starting an interface on hardware that requires external
    # power when no power is detected. Solution: Supply proper voltage to your
    # transceiver. Refer to the NI-XNET Hardware Overview in the NI-XNET Hardware
    # and Software Manual for more information.
    MISSING_BUS_POWER = _cconsts.NX_ERR_MISSING_BUS_POWER
    # The connection with a CompactDAQ chassis was lost, and the host software and
    # modules are out of sync. There is no direct recovery for this problem until
    # the chassis is reset. Solutions: Call DAQmx Reset Device as the first VI or
    # function in your application, prior to creating XNET sessions. Alternately,
    # you could reset the CompactDAQ chassis in Measurement and Automation
    # Explorer (MAX).
    CDAQ_CONNECTION_LOST = _cconsts.NX_ERR_CDAQ_CONNECTION_LOST
    # The transceiver value set is invalid (for this port, e.g. LS on a HS port)
    # or you are trying to perform an operation that requires a different
    # transceiver (e.g., trying to change the state of a disconnected
    # transceiver). Solution: set a valid value.
    INVALID_TRANSCEIVER = _cconsts.NX_ERR_INVALID_TRANSCEIVER
    # The baud rate value set is invalid. Solution: set a valid value.
    INVALID_BAUD_RATE = _cconsts.NX_ERR_INVALID_BAUD_RATE
    # No baud rate value has been set. Solution: set a valid value.
    BAUD_RATE_NOT_CONFIGURED = _cconsts.NX_ERR_BAUD_RATE_NOT_CONFIGURED
    # The bit timing values set are invalid. Solution: set valid values.
    INVALID_BIT_TIMINGS = _cconsts.NX_ERR_INVALID_BIT_TIMINGS
    # The baud rate set does not match the transceiver's allowed range. Solution:
    # change either the baud rate or the transceiver.
    BAUD_RATE_XCVR_MISMATCH = _cconsts.NX_ERR_BAUD_RATE_XCVR_MISMATCH
    # The configured terminal is not known for this interface. Solution: Make sure
    # that that you pass in a valid value to Connect Terminals or Disconnect
    # Terminals.
    UNKNOWN_TIMING_SOURCE = _cconsts.NX_ERR_UNKNOWN_TIMING_SOURCE
    # The configured terminal is inappropriate for the hardware. For example,
    # setting a source to FrontPanel0 on XNET hardware that doesn't have
    # front-panel trigger inputs, or selecting PXI_Clk10 for a non-PXI device.
    # Solution: Pick an appropriate terminal for the hardware.
    UNKNOWN_SYNCHRONIZATION_SOURCE = _cconsts.NX_ERR_UNKNOWN_SYNCHRONIZATION_SOURCE
    # The source that you connected to the Master Timebase destination is missing.
    # When the start trigger is received, the interface verifies that a signal is
    # present on the configured source. This check has determined that this signal
    # is missing. Solution: Verify that your cables are configured correctly and
    # that your timebase source is generating an appropriate waveform.
    MISSING_TIMEBASE_SOURCE = _cconsts.NX_ERR_MISSING_TIMEBASE_SOURCE
    # The source that you connected to the Master Timebase destination is not
    # generating an appropriate signal. When the start trigger is received, the
    # interface verifies that a signal of a known frequency is present on the
    # configured source. This check has determined that this source is generating
    # a signal, but that the signal is not one of the supported frequencies for
    # this hardware. Solution: Verify that your source is generating a signal at a
    # supported frequency.
    UNKNOWN_TIMEBASE_FREQUENCY = _cconsts.NX_ERR_UNKNOWN_TIMEBASE_FREQUENCY
    # You are trying to disconnect a synchronization terminal that is not
    # currently connected. Solution: Only disconnect synchronization terminals
    # that have previously been connected.
    UNCONNECTED_SYNCHRONIZATION_SOURCE = _cconsts.NX_ERR_UNCONNECTED_SYNCHRONIZATION_SOURCE
    # You are trying to connect a synchronization terminal that is already in use.
    # For example, you are trying to connect a trigger line to the Master Timebase
    # when a different trigger line is already connected to the Master Timebase.
    # Solution: Only connect to synchronization terminals that are not currently
    # in use.
    CONNECTED_SYNCHRONIZATION_TERMINAL = _cconsts.NX_ERR_CONNECTED_SYNCHRONIZATION_TERMINAL
    # You are trying to connect an XNET terminal as a source terminal, but the
    # desired XNET terminal is not valid as a source terminal. Solution: Only
    # connect valid source terminals to the source terminal in XNET Connect
    # Terminals.
    INVALID_SYNCHRONIZATION_SOURCE = _cconsts.NX_ERR_INVALID_SYNCHRONIZATION_SOURCE
    # You are trying to connect an XNET terminal as a destination terminal, but
    # the desired XNET terminal is not valid as a destination terminal. Solution:
    # Only connect valid destination terminals to the destination terminal in XNET
    # Connect Terminals.
    INVALID_SYNCHRONIZATION_DESTINATION = _cconsts.NX_ERR_INVALID_SYNCHRONIZATION_DESTINATION
    # You are trying to connect two XNET terminals that are incompatible.
    # Solution: Only connect a source and destination terminals that are
    # compatible with each other.
    INVALID_SYNCHRONIZATION_COMBINATION = _cconsts.NX_ERR_INVALID_SYNCHRONIZATION_COMBINATION
    # The source that you connected to the Master Timebase destination has
    # disappeared. When the start trigger is received, the interface verifies that
    # a signal is present on the configured source. This check has determined that
    # this signal was present, but while the interface was running, the signal
    # disappeared, so all timebase configuration has reverted to using the onboard
    # (unsynchronized) oscillator. Solution: Verify that your cables are
    # configured correctly and that your timebase source is generating an
    # appropriate waveform the entire time your application is running.
    TIMEBASE_DISAPPEARED = _cconsts.NX_ERR_TIMEBASE_DISAPPEARED
    # You called Read (State : FlexRay : Cycle Macrotick), and the FlexRay
    # Macrotick is not connected as the master timebase of the interface.
    # Solution: Call Connect Terminals to connect source of FlexRay Macrotick to
    # destination of Master Timebase.
    MACROTICK_DISCONNECTED = _cconsts.NX_ERR_MACROTICK_DISCONNECTED
    # The database specified could not be opened. Solution: Check that the alias
    # and/or the file exist and that it is a valid database.
    CANNOT_OPEN_DATABASE_FILE = _cconsts.NX_ERR_CANNOT_OPEN_DATABASE_FILE
    # The cluster was not found in the database. Solution: Make sure you only
    # initialize a cluster in a session that is defined in the database.
    CLUSTER_NOT_FOUND = _cconsts.NX_ERR_CLUSTER_NOT_FOUND
    # The frame was not found in the database. Solution: Make sure you only
    # initialize frames in a session that are defined in the database.
    FRAME_NOT_FOUND = _cconsts.NX_ERR_FRAME_NOT_FOUND
    # The signal was not found in the database. Solution: Make sure you only
    # initialize signals in a session that are defined in the database.
    SIGNAL_NOT_FOUND = _cconsts.NX_ERR_SIGNAL_NOT_FOUND
    # A necessary property for a cluster was not found in the database. Solution:
    # Make sure you only initialize a cluster in a session that is completely
    # defined in the database.
    UNCONFIGURED_CLUSTER = _cconsts.NX_ERR_UNCONFIGURED_CLUSTER
    # A necessary property for a frame was not found in the database. Solution:
    # Make sure you only initialize frames in a session that are completely
    # defined in the database.
    UNCONFIGURED_FRAME = _cconsts.NX_ERR_UNCONFIGURED_FRAME
    # A necessary property for a signal was not found in the database. Solution:
    # Make sure you only initialize signals in a session that are completely
    # defined in the database.
    UNCONFIGURED_SIGNAL = _cconsts.NX_ERR_UNCONFIGURED_SIGNAL
    # Multiple clusters have been specified in one session, either directly
    # (Stream I/O), or through the signals or frames specified. Solution: Make
    # sure that in one session, you open only one cluster, including frames or
    # signals that belong to the same cluster.
    MULTIPLE_CLUSTERS = _cconsts.NX_ERR_MULTIPLE_CLUSTERS
    # You specified a database of ':subordinate:' for a session mode other than
    # mode of Frame Input Stream. Solution: either open a Frame Input Stream
    # session, or use a real or in-memory database.
    SUBORDINATE_NOT_ALLOWED = _cconsts.NX_ERR_SUBORDINATE_NOT_ALLOWED
    # The interface name given does not specify a valid and existing interface.
    # Solution: Use a valid and existing interface. These can be obtained using
    # MAX, XNET system properties, or the LabVIEW XNET Interface IO name. If you
    # are using CompactRIO, refer to the topic "Getting Started with CompactRIO"
    # in the NI-XNET Hardware and Software Help.
    INVALID_INTERFACE = _cconsts.NX_ERR_INVALID_INTERFACE
    # The operation is invalid for this interface (e.g. you tried to open a set of
    # FlexRay frames on a CAN interface, or tried to request a CAN property from a
    # FlexRay interface). Solution: run this operation on a suitable interface.
    INVALID_PROTOCOL = _cconsts.NX_ERR_INVALID_PROTOCOL
    # You tried to set the AutoStart property to FALSE for an Input session. This
    # is not allowed. Solution: don't set the AutoStart property (TRUE is
    # default).
    INPUT_SESSION_MUST_AUTO_START = _cconsts.NX_ERR_INPUT_SESSION_MUST_AUTO_START
    # The property ID you specified is not valid (or not valid for the current
    # session mode or form factor).
    INVALID_PROPERTY_ID = _cconsts.NX_ERR_INVALID_PROPERTY_ID
    # The contents of the property is bigger than the size specified. Use the
    # nxGetPropertySize function to determine the size of the buffer needed.
    INVALID_PROPERTY_SIZE = _cconsts.NX_ERR_INVALID_PROPERTY_SIZE
    # The function you called is not defined for the session mode (e.g. you called
    # a frame I/O function on a signal I/O session).
    INCORRECT_MODE = _cconsts.NX_ERR_INCORRECT_MODE
    # The data that you passed to the XNET Write is too small to hold all the data
    # specified for the session. Solution: determine the number of elements
    # (frames or signals) that you configured for the session, and pass that
    # number of elements to XNET Write.
    BUFFER_TOO_SMALL = _cconsts.NX_ERR_BUFFER_TOO_SMALL
    # For Signal Output sessions, the multiplexer signals used in the session must
    # be specified explicitly in the signal list.
    MUST_SPECIFY_MULTIPLEXERS = _cconsts.NX_ERR_MUST_SPECIFY_MULTIPLEXERS
    # You used an XNET Session IO name, and that session was not found in your
    # LabVIEW project. Solution: Within LabVIEW project, right-click the target
    # (RT or My Computer), and select New > NI-XNET Session. Add the VI that uses
    # the session under the target. If you are using the session with a built
    # application (.EXE), ensure that you copy the built configuration file
    # nixnetSession.txt such that it resides in the same folder as the executable.
    SESSION_NOT_FOUND = _cconsts.NX_ERR_SESSION_NOT_FOUND
    # You used the same XNET session name in multiple top-level VIs, which is not
    # supported. Solution: Use each session in only one top-level VI (application)
    # at a time.
    MULTIPLE_USE_OF_SESSION = _cconsts.NX_ERR_MULTIPLE_USE_OF_SESSION
    # To execute this function properly, the session's list must contain only one
    # frame. Solution: break your session up into multiple, each of which contains
    # only one frame.
    ONLY_ONE_FRAME = _cconsts.NX_ERR_ONLY_ONE_FRAME
    # You used the same alias for different database files which is not allowed.
    # Solution: Use each alias only for a single database file.
    DUPLICATE_ALIAS = _cconsts.NX_ERR_DUPLICATE_ALIAS
    # You try to deploy a database file while another deployment is in progress.
    # Solution: wait until the other deployment has finished and try again.
    DEPLOYMENT_IN_PROGRESS = _cconsts.NX_ERR_DEPLOYMENT_IN_PROGRESS
    # A signal or frame session has been opened, but it doesn't contain signals or
    # frames. Solution: specify at least one signal or frame.
    NO_FRAMES_OR_SIGNALS = _cconsts.NX_ERR_NO_FRAMES_OR_SIGNALS
    # An invalid value has been specified for the 'mode' parameter. Solution:
    # specify a valid value.
    INVALID_MODE = _cconsts.NX_ERR_INVALID_MODE
    # A session was created by references, but no database references have been
    # specified. Solution: specify at least one appropriate database reference
    # (i.e. signal or frame or cluster ref depending on the session mode).
    NEED_REFERENCE = _cconsts.NX_ERR_NEED_REFERENCE
    # The interface has already been opened with different cluster settings than
    # the ones specified for this session. Solution: make sure that the cluster
    # settings agree for the interface, or use a different interface.
    DIFFERENT_CLUSTER_OPEN = _cconsts.NX_ERR_DIFFERENT_CLUSTER_OPEN
    # The cycle repetition of a frame in the database for the FlexRay protocol is
    # invalid. Solution: Make sure that the cycle repetition is a power of 2
    # between 1 and 64.
    FLEX_RAY_INVALID_CYCLE_REP = _cconsts.NX_ERR_FLEX_RAY_INVALID_CYCLE_REP
    # You called XNET Clear for the session, then tried to perform another
    # operation. Solution: Defer clear (session close) until you are done using
    # it. This error can also occur if you branch a wire after creating the
    # session. Solution: Do not branch a session to multiple flows in the diagram.
    SESSION_CLEARED = _cconsts.NX_ERR_SESSION_CLEARED
    # You called Create Session VI with a list of items that does not match the
    # mode. This includes using: 1) signal items for a Frame I/O mode 2) frame
    # items for a Signal I/O mode 3) cluster item for a mode other than Frame
    # Input Stream or Frame Output Stream
    WRONG_MODE_FOR_CREATE_SELECTION = _cconsts.NX_ERR_WRONG_MODE_FOR_CREATE_SELECTION
    # You tried to create a new session while the interface is already running.
    # Solution: Create all sessions before starting any of them.
    INTERFACE_RUNNING = _cconsts.NX_ERR_INTERFACE_RUNNING
    # You wrote a frame whose payload length is larger than the maximum payload
    # allowed by the database (e.g. wrote 10 bytes for CAN frame, max 8 bytes).
    # Solution: Never write more payload bytes than the Payload Length Maximum
    # property of the session.
    FRAME_WRITE_TOO_LARGE = _cconsts.NX_ERR_FRAME_WRITE_TOO_LARGE
    # You called a Read function with a nonzero timeout, and you used a negative
    # numberToRead. Negative value for numberToRead requests all available data
    # from the Read, which is ambiguous when used with a timeout. Solutions: 1)
    # Pass timeout of and numberToRead of -1, to request all available data. 2)
    # Pass timeout > 0, and numberToRead > 0, to wait for a specific number of
    # data elements.
    TIMEOUT_WITHOUT_NUM_TO_READ = _cconsts.NX_ERR_TIMEOUT_WITHOUT_NUM_TO_READ
    # Timestamps are not (yet) supported for Write Signal XY. Solution: Do not
    # provide a timestamp array for Write Signal XY.
    TIMESTAMPS_NOT_SUPPORTED = _cconsts.NX_ERR_TIMESTAMPS_NOT_SUPPORTED
    # The condition parameter passed to Wait is not known. Solution: Pass a valid
    # parameter.
    UNKNOWN_CONDITION = _cconsts.NX_ERR_UNKNOWN_CONDITION
    # You attempted an I/O operation, but the session is not yet started (and the
    # AutoStart property is set to FALSE). Solution: call Start before you use
    # this IO operation.
    SESSION_NOT_STARTED = _cconsts.NX_ERR_SESSION_NOT_STARTED
    # The maximum number of Wait operations has been exceeded. Solution: If you
    # are waiting for multiple events on the interface, use fewer Wait operations
    # on this interface (even for multiple sessions). If you are waiting for
    # multiple events for a frame (e.g. transmit complete), use only one Wait at a
    # time for that frame.
    MAX_WAITS_EXCEEDED = _cconsts.NX_ERR_MAX_WAITS_EXCEEDED
    # You used an invalid name for an XNET Device. Solution: Get valid XNET Device
    # names from the XNET System properties (only).
    INVALID_DEVICE = _cconsts.NX_ERR_INVALID_DEVICE
    # A terminal name passed to ConnectTerminals or DisconnectTerminals is
    # unknown. Solution: only pass valid names.
    INVALID_TERMINAL_NAME = _cconsts.NX_ERR_INVALID_TERMINAL_NAME
    # You tried to blink the port LEDs but these are currently busy. Solution:
    # stop all applications running on that port; do not access it from MAX or LV
    # Project.
    PORT_LE_DS_BUSY = _cconsts.NX_ERR_PORT_LE_DS_BUSY
    # You tried to set a FlexRay keyslot ID that is not listed as valid in the
    # database. Solution: only pass slot IDs of frames that have the startup or
    # sync property set in the database.
    INVALID_KEYSLOT = _cconsts.NX_ERR_INVALID_KEYSLOT
    # You tried to set a queue size that is bigger than the maximum allowed.
    # Solution: Specify an in-range queue size.
    MAX_QUEUE_SIZE_EXCEEDED = _cconsts.NX_ERR_MAX_QUEUE_SIZE_EXCEEDED
    # You wrote a frame whose payload length is different than the payload length
    # configured by the database. Solution: Never write a different payload length
    # for a frame that is different than the configured payload length.
    FRAME_SIZE_MISMATCH = _cconsts.NX_ERR_FRAME_SIZE_MISMATCH
    # The index to indicate an session list element is too large. Solution:
    # Specify an index in the range ... NumInList-1.
    INDEX_TOO_BIG = _cconsts.NX_ERR_INDEX_TOO_BIG
    # You have tried to create a session that is invalid for the mode of the
    # driver/firmware. For example, you are using the Replay Exclusive mode for
    # Stream Output and you have an output session open.
    SESSION_MODE_INCOMPATIBILITY = _cconsts.NX_ERR_SESSION_MODE_INCOMPATIBILITY
    # You have tried to create a session using a frame that is incompatible with
    # the selected session type. For example, you are using a LIN diagnostic frame
    # with a single point output session.
    SESSION_TYPE_FRAME_INCOMPATIBILITY = _cconsts.NX_ERR_SESSION_TYPE_FRAME_INCOMPATIBILITY
    # The trigger signal for a frame is allowed only in Single Point Signal
    # sessions (Input or Output). For Output Single Point Signal sessions, only
    # one trigger signal is allowed per frame. Solution: Do not use the trigger
    # signal, or change to a single point I/O session.
    TRIGGER_SIGNAL_NOT_ALLOWED = _cconsts.NX_ERR_TRIGGER_SIGNAL_NOT_ALLOWED
    # To execute this function properly, the session's list must contain only one
    # cluster. Solution: Use only one cluster in the session.
    ONLY_ONE_CLUSTER = _cconsts.NX_ERR_ONLY_ONE_CLUSTER
    # You attempted to convert a CAN or LIN frame with a payload length greater
    # than 8. For example, you may be converting a frame that uses a higher layer
    # transport protocol, such as SAE-J1939. NI-XNET currently supports conversion
    # of CAN/LIN frames only (layer 2). Solutions: 1) Implement higher layer
    # protocols (including signal conversion) within your code. 2) Contact
    # National Instruments to request this feature in a future version.
    CONVERT_INVALID_PAYLOAD = _cconsts.NX_ERR_CONVERT_INVALID_PAYLOAD
    # Allocation of memory failed for the data returned from LabVIEW XNET Read.
    # Solutions: 1) Wire a smaller "number to read" to XNET Read (default -1 uses
    # queue size). 2) For Signal Input Waveform, use a smaller resample rate. 3)
    # Set smaller value for session's queue size property (default is large to
    # avoid loss of data).
    MEMORY_FULL_READ_DATA = _cconsts.NX_ERR_MEMORY_FULL_READ_DATA
    # Allocation of memory failed in the firmware. Solutions: 1) Create less
    # firmware objects 2) Set smaller value for output session's queue size
    # property (default is large to avoid loss of data).
    MEMORY_FULL_FIRMWARE = _cconsts.NX_ERR_MEMORY_FULL_FIRMWARE
    # The NI-XNET driver no longer can communicate with the device. Solution: Make
    # sure the device has not been removed from the computer.
    COMMUNICATION_LOST = _cconsts.NX_ERR_COMMUNICATION_LOST
    # A LIN schedule has an invalid priority. Solution: Use a valid priority (0 =
    # NULL schedule, 1..254 = Run once schedule, 255 = Continuous schedule).
    INVALID_PRIORITY = _cconsts.NX_ERR_INVALID_PRIORITY
    # (Dis)ConnectTerminals is not allowed for XNET C Series modules. Solution: To
    # connect the module start trigger, use the Session property Interface Source
    # Terminal Start Trigger.
    SYNCHRONIZATION_NOT_ALLOWED = _cconsts.NX_ERR_SYNCHRONIZATION_NOT_ALLOWED
    # You requested a time (like Start or Communication Time) before the event has
    # happened. Solution: Request the time only after it occurred.
    TIME_NOT_REACHED = _cconsts.NX_ERR_TIME_NOT_REACHED
    # An internal input queue overflowed. Solution: Attempt to pull data from the
    # hardware faster. If you are connected by an external bus (for example, USB
    # or Ethernet), you can try to use a faster connection.
    INTERNAL_INPUT_QUEUE_OVERFLOW = _cconsts.NX_ERR_INTERNAL_INPUT_QUEUE_OVERFLOW
    # A bad firmware image file can not be loaded to the hardware. Solution:
    # Uninstall and reinstall the NI-XNET software as the default firmware file
    # may be corrupt. If you are using a custom firmware file, try rebuilding it.
    BAD_IMAGE_FILE = _cconsts.NX_ERR_BAD_IMAGE_FILE
    # The encoding of embedded network data (CAN, FlexRay, LIN, etc.) within the
    # TDMS file is invalid. Solutions: 1) In the application that wrote (created)
    # the logfile, and the application in which you are reading it, confirm that
    # both use the same major version for frame data encoding
    # (NI_network_frame_version property of the TDMS channel). 2) Ensure that your
    # file was not corrupted.
    INVALID_LOGFILE = _cconsts.NX_ERR_INVALID_LOGFILE
    # The NI-XNET hardware no longer can communicate with the transceiver cable.
    # This may be due to the cable being removed, a power loss event, an over
    # voltage condition on the power input, or a general communication error.
    # Solution: Make sure the dongle is properly latched and, for some hardware,
    # external power is properly applied. To detect other errors, stop your
    # application and execute a self test.
    DONGLE_COMMUNICATION_LOST = _cconsts.NX_ERR_DONGLE_COMMUNICATION_LOST
    # A property value was out of range or incorrect. Solution: specify a correct
    # value.
    INVALID_PROPERTY_VALUE = _cconsts.NX_ERR_INVALID_PROPERTY_VALUE
    # Integration of the interface into the FlexRay cluster failed, so
    # communication did not start for the interface. Solution: check the cluster
    # and/or interface parameters and verify that there are startup frames
    # defined.
    FLEX_RAY_INTEGRATION_FAILED = _cconsts.NX_ERR_FLEX_RAY_INTEGRATION_FAILED
    # The PDU was not found in the database. Solution: Make sure you initialize
    # only PDUs in a session that are defined in the database.
    PDU_NOT_FOUND = _cconsts.NX_ERR_PDU_NOT_FOUND
    # A necessary property for a PDU was not found in the database. Solution: Make
    # sure you initialize only PDUs in a session that are completely defined in
    # the database.
    UNCONFIGURED_PDU = _cconsts.NX_ERR_UNCONFIGURED_PDU
    # You tried to open the same PDU twice. This is not permitted. Solution: Open
    # each PDU only once.
    DUPLICATE_PDU_OBJECT = _cconsts.NX_ERR_DUPLICATE_PDU_OBJECT
    # You can access this database object only by PDU, not by frame. Solution: For
    # CAN and LIN, this is not supported by the current version of NI-XNET; for
    # FlexRay, make sure the database is set to use PDUs.
    NEED_PDU = _cconsts.NX_ERR_NEED_PDU
    # Remote communication with the LabVIEW RT target failed. Solution: check if
    # NI-XNET has been installed on the RT target and check if the NI-XNET RPC
    # server has been started.
    RPC_COMMUNICATION = _cconsts.NX_ERR_RPC_COMMUNICATION
    # File transfer communication with the LabVIEW Real-Time (RT) target failed.
    # Solution: check if the RT target has been powered on, the RT target has been
    # connected to the network, and if the IP address settings are correct.
    FILE_TRANSFER_COMMUNICATION = _cconsts.NX_ERR_FILE_TRANSFER_COMMUNICATION
    # File transfer communication with the LabVIEW Real-Time (RT) target failed.
    # Solution: check if the RT target has been powered on, the RT target has been
    # connected to the network, and if the IP address settings are correct.
    FTP_COMMUNICATION = _cconsts.NX_ERR_FTP_COMMUNICATION
    # File transfer to the LabVIEW Real-Time (RT) target failed, because the
    # required files could not be accessed. Solution: You may have executed a VI
    # that opened the database, but did not close. If that is the case, you should
    # change the VI to call Database Close, then reboot the RT controller to
    # continue.
    FILE_TRANSFER_ACCESS = _cconsts.NX_ERR_FILE_TRANSFER_ACCESS
    # File transfer to the LabVIEW Real-Time (RT) target failed, because the
    # required files could not be accessed. Solution: You may have executed a VI
    # that opened the database, but did not close. If that is the case, you should
    # change the VI to call Database Close, then reboot the RT controller to
    # continue.
    FTP_FILE_ACCESS = _cconsts.NX_ERR_FTP_FILE_ACCESS
    # The database file you want to use is already assigned to another alias.
    # Solution: Each database file can only be assigned to a single alias. Use the
    # alias that is already assigned to the database instead.
    DATABASE_ALREADY_IN_USE = _cconsts.NX_ERR_DATABASE_ALREADY_IN_USE
    # An internal file used by NI-XNET could not be accessed. Solution: Make sure
    # that the internal NI-XNET files are not write protected and that the
    # directories for these files exist.
    INTERNAL_FILE_ACCESS = _cconsts.NX_ERR_INTERNAL_FILE_ACCESS
    # The file cannot be deployed because another file deployment is already
    # active. Solution: wait until the other file deployment has finished and try
    # again.
    FILE_TRANSFER_ACTIVE = _cconsts.NX_ERR_FILE_TRANSFER_ACTIVE
    # The nixnet.dll or one of its components could not be loaded. Solution: try
    # reinstalling NI-XNET. If the error persists,contact National Instruments.
    DLL_LOAD = _cconsts.NX_ERR_DLL_LOAD
    # You attempted to perform an action on a session or interface that is
    # started, and the action that requires the session/interface to be stopped.
    # Solution: Stop the object before performing this action.
    OBJECT_STARTED = _cconsts.NX_ERR_OBJECT_STARTED
    # You have passed a default payload to the firmware where the number of bytes
    # in the payload is larger than the number of bytes that this frame can
    # transmit. Solution: Decrease the number of bytes in your default payload.
    DEFAULT_PAYLOAD_NUM_BYTES = _cconsts.NX_ERR_DEFAULT_PAYLOAD_NUM_BYTES
    # You attempted to set a CAN arbitration ID with an invalid value. For
    # example, a CAN standard arbitration ID supports only 11 bits. If you attempt
    # to set a standard arbitration ID that uses more than 11 bits, this error is
    # returned. Solution: Use a valid arbitration ID.
    INVALID_ARBITRATION_ID = _cconsts.NX_ERR_INVALID_ARBITRATION_ID
    # You attempted to set a LIN ID with an invalid value. For example, a LIN ID
    # supports only 6 bits. If you attempt to set an ID that uses more than 6
    # bits, this error is returned. Solution: Use a valid LIN ID.
    INVALID_LIN_ID = _cconsts.NX_ERR_INVALID_LIN_ID
    # Too many open files. NI-XNET allows up to 7 database files to be opened
    # simultaneously. Solution: Open fewer files.
    TOO_MANY_OPEN_FILES = _cconsts.NX_ERR_TOO_MANY_OPEN_FILES
    # Bad reference has been passed to a database function, e.g. a session
    # reference, or frame reference to retrieve properties from a signal.
    DATABASE_BAD_REFERENCE = _cconsts.NX_ERR_DATABASE_BAD_REFERENCE
    # Creating a database file failed. Solution: Verify access rights to the
    # destination directory or check if overwritten file has read only permission.
    CREATE_DATABASE_FILE = _cconsts.NX_ERR_CREATE_DATABASE_FILE
    # A cluster with the same name already exists in the database. Solution: Use
    # another name for this cluster.
    DUPLICATE_CLUSTER_NAME = _cconsts.NX_ERR_DUPLICATE_CLUSTER_NAME
    # A frame with the same name already exists in the cluster. Solution: Use
    # another name for this frame.
    DUPLICATE_FRAME_NAME = _cconsts.NX_ERR_DUPLICATE_FRAME_NAME
    # A signal with the same name already exists in the frame. Solution: Use
    # another name for this signal.
    DUPLICATE_SIGNAL_NAME = _cconsts.NX_ERR_DUPLICATE_SIGNAL_NAME
    # An ECU with the same name already exists in the cluster. Solution: Use
    # another name for this ECU.
    DUPLICATE_ECU_NAME = _cconsts.NX_ERR_DUPLICATE_ECU_NAME
    # A subframe with the same name already exists in the frame. Solution: Use
    # another name for this subframe.
    DUPLICATE_SUBFRAME_NAME = _cconsts.NX_ERR_DUPLICATE_SUBFRAME_NAME
    # The operation is improper for the protocol in use, e.g. you cannot assign
    # FlexRay channels to a CAN frame.
    IMPROPER_PROTOCOL = _cconsts.NX_ERR_IMPROPER_PROTOCOL
    # Wrong parent relationship for a child that you are creating with XNET
    # Database Create.
    OBJECT_RELATION = _cconsts.NX_ERR_OBJECT_RELATION
    # The retrieved required property is not defined on the specified object.
    # Solution: Make sure that your database file has this property defined or
    # that you set it in the objects created in memory.
    UNCONFIGURED_REQUIRED_PROPERTY = _cconsts.NX_ERR_UNCONFIGURED_REQUIRED_PROPERTY
    # The feature is not supported under LabVIEW RT, e.g.Save Database
    NOT_SUPPORTED_ON_RT = _cconsts.NX_ERR_NOT_SUPPORTED_ON_RT
    # The object name contains unsupported characters. The name must contain just
    # alphanumeric characters and the underscore, but cannot begin with a digit.
    # The maximum size is 128.
    NAME_SYNTAX = _cconsts.NX_ERR_NAME_SYNTAX
    # Unsupported database format. For reading a database, the extension must be
    # .xml, .dbc, .ncd, or .ldf. For saving, the extension must be .xml or .ldf
    FILE_EXTENSION = _cconsts.NX_ERR_FILE_EXTENSION
    # Database object not found, e.g. an object with given name doesn't exist.
    DATABASE_OBJECT_NOT_FOUND = _cconsts.NX_ERR_DATABASE_OBJECT_NOT_FOUND
    # Database cache file cannot be removed or replaced on the disc, e.g. it is
    # write-protected.
    REMOVE_DATABASE_CACHE_FILE = _cconsts.NX_ERR_REMOVE_DATABASE_CACHE_FILE
    # You are trying to write a read-only property, e.g. the mux value on a signal
    # is a read only property (can be changed on the subframe).
    READ_ONLY_PROPERTY = _cconsts.NX_ERR_READ_ONLY_PROPERTY
    # You are trying to change a signal to be a mux signal, but a mux is already
    # defined in this frame
    FRAME_MUX_EXISTS = _cconsts.NX_ERR_FRAME_MUX_EXISTS
    # You are trying to define FlexRay in-cycle-repetition slots before defining
    # the first slot. Define the first slot (frame ID) before defining
    # in-cycle-repetition slots.
    UNDEFINED_FIRST_SLOT = _cconsts.NX_ERR_UNDEFINED_FIRST_SLOT
    # You are trying to define FlexRay in-cycle-repetition channels before
    # defining the first channels. Define the Channel Assignment on a frame before
    # defining in-cycle-repetition channels.
    UNDEFINED_FIRST_CHANNELS = _cconsts.NX_ERR_UNDEFINED_FIRST_CHANNELS
    # You must define the protocol before setting this property, e.g. the frame ID
    # has a different meaning in a CAN or FlexRay cluster.
    UNDEFINED_PROTOCOL = _cconsts.NX_ERR_UNDEFINED_PROTOCOL
    # The database information on the real-time system has been created with an
    # older NI-XNET version. This version is no longer supported. To correct this
    # error, re-deploy your database to the real-time system.
    OLD_DATABASE_CACHE_FILE = _cconsts.NX_ERR_OLD_DATABASE_CACHE_FILE
    # Frame ConfigStatus: A signal within the frame exceeds the frame boundaries
    # (Payload Length).
    DB_CONFIG_SIG_OUT_OF_FRAME = _cconsts.NX_ERR_DB_CONFIG_SIG_OUT_OF_FRAME
    # Frame ConfigStatus: A signal within the frame overlaps another signal.
    DB_CONFIG_SIG_OVERLAPPED = _cconsts.NX_ERR_DB_CONFIG_SIG_OVERLAPPED
    # Frame ConfigStatus: A integer signal within the frame is defined with more
    # than 52 bits. Not supported.
    DB_CONFIG_SIG52_BIT_INTEGER = _cconsts.NX_ERR_DB_CONFIG_SIG52_BIT_INTEGER
    # Frame ConfigStatus: Frame is defined with wrong number of bytes Allowed
    # values: - CAN: 0-8, - Flexray: 0-254 and even number.
    DB_CONFIG_FRAME_NUM_BYTES = _cconsts.NX_ERR_DB_CONFIG_FRAME_NUM_BYTES
    # You are trying to add transmitted FlexRay frames to an ECU, with at least
    # two of them having Startup or Sync property on. Only one Sync or Startup
    # frame is allowed to be sent by an ECU.
    MULT_SYNC_STARTUP = _cconsts.NX_ERR_MULT_SYNC_STARTUP
    # You are trying to add TX/RX frames to an ECU which are defined in a
    # different cluster than the ECU.
    INVALID_CLUSTER = _cconsts.NX_ERR_INVALID_CLUSTER
    # Database name parameter is incorrect. Solution: Use a valid name for the
    # database, e.g. ":memory:" for in-memory database.
    DATABASE_NAME = _cconsts.NX_ERR_DATABASE_NAME
    # Database object is locked because it is used in a session. Solution:
    # Configure the database before using it in a session.
    DATABASE_OBJECT_LOCKED = _cconsts.NX_ERR_DATABASE_OBJECT_LOCKED
    # Alias name passed to a function is not defined. Solution: Define the alias
    # before calling the function.
    ALIAS_NOT_FOUND = _cconsts.NX_ERR_ALIAS_NOT_FOUND
    # Database file cannot be saved because frames are assigned to FlexRay
    # channels not defined in the cluster. Solution: Verify that all frames in the
    # FlexRay cluster are assigned to an existing cluster channel.
    CLUSTER_FRAME_CHANNEL_RELATION = _cconsts.NX_ERR_CLUSTER_FRAME_CHANNEL_RELATION
    # Frame ConfigStatus: This FlexRay frame transmitted in a dynamic segment uses
    # both channels A and B. This is not allowed. Solution: Use either channel A
    # or B.
    DYN_FLEX_RAY_FRAME_CHAN_AAND_B = _cconsts.NX_ERR_DYN_FLEX_RAY_FRAME_CHAN_AAND_B
    # Database is locked because it is being modified by an another instance of
    # the same application. Solution: Close the database in the other application
    # instance.
    DATABASE_LOCKED_IN_USE = _cconsts.NX_ERR_DATABASE_LOCKED_IN_USE
    # A frame name is ambiguous, e.g. a frame with the same name exists in another
    # cluster. Solution: Specify the cluster name for the frame using the required
    # syntax.
    AMBIGUOUS_FRAME_NAME = _cconsts.NX_ERR_AMBIGUOUS_FRAME_NAME
    # A signal name is ambiguous, e.g. a signal with the same name exists in
    # another frame. Solution: Use [frame].[signal] syntax for the signal.
    AMBIGUOUS_SIGNAL_NAME = _cconsts.NX_ERR_AMBIGUOUS_SIGNAL_NAME
    # An ECU name is ambiguous, e.g. an ECU with the same name exists in another
    # cluster. Solution: Specify the cluster name for the ECU using the required
    # syntax.
    AMBIGUOUS_ECU_NAME = _cconsts.NX_ERR_AMBIGUOUS_ECU_NAME
    # A subframe name is ambiguous, e.g. a subframe with the same name exists in
    # another cluster. Solution: Specify the cluster name for the subframe using
    # the required syntax.
    AMBIGUOUS_SUBFRAME_NAME = _cconsts.NX_ERR_AMBIGUOUS_SUBFRAME_NAME
    # A LIN schedule name is ambiguous, e.g. a schedule with the same name exists
    # in another cluster. Solution: Specify the cluster name for the schedule
    # using the required syntax.
    AMBIGUOUS_SCHEDULE_NAME = _cconsts.NX_ERR_AMBIGUOUS_SCHEDULE_NAME
    # A LIN schedule with the same name already exists in the database. Solution:
    # Use another name for this schedule.
    DUPLICATE_SCHEDULE_NAME = _cconsts.NX_ERR_DUPLICATE_SCHEDULE_NAME
    # A LIN diagnostic schedule change requires the diagnostic schedule to be
    # defined in the database. Solution: Define the diagnostic schedule in the
    # database.
    DIAGNOSTIC_SCHEDULE_NOT_DEFINED = _cconsts.NX_ERR_DIAGNOSTIC_SCHEDULE_NOT_DEFINED
    # Multiplexers (mode-dependent signals) are not supported when the given
    # protocol is used. Solution: Contact National Instruments to see whether
    # there is a newer NI-XNET version that supports multiplexers for the given
    # protocol.
    PROTOCOL_MUX_NOT_SUPPORTED = _cconsts.NX_ERR_PROTOCOL_MUX_NOT_SUPPORTED
    # Saving a FIBEX file containing a LIN cluster is not supported in this
    # NI-XNET version. Solution: Contact National Instruments to see whether there
    # is a newer NI-XNET version that supports saving a FIBEX file that contains a
    # LIN cluster.
    SAVE_LI_NNOT_SUPPORTED = _cconsts.NX_ERR_SAVE_LI_NNOT_SUPPORTED
    # This property requires an ECU configured as LIN master to be present in this
    # cluster. Solution: Create a LIN master ECU in this cluster.
    LI_NMASTER_NOT_DEFINED = _cconsts.NX_ERR_LI_NMASTER_NOT_DEFINED
    # You cannot mix open of NI-XNET database objects as both manual and
    # automatic. You open manually by calling the Database Open VI. You open
    # automatically when you 1) wire the IO name directly to a property node or
    # VI, 2) branch a wire to multiple data flows on the diagram, 3) use the IO
    # name with a VI or property node after closing it with the Database Close VI.
    # Solution: Change your diagram to use the manual technique in all locations
    # (always call Open and Close VIs), or to use the automatic technique in all
    # locations (never call Open or Close VIs).
    MIX_AUTO_MANUAL_OPEN = _cconsts.NX_ERR_MIX_AUTO_MANUAL_OPEN
    # Due to problems in LabVIEW versions 8.5 through 8.6.1, automatic open of
    # NI-XNET database objects is not supported. You open automatically when you
    # 1) wire the IO name directly to a property node or VI, 2) branch a wire to
    # multiple data flows on the diagram, 3) use the IO name with a VI or property
    # node after closing it with the Database Close VI. Solution: Change your
    # diagram to call the Database Open VI prior to any use (VI or property node)
    # in a data flow (including a new wire branch). Change your diagram to call
    # the Database Close VI when you are finished using the database in your
    # application.
    AUTO_OPEN_NOT_SUPPORTED = _cconsts.NX_ERR_AUTO_OPEN_NOT_SUPPORTED
    # You called a Write function with the number of array elements (frames or
    # signals) different than the number of elements configured in the session
    # (such as the "list" parameter of the Create Session function). Solution:
    # Write the same number of elements as configured in the session.
    WRONG_NUM_SIGNALS_WRITTEN = _cconsts.NX_ERR_WRONG_NUM_SIGNALS_WRITTEN
    # You used XNET session from multiple LabVIEW projects (or multiple
    # executables), which NI-XNET does not support. Solution: Run XNET sessions in
    # only one LabVIEW project at a time.
    MULTIPLE_LV_PROJECT = _cconsts.NX_ERR_MULTIPLE_LV_PROJECT
    # When an XNET session is used at runtime, all sessions in the same scope are
    # created on the interface. The same scope is defined as all sessions within
    # the same LabVIEW project which use the same cluster and interface (same
    # physical cable configuration). If you attempt to use a session in the same
    # scope after running the VI, this error occurs. The most likely cause is that
    # you added a new session, and tried to use that new session in a running VI.
    # Solution: Configure all session in LabVIEW project, then run the VI(s) that
    # use those sessions.
    SESSION_CONFLICT_LV_PROJECT = _cconsts.NX_ERR_SESSION_CONFLICT_LV_PROJECT
    # You used an empty name for an XNET database object (database, cluster, ECU,
    # frame, or signal). Empty name is not supported. Solution: Refer to NI-XNET
    # help for IO names to review the required syntax for the name, and change
    # your code to use that syntax.
    DB_OBJECT_NAME_EMPTY = _cconsts.NX_ERR_DB_OBJECT_NAME_EMPTY
    # You used a name for an XNET database object (such as frame or signal) that
    # did not include a valid cluster selection. Solution: Refer to the NI-XNET
    # help for the IO name that you are using, and use the syntax specified for
    # that class, which includes the cluster selection.
    MISSING_ALIAS_IN_DB_OBJECT_NAME = _cconsts.NX_ERR_MISSING_ALIAS_IN_DB_OBJECT_NAME
    # Unsupported FIBEX file version. Solution: Use only FIBEX versions that are
    # supported by this version of NI-XNET. Please see the NI-XNET documentation
    # for information on which FIBEX versions are currently supported.
    FIBEX_IMPORT_VERSION = _cconsts.NX_ERR_FIBEX_IMPORT_VERSION
    # You used an empty name for the XNET Session. Empty name is not supported.
    # Solution: Use a valid XNET session name from your LabVIEW project.
    EMPTY_SESSION_NAME = _cconsts.NX_ERR_EMPTY_SESSION_NAME
    # There is not enough message RAM on the FlexRay hardware to configure the
    # data partition for the object(s). Solution: Please refer to the manual for
    # limitations on the number of objects that can be created at any given time
    # based on the payload length.
    NOT_ENOUGH_MESSAGE_RAM_FOR_OBJECT = _cconsts.NX_ERR_NOT_ENOUGH_MESSAGE_RAM_FOR_OBJECT
    # The FlexRay keyslot ID has been configured and a startup session has been
    # created. Either the keyslot ID needs to be configured OR the startup session
    # needs to be created. Both cannot exist at the same time. Solution: Choose a
    # single method to configure startup sessions in your application.
    KEY_SLOT_ID_CONFIG = _cconsts.NX_ERR_KEY_SLOT_ID_CONFIG
    # An unsupported session was created. For example, stream output is not
    # supported on FlexRay hardware. Solution: Only use supported sessions in your
    # application.
    UNSUPPORTED_SESSION = _cconsts.NX_ERR_UNSUPPORTED_SESSION
    # An XNET session was created after starting the Interface. Only the Stream
    # Input session in the subordinate mode can be created after the Interface has
    # started. Solution: Create sessions prior to starting the XNET Interface in
    # your application.
    OBJECT_CREATED_AFTER_START = _cconsts.NX_ERR_OBJECT_CREATED_AFTER_START
    # The Single Slot property was enabled on the XNET FlexRay Interface after the
    # interface had started. Solution: Enable the Single Slot property prior to
    # starting the XNET FlexRay Interface.
    SINGLE_SLOT_ENABLED_AFTER_START = _cconsts.NX_ERR_SINGLE_SLOT_ENABLED_AFTER_START
    # The FlexRay macrotick offset specified for XNET Create Timing Source is
    # unsupported. Example: Specifying a macrotick offset greater than
    # MacroPerCycle will result in this error. Solution: Specify a macrotick
    # offset within the supported range for the cluster.
    UNSUPPORTED_NUM_MACROTICKS = _cconsts.NX_ERR_UNSUPPORTED_NUM_MACROTICKS
    # You used invalid syntax in the name of a database object (signal, frame, or
    # ECU). For example, you may have specified a frame's name as
    # [cluster].[frame], which is allowed in NI-XNET for C/C++, but not NI-XNET
    # for LabVIEW. Solution: Use the string syntax specified in the help topic for
    # the XNET I/O name class you are using.
    BAD_SYNTAX_IN_DATABASE_OBJECT_NAME = _cconsts.NX_ERR_BAD_SYNTAX_IN_DATABASE_OBJECT_NAME
    # A LIN schedule entry name is ambiguous, e.g. a schedule entry with the same
    # name exists in another schedule. Solution: Specify the schedule name for the
    # schedule entry using the required syntax.
    AMBIGUOUS_SCHEDULE_ENTRY_NAME = _cconsts.NX_ERR_AMBIGUOUS_SCHEDULE_ENTRY_NAME
    # A LIN schedule entry with the same name already exists in the schedule.
    # Solution: Use another name for this schedule entry.
    DUPLICATE_SCHEDULE_ENTRY_NAME = _cconsts.NX_ERR_DUPLICATE_SCHEDULE_ENTRY_NAME
    # At least one of the frames in the session has an undefined identifier.
    # Solution: Set the frame's "Identifier (Slot)" property before creating the
    # session.
    UNDEFINED_FRAME_ID = _cconsts.NX_ERR_UNDEFINED_FRAME_ID
    # At least one of the frames in the session has an undefined payload length.
    # Solution: Set the frame's "Payload Length (in bytes)" property before
    # creating the session.
    UNDEFINED_FRAME_PAYLOAD_LENGTH = _cconsts.NX_ERR_UNDEFINED_FRAME_PAYLOAD_LENGTH
    # At least one of the signals in the session has an undefined start bit.
    # Solution: Set the "Start Bit" property of the signal before creating the
    # session.
    UNDEFINED_SIGNAL_START_BIT = _cconsts.NX_ERR_UNDEFINED_SIGNAL_START_BIT
    # At least one of the signals in the session has an undefined number of bits.
    # Solution: Set the "Number of Bits" property of the signal before creating
    # the session.
    UNDEFINED_SIGNAL_NUM_BITS = _cconsts.NX_ERR_UNDEFINED_SIGNAL_NUM_BITS
    # At least one of the signals in the session has an undefined byte order.
    # Solution: Set the "Byte Order" property of the signal before creating the
    # session.
    UNDEFINED_SIGNAL_BYTE_ORDER = _cconsts.NX_ERR_UNDEFINED_SIGNAL_BYTE_ORDER
    # At least one of the signals in the session has an undefined data type.
    # Solution: Set the "Data Type" property of the signal before creating the
    # session.
    UNDEFINED_SIGNAL_DATA_TYPE = _cconsts.NX_ERR_UNDEFINED_SIGNAL_DATA_TYPE
    # At least one of the subframes in the session has an undefined multiplexer
    # value. Solution: Set the "Multiplexer Value" property of the subframe before
    # creating the session.
    UNDEFINED_SUBF_MUX_VALUE = _cconsts.NX_ERR_UNDEFINED_SUBF_MUX_VALUE
    # You provided an invalid index to Write (State LIN Schedule Change).
    # Solution: Use a number from to N-1, where N is the number of LIN schedules
    # returned from the cluster property LIN Schedules. If you are using LabVIEW,
    # the string for the number must be decimal (not hexadecimal).
    INVALID_LIN_SCHED_INDEX = _cconsts.NX_ERR_INVALID_LIN_SCHED_INDEX
    # You provided an invalid name to Write (State LIN Schedule Change). Solution:
    # Use a valid LIN schedule name returned from the cluster property LIN
    # Schedules, or the session property Interface LIN Schedules. You can use the
    # short name (schedule only) or long name (schedule plus database and
    # cluster).
    INVALID_LIN_SCHED_NAME = _cconsts.NX_ERR_INVALID_LIN_SCHED_NAME
    # You provided an invalid active index for the session property.
    INVALID_ACTIVE_FRAME_INDEX = _cconsts.NX_ERR_INVALID_ACTIVE_FRAME_INDEX
    # You provided an invalid name for Frame:Active of the session property node.
    # Solution: Use a valid item name from the session's List property. You can
    # use the short name (frame or signal only) or long name (frame/signal plus
    # database and cluster).
    INVALID_ACTIVE_FRAME_NAME = _cconsts.NX_ERR_INVALID_ACTIVE_FRAME_NAME
    # The database you are using requires using PDUs, and the operation is
    # ambiguous with respect to PDUs. Example: You are trying to get the frame
    # parent of the signal, but the PDU in which the signal is contained is
    # referenced in multiple frames.
    AMBIGUOUS_PDU = _cconsts.NX_ERR_AMBIGUOUS_PDU
    # A PDU with the same name already exists in the cluster. Solution: Use
    # another name for this PDU.
    DUPLICATE_PDU = _cconsts.NX_ERR_DUPLICATE_PDU
    # You are trying to assign start bits or update bits to PDUs referenced in a
    # frame, but the number of elements in this array is different than the number
    # of referenced PDUs. Solution: Use the same number of elements in the array
    # as in the PDU references array.
    NUMBER_OF_PD_US = _cconsts.NX_ERR_NUMBER_OF_PD_US
    # The configuration of this object requires using advanced PDUs, which the
    # given protocol does not support. Solution: You cannot use this object in the
    # given protocol.
    PD_US_REQUIRED = _cconsts.NX_ERR_PD_US_REQUIRED
    # The maximum number of PDUs has been exceeded. Solution: Use fewer PDUs in
    # your sessions.
    MAX_PD_US = _cconsts.NX_ERR_MAX_PD_US
    # This mode value is not currently supported. Solution: Use a valid value.
    UNSUPPORTED_MODE = _cconsts.NX_ERR_UNSUPPORTED_MODE
    # The firmware image on your XNET hardware is corrupted. Solution: Update the
    # firmware of this XNET hardware in MAX.
    BAD_FPGA_SIGNATURE = _cconsts.NX_ERR_BAD_FPGA_SIGNATURE
    BADC_SERIES_FPGA_SIGNATURE = _cconsts.NX_ERR_BADC_SERIES_FPGA_SIGNATURE
    # The firmware version of your XNET hardware is not in sync with your host
    # computer. Solution: Update the firmware of this XNET hardware in MAX.
    BAD_FPGA_REVISION = _cconsts.NX_ERR_BAD_FPGA_REVISION
    BADC_SERIES_FPGA_REVISION = _cconsts.NX_ERR_BADC_SERIES_FPGA_REVISION
    # The firmware version of your XNET C Series module is not in sync with the
    # NI-XNET software on your remote target. Solution: Update the NI-XNET
    # software on the remote target.
    BAD_FPGA_REVISION_ON_TARGET = _cconsts.NX_ERR_BAD_FPGA_REVISION_ON_TARGET
    # The terminal you are trying to use is already in use. Only one connection
    # per terminal is allowed. Solution: disconnect the terminal that is already
    # in use.
    ROUTE_IN_USE = _cconsts.NX_ERR_ROUTE_IN_USE
    # You need to install a supported version of NI-DAQmx for your XNET C Series
    # module to work correctly with your Compact DAQ system. Solution: Check the
    # NI-XNET readme file for supported versions of the NI-DAQmx driver software.
    DA_QMX_INCORRECT_VERSION = _cconsts.NX_ERR_DA_QMX_INCORRECT_VERSION
    # Unable to create the requested route. This may be caused by a routing
    # conflict or an invalid terminal name. Solution: Fix invalid terminal names,
    # such as a blank string. Since NI-XNET relies on the NI-DAQmx driver software
    # to create routes on Compact DAQ chassis, use DAQmx to resolve routing
    # conflicts.
    ADD_ROUTE = _cconsts.NX_ERR_ADD_ROUTE
    # You attempted to transmit a go to sleep frame (by setting the LIN Sleep mode
    # to Remote Sleep) on a LIN interface configured as slave. In conformance with
    # the LIN protocol standard, only an interface configured as master may
    # transmit a go to sleep frame.
    REMOTE_SLEEP_ON_LIN_SLAVE = _cconsts.NX_ERR_REMOTE_SLEEP_ON_LIN_SLAVE
    # You attempted to set properties related to Sleep and Wakeup when the FlexRay
    # cluster defined in the Fibex file does not support it. Solution: Edit the
    # Fibex file used in your application to include all relevant cluster wakeup
    # attributes.
    SLEEP_WAKEUP_NOT_SUPPORTED = _cconsts.NX_ERR_SLEEP_WAKEUP_NOT_SUPPORTED
    # The data payload written for a diagnostic frame for transmit does not
    # conform to the LIN transport layer specification. Solution: Ensure the data
    # payload for a diagnostic frame conforms to the transport layer
    # specification.
    LIN_TRANSPORT_LAYER = _cconsts.NX_ERR_LIN_TRANSPORT_LAYER
    # An error occurred within the NI-XNET example code for logfile access (TDMS).
    # Solution: For LabVIEW, the subVI with the error is shown as the source, and
    # you can open that subVI to determine the cause of the problem. For other
    # programming languages, review the source code for the logfile example to
    # determine the cause of the problem.
    LOGFILE = _cconsts.NX_ERR_LOGFILE
    # You attempted to write a LIN schedule and use a stream output replay timing
    # mode concurrently. You can only use the stream output immediate timing mode
    # cuncurrently with the LIN scheduler.
    STRM_OUT_TMG_LIN_SCHEDULER_CONFLICT = _cconsts.NX_ERR_STRM_OUT_TMG_LIN_SCHEDULER_CONFLICT
    # You attempted to create a session that is incompatible with the LIN
    # interface personality (master or slave), or set the LIN interface
    # personality to one that is incompatible with a session already created for
    # it. For example, setting the LIN interface to slave after creating a stream
    # output session will report this error, because only LIN interface as master
    # supports stream output.
    SESSN_TYPE_LIN_INTF_PRS_INCOMPATIBLE = _cconsts.NX_ERR_SESSN_TYPE_LIN_INTF_PRS_INCOMPATIBLE
    # You attempted to save an LDF or DBC database, but the passed reference is
    # not a database cluster. Solution: A cluster reference must be used to
    # specify the cluster you want to export.
    SAVE_CLUSTER_ONLY = _cconsts.NX_ERR_SAVE_CLUSTER_ONLY
    # Need to define for compatibility with older versions
    SAVE_LDF_CLUSTER_ONLY = _cconsts.NX_ERR_SAVE_LDF_CLUSTER_ONLY
    # You tried to assign the same interface name twice. This is not permitted.
    # Solution: Assign a unique name to an interface.
    DUPLICATE_INTERFACE_NAME = _cconsts.NX_ERR_DUPLICATE_INTERFACE_NAME
    # Transceiver cable hardware revision is too new. The current driver does not
    # support this transceiver cable. Solution: Upgrade the NI-XNET driver.
    INCOMPATIABLE_TRANSCEIVER_REVISION = _cconsts.NX_ERR_INCOMPATIABLE_TRANSCEIVER_REVISION
    # Transceiver cable image revision is too new. The current driver does not
    # support this transceiver cable. Solution: Upgrade the NI-XNET driver or
    # downgrade the image on the transceiver cable.
    INCOMPATIABLE_TRANSCEIVER_IMAGE = _cconsts.NX_ERR_INCOMPATIABLE_TRANSCEIVER_IMAGE
    # The property does not apply to this type of hardware. Solution: Do not apply
    # the property to this type of hardware.
    PROPERTY_NOTSUPPORTED = _cconsts.NX_ERR_PROPERTY_NOTSUPPORTED
    # Exporting cluster into the specified database type failed. Solution: Ensure
    # the database configuration is complete. Refer to the standard documentation
    # for the related file format.
    SEMANTIC = _cconsts.NX_ERR_EXPORT_SEMANTIC
    # A J1939 input queue overflowed. Reading large J1939 frames can make the
    # queue overflow, and the Read function delivers fewer frames then specified.
    # Solution: Call the Read function again to read the remaining frames.
    J1939_QUEUE_OVERFLOW = _cconsts.NX_ERR_J1939_QUEUE_OVERFLOW
    # You are trying to transmit a non-J1939 frame with more than 8 bytes. Only
    # J1939 frames can use the J1939 transport protocol. Solution: Verify the
    # transport protocol property on the frame in the database.
    NON_J1939_FRAME_SIZE = _cconsts.NX_ERR_NON_J1939_FRAME_SIZE
    # You are trying to transmit a J1939 frame, but no J1939 address is assigned
    # to the session. Solution: Set the address using the J1939 address property.
    J1939_MISSING_ADDRESS = _cconsts.NX_ERR_J1939_MISSING_ADDRESS
    # The received J1939 TP.CM_CTS message has the wrong total size.
    J1939_ADDRESS_LOST = _cconsts.NX_ERR_J1939_ADDRESS_LOST
    # The next packet value of the received J1939 TP.CM_CTS message is larger than
    # the total number of packets.
    J1939_CTS_NEXT_PCK_LARGER_TOTAL_PCK_NUM = _cconsts.NX_ERR_J1939_CTS_NEXT_PCK_LARGER_TOTAL_PCK_NUM
    # The received J1939 TP.CM_CTS message has a number of packets of 0, but the
    # next packet number is not 255.
    J1939_CTS_NEXT_PCK = _cconsts.NX_ERR_J1939_CTS_NEXT_PCK
    # The received J1939 TP.CM_CTS message has not does not have the same PGN as
    # in the TP.CM_RTS message.
    J1939_CTS_NEXT_PCK_NULL = _cconsts.NX_ERR_J1939_CTS_NEXT_PCK_NULL
    # The received J1939 TP.CM_CTS message does not have the same PGN as in the
    # TP.CM_RTS message.
    J1939_CTS_PGN = _cconsts.NX_ERR_J1939_CTS_PGN
    # Received unexpected sequence number in the J1939 TP.DT message.
    J1939_UNEXPECTED_SEQ_NUM = _cconsts.NX_ERR_J1939_UNEXPECTED_SEQ_NUM
    # More Packets are requested than allowed in the J1939 TP.CM_CTS message.
    J1939_MORE_PCK_REQ_THAN_ALLOWED = _cconsts.NX_ERR_J1939_MORE_PCK_REQ_THAN_ALLOWED
    # J1939 Timeout T1 while waiting for data.
    J1939_TIMEOUT_T1 = _cconsts.NX_ERR_J1939_TIMEOUT_T1
    # J1939 Timeout T2 while waiting for data.
    J1939_TIMEOUT_T2 = _cconsts.NX_ERR_J1939_TIMEOUT_T2
    # J1939 Timeout T3 while waiting for TP.CM_CTS or TP.CM_EndOfMsgAck.
    J1939_TIMEOUT_T3 = _cconsts.NX_ERR_J1939_TIMEOUT_T3
    # J1939 Timeout T4 while waiting for next CTS MSG.
    J1939_TIMEOUT_T4 = _cconsts.NX_ERR_J1939_TIMEOUT_T4
    # Received wrong DLC in the J1939 TP.CM_RTS message. DLC must be 8.
    J1939_RTS_DLC = _cconsts.NX_ERR_J1939_RTS_DLC
    # Received wrong DLC in the J1939 TP.CM_CTS message. DLC must be 8.
    J1939_CTS_DLC = _cconsts.NX_ERR_J1939_CTS_DLC
    # Received wrong DLC in the J1939 TP.CM_BAM message. DLC must be 8.
    J1939_BAM_DLC = _cconsts.NX_ERR_J1939_BAM_DLC
    # Received wrong DLC in the J1939 TP.DT message. DLC must be 8.
    J1939_DT_DLC = _cconsts.NX_ERR_J1939_DT_DLC
    # Received wrong DLC in the J1939 TP.CM_Abort message. DLC must be 8.
    J1939_ABORT_DLC = _cconsts.NX_ERR_J1939_ABORT_DLC
    # Received wrong DLC in the J1939 TP.CM_EndOfMsgAck message. DLC must be 8.
    J1939_EOMA_DLC = _cconsts.NX_ERR_J1939_EOMA_DLC
    # Received wrong PGN in the J1939 TP.CM_Abort message.
    J1939_ABORT_PGN = _cconsts.NX_ERR_J1939_ABORT_PGN
    # Internal error occurred for send TP.CM_CTS Hold Message.
    J1939_CTS_HOLD_MSG = _cconsts.NX_ERR_J1939_CTS_HOLD_MSG
    # Invalid total message size in J1939 TP.CM_RTS message. Expect 9..1785.
    J1939_INVALID_TOTAL_SIZE = _cconsts.NX_ERR_J1939_INVALID_TOTAL_SIZE
    # Total number of packets in received J1939 TP.CM_RTS message must be greater
    # than 1.
    J1939_TOTAL_PCK_NUM = _cconsts.NX_ERR_J1939_TOTAL_PCK_NUM
    # Reserved data bytes in J1939 received message are not BFF63FF.
    J1939_RESERVED_DATA = _cconsts.NX_ERR_J1939_RESERVED_DATA
    # Not enough system resources for the J1939 Transport Protocol.
    J1939_NOT_ENOUGH_SYS_RES = _cconsts.NX_ERR_J1939_NOT_ENOUGH_SYS_RES
    # Received J1939 TP.CM_Abort message with reason ActiveConnection: Already in
    # one or more connection managed sessions and cannot support another.
    J1939_ABORT_MSG_ACTIVE_CONNECTION = _cconsts.NX_ERR_J1939_ABORT_MSG_ACTIVE_CONNECTION
    # Received J1939 TP.CM_Abort message with reason NotEnoughSystemResources:
    # System resources were needed for another task, so this connection managed
    # session was terminated.
    J1939_ABORT_MSG_NOT_ENOUGH_SYS_RES = _cconsts.NX_ERR_J1939_ABORT_MSG_NOT_ENOUGH_SYS_RES
    # Received J1939 TP.CM_Abort message with reason Timeout: A timeout occurred,
    # and this is the connection abort to close the session.
    J1939_ABORT_MSG_TIMEOUT = _cconsts.NX_ERR_J1939_ABORT_MSG_TIMEOUT
    # Received J1939 TP.CM_Abort message with reason CtsReceived: CTS messages
    # received when data transfer is in progress.
    J1939_ABORT_MSG_CTS_REC = _cconsts.NX_ERR_J1939_ABORT_MSG_CTS_REC
    # Received J1939 TP.CM_Abort message with reason MaxRetransmit: Maximum
    # retransmit request limit reached.
    J1939_ABORT_MSG_MAX_RETRANSMIT = _cconsts.NX_ERR_J1939_ABORT_MSG_MAX_RETRANSMIT
    # Remote communication with the LabVIEW RT target failed because the host and
    # target versions of NI-XNET are different. Solution: On the target, install
    # the same NI-XNET version that is installed on the host.
    RPC_VERSION = _cconsts.NX_ERR_RPC_VERSION
    # The CAN frame I/O mode is higher than the CAN cluster I/O mode. This frame
    # cannot be transmitted on the network. Solution: Change the frame or cluster
    # I/O mode.
    FRAME_CAN_IO_MODE = _cconsts.NX_ERR_FRAME_CAN_IO_MODE
    # The current driver cannot update the firmware on your hardware. Solution:
    # Ask National Instruments for compatible driver software.
    INCOMPATIBLE_FLASH = _cconsts.NX_ERR_INCOMPATIBLE_FLASH
    # You are trying to use the CAN Transmit I/O Mode (TxIoMode) property in an
    # unsupported interface mode. Solution: You can use this property in only
    # non-ISO or ISO Legacy mode.
    TX_IO_MODE = _cconsts.NX_ERR_TX_IO_MODE
    # You are trying to use the XS Transceiver Cable on unsupported hardware. This
    # currently requires a PXIe-8510 board.
    XS_DONGLE_UNSUPPORTED_BOARD = _cconsts.NX_ERR_XS_DONGLE_UNSUPPORTED_BOARD
    # You are trying to use a database alias name that contains an invalid
    # character (for example, a comma).
    INVALID_CHAR_IN_DATABASE_ALIAS = _cconsts.NX_ERR_INVALID_CHAR_IN_DATABASE_ALIAS
    # You are trying to use a database filepath that contains an invalid character
    # (for example, a comma).
    INVALID_CHAR_IN_DATABASE_FILEPATH = _cconsts.NX_ERR_INVALID_CHAR_IN_DATABASE_FILEPATH
    # You are trying to use CAN FD with a non-HS/FD port. CAN FD is supported with
    # High Speed CAN only.
    INVALID_CAN_FD_PORT_TYPE = _cconsts.NX_ERR_INVALID_CAN_FD_PORT_TYPE
    # An unconditional LIN schedule entry is wrongly configured.
    # Solution: Reference exactly one frame in the entry.
    INV_UNCONDITIONAL_ENTRY = _cconsts.NX_ERR_INV_UNCONDITIONAL_ENTRY
    # An event LIN schedule entry has no collision resolving schedule assigned.
    # Solution: Assign a schedule to the schedule entry.
    EVENT_ENTRY_NO_SCHEDULE = _cconsts.NX_ERR_EVENT_ENTRY_NO_SCHEDULE
    # You have connected your USB device to a port that only supports Full Speed
    # (USB 1.1). NI-XNET USB devices require at least High Speed (USB 2.0+)
    # support for correct operation.
    UNSUPPORTED_USB_SPEED = _cconsts.NX_ERR_UNSUPPORTED_USB_SPEED


class Warn(enum.Enum):
    # The CAN FD baud rate you supplied exceeds the capabilities the transceiver
    # manufacturer specified. In our internal testing, we have found this baud
    # rate to run, but bus errors may be detected or generated during
    # communication. Refer to the NI-XNET CAN Hardware Overview section in the
    # NI-XNET Hardware and Software Manual for more information.
    FD_BAUD_EXCEEDS_CAPABILITY = _cconsts.NX_WARN_FD_BAUD_EXCEEDS_CAPABILITY
    # There is a warning from importing the database file. For details, refer to
    # the import log file nixnetfx-log.txt or nixnetldf-log.txt under
    # %LOCALAPPDATA%\\National Instruments\\NI-XNET\\log. On Windows XP, the files
    # can be found under %USERPROFILE%\\Local Settings\\Application Data\\National
    # Instruments\\NI-XNET\\log. Please note that this location may be hidden on
    # your computer.
    DATABASE_IMPORT = _cconsts.NX_WARN_DATABASE_IMPORT
    # The database file has been imported, but it was not created by the XNET
    # Editor or using the XNET API. Saving the database file with the XNET API or
    # XNET Editor may lose information from the original file.
    DATABASE_IMPORT_FIBEX_NO_XNET_FILE = _cconsts.NX_WARN_DATABASE_IMPORT_FIBEX_NO_XNET_FILE
    # The database file was not created by the XNET Editor or using the XNET API.
    # Additionally, there is another warning. For details, refer to the import log
    # file nixnetfx-log.txt under %LOCALAPPDATA%\\National Instruments\\NI-XNET\\log.
    # On Windows XP, the file can be found under %USERPROFILE%\\Local
    # Settings\\Application Data\\National Instruments\\NI-XNET\\log. Please note that
    # this location may be hidden on your computer.
    DATABASE_IMPORT_FIBEX_NO_XNET_FILE_PLUS_WARNING = _cconsts.NX_WARN_DATABASE_IMPORT_FIBEX_NO_XNET_FILE_PLUS_WARNING
    # Close Database returns a warning instead of an error when an invalid
    # reference is passed to the function.
    DATABASE_BAD_REFERENCE = _cconsts.NX_WARN_DATABASE_BAD_REFERENCE
    # Your are retrieving signals from a frame that uses advanced PDU
    # configuration. The signal start bit is given relative to the PDU, and it may
    # be different than the start bit relative to the frame.
    ADVANCED_PDU = _cconsts.NX_WARN_ADVANCED_PDU
    # The multiplexer size exceeds 16 bit. This is not supported for Single Point
    # sessions.
    MUX_EXCEEDS16_BIT = _cconsts.NX_WARN_MUX_EXCEEDS16_BIT


class ObjectClass(enum.Enum):
    DATABASE = _cconsts.NX_CLASS_DATABASE
    CLUSTER = _cconsts.NX_CLASS_CLUSTER
    FRAME = _cconsts.NX_CLASS_FRAME
    SIGNAL = _cconsts.NX_CLASS_SIGNAL
    SUBFRAME = _cconsts.NX_CLASS_SUBFRAME
    ECU = _cconsts.NX_CLASS_ECU
    LIN_SCHED = _cconsts.NX_CLASS_LIN_SCHED
    LIN_SCHED_ENTRY = _cconsts.NX_CLASS_LIN_SCHED_ENTRY
    PDU = _cconsts.NX_CLASS_PDU
    SESSION = _cconsts.NX_CLASS_SESSION
    SYSTEM = _cconsts.NX_CLASS_SYSTEM
    DEVICE = _cconsts.NX_CLASS_DEVICE
    INTERFACE = _cconsts.NX_CLASS_INTERFACE
    ALIAS = _cconsts.NX_CLASS_ALIAS


class CreateSessionMode(enum.Enum):
    """Create Session Mode.

    The session mode specifies the data type (signals or frames), direction
    (input or output), and how data is transferred between your application and
    the network.

    Values:
        SIGNAL_IN_SINGLE_POINT:
            Reads the most recent value received for each signal. This mode
            typically is used for control or simulation applications, such as
            Hardware In the Loop (HIL).
        SIGNAL_IN_WAVEFORM:
            Using the time when the signal frame is received, resamples the
            signal data to a waveform with a fixed sample rate. This mode
            typically is used for synchronizing XNET data with DAQmx
            analog/digital input channels.
        SIGNAL_IN_XY:
            For each frame received, provides its signals as a value/timestamp
            pair. This is the recommended mode for reading a sequence of all
            signal values.
        SIGNAL_OUT_SINGLE_POINT:
            Writes signal values for the next frame transmit. This mode
            typically is used for control or simulation applications, such as
            Hardware In the Loop (HIL).
        SIGNAL_OUT_WAVEFORM:
            Using the time when the signal frame is transmitted according to the
            database, resamples the signal data from a waveform with a fixed
            sample rate. This mode typically is used for synchronizing XNET data
            with DAQmx analog/digital output channels.
        SIGNAL_OUT_XY:
            Provides a sequence of signal values for transmit using each frame's
            timing as the database specifies. This is the recommended mode for
            writing a sequence of all signal values.
        FRAME_IN_STREAM:
            Reads all frames received from the network using a single stream.
            This mode typically is used for analyzing and/or logging all frame
            traffic in the network.
        FRAME_IN_QUEUED:
            Reads data from a dedicated queue per frame. This mode enables your
            application to read a sequence of data specific to a frame (for
            example, CAN identifier).
        FRAME_IN_SINGLE_POINT:
            Reads the most recent value received for each frame. This mode
            typically is used for control or simulation applications that
            require lower level access to frames (not signals).
        FRAME_OUT_STREAM:
            Transmits an arbitrary sequence of frame values using a single
            stream. The values are not limited to a single frame in the
            database, but can transmit any frame.
        FRAME_OUT_QUEUED:
            Provides a sequence of values for a single frame, for transmit using
            that frame's timing as the database specifies.
        FRAME_OUT_SINGLE_POINT:
            Writes frame values for the next transmit. This mode typically is
            used for control or simulation applications that require lower level
            access to frames (not signals).
        SIGNAL_CONVERSION_SINGLE_POINT:
            This mode does not use any hardware. It is used to convert data
            between the signal representation and frame representation.
    """
    SIGNAL_IN_SINGLE_POINT = _cconsts.NX_MODE_SIGNAL_IN_SINGLE_POINT
    SIGNAL_IN_WAVEFORM = _cconsts.NX_MODE_SIGNAL_IN_WAVEFORM
    SIGNAL_IN_XY = _cconsts.NX_MODE_SIGNAL_IN_XY
    SIGNAL_OUT_SINGLE_POINT = _cconsts.NX_MODE_SIGNAL_OUT_SINGLE_POINT
    SIGNAL_OUT_WAVEFORM = _cconsts.NX_MODE_SIGNAL_OUT_WAVEFORM
    SIGNAL_OUT_XY = _cconsts.NX_MODE_SIGNAL_OUT_XY
    FRAME_IN_STREAM = _cconsts.NX_MODE_FRAME_IN_STREAM
    FRAME_IN_QUEUED = _cconsts.NX_MODE_FRAME_IN_QUEUED
    FRAME_IN_SINGLE_POINT = _cconsts.NX_MODE_FRAME_IN_SINGLE_POINT
    FRAME_OUT_STREAM = _cconsts.NX_MODE_FRAME_OUT_STREAM
    FRAME_OUT_QUEUED = _cconsts.NX_MODE_FRAME_OUT_QUEUED
    FRAME_OUT_SINGLE_POINT = _cconsts.NX_MODE_FRAME_OUT_SINGLE_POINT
    SIGNAL_CONVERSION_SINGLE_POINT = _cconsts.NX_MODE_SIGNAL_CONVERSION_SINGLE_POINT


class StartStopScope(enum.Enum):
    """Start/Stop Scope enum.

    Values:
        NORMAL:
            The session is started followed by starting the interface. This is
            equivalent to calling :any:`nixnet._session.base.SessionBase.start`
            with the Session Only Scope followed by calling
            :any:`nixnet._session.base.SessionBase.start` with the Interface Only Scope.
        SESSION_ONLY:
            The session is placed into the Started state (refer to State Models).
            If the interface is in the Stopped state before this function runs,
            the interface remains in the Stopped state, and no communication
            occurs with the bus. To have multiple sessions start at exactly the
            same time, start each session with the Session Only Scope. When you
            are ready for all sessions to start communicating on the associated
            interface, call :any:`nixnet._session.base.SessionBase.start` with
            the Interface Only scope. Starting a previously started session is
            considered a no-op. This operation sends the command to start the
            session, but does not wait for the session to be started. It is
            ideal for a real-time application where performance is critical.
        INTERFACE_ONLY:
            If the underlying interface is not previously started, the interface
            is placed into the Started state (refer to State Models). After the
            interface starts communicating, all previously started sessions can
            transfer data to and from the bus. Starting a previously started
            interface is considered a no-op.
        SESSION_ONLY_BLOCKING:
            The session is placed in the Started state (refer to State Models).
            If the interface is in the Stopped state before this function runs,
            the interface remains in the Stopped state, and no communication
            occurs with the bus. To have multiple sessions start at exactly the
            same time, start each session with the Session Only Scope. When you
            are ready for all sessions to start communicating on the associated
            interface, call nxStart with the Interface Only Scope. Starting a
            previously started session is considered a no-op. This operation
            waits for the session to start before completing.
    """
    NORMAL = _cconsts.NX_START_STOP_NORMAL
    SESSION_ONLY = _cconsts.NX_START_STOP_SESSION_ONLY
    INTERFACE_ONLY = _cconsts.NX_START_STOP_INTERFACE_ONLY
    SESSION_ONLY_BLOCKING = _cconsts.NX_START_STOP_SESSION_ONLY_BLOCKING


class BlinkMode(enum.Enum):
    DISABLE = _cconsts.NX_BLINK_DISABLE
    ENABLE = _cconsts.NX_BLINK_ENABLE


class ReadState(enum.Enum):
    TIME_CURRENT = _cconsts.NX_STATE_TIME_CURRENT
    TIME_COMMUNICATING = _cconsts.NX_STATE_TIME_COMMUNICATING
    TIME_START = _cconsts.NX_STATE_TIME_START
    SESSION_INFO = _cconsts.NX_STATE_SESSION_INFO
    CAN_COMM = _cconsts.NX_STATE_CAN_COMM
    FLEX_RAY_COMM = _cconsts.NX_STATE_FLEX_RAY_COMM
    FLEX_RAY_STATS = _cconsts.NX_STATE_FLEX_RAY_STATS
    LIN_COMM = _cconsts.NX_STATE_LIN_COMM
    J1939_COMM = _cconsts.NX_STATE_J1939_COMM


class WriteState(enum.Enum):
    LIN_SCHEDULE_CHANGE = _cconsts.NX_STATE_LIN_SCHEDULE_CHANGE
    LIN_DIAGNOSTIC_SCHEDULE_CHANGE = _cconsts.NX_STATE_LIN_DIAGNOSTIC_SCHEDULE_CHANGE
    FLEX_RAY_SYMBOL = _cconsts.NX_STATE_FLEX_RAY_SYMBOL


class IntfCanFdIsoMode(enum.Enum):
    ISO = _cconsts.NX_CAN_FD_MODE_ISO
    NON_ISO = _cconsts.NX_CAN_FD_MODE_NON_ISO
    ISO_LEGACY = _cconsts.NX_CAN_FD_MODE_ISO_LEGACY


class CanFdIsoMode(enum.Enum):
    ISO = _cconsts.NX_CAN_FD_MODE_ISO
    NON_ISO = _cconsts.NX_CAN_FD_MODE_NON_ISO
    ISO_LEGACY = _cconsts.NX_CAN_FD_MODE_ISO_LEGACY


class SessionInfoState(enum.Enum):
    STOPPED = _cconsts.NX_SESSION_INFO_STATE_STOPPED
    STARTED = _cconsts.NX_SESSION_INFO_STATE_STARTED
    MIX = _cconsts.NX_SESSION_INFO_STATE_MIX


class CanCommState(enum.Enum):
    """CAN Comm State.

    Values:
        ERROR_ACTIVE:
            This state reflects normal communication, with few errors detected.
            The CAN interface remains in this state as long as receive error
            counter and transmit error counter are both below 128.
        ERROR_PASSIVE:
            If either the receive error counter or transmit error counter
            increment above 127, the CAN interface transitions into this state.
            Although communication proceeds, the CAN device generally is assumed
            to have problems with receiving frames.

            When a CAN interface is in error passive state, acknowledgement
            errors do not increment the transmit error counter. Therefore, if
            the CAN interface transmits a frame with no other device (ECU)
            connected, it eventually enters error passive state due to
            retransmissions, but does not enter bus off state.
        BUS_OFF:
            If the transmit error counter increments above 255, the CAN
            interface transitions into this state. Communication immediately
            stops under the assumption that the CAN interface must be isolated
            from other devices.

            When a CAN interface transitions to the bus off state, communication
            stops for the interface. All NI-XNET sessions for the interface no
            longer receive or transmit frame values. To restart the CAN
            interface and all its sessions, call
            :any:`nixnet._session.base.SessionBase.start`.
        INIT:
            This is the CAN interface initial state on power-up. The interface
            is essentially off, in that it is not attempting to communicate with
            other nodes (ECUs).

            When the start trigger occurs for the CAN interface, it transitions
            from the Init state to the Error Active state. When the interface
            stops due to a call to :any:`nixnet._session.base.SessionBase.stop`.,
            the CAN interface transitions from either Error Active or Error Passive
            to the Init state. When the interface stops due to the Bus Off state,
            it remains in that state until you restart.
    """
    ERROR_ACTIVE = _cconsts.NX_CAN_COMM_STATE_ERROR_ACTIVE
    ERROR_PASSIVE = _cconsts.NX_CAN_COMM_STATE_ERROR_PASSIVE
    BUS_OFF = _cconsts.NX_CAN_COMM_STATE_BUS_OFF
    INIT = _cconsts.NX_CAN_COMM_STATE_INIT


class CanLastErr(enum.Enum):
    NONE = _cconsts.NX_CAN_LAST_ERR_NONE
    STUFF = _cconsts.NX_CAN_LAST_ERR_STUFF
    FORM = _cconsts.NX_CAN_LAST_ERR_FORM
    ACK = _cconsts.NX_CAN_LAST_ERR_ACK
    BIT1 = _cconsts.NX_CAN_LAST_ERR_BIT1
    BIT0 = _cconsts.NX_CAN_LAST_ERR_BIT0
    CRC = _cconsts.NX_CAN_LAST_ERR_CRC


class CaNioMode(enum.Enum):
    CAN = _cconsts.NX_CA_NIO_MODE_CAN
    CANFD = _cconsts.NX_CA_NIO_MODE_CAN_FD
    CANFDBRS = _cconsts.NX_CA_NIO_MODE_CAN_FD_BRS


class FlexRayPocState(enum.Enum):
    DEFAULT_CONFIG = _cconsts.NX_FLEX_RAY_POC_STATE_DEFAULT_CONFIG
    READY = _cconsts.NX_FLEX_RAY_POC_STATE_READY
    NORMAL_ACTIVE = _cconsts.NX_FLEX_RAY_POC_STATE_NORMAL_ACTIVE
    NORMAL_PASSIVE = _cconsts.NX_FLEX_RAY_POC_STATE_NORMAL_PASSIVE
    HALT = _cconsts.NX_FLEX_RAY_POC_STATE_HALT
    MONITOR = _cconsts.NX_FLEX_RAY_POC_STATE_MONITOR
    CONFIG = _cconsts.NX_FLEX_RAY_POC_STATE_CONFIG


class LinCommState(enum.Enum):
    IDLE = _cconsts.NX_LIN_COMM_STATE_IDLE
    ACTIVE = _cconsts.NX_LIN_COMM_STATE_ACTIVE
    INACTIVE = _cconsts.NX_LIN_COMM_STATE_INACTIVE


class LinDiagnosticSchedule(enum.Enum):
    NULL = _cconsts.NX_LIN_DIAGNOSTIC_SCHEDULE_NULL
    MASTER_REQ = _cconsts.NX_LIN_DIAGNOSTIC_SCHEDULE_MASTER_REQ
    SLAVE_RESP = _cconsts.NX_LIN_DIAGNOSTIC_SCHEDULE_SLAVE_RESP


class LinLastErrCode(enum.Enum):
    NONE = _cconsts.NX_LIN_LAST_ERR_CODE_NONE
    UNKNOWN_ID = _cconsts.NX_LIN_LAST_ERR_CODE_UNKNOWN_ID
    FORM = _cconsts.NX_LIN_LAST_ERR_CODE_FORM
    FRAMING = _cconsts.NX_LIN_LAST_ERR_CODE_FRAMING
    READBACK = _cconsts.NX_LIN_LAST_ERR_CODE_READBACK
    TIMEOUT = _cconsts.NX_LIN_LAST_ERR_CODE_TIMEOUT
    CRC = _cconsts.NX_LIN_LAST_ERR_CODE_CRC


class Condition(enum.Enum):
    TRANSMIT_COMPLETE = _cconsts.NX_CONDITION_TRANSMIT_COMPLETE
    INTF_COMMUNICATING = _cconsts.NX_CONDITION_INTF_COMMUNICATING
    INTF_REMOTE_WAKEUP = _cconsts.NX_CONDITION_INTF_REMOTE_WAKEUP


class GetDbcAttributeMode(enum.Enum):
    ATTRIBUTE = _cconsts.NX_GET_DBC_MODE_ATTRIBUTE
    ENUMERATION_LIST = _cconsts.NX_GET_DBC_MODE_ENUMERATION_LIST
    ATTRIBUTE_LIST = _cconsts.NX_GET_DBC_MODE_ATTRIBUTE_LIST
    VALUE_TABLE_LIST = _cconsts.NX_GET_DBC_MODE_VALUE_TABLE_LIST


class Merge(enum.Enum):
    COPY_USE_SOURCE = _cconsts.NXDB_MERGE_COPY_USE_SOURCE
    COPY_USE_TARGET = _cconsts.NXDB_MERGE_COPY_USE_TARGET
    MERGE_USE_SOURCE = _cconsts.NXDB_MERGE_MERGE_USE_SOURCE
    MERGE_USE_TARGET = _cconsts.NXDB_MERGE_MERGE_USE_TARGET


class DongleState(enum.Enum):
    NO_DONGLE_NO_EXT_POWER = _cconsts.NX_DONGLE_STATE_NO_DONGLE_NO_EXT_POWER
    NO_DONGLE_EXT_POWER = _cconsts.NX_DONGLE_STATE_NO_DONGLE_EXT_POWER
    DONGLE_NO_EXT_POWER = _cconsts.NX_DONGLE_STATE_DONGLE_NO_EXT_POWER
    READY = _cconsts.NX_DONGLE_STATE_READY
    BUSY = _cconsts.NX_DONGLE_STATE_BUSY
    COMM_ERROR = _cconsts.NX_DONGLE_STATE_COMM_ERROR
    OVER_CURRENT = _cconsts.NX_DONGLE_STATE_OVER_CURRENT


class DongleId(enum.Enum):
    LSCAN = _cconsts.NX_DONGLE_ID_LS_CAN
    HSCAN = _cconsts.NX_DONGLE_ID_HS_CAN
    SWCAN = _cconsts.NX_DONGLE_ID_SW_CAN
    XSCAN = _cconsts.NX_DONGLE_ID_XS_CAN
    LIN = _cconsts.NX_DONGLE_ID_LIN
    DONGLE_LESS = _cconsts.NX_DONGLE_ID_DONGLE_LESS
    UNKNOWN = _cconsts.NX_DONGLE_ID_UNKNOWN


class Phase(enum.Enum):
    DEVELOPMENT = _cconsts.NX_PHASE_DEVELOPMENT
    ALPHA = _cconsts.NX_PHASE_ALPHA
    BETA = _cconsts.NX_PHASE_BETA
    RELEASE = _cconsts.NX_PHASE_RELEASE


class DevForm(enum.Enum):
    PXI = _cconsts.NX_DEV_FORM_PXI
    PCI = _cconsts.NX_DEV_FORM_PCI
    C_SERIES = _cconsts.NX_DEV_FORM_C_SERIES
    PX_IE = _cconsts.NX_DEV_FORM_PX_IE
    USB = _cconsts.NX_DEV_FORM_USB


class CanTermCap(enum.Enum):
    NO = _cconsts.NX_CAN_TERM_CAP_NO
    YES = _cconsts.NX_CAN_TERM_CAP_YES


class CanTerm(enum.Enum):
    NO = _cconsts.NX_CAN_TERM_CAP_NO
    YES = _cconsts.NX_CAN_TERM_CAP_YES
    OFF = _cconsts.NX_CAN_TERM_OFF
    ON = _cconsts.NX_CAN_TERM_ON


class CanTcvrCap(enum.Enum):
    HS = _cconsts.NX_CAN_TCVR_CAP_HS
    LS = _cconsts.NX_CAN_TCVR_CAP_LS
    XS = _cconsts.NX_CAN_TCVR_CAP_XS
    XSHSLS = _cconsts.NX_CAN_TCVR_CAP_XS_HS_LS
    UNKNOWN = _cconsts.NX_CAN_TCVR_CAP_UNKNOWN


class Protocol(enum.Enum):
    UNKNOWN = _cconsts.NX_PROTOCOL_UNKNOWN
    CAN = _cconsts.NX_PROTOCOL_CAN
    FLEX_RAY = _cconsts.NX_PROTOCOL_FLEX_RAY
    LIN = _cconsts.NX_PROTOCOL_LIN


class AppProtocol(enum.Enum):
    NONE = _cconsts.NX_APP_PROTOCOL_NONE
    J1939 = _cconsts.NX_APP_PROTOCOL_J1939


class CanTcvrState(enum.Enum):
    NORMAL = _cconsts.NX_CAN_TCVR_STATE_NORMAL
    SLEEP = _cconsts.NX_CAN_TCVR_STATE_SLEEP
    SW_WAKEUP = _cconsts.NX_CAN_TCVR_STATE_SW_WAKEUP
    SW_HIGH_SPEED = _cconsts.NX_CAN_TCVR_STATE_SW_HIGH_SPEED


class CanTcvrType(enum.Enum):
    HS = _cconsts.NX_CAN_TCVR_TYPE_HS
    LS = _cconsts.NX_CAN_TCVR_TYPE_LS
    SW = _cconsts.NX_CAN_TCVR_TYPE_SW
    EXT = _cconsts.NX_CAN_TCVR_TYPE_EXT
    DISC = _cconsts.NX_CAN_TCVR_TYPE_DISC


class FlexRayTerm(enum.Enum):
    OFF = _cconsts.NX_FLEX_RAY_TERM_OFF
    ON = _cconsts.NX_FLEX_RAY_TERM_ON


class LinSleep(enum.Enum):
    REMOTE_SLEEP = _cconsts.NX_LIN_SLEEP_REMOTE_SLEEP
    REMOTE_WAKE = _cconsts.NX_LIN_SLEEP_REMOTE_WAKE
    LOCAL_SLEEP = _cconsts.NX_LIN_SLEEP_LOCAL_SLEEP
    LOCAL_WAKE = _cconsts.NX_LIN_SLEEP_LOCAL_WAKE


class LinTerm(enum.Enum):
    OFF = _cconsts.NX_LIN_TERM_OFF
    ON = _cconsts.NX_LIN_TERM_ON


class OutStrmTimng(enum.Enum):
    IMMEDIATE = _cconsts.NX_OUT_STRM_TIMNG_IMMEDIATE
    REPLAY_EXCLUSIVE = _cconsts.NX_OUT_STRM_TIMNG_REPLAY_EXCLUSIVE
    REPLAY_INCLUSIVE = _cconsts.NX_OUT_STRM_TIMNG_REPLAY_INCLUSIVE


class CanPendTxOrder(enum.Enum):
    AS_SUBMITTED = _cconsts.NX_CAN_PEND_TX_ORDER_AS_SUBMITTED
    BY_IDENTIFIER = _cconsts.NX_CAN_PEND_TX_ORDER_BY_IDENTIFIER


class FlexRaySleep(enum.Enum):
    LOCAL_SLEEP = _cconsts.NX_FLEX_RAY_SLEEP_LOCAL_SLEEP
    LOCAL_WAKE = _cconsts.NX_FLEX_RAY_SLEEP_LOCAL_WAKE
    REMOTE_WAKE = _cconsts.NX_FLEX_RAY_SLEEP_REMOTE_WAKE


class FrmFlexRayChAssign(enum.Enum):
    A = _cconsts.NX_FRM_FLEX_RAY_CH_ASSIGN_A
    B = _cconsts.NX_FRM_FLEX_RAY_CH_ASSIGN_B
    AAND_B = _cconsts.NX_FRM_FLEX_RAY_CH_ASSIGN_AAND_B
    NONE = _cconsts.NX_FRM_FLEX_RAY_CH_ASSIGN_NONE


class ClstFlexRaySampClkPer(enum.Enum):
    P0125US = _cconsts.NX_CLST_FLEX_RAY_SAMP_CLK_PER_P0125US
    P025US = _cconsts.NX_CLST_FLEX_RAY_SAMP_CLK_PER_P025US
    P05US = _cconsts.NX_CLST_FLEX_RAY_SAMP_CLK_PER_P05US


class FrmFlexRayTiming(enum.Enum):
    CYCLIC = _cconsts.NX_FRM_FLEX_RAY_TIMING_CYCLIC
    EVENT = _cconsts.NX_FRM_FLEX_RAY_TIMING_EVENT


class FrmCanTiming(enum.Enum):
    CYCLIC_DATA = _cconsts.NX_FRM_CAN_TIMING_CYCLIC_DATA
    EVENT_DATA = _cconsts.NX_FRM_CAN_TIMING_EVENT_DATA
    CYCLIC_REMOTE = _cconsts.NX_FRM_CAN_TIMING_CYCLIC_REMOTE
    EVENT_REMOTE = _cconsts.NX_FRM_CAN_TIMING_EVENT_REMOTE
    CYCLIC_EVENT = _cconsts.NX_FRM_CAN_TIMING_CYCLIC_EVENT


class SigByteOrdr(enum.Enum):
    LITTLE_ENDIAN = _cconsts.NX_SIG_BYTE_ORDR_LITTLE_ENDIAN
    BIG_ENDIAN = _cconsts.NX_SIG_BYTE_ORDR_BIG_ENDIAN


class SigDataType(enum.Enum):
    SIGNED = _cconsts.NX_SIG_DATA_TYPE_SIGNED
    UNSIGNED = _cconsts.NX_SIG_DATA_TYPE_UNSIGNED
    IEEE_FLOAT = _cconsts.NX_SIG_DATA_TYPE_IEEE_FLOAT


class LinSchedRunMode(enum.Enum):
    CONTINUOUS = _cconsts.NX_LIN_SCHED_RUN_MODE_CONTINUOUS
    ONCE = _cconsts.NX_LIN_SCHED_RUN_MODE_ONCE
    NULL = _cconsts.NX_LIN_SCHED_RUN_MODE_NULL


class LinSchedEntryType(enum.Enum):
    UNCONDITIONAL = _cconsts.NX_LIN_SCHED_ENTRY_TYPE_UNCONDITIONAL
    SPORADIC = _cconsts.NX_LIN_SCHED_ENTRY_TYPE_SPORADIC
    EVENT_TRIGGERED = _cconsts.NX_LIN_SCHED_ENTRY_TYPE_EVENT_TRIGGERED
    NODE_CONFIG_SERVICE = _cconsts.NX_LIN_SCHED_ENTRY_TYPE_NODE_CONFIG_SERVICE


class FrmLinChecksum(enum.Enum):
    CLASSIC = _cconsts.NX_FRM_LIN_CHECKSUM_CLASSIC
    ENHANCED = _cconsts.NX_FRM_LIN_CHECKSUM_ENHANCED


class FrameType(enum.Enum):
    CAN_DATA = _cconsts.NX_FRAME_TYPE_CAN_DATA
    CAN_REMOTE = _cconsts.NX_FRAME_TYPE_CAN_REMOTE
    CAN_BUS_ERROR = _cconsts.NX_FRAME_TYPE_CAN_BUS_ERROR
    CAN20_DATA = _cconsts.NX_FRAME_TYPE_CAN20_DATA
    CANFD_DATA = _cconsts.NX_FRAME_TYPE_CANFD_DATA
    CANFDBRS_DATA = _cconsts.NX_FRAME_TYPE_CANFDBRS_DATA
    FLEX_RAY_DATA = _cconsts.NX_FRAME_TYPE_FLEX_RAY_DATA
    FLEX_RAY_NULL = _cconsts.NX_FRAME_TYPE_FLEX_RAY_NULL
    FLEX_RAY_SYMBOL = _cconsts.NX_FRAME_TYPE_FLEX_RAY_SYMBOL
    LIN_DATA = _cconsts.NX_FRAME_TYPE_LIN_DATA
    LIN_BUS_ERROR = _cconsts.NX_FRAME_TYPE_LIN_BUS_ERROR
    LIN_NO_RESPONSE = _cconsts.NX_FRAME_TYPE_LIN_NO_RESPONSE
    J1939_DATA = _cconsts.NX_FRAME_TYPE_J1939_DATA
    SPECIAL_DELAY = _cconsts.NX_FRAME_TYPE_SPECIAL_DELAY
    SPECIAL_LOG_TRIGGER = _cconsts.NX_FRAME_TYPE_SPECIAL_LOG_TRIGGER
    SPECIAL_START_TRIGGER = _cconsts.NX_FRAME_TYPE_SPECIAL_START_TRIGGER
