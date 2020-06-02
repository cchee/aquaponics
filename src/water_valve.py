# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Water Valve Controller
#
from actuator import Actuator

# How to use
ACTUATOR_ID = "water_valve" # Must be unique in MQTT
ACTUATOR_CHANNEL = 5
TEST_MQTT_HOST = "localhost"
TEST_MQTT_PORT = 1883
TEST_MQTT_TOPIC = "fish_tank/water_level"
TEST_MQTT_QOS = 0
DEBUG = False
water_valve = Actuator(ACTUATOR_ID, ACTUATOR_CHANNEL, TEST_MQTT_HOST, TEST_MQTT_PORT, TEST_MQTT_TOPIC, TEST_MQTT_QOS, DEBUG)
water_valve.run()
