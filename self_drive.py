import time
from functions import motor_forward, motor_backward, motor_stop, set_angle

def auto_loop(should_stop):
    while not should_stop():
        motor_forward()
        set_angle(30)
        time.sleep(1)

        motor_backward()
        set_angle(45)
        time.sleep(1)

        motor_stop()
        time.sleep(0.5)
