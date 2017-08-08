===========  =============================================================
Info         Communicate over CAN or LIN via NI-XNET hardware with Python.
Author       National Instruments
===========  =============================================================

.. image:: https://img.shields.io/pypi/v/nixnet.svg
    :target: https://pypi.python.org/pypi/nixnet
    :alt: PyPI

.. image:: https://readthedocs.org/projects/nixnet/badge/?version=latest
    :target: http://nixnet.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation

.. image:: https://img.shields.io/pypi/l/nixnet.svg
    :target: https://github.com/ni/nixnet-python/blob/master/LICENSE
    :alt: License

.. image:: https://img.shields.io/pypi/pyversions/nixnet.svg
    :target: https://pypi.python.org/pypi/nixnet
    :alt: Language versions

.. image:: https://travis-ci.org/ni/nixnet-python.svg?branch=master
    :target: https://travis-ci.org/ni/nixnet-python
    :alt: Build

.. image:: https://coveralls.io/repos/github/ni/nixnet-python/badge.svg?branch=master
    :target: https://coveralls.io/github/ni/nixnet-python?branch=master
    :alt: Unit-test Coverage

.. code-block:: python

   >>> import nixnet
   >>> with nixnet.FrameInStreamSession('CAN1') as input_session:
   >>>     input_session.intf.can_term = constants.CanTerm.ON
   >>>     input_session.intf.baud_rate = 125000

   >>>     frames = input_session.frames.read(count)
   >>>     for frame in frames:
   >>>         print('Received frame:')
   >>>         print(frame)

Quick Start
===========

Running **nixnet** requires NI-XNET or NI-XNET Runtime. Visit the
`ni.com/downloads <http://www.ni.com/downloads/>`_ to download the latest version
of NI-XNET.

**nixnet** can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nixnet

Now you should be able to move onto the `Examples <https://github.com/ni/nixnet-python/tree/master/nixnet_examples>`_.

Resources
=========

- `Documentation <http://nixnet.readthedocs.io>`_.
- `Source <https://github.com/ni/nixnet-python>`_.

Product Support
---------------

The **nixnet** package and NI-XNET are supported by NI. For support, open
a request through the NI support portal at `ni.com <http://www.ni.com>`_.

Bugs / Feature Requests
-----------------------

We welcome all kinds of contributions.  If you have a bug to report or a feature
request for **nixnet**, feel free to `open an issue on Github
<https://github.com/ni/nixnet-python/issues>`_ or `contribute the change yourself
<https://github.com/ni/nixnet-python/blob/master/CONTRIBUTING.rst>`_.

Status
======

**nixnet** is still early in its development with all the bugs, unimplemented
features, and API changes that go along with that.

The areas that are more mature include:

- ``FrameInStreamSession`` with reading and writing bytes, raw frames, and can frames.
- ``FrameOutStreamSession`` with writing bytes, raw frames, and can frames.
- ``FrameInQueuedSession`` with reading bytes, raw frames, and can frames.
- ``FrameOutQueuedSession`` with writing bytes, raw frames, and can frames.
- ``FrameInSinglePointSession`` with reading bytes, raw frames, and can frames.
- ``FrameOutSinglePointSession`` with writing bytes, raw frames, and can frames.
- ``SignalInSinglePointSession`` with reading values (timestamps are available but less mature).
- ``SignalOutSinglePointSession`` with writing values.

**nixnet** currently supports

- Windows operating system.
- CPython 2.7.7+, 3.4+, PyPy2, and PyPy3.

You can checkout the `issues page <https://github.com/ni/nixnet-python/issues>`_ for more details.

License
=======

**nixnet** is licensed under an MIT-style license (see
`LICENSE <https://github.com/ni/nixnet-python/blob/master/LICENSE>`__).
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.
