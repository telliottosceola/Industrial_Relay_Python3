#import the pyserial module
import serial
import ncd_industrial_relay
import time


#set up your serial port with the desire COM port and baudrate.
serial_port = serial.Serial('/dev/tty.usbserial-AG0JUHU4', baudrate=115200, bytesize=8, stopbits=1, timeout=.5)
#instantiate the board object and pass it the serial port
board1 = ncd_industrial_relay.Relay_Controller(serial_port)

previousInputState = 256;

while(True):
    input = board1.read_single_ad8(1)
    # print(input)
    if input[0] != previousInputState:
        print(input[0])
        previousInputState = input[0]
        if input[0] < 128:
            board1.turn_on_all_relays()
        else:
            board1.turn_off_all_relays()

serial_port.close()
