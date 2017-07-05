from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes  # type: ignore
import warnings

from nixnet import _cconsts
from nixnet import _cfuncs
from nixnet import errors


def check_for_error(error_code):
    if error_code & _cconsts.NX_STATUS_ERROR:
        buffer_size = 2048
        error_buffer = ctypes.create_string_buffer(buffer_size)

        _cfuncs.lib.nx_status_to_string(error_code, buffer_size, error_buffer)

        raise errors.XnetError(error_buffer.value.decode("ascii"), error_code)
    elif error_code != _cconsts.NX_SUCCESS:
        buffer_size = 2048
        error_buffer = ctypes.create_string_buffer(buffer_size)

        _cfuncs.lib.nx_status_to_string(error_code, buffer_size, error_buffer)

        warnings.warn(errors.XnetWarning(
            error_buffer.value.decode("ascii"), error_code))
