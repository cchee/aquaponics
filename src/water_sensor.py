# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Contactless Water Level Sensor class - instance of this class monitor water level
#                                        and then publishes to MQTT for value changes.
#
import RPi.GPIO as GPIO
from sensor import Sensor

class WaterLevelSensor(Sensor):

    mode = None
    value = None

    def __init__(self, name, channel, mode, mqtthost, mqttport, topic, qos, retain):
        super().__init__(self, name, channel, INTERVAL, GPIO.PUD_UP, mqtthost, mqttport, topic, qos, retain):
        self.mode = mode

    # sensor sensitivity settings
    def mode(self, value):
        self.value = value
        GPIO.setup(self.mode, GPIO.OUT)
        GPIO.output(self.mode, self.value)

    def mode(self):
        return self.value

TEST_MQTT_HOST = "test.mosquitto.org"
TEST_MQTT_PORT = 1883
sensor = WaterLevelSensor("water_level", 2, 3, TEST_MQTT_HOST, TEST_MQTT_PORT, "fish_tank/upper_water_level", 0, True)
sensor.run()
