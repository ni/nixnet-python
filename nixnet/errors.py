from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import typing  # NOQA: F401
import warnings

from nixnet import _enums

__all__ = ['XnetError', 'XnetWarning', 'XnetResourceWarning']


class Error(Exception):
    """Base error class for module."""
    pass


class XnetError(Error):
    """Error raised by any NI-XNET method."""
    def __init__(
        self,
        message,  # type: typing.Text
        error_code,  # type: int
    ):
        # type: (...) -> None
        """Initialize error.

        Args:
            message: A string specifing the error message.
            error_code: An integer specifing the NI-XNET error code.
        """
        super(XnetError, self).__init__(message)

        self._error_code = error_code

        try:
            self._error_type = _enums.Err(self._error_code)
        except ValueError:
            self._error_type = _enums.Err.INTERNAL_ERROR

    @property
    def error_code(self):
        # type: (...) -> int
        """Error code reported by NI-XNET.

        Returns:
            An integer specifing the NI-XNET error code.
        """
        return self._error_code

    @property
    def error_type(self):
        # type: (...) -> _enums.Err
        """Error enum reported by NI-XNET.

        Returns:
            A :any:`nixnet._enums.Err` specifing the NI-XNET error type.
        """
        return self._error_type


class XnetWarning(Warning):
    """Warning raised by any NI-XNET method."""
    def __init__(
        self,
        message,  # type: typing.Text
        error_code,  # type: int
    ):
        # type: (...) -> None
        """Initialize warning.

        Args:
            message: A string specifing the warning message.
            error_code: An integer specifing the NI-DAQmx error code.
        """
        super(XnetWarning, self).__init__(
            'Warning {0} occurred.\n\n{1}'.format(error_code, message))

        self._error_code = error_code

        try:
            self._error_type = _enums.Warn(self._error_code)
        except ValueError:
            self._error_type = None

    @property
    def error_code(self):
        # type: (...) -> int
        """Error code reported by NI-XNET.

        Returns:
            An integer specifing the NI-XNET error code.
        """
        return self._error_code

    @property
    def error_type(self):
        # type: (...) -> _enums.Warn
        """Warning enum reported by NI-XNET.

        Returns:
            A :any:`nixnet._enums.Warn` specifiing the NI-XNET warning type.
        """
        return self._error_type


class _ResourceWarning(Warning):
    """Resource warning raised by any NI-XNET method.

    Used in place of built-in ResourceWarning to allow Python 2.7 support.
    """
    pass


# If ResourceWarning is in exceptions, it is also in the built-in namespace.
try:
    XnetResourceWarning = ResourceWarning  # type: typing.Type[Warning]
except NameError:
    XnetResourceWarning = _ResourceWarning  # type: ignore

warnings.filterwarnings("always", category=XnetWarning)
warnings.filterwarnings("always", category=XnetResourceWarning)
