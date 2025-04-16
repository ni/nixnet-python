import time

import six

import nixnet
from nixnet import constants
from nixnet import types


def main():
    interface1 = 'LIN1'
    interface2 = 'LIN2'
    database = 'NIXNET_exampleLDF'

    with nixnet.FrameInStreamSession(interface1, database) as input_session:
        with nixnet.FrameOutStreamSession(interface2, database) as output_session:
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

            output_session.intf.lin_master = True

            # Start the input session manually to make sure that the first
            # frame value sent before the initial read will be received.
            input_session.start()

            # Set the schedule. This will also automatically enable master mode.
            output_session.change_lin_schedule(0)

            user_value = six.moves.input('Enter payload [int, int]: ')
            try:
                payload_list = [int(x.strip()) for x in user_value.split(",")]
            except ValueError:
                payload_list = [2, 4, 8, 16]
                print('Unrecognized input ({}). Setting data buffer to {}'.format(user_value, payload_list))

            id = 0
            payload = bytearray(payload_list)
            frame = types.LinFrame(id, constants.FrameType.LIN_DATA, payload)

            print('The same values should be received. Press q to quit')
            i = 0
            while True:
                for index, byte in enumerate(payload):
                    payload[index] = byte + i

                frame.payload = payload
                output_session.frames.write([frame])
                print('Sent frame with ID: {} payload: {}'.format(frame.identifier,
                                                                  list(frame.payload)))

                # Wait 1 s and then read the received values.
                # They should be the same as the ones sent.
                time.sleep(1)

                count = 1
                frames = input_session.frames.read(count)
                for frame in frames:
                    print('Received frame with ID: {} payload: {}'.format(frame.identifier,
                                                                          list(six.iterbytes(frame.payload))))

                i += 1
                if max(payload) + i > 0xFF:
                    i = 0

                inp = six.moves.input('Hit enter to continue (q to quit): ')
                if inp.lower() == 'q':
                    break

            print('Data acquisition stopped.')


if __name__ == '__main__':
    main()
