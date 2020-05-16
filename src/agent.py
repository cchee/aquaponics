# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Agent class - provides basic signal handler for running process
#
import os
import signal

class Agent:

    def __init__(self, sig, handler):
        signal.signal(sig, handler)
        self.hostname = os.uname()[1]
        self.hpid = os.getpid()

    def get_pid(self):
        return self.pid

    def get_hostname(self):
        return self.hostname
