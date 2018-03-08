from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import ctypes  # type: ignore
import warnings

from nixnet import _cconsts
from nixnet import _cfuncs
from nixnet import _ctypedefs
from nixnet import errors


def check_for_error(error_code):
    if error_code & _cconsts.NX_STATUS_ERROR:
        status = status_to_string(error_code)
        raise errors.XnetError(status, error_code)
    elif error_code != _cconsts.NX_SUCCESS:
        status = status_to_string(error_code)
        warnings.warn(errors.XnetWarning(status, error_code))


def status_to_string(status_code):
    buffer_size = 2048
    buffer_size_ctypes = _ctypedefs.u32(buffer_size)
    buffer_ctypes = ctypes.create_string_buffer(buffer_size)
    status_code_ctypes = _ctypedefs.nxStatus_t(status_code)
    _cfuncs.lib.nx_status_to_string(status_code_ctypes, buffer_size_ctypes, buffer_ctypes)
    status_string = buffer_ctypes.value.decode("ascii")
    return status_string
