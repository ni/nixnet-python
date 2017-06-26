from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


def open_database(
        database_name,
        database_ref):
    raise NotImplementedError("Placeholder")


def close_database(
        database_ref,
        close_all_refs):
    raise NotImplementedError("Placeholder")


def create_object(
        parent_object_ref,
        object_class,
        object_name,
        db_object_ref):
    raise NotImplementedError("Placeholder")


def find_object(
        parent_object_ref,
        object_class,
        object_name,
        db_object_ref):
    raise NotImplementedError("Placeholder")


def delete_object(
        db_object_ref):
    raise NotImplementedError("Placeholder")


def save_database(
        database_ref,
        db_filepath):
    raise NotImplementedError("Placeholder")


def get_property(
        db_object_ref,
        property_id,
        property_size,
        property_value):
    raise NotImplementedError("Placeholder")


def get_property_size(
        db_object_ref,
        property_id,
        property_size):
    raise NotImplementedError("Placeholder")


def set_property(
        db_object_ref,
        property_id,
        property_size,
        property_value):
    raise NotImplementedError("Placeholder")


def get_dbc_attribute_size(
        db_object_ref,
        mode,
        attribute_name,
        attribute_text_size):
    raise NotImplementedError("Placeholder")


def get_dbc_attribute(
        db_object_ref,
        mode,
        attribute_name,
        attribute_text_size,
        attribute_text,
        is_default):
    raise NotImplementedError("Placeholder")


def merge(
        target_cluster_ref,
        source_obj_ref,
        copy_mode,
        prefix,
        wait_for_complete,
        percent_complete):
    raise NotImplementedError("Placeholder")


def add_alias(
        database_alias,
        database_filepath,
        default_baud_rate):
    raise NotImplementedError("Placeholder")


def add_alias64(
        database_alias,
        database_filepath,
        default_baud_rate):
    raise NotImplementedError("Placeholder")


def remove_alias(
        database_alias):
    raise NotImplementedError("Placeholder")


def deploy(
        ip_address,
        database_alias,
        wait_for_complete,
        percent_complete):
    raise NotImplementedError("Placeholder")


def undeploy(
        ip_address,
        database_alias):
    raise NotImplementedError("Placeholder")


def get_database_list(
        ip_address,
        size_of_alias_buffer,
        alias_buffer,
        size_of_filepath_buffer,
        filepath_buffer,
        number_of_databases):
    raise NotImplementedError("Placeholder")


def get_database_list_sizes(
        ip_address,
        sizeof_alias_buffer,
        sizeof_filepath_buffer):
    raise NotImplementedError("Placeholder")
