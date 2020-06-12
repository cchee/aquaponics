# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Agent class - provides basic signal handler for running process
#
import os
import signal

class Agent:

    def __init__(self, sighandlers):
        self.hostname = os.uname()[1]
        self.pid = os.getpid()
        for sig, handler in sighandlers.items():
            signal.signal(sig, handler)

    def get_pid(self):
        return self.pid

    def get_hostname(self):
        return self.hostname
