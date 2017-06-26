from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import typing

from nixnet import _ctypedefs
from nixnet import _enums


def nx_create_session(
        database_name: typing.Text,
        cluster_name: typing.Text,
        list: typing.Text,
        interface: typing.Text,
        mode: _enums.CreateSessionMode) -> _ctypedefs.nxSessionRef_t:
    ...


def nx_create_session_by_ref(
        database_refs: typing.List[_ctypedefs.nxDatabaseRef_t],
        interface: typing.Text,
        mode: _enums.CreateSessionMode) -> _ctypedefs.nxSessionRef_t:
    ...


def nx_get_property_size(
        session_ref: _ctypedefs.nxSessionRef_t,
        property_id: int) -> int:
    ...


def nx_get_sub_property_size(
        session_ref: _ctypedefs.nxSessionRef_t,
        active_index: int,
        property_id: int) -> int:
    ...


def nx_read_signal_single_point(
        session_ref: _ctypedefs.nxSessionRef_t) -> typing.Tuple[typing.List[float], typing.List[int]]:
    ...


def nx_read_signal_waveform(
        session_ref: _ctypedefs.nxSessionRef_t,
        timeout: float) -> typing.Tuple[int, float, typing.List[float], int]:
    ...


def nx_read_signal_xy(
        session_ref: _ctypedefs.nxSessionRef_t,
        time_limit: int) -> typing.Tuple[typing.List[float], typing.List[int], typing.List[int]]:
    ...


def nx_write_signal_single_point(
        session_ref: _ctypedefs.nxSessionRef_t,
        value_buffer: typing.List[float]) -> None:
    ...


def nx_write_signal_waveform(
        session_ref: _ctypedefs.nxSessionRef_t,
        timeout: float,
        value_buffer: typing.List[float]) -> None:
    ...


def nx_write_signal_xy(
        session_ref: _ctypedefs.nxSessionRef_t,
        timeout: float,
        value_buffer: typing.List[float],
        timestamp_buffer: typing.List[int],
        num_pairs_buffer: typing.List[int]) -> None:
    ...


def nx_blink(
        interface_ref: _ctypedefs.nxSessionRef_t,
        modifier: _enums.BlinkMode) -> None:
    ...


def nx_clear(
        session_ref: _ctypedefs.nxSessionRef_t) -> None:
    ...


def nx_connect_terminals(
        session_ref: _ctypedefs.nxSessionRef_t,
        source: typing.Text,
        destination: typing.Text) -> None:
    ...


def nx_disconnect_terminals(
        session_ref: _ctypedefs.nxSessionRef_t,
        source: typing.Text,
        destination: typing.Text) -> None:
    ...


def nx_flush(
        session_ref: _ctypedefs.nxSessionRef_t) -> None:
    ...


def nx_start(
        session_ref: _ctypedefs.nxSessionRef_t,
        scope: _enums.StartStopScope) -> None:
    ...


def nx_stop(
        session_ref: _ctypedefs.nxSessionRef_t,
        scope: _enums.StartStopScope) -> None:
    ...


def nx_status_to_string(
        status: typing.Any) -> typing.Any:
    ...


def nx_system_open() -> _ctypedefs.nxSessionRef_t:
    ...


def nx_system_close(
        system_ref: _ctypedefs.nxSessionRef_t) -> None:
    ...


def nx_wait(
        session_ref: _ctypedefs.nxSessionRef_t,
        condition: int,
        param_in: int,
        timeout: float) -> int:
    ...


def nxdb_open_database(
        database_name: typing.Text) -> _ctypedefs.nxDatabaseRef_t:
    ...


def nxdb_close_database(
        database_ref: _ctypedefs.nxDatabaseRef_t,
        close_all_refs: bool) -> None:
    ...


def nxdb_create_object(
        parent_object_ref: _ctypedefs.nxDatabaseRef_t,
        object_class: _enums.ObjectClass,
        object_name: typing.Text) -> _ctypedefs.nxDatabaseRef_t:
    ...


def nxdb_find_object(
        parent_object_ref: _ctypedefs.nxDatabaseRef_t,
        object_class: _enums.ObjectClass,
        object_name: typing.Text) -> _ctypedefs.nxDatabaseRef_t:
    ...


def nxdb_delete_object(
        db_object_ref: _ctypedefs.nxDatabaseRef_t) -> None:
    ...


def nxdb_save_database(
        database_ref: _ctypedefs.nxDatabaseRef_t,
        db_filepath: typing.Text) -> None:
    ...


def nxdb_get_property_size(
        db_object_ref: _ctypedefs.nxDatabaseRef_t,
        property_id: int) -> int:
    ...


def nxdb_get_dbc_attribute_size(
        db_object_ref: _ctypedefs.nxDatabaseRef_t,
        mode: int,
        attribute_name: typing.Text) -> int:
    ...


def nxdb_get_dbc_attribute(
        db_object_ref: _ctypedefs.nxDatabaseRef_t,
        mode: int,
        attribute_name: typing.Text,
        attribute_text_size: int,
        attribute_text: typing.Text) -> int:
    ...


def nxdb_merge(
        target_cluster_ref: _ctypedefs.nxDatabaseRef_t,
        source_obj_ref: _ctypedefs.nxDatabaseRef_t,
        copy_mode: int,
        prefix: typing.Text,
        wait_for_complete: bool) -> int:
    ...


def nxdb_add_alias(
        database_alias: typing.Text,
        database_filepath: typing.Text,
        default_baud_rate: int) -> None:
    ...


def nxdb_add_alias64(
        database_alias: typing.Text,
        database_filepath: typing.Text,
        default_baud_rate: int) -> None:
    ...


def nxdb_remove_alias(
        database_alias: typing.Text) -> None:
    ...


def nxdb_deploy(
        ip_address: typing.Text,
        database_alias: typing.Text,
        wait_for_complete: bool) -> int:
    ...


def nxdb_undeploy(
        ip_address: typing.Text,
        database_alias: typing.Text) -> None:
    ...


def nxdb_get_database_list(
        ip_address: typing.Text) -> typing.Any:
    ...


