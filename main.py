from servo_controller import init_arduino, write_to_arduino
from ball_detection import return_position_ball, return_position_ball2
import time
import cv2


arduino = init_arduino()
write_to_arduino(arduino, 0)
cap = cv2.VideoCapture(0)
setpoint = 337
error = 0
error_sum = 0
error_div = 0
error_prev = 0
Kp = 0.12
Ki = 0.005
Kd = 0.01
dt = 0.01
while True:
    timestamp = time.time()
    error = setpoint - return_position_ball(cap)
    error_sum += error * dt
    error_div = (error - error_prev)/dt
    stuuractie = Kp * error + Ki * error_sum + Kd * error_div
    write_to_arduino(arduino, int(stuuractie))
    error_prev = error
    dt = time.time() - timestamp
    if dt < 0.01:
        time.sleep(0.01 - dt)
        dt = 0.01
    print(dt)

