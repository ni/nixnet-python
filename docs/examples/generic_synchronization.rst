Generic Synchronization Example
===============================

This example demonstrates how to synchronize two :any:`nixnet.session.FrameInStreamSession`
session types on different interfaces.

These principles can be extended to any session type and quantity.
Sessions are created, configured, and started for each interface sequentially.

The interfaces that will listen for a clock should be created and configured first.
Interface properties need only be set once per interface. The connect_terminals function
acts like an interface property and needs to be set only once per interface. Listening
sessions can then be started with the "Session Only" scope. The last session to be started
on a particul interface can be started with the normal scope which will cause it to start
listening for a start trigger.

The interface that will drive the master timebase clock should be created and configured
last. The master timebase is configured to be output via connect_terminals and then the
interface can be started with normal scope.

Generic Synchronization
-----------------------

.. literalinclude:: ../../nixnet_examples/generic_synchronization.py
   :pyobject: main