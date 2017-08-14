Adapting CAN examples to LIN
============================

To adapt the examples from CAN to LIN, reference signals in a database that use LIN:
   ``write``:
      Accepts any frame type.
   ``read``:
      Chooses the frame object to create based on the ``frame_type`` field in
      the raw data.  This can be overridden by passing a custom
      :any:`nixnet.types.FrameFactory` in the ``frame_type`` parameter.
   ``change_lin_sched``:
      Writes a request for the LIN interface to change
      the running schedule.

This displays the diff of ``can_frame_stream_io.py`` and 
``lin_frame_stream_io.py`` to demonstrate the changes required to
update CAN example code for LIN.

.. literalinclude:: ../../nixnet_examples/lin_frame_stream_io.py
	:diff: ../../nixnet_examples/can_frame_stream_io.py
