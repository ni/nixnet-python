from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pprint

import six

from nixnet import constants
from nixnet import nx


pp = pprint.PrettyPrinter(indent=4)


def main():
    database_name = ':memory:'
    cluster_name = ''
    list = ''
    interface = 'CAN2'
    mode = constants.CreateSessionMode.FRAME_IN_STREAM

    with nx.Session(database_name, cluster_name, list, interface, mode) as session:
        session.intf_baud_rate = 125000

        print('Logging all received frames. Press q to quit')
        while True:
            count = 250
            timeout = constants.TIMEOUT_NONE
            frames = session.read_frame(count, timeout)

            for frame in frames:
                pp.pprint(frame)

            inp = six.input()
            if inp == 'q':
                break

        print('Data acquisition stopped.')


if __name__ == '__main__':
    main()
