# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Water Valve Controller
#
from actuator import Actuator

# How to use
WATER_VALVE_CHANNEL = 5
TEST_MQTT_HOST = "test.mosquitto.org"
TEST_MQTT_PORT = 1883
water_valve = Actuator("water_valve", WATER_VALVE_CHANNEL, TEST_MQTT_HOST, TEST_MQTT_PORT, "fish_tank/water_level", 0, False)
water_valve.run()
