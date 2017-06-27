from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pprint
import six
import time

from nixnet import constants
from nixnet import nx


pp = pprint.PrettyPrinter(indent=4)


def main():
    database_name = ':memory:'
    cluster_name = ''
    list = ''
    interface1 = 'CAN1'
    interface2 = 'CAN2'
    input_mode = constants.CreateSessionMode.FRAME_IN_STREAM
    output_mode = constants.CreateSessionMode.FRAME_OUT_STREAM

    with nx.Session(database_name, cluster_name, list, interface1, input_mode) as input_session:
        print('Input session created successfully.')
        with nx.Session(database_name, cluster_name, list, interface2, output_mode) as output_session:
            print('Output session created successfully.')

            print('Are you using a terminated cable? Enter Y or N')
            terminated_cable = six.input()
            if terminated_cable.lower() == "y":
                output_session.intf_can_term = contants.CanTerm.OFF
            else:
                input_session.intf_can_term = contants.CanTerm.ON
                output_session.intf_can_term = contants.CanTerm.ON

            input_session.intf_baud_rate = 125000
            output_session.intf_baud_rate = 125000
            print('Properties set successfully.')

            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start(constants.StartStopScope.NORMAL)
            print('Input session started manually.')

            try:
                id = int(six.input('Enter identifier: '))
            except ValueError:
                print('Not a number')

            try:
                payloadList = [int(x) for x in six.input('Enter payload: ').split()]
            except ValueError:
                print('Not a number')

            payload = bytearray(payloadList)
            number_of_bytes_for_frames = len(payload)
            extended = False

            print('The same values should be received. Press q to quit')
            i = 0
            while true:
                for byte in payload:
                    byte = byte + i
                with CANFrame(identifier, extended, constants.FRAME_TYPE_CAN_DATA, payload) as frame:
                    output_session.write_frame(list(frame), number_of_bytes_for_frames, 10)
                    print('Sent frame with ID %s payload: %s' % (id, list(payload)))

                # Wait 100 ms and then read the received values.
                # They should be the same as the ones sent.
                time.sleep(0.1)

                count = constants.READ_ALL_AVAILABLE
                timeout = constants.TIMEOUT_NONE
                frames = input_session.read_frame(count, timeout)
                for frame in frames:
                    print('Received frame: ')
                    pp.pprint(frame)

                i += 1
                if max(payload) + i > 0xFF:
                    i = 0

                inp = six.input()
                if inp == 'q':
                    break

            print('Data acquisition stopped.')


if __name__ == '__main__':
    main()
