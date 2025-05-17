import time
import RPi.GPIO as GPIO
from functions import motor_forward, motor_stop, set_angle
from gpio_config import get_components

pins = get_components()
sensor_left = pins["sensor_left"]
sensor_center = pins["sensor_center"]
sensor_right = pins["sensor_right"]

GPIO.setup(sensor_left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sensor_center, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sensor_right, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def auto_loop(should_stop):
    last_turn = 'center'

    while not should_stop():
        left = GPIO.input(sensor_left)     
        center = GPIO.input(sensor_center) 
        right = GPIO.input(sensor_right)   

        print(f"L: {left}, C: {center}, R: {right}")

        if center == GPIO.HIGH and left == GPIO.HIGH and right == GPIO.HIGH:
            set_angle(40)
            motor_forward(70)
            last_turn = 'center'

        elif center == GPIO.HIGH and right == GPIO.LOW:
            set_angle(25)
            motor_forward(70)
            last_turn = 'left'

        elif center == GPIO.HIGH and left == GPIO.LOW:
            set_angle(55)
            motor_forward(70)
            last_turn = 'right'

        elif center == GPIO.LOW and left == GPIO.LOW:
            set_angle(70)
            motor_forward(60)
            last_turn = 'right'

        elif center == GPIO.LOW and right == GPIO.LOW:
            set_angle(10)
            motor_forward(60)
            last_turn = 'left'

        else:
            motor_forward(40)
            if last_turn == 'left':
                set_angle(15)
            elif last_turn == 'right':
                set_angle(65)
            else:
                set_angle(40)

        time.sleep(0.05)

    motor_stop()
    set_angle(40)
