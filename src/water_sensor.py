# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Contactless Water Level Sensor class - instance of this class monitor water level
# XKC-Y25-V                              and then publishes to MQTT for value changes.
# Brown  - 5V
# Yellow - OUT (to any GPIO pin as INPUT)
# Blue   - GND
# Black  - Mode (toggle to adjust sensor sensitive)
#
import RPi.GPIO as GPIO
from sensor import INTERVAL
from sensor import Sensor

SENSOR_CHANNEL = 2
MODE_CHANNEL = 3

class WaterLevelSensor(Sensor):

    mode = MODE_CHANNEL
    value = 0

    def __init__(self, name, channel, mode, mqtthost, mqttport, topic, qos, retain, debug):
        super().__init__(name, channel, INTERVAL, None, mqtthost, mqttport, topic, qos, retain, debug)
        self.mode = mode

    # sensor sensitivity settings
    def toggle_mode(self):
        self.value = self.value + 1
        GPIO.setup(self.mode, GPIO.OUT)
        GPIO.output(self.mode, (self.value % 2))

    def mode(self):
        return self.value

# How to use it
TEST_MQTT_HOST = "test.mosquitto.org"
TEST_MQTT_PORT = 1883
sensor = WaterLevelSensor("water_level_sensor", SENSOR_CHANNEL, MODE_CHANNEL, TEST_MQTT_HOST, TEST_MQTT_PORT, "fish_tank/upper_water_level", 0, True, False)
sensor.run()
