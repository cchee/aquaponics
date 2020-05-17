# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# GPIOMonitor class - this is the base class for all GPIO actuator/sensor
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

class GPIOMonitor(Agent):

    def __init__(self, mode, warning, sig, handler):
        super().__init__(sig, handler)
        self.version = GPIO.VERSION
        GPIO.setmode(mode)
        GPIO.setwarnings(warning)

    def get_version(self):
        return self.version
