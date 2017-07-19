from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import mock  # type: ignore

from nixnet import _cfuncs
from nixnet import _ctypedefs

from nixnet_examples import can_frame_queued_io
from nixnet_examples import can_frame_stream_io
from nixnet_examples import can_signal_single_point_io


MockXnetLibrary = mock.create_autospec(_cfuncs.XnetLibrary, spec_set=True, instance=True)
MockXnetLibrary.nx_create_session.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_set_property.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_get_property.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_start.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_write_frame.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_read_frame.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_write_signal_single_point.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_read_signal_single_point.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_stop.return_value = _ctypedefs.u32(0)
MockXnetLibrary.nx_clear.return_value = _ctypedefs.u32(0)


def six_input(queue):
    queue.reverse()

    def _six_input(prompt=""):
        value = queue.pop()
        return value

    return _six_input


@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
@mock.patch('six.moves.input', six_input(['y', '1, 2, 3', 'q']))
@mock.patch('time.sleep', lambda time: None)
def test_can_frame_queued_empty_session():
    can_frame_queued_io.main()


@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
@mock.patch('six.moves.input', six_input(['y', '1, 2, 3', 'q']))
@mock.patch('time.sleep', lambda time: None)
def test_can_frame_stream_empty_session():
    can_frame_stream_io.main()


@mock.patch('nixnet._cfuncs.lib', MockXnetLibrary)
@mock.patch('six.moves.input', six_input(['y', '1, 2', 'q']))
@mock.patch('time.sleep', lambda time: None)
def test_can_signal_single_point_empty_session():
    can_signal_single_point_io.main()
