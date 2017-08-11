from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def pytest_addoption(parser):
    parser.addoption(
        "--can-out-interface", default="CAN1",
        action="store",
        help="The CAN interface to use with the tests")
    parser.addoption(
        "--can-in-interface", default="CAN2",
        action="store",
        help="The CAN interface to use with the tests")
    parser.addoption(
        "--lin-out-interface", default="LIN1",
        action="store",
        help="The LIN interface to use with the tests")
    parser.addoption(
        "--lin-in-interface", default="LIN2",
        action="store",
        help="The LIN interface to use with the tests")
