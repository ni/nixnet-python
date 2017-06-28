from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import _funcs


def create_object(
        parent_object_ref,
        object_class,
        object_name):
    return _funcs.nxdb_create_object(parent_object_ref, object_class, object_name)


def find_object(
        parent_object_ref,
        object_class,
        object_name):
    return _funcs.nxdb_find_object(parent_object_ref, object_class, object_name)


def delete_object(db_object_ref):
    _funcs.nxdb_delete_object(db_object_ref)


def add_alias64(
        database_alias,
        database_filepath,
        default_baud_rate):
    _funcs.nxdb_add_alias64(database_alias, database_filepath, default_baud_rate)


def remove_alias(
        database_alias):
    _funcs.nxdb_remove_alias(database_alias)


def deploy(
        ip_address,
        database_alias,
        wait_for_complete):
    return _funcs.nxdb_deploy(ip_address, database_alias, wait_for_complete)


def undeploy(
        ip_address,
        database_alias):
    _funcs.nxdb_undeploy(ip_address, database_alias)


def get_database_list(
        ip_address,
        size_of_alias_buffer,
        alias_buffer,
        size_of_filepath_buffer,
        filepath_buffer,
        number_of_databases):
    raise NotImplementedError("Placeholder")
