Single-Point I/O Example
========================

This example uses :any:`nixnet.session.SignalInSinglePointSession` and
:any:`nixnet.session.SignalOutSinglePointSession` to demonstrate how single-point sessions
work.

To adapt this to Frames, just change the sessions to
:any:`nixnet.session.FrameInSinglePointSession` and
:any:`nixnet.session.FrameOutSinglePointSession` with frames instead of
signals.  Then adjust ``read``/``write`` to take a frame object per frame
configured in the session rather than signals.  This works for both CAN and LIN
frames.  See :doc:`queued_io` to see how to read and write frames.

.. literalinclude:: ../../nixnet_examples/can_signal_single_point_io.py
   :pyobject: main
