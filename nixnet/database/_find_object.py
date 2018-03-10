from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import typing  # NOQA: F401

from nixnet import _cconsts
from nixnet import _errors
from nixnet import _funcs
from nixnet import constants
from nixnet.database import _database_object  # NOQA: F401


def find_object(
        parent_handle,  # type: int
        object_class,  # type: typing.Any
        object_name,  # type: typing.Text
):
    # type: (...) -> _database_object.DatabaseObject
    from nixnet.database._cluster import Cluster
    from nixnet.database._ecu import Ecu
    from nixnet.database._frame import Frame
    from nixnet.database._lin_sched import LinSched
    from nixnet.database._lin_sched_entry import LinSchedEntry
    from nixnet.database._pdu import Pdu
    from nixnet.database._signal import Signal
    from nixnet.database._subframe import SubFrame

    class_enum = {
        Cluster: constants.ObjectClass.CLUSTER,
        Ecu: constants.ObjectClass.ECU,
        Frame: constants.ObjectClass.FRAME,
        LinSched: constants.ObjectClass.LIN_SCHED,
        LinSchedEntry: constants.ObjectClass.LIN_SCHED_ENTRY,
        Pdu: constants.ObjectClass.PDU,
        Signal: constants.ObjectClass.SIGNAL,
        SubFrame: constants.ObjectClass.SUBFRAME,
    }.get(object_class)

    if class_enum is None:
        raise ValueError("Unsupported value provided for argument object_class.", object_class)

    found_handle = _funcs.nxdb_find_object(parent_handle, class_enum, object_name)
    if found_handle == 0:
        _errors.raise_xnet_error(_cconsts.NX_ERR_DATABASE_OBJECT_NOT_FOUND)

    return object_class(_handle=found_handle)
