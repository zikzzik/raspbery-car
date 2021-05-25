import time
import RPi.GPIO as GPIO


# global
Motor_A_EN = 4
Motor_B_EN = 17
Motor_A_Pin1 = 14
Motor_A_Pin2 = 15
Motor_B_Pin1 = 27
Motor_B_Pin2 = 18


class CarAction:

    def __init__(self):
        GPIO.cleanup()
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.setup()

    def stop_motor(self):
        GPIO.output(Motor_A_Pin1, GPIO.LOW)
        GPIO.output(Motor_A_Pin2, GPIO.LOW)
        GPIO.output(Motor_B_Pin1, GPIO.LOW)
        GPIO.output(Motor_B_Pin2, GPIO.LOW)
        GPIO.output(Motor_A_EN, GPIO.LOW)
        GPIO.output(Motor_B_EN, GPIO.LOW)

    def setup(self):
        global pwm_A, pwm_B
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Motor_A_EN, GPIO.OUT)
        GPIO.setup(Motor_B_EN, GPIO.OUT)
        GPIO.setup(Motor_A_Pin1, GPIO.OUT)
        GPIO.setup(Motor_A_Pin2, GPIO.OUT)
        GPIO.setup(Motor_B_Pin1, GPIO.OUT)
        GPIO.setup(Motor_B_Pin2, GPIO.OUT)

        self.stop_motor()       # Avoid motor starting to rotate automatically after initialization
        try:                        # Try is used here to avoid errors due to repeated PWM settings
            pwm_A = GPIO.PWM(Motor_A_EN, 1000)
            pwm_B = GPIO.PWM(Motor_B_EN, 1000)
        except:
            pass

    def motor_A(self, direction, speed):
        if direction == 1:
            GPIO.output(Motor_A_Pin1, GPIO.HIGH)
            GPIO.output(Motor_A_Pin2, GPIO.LOW)
            pwm_A.start(100)
            pwm_A.ChangeDutyCycle(speed)
        if direction == -1:
            GPIO.output(Motor_A_Pin1, GPIO.LOW)
            GPIO.output(Motor_A_Pin2, GPIO.HIGH)
            pwm_A.start(100)
            pwm_A.ChangeDutyCycle(speed)

    def motor_B(self, direction, speed):
        if direction == 1:
            GPIO.output(Motor_B_Pin1, GPIO.HIGH)
            GPIO.output(Motor_B_Pin2, GPIO.LOW)
            pwm_B.start(100)
            pwm_B.ChangeDutyCycle(speed)
        if direction == -1:
            GPIO.output(Motor_B_Pin1, GPIO.LOW)
            GPIO.output(Motor_B_Pin2, GPIO.HIGH)
            pwm_B.start(100)
            pwm_B.ChangeDutyCycle(speed)

    def right(self, action_time, speed):
        self.motor_A(1, speed)
        self.motor_B(1, speed)
        time.sleep(action_time)

    def left(self, action_time, speed):
        self.motor_A(-1, speed)
        self.motor_B(-1, speed)
        time.sleep(action_time)

    def forward(self, action_time, speed):
        self.motor_A(1, speed)
        self.motor_B(-1, speed)
        time.sleep(action_time)

    def backward(self, action_time, speed):
        self.motor_A(-1, speed)
        self.motor_B(1, speed)
        time.sleep(action_time)


# if __name__ == "__main__":
#     a = CarAction()
#     a.stop_motor()
#     a.forward(1, 50)
#     a.backward(1, 50)
#     a.left(1, 50)
#     a.right(1, 50)
#     a.stop_motor()