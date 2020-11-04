#import the pyserial module
import serial
import ncd_industrial_relay
import time


#set up your serial port with the desire COM port and baudrate.
serial_port = serial.Serial('/dev/tty.usbserial-AG0JV64T', baudrate=115200, bytesize=8, stopbits=1, timeout=.5)
#instantiate the board object and pass it the serial port
board1 = ncd_industrial_relay.Relay_Controller(serial_port)

board1.turn_on_relay_by_index(1)

response = board1.get_relay_status_by_index(1)
print(response[0])

time.sleep(2)

board1.turn_off_relay_by_index(1)

response = board1.get_relay_status_by_index(1)
print(response[0])

serial_port.close()
