# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# MCP3208 class - the instance of this class provides a very
#                 simple interface to MCP3208
#
from spidev import SpiDev

class MCP3208:
    def __init__(self, bus = 0, device = 0):
        self.bus = bus
        self.device = device
        self.spi = SpiDev()
        self.open()

    def open(self):
        self.spi.open(self.bus, self.device)

    def read(self, channel = 0):
        adc = self.xfre2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data

    def close(self):
        self.spi.close()
