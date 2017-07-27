from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest  # type: ignore

from nixnet import _lib


def test_unsupported_platform():
    """Hard to make this a good test, so at least verifying the error reporting.

    For now, we'll just verify the calls don't call catastrophically fail and
    someone can always run py.test with ``-s``_.
    """
    with pytest.raises(_lib.PlatformUnsupportedError) as excinfo:
        _lib._import_unsupported()
    print(excinfo.value.args)


def test_function_not_supported():
    """Hard to make this a good test, so at least verifying the error reporting.

    For now, we'll just verify the calls don't call catastrophically fail and
    someone can always run py.test with ``-s``_.
    """
    ctypes_mock = object()
    lib = _lib.XnetLibrary(ctypes_mock)
    with pytest.raises(_lib.XnetFunctionNotSupportedError) as excinfo:
        lib.strange_and_unusual_funcion
    print(excinfo.value.args)
