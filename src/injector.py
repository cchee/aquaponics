
# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Injector class - this class simulate change in GPIO pins state. it is used
#                  for testing GPIO pin read agent
#
import RPi.GPIO as GPIO
import signal
import sys
import time
from gpio import GPIOMonitor

def signal_handler(sig, frame):
    print('Ctrl-C pressed. GPIO cleanup.')
    GPIO.cleanup()
    sys.exit(0)

class Injector(GPIOMonitor):

    def __init__(self, channel):
        super().__init__(GPIO.BCM, False, {signal.SIGINT : signal_handler})
        self.channel = channel

    def set_value(self, value):
        GPIO.setup(self.channel, GPIO.OUT)
        GPIO.output(self.channel, int(value))

    def get_pin(self):
        return self.channel

injector = Injector(6)
interval = 1
i = 0
while True:
    i = i + 1
    injector.set_value(i)
    print("Injected PIN {} with value {} at {}s interval".format(injector.get_pin(), i%2, interval));
    if (interval > 0):
        time.sleep(interval)
