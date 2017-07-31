from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

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

    with nixnet.SignalInWaveformSession(
            interface1,
            database_name,
            cluster_name,
            input_signals) as input_session:
        with nixnet.SignalOutWaveformSession(
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

            out_waveforms = []
            for out_signal in output_signals:
                user_value = six.moves.input('Enter "{}" signal values [float, ...]: '.format(out_signal))
                try:
                    out_waveforms.append([float(x.strip()) for x in user_value.split(",")])
                except ValueError:
                    out_waveforms.append([24.5343, 77.0129])
                    print('Unrecognized input ({}). Setting waveform to {}'.format(user_value, out_waveforms[-1]))

            value_count = set(len(waveform) for waveform in out_waveforms)
            if 1 < len(value_count):
                out_waveforms = [
                    [24.5343 + i, 77.0129 + i]
                    for i, _ in enumerate(output_signals)
                ]
                print('Inconsistent waveform lengths. Setting each waveform to {}', out_waveforms)

            print('The same values should be received. Press q to quit')
            i = 0
            while True:
                for waveform_index, waveform in enumerate(out_waveforms):
                    for value_index, value in enumerate(waveform):
                        out_waveforms[waveform_index][value_index] = value + i
                output_session.signals.write(out_waveforms)
                print('Sent signal values: {}'.format(pp.pformat(out_waveforms)))

                # Wait 1 s and then read the received values.
                # They should be the same as the ones sent.
                time.sleep(1)

                t0, dt, signals = input_session.signals.read(len(out_waveforms[0]))
                print('Received signal at {} in intervals of {}: {}'.format(
                    convert_timestamp(t0),
                    dt,
                    signals))

                i += 1
                for waveform in out_waveforms:
                    if max(waveform) + i > sys.float_info.max:
                        i = 0
                        break

                inp = six.moves.input('Hit enter to continue (q to quit): ')
                if inp.lower() == 'q':
                    break

            print('Data acquisition stopped.')


if __name__ == '__main__':
    main()
