from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import copy
import mock  # type: ignore

import pytest  # type: ignore

from nixnet import _cfuncs
from nixnet import _ctypedefs

from nixnet_examples import can_frame_queued_io
from nixnet_examples import can_frame_stream_io
from nixnet_examples import can_signal_conversion
from nixnet_examples import can_signal_single_point_io
from nixnet_examples import lin_frame_stream_io
from nixnet_examples import programmatic_database_usage


MockXnetLibrary = mock.create_autospec(_cfuncs.XnetLibrary, spec_set=True, instance=True)
MockXnetLibrary.nx_create_session.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_set_property.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_get_property.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_start.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_write_frame.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_read_frame.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_write_signal_single_point.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_read_signal_single_point.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_write_state.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_convert_frames_to_signals_single_point.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_convert_signals_to_frames_single_point.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_stop.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_clear.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_system_open.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nxdb_add_alias64.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nxdb_remove_alias.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_system_close.return_value = _ctypedefs.u32(0)


def six_input(queue):
    # Leave `input_values` alone for easier debugging
    queue = copy.copy(queue)
    queue.reverse()

    def _six_input(prompt=""):
        value = queue.pop()
        return value

    return _six_input


@pytest.mark.parametrize("input_values", [
    ['y', '1, 2, 3', 'q'],
    ['n', '1, 2, 3', 'q'],
    ['invalid', '1, 2, 3', 'q'],
    ['y', 'invalid', 'q'],
    ['y', 'invalid'] + 0x100 * [''] + ['q'],
])
@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
@mock.patch('time.sleep', lambda time: None)
def test_can_frame_queued_empty_session(input_values):
    with mock.patch('six.moves.input', six_input(input_values)):
        can_frame_queued_io.main()


@pytest.mark.parametrize("input_values", [
    ['y', '1, 2, 3', 'q'],
    ['n', '1, 2, 3', 'q'],
    ['invalid', '1, 2, 3', 'q'],
    ['y', 'invalid', 'q'],
    ['y', 'invalid'] + 0x100 * [''] + ['q'],
])
@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
@mock.patch('time.sleep', lambda time: None)
def test_can_frame_stream_empty_session(input_values):
    with mock.patch('six.moves.input', six_input(input_values)):
        can_frame_stream_io.main()


@pytest.mark.parametrize("input_values", [
    ['y', '1, 2', 'q'],
    ['n', '1, 2', 'q'],
    ['invalid', '1, 2', 'q'],
    ['y', '1', 'q'],
    ['y', '1, 2, 3', 'q'],
    ['y', 'invalid', 'q'],
    ['y', 'invalid'] + 0x100 * [''] + ['q'],
])
@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
@mock.patch('time.sleep', lambda time: None)
def test_can_signal_single_point_empty_session(input_values):
    with mock.patch('six.moves.input', six_input(input_values)):
        can_signal_single_point_io.main()


@pytest.mark.parametrize("input_values", [
    ['1, 2'],
    ['1'],
    ['<invalid>'],
])
@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
@mock.patch('time.sleep', lambda time: None)
def test_can_signal_conversion_empty_session(input_values):
    with mock.patch('six.moves.input', six_input(input_values)):
        can_signal_conversion.main()


@pytest.mark.parametrize("input_values", [
    ['y', '1, 2, 3', 'q'],
    ['n', '1, 2, 3', 'q'],
    ['invalid', '1, 2, 3', 'q'],
    ['y', 'invalid', 'q'],
    ['y', 'invalid'] + 0x100 * [''] + ['q'],
])
@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
@mock.patch('time.sleep', lambda time: None)
def test_lin_frame_stream_empty_session(input_values):
    with mock.patch('six.moves.input', six_input(input_values)):
        lin_frame_stream_io.main()


@pytest.mark.parametrize("input_values", [
    ['y', '1, 2'],
    ['n', '1, 2'],
    ['y', 'invalid'],
    ['invalid', 'invalid'],
])
@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
@mock.patch('time.sleep', lambda time: None)
def test_programmatic_database_usage(input_values):
    with mock.patch('six.moves.input', six_input(input_values)):
        programmatic_database_usage.main()
