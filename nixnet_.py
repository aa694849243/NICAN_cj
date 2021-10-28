import nixnet
from nixnet import constants
from nixnet.types import CanIdentifier

with nixnet.FrameInStreamSession('CAN1') as input_session:
    input_session.intf.can_term = constants.CanTerm.ON
    input_session.intf.baud_rate = 1000000
    input_session.start()
    print('start')
    while True:
        a = input()
        if a == 'q':
            break
    frames = input_session.frames.read(100)
    # print(len(frames))
    for frame in frames:
        print('Received frame:')
        print(list(frame.payload))
    print('end')
