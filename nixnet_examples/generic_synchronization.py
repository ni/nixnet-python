from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import six
import time


import nixnet
from nixnet import constants
from nixnet import types


def main():
    interface1 = 'CAN1'
    interface2 = 'CAN2'

    # Create the sessions. ExitStack() can be used for high session counts
    with nixnet.FrameInStreamSession(interface1) as interface1_input:
        with nixnet.FrameInStreamSession(interface2) as interface2_input:
            with nixnet.FrameOutStreamSession(interface2) as interface2_output:
                # Set session and interface properties such as termination
                # Note that interface properties only need to be set once per interface
                interface1_input.intf.baud_rate = 125000
                interface1_input.intf.can_term = constants.CanTerm.ON

                # Connect the start trigger terminals for the listening interface
                interface1_input.connect_terminals(constants.Terminal.FRONT_PANEL_0, constants.Terminal.START_TRIGGER)

                # Start the listening interface sessions
                interface1_input.start()

                # Set session and interface properties such as termination
                # Note that interface properties only need to be set once per interface
                interface2_input.intf.baud_rate = 125000
                interface2_input.intf.can_term = constants.CanTerm.ON
                interface2_input.intf.echo_tx = True

                # Connect the start trigger terminals for the interface driving the start trigger
                interface2_input.connect_terminals(constants.Terminal.START_TRIGGER, constants.Terminal.FRONTPANEL_1)

                # Starting the sessions on the driving interface will trigger the start of the listening sessions
                interface2_input.start(constants.StartStopScope.SESSION_ONLY)
                interface2_output.start()

                # Request values to transmit from user
                user_value = six.moves.input('Enter payload [int, int, ...]: ')
                try:
                    payload_list = [int(x.strip()) for x in user_value.split(",")]
                except ValueError:
                    payload_list = [2, 4, 8, 16]
                    print('Unrecognized input ({}). Setting data buffer to {}'.format(user_value, payload_list))

                id = types.CanIdentifier(1)
                payload = bytearray(payload_list)
                frame = types.CanFrame(id, constants.FrameType.CAN_DATA, payload)

                print('The same values should be received. Press q to quit')
                i = 0
                while True:
                    # Apply the user input to the frame payload
                    for index, byte in enumerate(payload):
                        payload[index] = byte + i

                    frame.payload = payload
                    # Write the specified frame to the bus
                    interface2_output.frames.write([frame])
                    print('Sent frame with ID {} payload: {}'.format(id, payload))

                    time.sleep(0.2)

                    # Read frames back from both input sessions
                    frames_to_read = 1
                    received_frames = interface1_input.frames.read(frames_to_read)
                    echoed_frames = interface2_input.frames.read(frames_to_read)
                    rx_frame_list = list(received_frames)
                    echo_frame_list = list(echoed_frames)
                    for frame in rx_frame_list:
                        print('Received frame: {}'.format(rx_frame_list[0]))
                        print('    payload={}'.format(list(six.iterbytes(rx_frame_list[0].payload))))
                        print('Echoed frame: {}'.format(echo_frame_list[0]))
                        print('    payload={}'.format(list(six.iterbytes(echo_frame_list[0].payload))))

                        # Subtract the timestamp from first frame in each list to obtain delta
                        delta_t = rx_frame_list[0].timestamp - echo_frame_list[0].timestamp
                        print('The delta between received timestamp and echo is: {}', delta_t)

                    i += 1
                    if max(payload) + i > 0xFF:
                        i = 0
                    inp = six.moves.input('Hit enter to continue (q to quit): ')
                    if inp.lower() == 'q':
                        break

                print('Data acquisition stopped.')


if __name__ == '__main__':
    main()
