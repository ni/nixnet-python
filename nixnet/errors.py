from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import warnings

from nixnet import _enums

__all__ = ['XnetError', 'XnetWarning', 'XnetResourceWarning']


class Error(Exception):
    """Base error class for module."""
    pass


class XnetError(Error):
    """Error raised by any NI-XNET method."""
    def __init__(self, message, error_code):
        """Initialize error.

        Args:
            message (string): Specifies the error message.
            error_code (int): Specifies the NI-XNET error code.
        """
        super(XnetError, self).__init__(message)

        self._error_code = error_code

        try:
            self._error_type = _enums.Err(self._error_code)
        except ValueError:
            self._error_type = _enums.Err.INTERNAL_ERROR

    @property
    def error_code(self):
        """Error code reported by NI-XNET.

        int: Specifies the NI-XNET error code.
        """
        return self._error_code

    @property
    def error_type(self):
        """Error enum reported by NI-XNET.

        :class:`nixnet._enums.Err`: Specifies the NI-XNET
            error type.
        """
        return self._error_type


class XnetWarning(Warning):
    """Warning raised by any NI-XNET method."""
    def __init__(self, message, error_code):
        """Initialize warning.

        Args:
            message (string): Specifies the warning message.
            error_code (int): Specifies the NI-DAQmx error code.
        """
        super(XnetWarning, self).__init__(
            'Warning {0} occurred.\n\n{1}'.format(error_code, message))

        self._error_code = error_code

        try:
            self._error_type = _enums.Warn(self._error_code)
        except ValueError:
            self._error_type = _enums.Err.INTERNAL_ERROR

    @property
    def error_code(self):
        """Error code reported by NI-XNET.

        int: Specifies the NI-XNET error code.
        """
        return self._error_code

    @property
    def error_type(self):
        """Warning enum reported by NI-XNET.

        :class:`nixnet._enums.Warn`: Specifies the NI-XNET
            warning type.
        """
        return self._error_type


class _ResourceWarning(Warning):
    """Resource warning raised by any NI-XNET method.

    Used in place of built-in ResourceWarning to allow Python 2.7 support.
    """
    pass


# If ResourceWarning is in exceptions, it is also in the built-in namespace.
try:
    XnetResourceWarning = ResourceWarning
except NameError:
    XnetResourceWarning = _ResourceWarning

warnings.filterwarnings("always", category=XnetWarning)
warnings.filterwarnings("always", category=XnetResourceWarning)
