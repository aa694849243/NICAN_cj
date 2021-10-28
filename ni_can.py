import can
from can.interfaces.nican import NicanBus as Bus

def print_message(msg):
    print(msg)


# test 11
bus_rx = Bus('CAN0', bitrate=1000000, log_errors=True)
logger = can.Logger("logfile_1.asc")  # save log to asc file
listeners = [
    print_message,  # Callback function, print the received messages
    logger,  # save received messages to asc file
]
notifier = can.Notifier(bus_rx, listeners)
running = True
while running:
    input()
    running = False
notifier.stop()
# stops the bus
bus_rx.shutdown()
