from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

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
            message(str): Error message.
            error_code(int): NI-XNET error code.
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
        """int: Error code reported by NI-XNET."""
        return self._error_code

    @property
    def error_type(self):
        # type: (...) -> _enums.Err
        """:any:`nixnet._enums.Err`: Error type reported by NI-XNET."""
        return self._error_type


class XnetWarning(Warning):
    """Warning raised by any NI-XNET method."""
    def __init__(
        self,
        message,  # type: typing.Text
        warning_code,  # type: int
    ):
        # type: (...) -> None
        """Initialize warning.

        Args:
            message(str): Warning message.
            warning_code(int): NI-XNET warning code.
        """
        super(XnetWarning, self).__init__(
            'Warning {0} occurred.\n\n{1}'.format(warning_code, message))

        self._warning_code = warning_code

        try:
            self._warning_type = _enums.Warn(self._warning_code)
        except ValueError:
            self._warning_type = None

    @property
    def warning_code(self):
        # type: (...) -> int
        """int: Warning code reported by NI-XNET."""
        return self._warning_code

    @property
    def warning_type(self):
        # type: (...) -> _enums.Warn
        """:any:`nixnet._enums.Warn`: Warning type reported by NI-XNET."""
        return self._warning_type


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
