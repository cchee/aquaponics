# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# GPIOAgent class - this is the base class for all GPIO actuators/sensors
#
import RPi.GPIO as GPIO
from agent import Agent
import re
import signal
import time

def has_event_based(version):
    tokens = re.sub(r'[a-z]+', '', version, re.I).split('.')
    if (int(tokens[1]) > 5):
        return True
    elif (int(tokens[2]) >= 1):
        return True
    return False

def has_multi_thread(version):
    tokens = re.sub(r'[a-z]+', '', version, re.I).split('.')
    if (int(tokens[1]) > 5):
        return True
    elif (int(tokens[2]) >= 2):
        return True
    return False

class GPIOAgent(Agent):

    def __init__(self, mode, warning, sighandlers):
        super().__init__(sighandlers)
        self.version = GPIO.VERSION
        self.event_based = has_event_based(self.version)
        self.multi_thread = has_multi_thread(self.version)
        GPIO.setmode(mode)
        GPIO.setwarnings(warning)

    def get_version(self):
        return self.version

    def is_event_based(self):
        return self.event_based

    def is_multi_thread(self):
        return self.multi_thread

