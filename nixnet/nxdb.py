from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

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


def deploy(
        ip_address,
        database_alias,
        wait_for_complete):
    return _funcs.nxdb_deploy(ip_address, database_alias, wait_for_complete)


def undeploy(
        ip_address,
        database_alias):
    _funcs.nxdb_undeploy(ip_address, database_alias)
