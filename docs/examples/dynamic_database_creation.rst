Dynamic Database Creation
=========================

This example programmatically modifies the in-memory database to
contain a cluster, a frame, and two signals. The database is then
used in a :any:`nixnet.session.SignalOutSinglePointSession` and
:any:`nixnet.session.SignalInSinglePointSession` to write and then
read a pair of signals.

.. _can_dynamic_database_creation_label:

CAN Dynamic Database Creation
-----------------------------

.. literalinclude:: ../../nixnet_examples/can_dynamic_database_creation.py

.. _lin_dynamic_database_creation_label:

LIN Dynamic Database Creation
-----------------------------

.. literalinclude:: ../../nixnet_examples/lin_dynamic_database_creation.py
