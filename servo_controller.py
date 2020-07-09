import serial
import time
import struct

left_most_value = 50
centre_value = 110
right_most_values = 170


def init_arduino():
    arduino = serial.Serial('COM8', 9600, timeout=.1)
    time.sleep(2)  # give the connection a second to settle
    return arduino


def write_to_arduino(arduino, value):
    valueToWrite = 220 - (value + 110)
    if valueToWrite == 90:
        valueToWrite = 91
    arduino.write(struct.pack('>B', valueToWrite))


# arduino = init_arduino()
# write_to_arduino(arduino, 0)
