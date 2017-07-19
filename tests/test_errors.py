from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import mock  # type: ignore

import pytest  # type: ignore

from nixnet import _cconsts
from nixnet import _cfuncs
from nixnet import _enums
from nixnet import _errors
from nixnet import errors


MockXnetLibrary = mock.create_autospec(_cfuncs.XnetLibrary, spec_set=True, instance=True)


@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
def test_success():
    _errors.check_for_error(_cconsts.NX_SUCCESS)


@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
def test_known_error():
    with pytest.raises(errors.XnetError) as excinfo:
        _errors.check_for_error(_enums.Err.SELF_TEST_ERROR1.value)
    assert excinfo.value.error_code == _enums.Err.SELF_TEST_ERROR1.value
    assert excinfo.value.error_type == _enums.Err.SELF_TEST_ERROR1
    assert excinfo.value.args == ('', )


@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
def test_unknown_error():
    error_code = -201232  # Arbitrary number
    # Ensure it is an unknown error
    with pytest.raises(ValueError):
        _enums.Err(error_code)

    with pytest.raises(errors.XnetError) as excinfo:
        _errors.check_for_error(error_code)
    assert excinfo.value.error_code == error_code
    assert excinfo.value.error_type == _enums.Err.INTERNAL_ERROR
    assert excinfo.value.args == ('', )


@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
def test_known_warning():
    with pytest.warns(errors.XnetWarning) as record:
        _errors.check_for_error(_enums.Warn.DATABASE_IMPORT.value)
    assert len(record) == 1
    assert record[0].message.error_code == _enums.Warn.DATABASE_IMPORT.value
    assert record[0].message.error_type == _enums.Warn.DATABASE_IMPORT
    assert record[0].message.args == ('Warning 1073098885 occurred.\n\n', )


@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
def test_unknown_warning():
    error_code = 201232  # Arbitrary number
    # Ensure it is an unknown error
    with pytest.raises(ValueError):
        _enums.Warn(error_code)

    with pytest.warns(errors.XnetWarning) as record:
        _errors.check_for_error(error_code)
    assert len(record) == 1
    assert record[0].message.error_code == error_code
    assert record[0].message.error_type is None
    assert record[0].message.args == ('Warning 201232 occurred.\n\n', )


@pytest.mark.integration
def test_driver_call():
    with pytest.raises(errors.XnetError) as excinfo:
        _errors.check_for_error(_enums.Err.SELF_TEST_ERROR1.value)
    assert excinfo.value.error_code == _enums.Err.SELF_TEST_ERROR1.value
    assert excinfo.value.error_type == _enums.Err.SELF_TEST_ERROR1
    assert excinfo.value.args == (
        'NI-XNET:  (Hex 0xBFF63002) Board self test failed(code 2). '
        'Solution: try reinstalling the driver or switching the slot(s) of the board(s). '
        'If the error persists,contact National Instruments.', )
