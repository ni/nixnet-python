from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


import ctypes  # type: ignore
import sys


class Error(Exception):
    pass


class PlatformUnsupportedError(Error):

    def __init__(self, platform):
        message = '{0} is unsupported by this package.'.format(platform)
        Error.__init__(self, message, platform)


class XnetNotFoundError(Error):

    def __init__(self, *args):
        message = (
            'Could not find an installation of NI-XNET. Please '
            'ensure that NI-XNET is installed on this machine or '
            'contact National Instruments for support.')
        Error.__init__(self, message, *args)


class XnetFunctionNotSupportedError(Error):

    def __init__(self, function):
        message = (
            'The NI-XNET function "{0}" is not supported in this '
            'version of NI-XNET. Visit ni.com/downloads to upgrade your '
            'version of NI-XNET.'.format(function))
        Error.__init__(self, message, function)


class XnetLibrary(object):
    """Proxy Library to consolidate nixnet-specific logic."""

    def __init__(self, library):
        self._library = library

    def __getattr__(self, function):
        try:
            return getattr(self._library, function)
        except AttributeError:
            raise XnetFunctionNotSupportedError(function)


def _import_win_lib(self):
    lib_name = "nixnet"
    try:
        cdll = ctypes.cdll.LoadLibrary(lib_name)
    except OSError:
        raise XnetNotFoundError()
    return XnetLibrary(cdll)


def _import_unsupported(self):
    raise PlatformUnsupportedError(sys.platform)


if sys.platform.startswith('win') or sys.platform.startswith('cli'):
    import_lib = _import_win_lib
else:
    import_lib = _import_unsupported
