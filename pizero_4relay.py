import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class relay:
    relay_pins = {"R1":31,"R2":33,"R3":35,"R4":37}

    def __init__(self, pins):
        self.pin = self.relay_pins[pins]
        self.pins = pins
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        GPIO.output(self.pin,GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin,GPIO.LOW)