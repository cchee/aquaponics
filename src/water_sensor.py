# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Contactless Water Level Sensor class - instance of this class monitor water level
# XKC-Y25-V                              and then publishes to MQTT for value changes.
# Brown  - 5V
# Yellow - OUT (signal output, to any GPIO pin as INPUT)
# Blue   - GND
# Black  - Mode
#
# Mode
# When black wire connects high level, yellow wire (output signal) is positive, and 
#   if there is induction, it outputs high level
#   if there is no induction, it outputs low level
# When black wire connects low  level, yellow wire (output signal) is neagtive, and
#   if there is induction, it outputs low level
#   if there is no induction, it outputs high level
#
# Sensor sensitivity adjustment
# 1. Open the back cover of the sensor head, use small screwdriver to adjust the
#    sensitivity knob
# 2. If the knob is rotated counter clockwise, it increases sensitivity,
#    otherwise decreases its sensitivity.

import RPi.GPIO as GPIO
from sensor import INTERVAL
from sensor import Sensor

DEBUG = False
SENSOR_CHANNEL = 2
MODE_CHANNEL = 3

class WaterLevelSensor(Sensor):

    mode = MODE_CHANNEL
    value = 0

    def __init__(self, name, channel, mode, mqtthost, mqttport, topic, qos, retain, debug):
        super().__init__(name, channel, INTERVAL, None, mqtthost, mqttport, topic, qos, retain, debug)
        GPIO.setup(mode, GPIO.OUT)
        GPIO.output(mode, int(self.value))
        self.mode = mode

    # sensor sensitivity settings
    def toggle_mode(self):
        self.value = (self.value + 1) % 2
        GPIO.output(self.mode, int(self.value))

    def mode(self):
        return self.value

# How to use it
TEST_MQTT_HOST = "localhost"
TEST_MQTT_PORT = 1883
sensor = WaterLevelSensor("overflow_water_level_sensor", SENSOR_CHANNEL, MODE_CHANNEL, TEST_MQTT_HOST, TEST_MQTT_PORT, "fish_tank/water_level", 0, True, DEBUG)
#sensor.toggle_mode()
sensor.run()
