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
    valueToWrite = 110 - value
    if valueToWrite == 90:
        valueToWrite = 91
    if valueToWrite <= 75:
        valueToWrite = 75
    elif valueToWrite > 145:
        valueToWrite = 145
    arduino.write(struct.pack('>B', valueToWrite))

#
# arduino = init_arduino()
# write_to_arduino(arduino, 0)
