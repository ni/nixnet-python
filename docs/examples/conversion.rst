Signal/Frame Conversion Example
===============================

This example uses :any:`nixnet.convert.SignalConversionSinglePointSession` to
take signal values from the user, converts them to frames, and converts them back.

To adapt this example to LIN frames, reference signals in a database that use LIN:
   ``convert_frames_to_signals``:
      Accepts any frame type.
   ``convert_signals_to_frames``:
      Chooses the frame object to create based on the ``frame_type`` field in
      the raw data.  This can be overridden by passing a custom
      :any:`nixnet.types.FrameFactory` in the ``frame_type`` parameter.

.. literalinclude:: ../../nixnet_examples/can_signal_conversion.py
   :pyobject: main
