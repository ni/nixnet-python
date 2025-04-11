from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import pytest  # type: ignore


def pytest_addoption(parser):
    parser.addoption(
        "--can-out-interface", default="None",
        action="store",
        help="The CAN interface to use with the tests")
    parser.addoption(
        "--can-in-interface", default="None",
        action="store",
        help="The CAN interface to use with the tests")
    parser.addoption(
        "--lin-out-interface", default="None",
        action="store",
        help="The LIN interface to use with the tests")
    parser.addoption(
        "--lin-in-interface", default="None",
        action="store",
        help="The LIN interface to use with the tests")


@pytest.fixture
def can_in_interface(request):
    interface = request.config.getoption("--can-in-interface")
    if interface.lower() == "none":
        pytest.skip("Test requires a CAN board")
    return interface


@pytest.fixture
def can_out_interface(request):
    interface = request.config.getoption("--can-out-interface")
    if interface.lower() == "none":
        pytest.skip("Test requires a CAN board")
    return interface


@pytest.fixture
def lin_in_interface(request):
    interface = request.config.getoption("--lin-in-interface")
    if interface.lower() == "none":
        pytest.skip("Test requires a LIN board")
    return interface


@pytest.fixture
def lin_out_interface(request):
    interface = request.config.getoption("--lin-out-interface")
    if interface.lower() == "none":
        pytest.skip("Test requires a LIN board")
    return interface


@pytest.fixture
def custom_database_path():
    tests_path = os.path.dirname(__file__)
    root_path = os.path.dirname(tests_path)
    database_path = os.path.join(root_path, 'nixnet_examples', 'databases', 'custom_database.dbc')
    return database_path
