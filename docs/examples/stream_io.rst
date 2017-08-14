Stream I/O Example
==================

This example uses :any:`nixnet.session.FrameInStreamSession` and
:any:`nixnet.session.FrameOutStreamSession` to demonstrate how streamed sessions
work.

CAN Stream I/O
--------------

.. literalinclude:: ../../nixnet_examples/can_frame_stream_io.py

LIN Stream I/O
--------------

.. literalinclude:: ../../nixnet_examples/lin_frame_stream_io.py

Refer to :doc:`can_lin_diff` for how to adapt from CAN to LIN.