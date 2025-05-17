import RPi.GPIO as GPIO

# Pini
motor_in1 = 17
motor_in2 = 27
motor_ena = 22

servo_pin = 18

sensor_left = 19
sensor_center = 6
sensor_right = 13

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([motor_in1, motor_in2, motor_ena, servo_pin], GPIO.OUT)
GPIO.setup(sensor_left, sensor_center, sensor_right, GPIO.IN)

motor_pwm = GPIO.PWM(motor_ena, 100)
motor_pwm.start(0)

servo_pwm = GPIO.PWM(servo_pin, 50)
servo_pwm.start(0)

def get_components():
    return {
        "motor_in1": motor_in1,
        "motor_in2": motor_in2,
        "motor_pwm": motor_pwm,
        "servo_pwm": servo_pwm,
        "sensor_left": sensor_left,
        "sensor_center": sensor_center,
        "sensor_right": sensor_right
    }
