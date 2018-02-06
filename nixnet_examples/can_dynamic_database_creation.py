from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from random import randint
import six
import time

import nixnet
from nixnet import constants
from nixnet import database


def main():
    database_name = ':CAN_Database:'
    cluster_name = 'CAN_Cluster'
    frame_name = 'CAN_Event_Frame'
    signal_1_name = 'CAN_Event_Signal_1'
    signal_2_name = 'CAN_Event_Signal_2'
    signal_list = [signal_1_name, signal_2_name]
    output_interface = 'CAN1'
    input_interface = 'CAN2'

    # Open an in-memory database.
    with database.Database(database_name) as db:

        # Add a CAN cluster, a frame, and two signals to the database.
        cluster = db.clusters.add(cluster_name)
        cluster.protocol = constants.Protocol.CAN
        cluster.baud_rate = 125000
        frame = cluster.frames.add(frame_name)
        frame.id = 1
        frame.payload_len = 2
        signal_1 = frame.mux_static_signals.add(signal_1_name)
        signal_1.byte_ordr = constants.SigByteOrdr.BIG_ENDIAN
        signal_1.data_type = constants.SigDataType.UNSIGNED
        signal_1.start_bit = 0
        signal_1.num_bits = 8
        signal_2 = frame.mux_static_signals.add(signal_2_name)
        signal_2.byte_ordr = constants.SigByteOrdr.BIG_ENDIAN
        signal_2.data_type = constants.SigDataType.UNSIGNED
        signal_2.start_bit = 8
        signal_2.num_bits = 8

        # Using the database we just created, write and then read a pair of signals.
        with nixnet.SignalOutSinglePointSession(
                output_interface,
                database_name,
                cluster_name,
                signal_list) as output_session:
            with nixnet.SignalInSinglePointSession(
                    input_interface,
                    database_name,
                    cluster_name,
                    signal_list) as input_session:
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
                # signal values sent before the initial read will be received.
                input_session.start()

                # Generate a pair of random values and send out the signals.
                output_values = [randint(0, 255), randint(0, 255)]
                output_session.signals.write(output_values)
                print('Sent signal values: {}'.format(output_values))

                # Wait 1 s and then read the received values.
                # They should be the same as the ones sent.
                time.sleep(1)

                input_signals = input_session.signals.read()
                input_values = [int(value) for timestamp, value in input_signals]
                print('Received signal values: {}'.format(input_values))


if __name__ == '__main__':
    main()
