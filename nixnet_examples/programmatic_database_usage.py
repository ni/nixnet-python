from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import six

import nixnet
from nixnet import constants
from nixnet.system import system
from nixnet import types


def main():
    with system.System() as my_system:
        database_alias = 'custom_database'
        database_filepath = os.path.join(os.path.dirname(__file__), 'nixnet_examples\databases\custom_database.dbc')
        default_baud_rate = 500000
        my_system.databases.add_alias(database_alias, database_filepath, default_baud_rate)

    database_name = 'custom_database'
    cluster_name = 'CAN_Cluster'
    output_frame = 'CANEventFrame1'
    interface = 'CAN1'

    with nixnet.FrameOutQueuedSession(
            interface,
            database_name,
            cluster_name,
            output_frame) as output_session:
        terminated_cable = six.moves.input('Are you using a terminated cable (Y or N)? ')
        if terminated_cable.lower() == "y":
            output_session.intf.can_term = constants.CanTerm.OFF
        elif terminated_cable.lower() == "n":
            output_session.intf.can_term = constants.CanTerm.ON
        else:
            print("Unrecognised input ({}), assuming 'n'".format(terminated_cable))
            output_session.intf.can_term = constants.CanTerm.ON

        user_value = six.moves.input('Enter payload [int, int]: ')
        try:
            payload_list = [int(x.strip()) for x in user_value.split(",")]
        except ValueError:
            payload_list = [2, 4, 8, 16]
            print('Unrecognized input ({}). Setting data buffer to {}'.format(user_value, payload_list))

        id = types.CanIdentifier(0)
        payload = bytearray(payload_list)
        frame = types.CanFrame(id, constants.FrameType.CAN_DATA, payload)

        print("Writing CAN frames using {} alias:".format(database_name))

        i = 0
        while i < 3:
            for index, byte in enumerate(payload):
                payload[index] = byte + i

            frame.payload = payload
            output_session.frames.write([frame])
            print('Sent frame with ID %s payload: %s' % (id, payload))
            i += 1

    with system.System() as my_system:
        del my_system.databases[database_name]

if __name__ == '__main__':
    main()
