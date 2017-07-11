from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
import pprint
import six
import sys
import time

import nixnet
from nixnet import constants


pp = pprint.PrettyPrinter(indent=4)


def convert_timestamp(timestamp):
    system_epoch = time.gmtime(0)
    system_epock_datetime = datetime.datetime(system_epoch.tm_year, system_epoch.tm_mon, system_epoch.tm_mday)
    xnet_epoch_datetime = datetime.datetime(1601, 1, 1)
    delta = system_epock_datetime - xnet_epoch_datetime
    date = datetime.datetime.fromtimestamp(timestamp * 100e-9) - delta
    return date


def main():
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    input_signals = ['CANEventSignal1', 'CANEventSignal2']
    output_signals = ['CANEventSignal1', 'CANEventSignal2']
    interface1 = 'CAN1'
    interface2 = 'CAN2'

    with nixnet.SignalInSinglePointSession(
            interface1,
            database_name,
            cluster_name,
            input_signals) as input_session:
        with nixnet.SignalOutSinglePointSession(
                interface2,
                database_name,
                cluster_name,
                output_signals) as output_session:
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
            # signal value sent before the initial read will be received.
            input_session.start()

            user_value = six.moves.input('Enter {} signal values [float, float]: '.format(len(input_signals)))
            try:
                value_buffer = [float(x.strip()) for x in user_value.split(",")]
            except ValueError:
                value_buffer = [24.5343, 77.0129]
                print('Unrecognized input ({}). Setting data buffer to {}', user_value, value_buffer)

            if len(value_buffer) != len(input_signals):
                value_buffer = [24.5343, 77.0129]
                print('Invalid number of signal values entered. Setting data buffer to {}', value_buffer)

            print('The same values should be received. Press q to quit')
            i = 0
            while True:
                for index, value in enumerate(value_buffer):
                    value_buffer[index] = value + i
                output_session.signals.write(value_buffer)
                print('Sent signal values: %s' % value_buffer)

                # Wait 1 s and then read the received values.
                # They should be the same as the ones sent.
                time.sleep(1)

                signals = input_session.signals.read()
                for timestamp, value in signals:
                    date = convert_timestamp(timestamp)
                    print('Received signal with timepstamp %s and value %s' % (date, value))

                i += 1
                if max(value_buffer) + i > sys.float_info.max:
                    i = 0

                inp = six.moves.input('Hit enter to continue (q to quit): ')
                if inp.lower() == 'q':
                    break

            print('Data acquisition stopped.')


if __name__ == '__main__':
    main()
