import RPi.GPIO as GPIO
import signal
import sys
import time
from gpio import GPIOMonitor
from random import seed
from random import randint

def signal_handler(sig, frame):
    print('Ctrl-C pressed. GPIO cleanup.')
    GPIO.cleanup()
    sys.exit(0)

class Injector(GPIOMonitor):

    trigger = 0

    def __init__(self, trigger):
        super().__init__(GPIO.BCM, False, signal.SIGINT, signal_handler)
        self.trigger = trigger
        GPIO.setup(self.trigger, GPIO.OUT)

    def set_value(self, value):
        GPIO.output(self.trigger, int(value))

    def get_pin(self):
        return self.trigger

#seed(1)
injector = Injector(4)
interval = 1
i = 0
while True:
    #i = randint(0, 100)
    i = i + 1
    injector.set_value(i)
    print("Injected PIN {} with value {} at {}s interval".format(injector.get_pin(), i%2, interval));
    if (interval > 0):
        time.sleep(interval)
