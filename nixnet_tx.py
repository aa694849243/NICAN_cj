import nixnet
from nixnet import constants
from nixnet import types
import time
def main():
    interface = 'CAN1'
    with nixnet.FrameOutStreamSession(interface) as output_session:
        output_session.intf.can_term = constants.CanTerm.ON
        output_session.intf.baud_rate = 1000000
        payload_list = [2, 4, 8, 16,16]
        payload = bytearray(payload_list)
        i = 0
        while True:
            for _ in range(10):
                id = types.CanIdentifier(_)
                frame = types.CanFrame(id, constants.FrameType.CAN_DATA, payload)
                frame.payload = payload
                output_session.frames.write([frame])
                print('Sent frame with ID: {} payload: {}'.format(frame.identifier,
                                                                  list(frame.payload)))
                # Wait 1 s and then read the received values.
                # They should be the same as the ones sent.
            inp = input('Hit enter to continue (q to quit): ')
            if inp.lower() == 'q':
                break

        print('Data acquisition stopped.')
if __name__ == '__main__':
    main()