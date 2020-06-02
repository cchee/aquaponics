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

    def __init__(self, trigger):
        super().__init__(GPIO.BCM, False, {signal.SIGINT : signal_handler})
        self.trigger = trigger

    def set_value(self, value):
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.output(self.trigger, int(value))

    def get_pin(self):
        return self.trigger

injector = Injector(6)
interval = 1
i = 0
while True:
    i = i + 1
    injector.set_value(i)
    print("Injected PIN {} with value {} at {}s interval".format(injector.get_pin(), i%2, interval));
    if (interval > 0):
        time.sleep(interval)
