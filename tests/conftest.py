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
