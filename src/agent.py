# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Agent class - provides basic signal handler for running process
#
import os
import signal

class Agent:

    hostname = os.uname()[1]
    pid = os.getpid()

    def __init__(self, sig, handler):
        signal.signal(sig, handler)

    def get_pid():
        return pid

    def get_hostname():
        return hostname
