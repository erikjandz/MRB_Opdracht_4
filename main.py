from servo_controller import init_arduino, write_to_arduino
from ball_detection import return_position_ball
import time


arduino = init_arduino()
write_to_arduino(arduino, 0)
setpoint = 195
error = 0
error_sum = 0
error_div = 0
error_prev = 0
Kp = 0.1
Ki = 0.02
Kd = 0.01
dt = 1
while True:
    error = setpoint - return_position_ball()
    error_sum += error * dt
    error_div = (error - error_prev)/dt
    stuuractie = Kp * error + Ki * error_sum + Kd * error_div
    write_to_arduino(arduino, int(stuuractie))
    error_prev = error