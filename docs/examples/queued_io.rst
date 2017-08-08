Queued I/O Example
==================

This example uses :any:`nixnet.session.FrameInQueuedSession` and
:any:`nixnet.session.FrameOutQueuedSession` to demonstrate how queued sessions
work.

To adapt this example to LIN frames, reference signals in a database that use LIN:
   ``write``:
      Accepts any frame type.
   ``read``:
      Chooses the frame object to create based on the ``frame_type`` field in
      the raw data.  This can be overridden by passing a custom
      :any:`nixnet.types.FrameFactory` in the ``frame_type`` parameter.

.. literalinclude:: ../../nixnet_examples/can_frame_queued_io.py
   :pyobject: main
