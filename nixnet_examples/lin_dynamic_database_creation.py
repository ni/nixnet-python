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
    database_name = ':memory:'
    cluster_name = 'LIN_Cluster'
    ecu_1_name = 'LIN_ECU_1'
    ecu_2_name = 'LIN_ECU_2'
    schedule_name = 'LIN_Schedule_1'
    schedule_entry_name = 'LIN_Schedule_Entry'
    frame_name = 'LIN_Frame'
    signal_1_name = 'LIN_Signal_1'
    signal_2_name = 'LIN_Signal_2'
    signal_list = [signal_1_name, signal_2_name]
    output_interface = 'LIN1'
    input_interface = 'LIN2'

    # Open the default in-memory database.
    # Database.close will be called by Database.__exit__ when exiting the 'with' block.
    with database.Database(database_name) as db:

        # Add a LIN cluster, a frame, and two signals to the database.
        cluster = db.clusters.add(cluster_name)
        cluster.protocol = constants.Protocol.LIN
        cluster.baud_rate = 19200
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

        # Add a LIN ECU and LIN Schedule to the cluster.
        ecu_1 = cluster.ecus.add(ecu_1_name)
        ecu_1.lin_protocol_ver = constants.LinProtocolVer.VER_2_2
        ecu_1.lin_master = True
        ecu_2 = cluster.ecus.add(ecu_2_name)
        ecu_2.lin_protocol_ver = constants.LinProtocolVer.VER_2_2
        ecu_2.lin_master = False
        cluster.lin_tick = 0.01
        schedule = cluster.lin_schedules.add(schedule_name)
        schedule.priority = 0
        schedule.run_mode = constants.LinSchedRunMode.CONTINUOUS
        schedule_entry = schedule.entries.add(schedule_entry_name)
        schedule_entry.delay = 1000.0
        schedule_entry.type = constants.LinSchedEntryType.UNCONDITIONAL
        schedule_entry.frames = [frame]

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
                    input_session.intf.lin_term = constants.LinTerm.ON
                    output_session.intf.lin_term = constants.LinTerm.OFF
                elif terminated_cable.lower() == "n":
                    input_session.intf.lin_term = constants.LinTerm.ON
                    output_session.intf.lin_term = constants.LinTerm.ON
                else:
                    print("Unrecognised input ({}), assuming 'n'".format(terminated_cable))
                    input_session.intf.lin_term = constants.LinTerm.ON
                    output_session.intf.lin_term = constants.LinTerm.ON

                # Start the input session manually to make sure that the first
                # signal values sent before the initial read will be received.
                input_session.start()

                # Set the schedule. This will also automatically enable master mode.
                output_session.change_lin_schedule(0)

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
