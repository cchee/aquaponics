# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Water Level Sensor
#
from xkcy25v import XKCY25VSensor

# How to use
SENSOR_ID = "water_overflow_sensor" # Must be unique in MQTT
SENSOR_CHANNEL = 2
MODE_CHANNEL = 3
TEST_MQTT_HOST = "localhost"
TEST_MQTT_PORT = 1883
TEST_MQTT_TOPIC = "fish_tank/water_level"
#TEST_MQTT_QOS = 0
#TEST_MQTT_RETAIN = True
#DEBUG = False

sensor = XKCY25VSensor(SENSOR_ID, SENSOR_CHANNEL, MODE_CHANNEL, TEST_MQTT_HOST, TEST_MQTT_PORT, TEST_MQTT_TOPIC)
#sensor.toggle_mode()
sensor.run()
