===========  =================================================================================================================================
Info         Contains a Python API for interacting with NI-XNET. See `GitHub <https://github.com/ni/nixnet-python/>`_ for the latest source.
Author       National Instruments
===========  =================================================================================================================================

.. image:: https://travis-ci.org/ni/nixnet-python.svg?branch=master
    :target: https://travis-ci.org/ni/nixnet-python
    :alt: Build

.. image:: https://pyup.io/repos/github/ni/nixnet-python/shield.svg
     :target: https://pyup.io/repos/github/ni/nixnet-python/
     :alt: Updates

About
=====

The **nixnet** package contains an API (Application Programming Interface) for
interacting with the NI-XNET driver in Python.  This package was created and is
supported by NI.

Some functions in the **nixnet** package may be unavailable with earlier
versions of the NI-XNET driver. Visit
`ni.com/downloads`_ to upgrade your version of
NI-XNET.

**nixnet** supports only the Windows operating system.

**nixnet** supports CPython 2.7, 3.4+, PyPy2, and PyPy3.

Installation
============

Running **nixnet** requires NI-XNET or NI-XNET Runtime. Visit the
`ni.com/downloads <http://www.ni.com/downloads/>`_ to download the latest version
of NI-XNET.

**nixnet** can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nixnet

Or **easy_install** from
`setuptools <http://pypi.python.org/pypi/setuptools>`_::

  $ python -m easy_install nixnet

You also can download the project source and run::

  $ python setup.py install

Support / Feedback
==================

The **nixnet** package is supported by NI. For support for **nixnet**, open
a request through the NI support portal at `ni.com <http://www.ni.com>`_.

Bugs / Feature Requests
=======================

To report a bug or submit a feature request, please use the
`GitHub issues page <https://github.com/ni/nixnet-python/issues>`_.

Documentation
=============

Documentation is available `here <http://nixnet-python.readthedocs.io>`_.

License
=======

**nixnet** is licensed under an MIT-style license (see
`LICENSE <https://github.com/ni/nixnet-python/blob/master/LICENSE>`__).
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.
