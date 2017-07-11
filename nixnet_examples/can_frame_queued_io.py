from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pprint
import six
import time

import nixnet
from nixnet import constants
from nixnet import types


pp = pprint.PrettyPrinter(indent=4)


def main():
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    input_frame = 'CANEventFrame1'
    output_frame = 'CANEventFrame1'
    interface1 = 'CAN1'
    interface2 = 'CAN2'

    with nixnet.FrameInQueuedSession(
            interface1,
            database_name,
            cluster_name,
            input_frame) as input_session:
        with nixnet.FrameOutQueuedSession(
                interface2,
                database_name,
                cluster_name,
                output_frame) as output_session:
            terminated_cable = six.moves.input('Are you using a terminated cable (Y or N)? ')
            if terminated_cable.lower() == "y":
                input_session.intf.can_term = constants.CanTerm.ON
                output_session.intf.can_term = constants.CanTerm.OFF
            elif terminated_cable.lower() == "n":
                input_session.intf.can_term = constants.CanTerm.ON
                output_session.intf.can_term = constants.CanTerm.ON
            else:
                print("Unrecognised input ({}), assuming 'n'".format(terminated_cable))
                input_session.intf.can_term = constants.CanTerm.ON
                output_session.intf.can_term = constants.CanTerm.ON

            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start()

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

            i = 0
            while True:
                for index, byte in enumerate(payload):
                    payload[index] = byte + i

                frame.payload = payload
                output_session.frames.write_can([frame])
                print('Sent frame with ID %s payload: %s' % (id, payload))

                # Wait 1 s and then read the received values.
                # They should be the same as the ones sent.
                time.sleep(1)

                count = 1
                frames = input_session.frames.read_can(count)
                for frame in frames:
                    print('Received frame: ')
                    pp.pprint(frame)

                i += 1
                if max(payload) + i > 0xFF:
                    i = 0

                inp = six.moves.input('Hit enter to continue (q to quit): ')
                if inp.lower() == 'q':
                    break

            print('Data acquisition stopped.')


if __name__ == '__main__':
    main()
