from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pprint
import six
import time

from nixnet import constants
from nixnet import nx
from nixnet import types


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
        with nx.Session(database_name, cluster_name, list, interface2, output_mode) as output_session:
            print('Are you using a terminated cable? Enter Y or N')
            terminated_cable = six.moves.input()
            if terminated_cable.lower() == "y":
                output_session.intf_can_term = constants.CanTerm.OFF
                input_session.intf_can_term = constants.CanTerm.ON
            elif terminated_cable.lower() == "n":
                input_session.intf_can_term = constants.CanTerm.ON
                output_session.intf_can_term = constants.CanTerm.ON
            else:
                print("Unrecognised input ({}), assuming 'n'".format(terminated_cable))
                input_session.intf_can_term = constants.CanTerm.ON
                output_session.intf_can_term = constants.CanTerm.ON

            input_session.intf_baud_rate = 125000
            output_session.intf_baud_rate = 125000

            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start(constants.StartStopScope.NORMAL)

            user_value = six.moves.input('Enter payload [int, int]: ')
            try:
                payload_list = [int(x.strip()) for x in user_value.split(",")]
            except ValueError:
                payload_list = [2, 4, 8, 16]
                print('Unrecognized input ({}). Setting data buffer to {}', user_value, payload_list)

            id = 0
            extended = False
            payload = bytearray(payload_list)
            frame = types.CanFrame(id, extended, constants.FrameType.CAN_DATA, payload)
            write_timeout = 10

            print('The same values should be received. Press q to quit')
            i = 0
            while True:
                for index, byte in enumerate(payload):
                    payload[index] = byte + i

                frame.payload = payload
                output_session.write_can_frame([frame], write_timeout)
                print('Sent frame with ID %s payload: %s' % (id, payload))

                # Wait 1 s and then read the received values.
                # They should be the same as the ones sent.
                time.sleep(1)

                count = 1
                read_timeout = constants.TIMEOUT_NONE
                frames = input_session.read_can_frame(count, read_timeout)
                for frame in frames:
                    print('Received frame: ')
                    pp.pprint(frame)

                i += 1
                if max(payload) + i > 0xFF:
                    i = 0

                inp = six.moves.input()
                if inp == 'q':
                    break

            print('Data acquisition stopped.')


if __name__ == '__main__':
    main()
