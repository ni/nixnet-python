from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import six

from nixnet import convert


def main():
    database_name = 'NIXNET_example'
    cluster_name = 'CAN_Cluster'
    signal_names = ['CANEventSignal1', 'CANEventSignal2']

    with convert.SignalConversionSinglePointSession(
            database_name,
            cluster_name,
            signal_names) as session:

        user_value = six.moves.input('Enter {} signal values [float, float]: '.format(len(signal_names)))
        try:
            expected_signals = [float(x.strip()) for x in user_value.split(",")]
        except ValueError:
            expected_signals = [24.5343, 77.0129]
            print('Unrecognized input ({}). Setting data buffer to {}'.format(user_value, expected_signals))

        if len(expected_signals) != len(signal_names):
            expected_signals = [24.5343, 77.0129]
            print('Invalid number of signal values entered. Setting data buffer to {}'.format(expected_signals))

        frames = session.convert_signals_to_frames(expected_signals)
        print('Frames:')
        for frame in frames:
            print('    {}'.format(frame))
            print('        payload={}'.format(list(six.iterbytes(frame.payload))))

        converted_signals = session.convert_frames_to_signals(frames)
        print('Signals: {}'.format([v for (_, v) in converted_signals]))


if __name__ == '__main__':
    main()
