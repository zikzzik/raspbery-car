import Adafruit_PCA9685
import time
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class CarController:
    def __init__(self, direction):
        self.direction = direction


    def forward(self):
        pass

    def packward(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def movement(self):
        if self.direction == 'forward':
            self.forward()
        if self.direction == 'backward':
            self.packward()
        if self.direction == 'left':
            print('up')
        if self.direction == 'right':
            print('down')


if __name__ == '__main__':
    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(50)  # Set the frequency of the PWM signal
    while True:
        pwm.set_pwm(3, 0, 300)
        time.sleep(1)
        pwm.set_pwm(3, 0, 400)
        time.sleep(1)