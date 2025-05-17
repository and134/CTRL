import RPi.GPIO as GPIO
import time
from gpio_config import get_components

pins = get_components()

def set_angle(angle):
    duty = 2 + (angle / 18)
    pins["servo_pwm"].ChangeDutyCycle(duty)
    time.sleep(0.1)

def motor_forward():
    GPIO.output(pins["motor_in1"], GPIO.LOW)
    GPIO.output(pins["motor_in2"], GPIO.HIGH)
    pins["motor_pwm"].ChangeDutyCycle(60)

def motor_backward():
    GPIO.output(pins["motor_in1"], GPIO.HIGH)
    GPIO.output(pins["motor_in2"], GPIO.LOW)
    pins["motor_pwm"].ChangeDutyCycle(60)

def motor_stop():
    GPIO.output(pins["motor_in1"], GPIO.LOW)
    GPIO.output(pins["motor_in2"], GPIO.LOW)
    pins["motor_pwm"].ChangeDutyCycle(0)
