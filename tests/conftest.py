from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def pytest_addoption(parser):
    parser.addoption(
        "--nixnet-out-interface", default="CAN1",
        action="store",
        help="The NI-XNET interface to use with the tests")
    parser.addoption(
        "--nixnet-in-interface", default="CAN2",
        action="store",
        help="The NI-XNET interface to use with the tests")
