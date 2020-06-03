# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Actuator class - instance of this class subscribes to MQTT topic for update
#                  and then set specific GPIO pin to enable/disable actuator.
#
import RPi.GPIO as GPIO
import signal
import sys
from gpio import GPIOAgent
from mqttsub import MQTTSubscriber

class Actuator(GPIOAgent):

    def __init__(self, name, channel, mqtthost, mqttport, topic, qos = 0, debug = False):
        super().__init__(GPIO.BCM, False, {signal.SIGINT : self.signal_handler})
        self.sub = MQTTSubscriber(name, mqtthost, mqttport, topic, qos, debug)
        self.channel = channel
        GPIO.setup(self.channel, GPIO.OUT)

    def signal_handler(self, sig, frame):
        print('Ctrl-C pressed. GPIO cleanup.')
        self.disconnect()
        GPIO.cleanup()
        sys.exit(0)

    def process_message(self, client, userdata, message):
        topic = str(message.topic)
        value = str(message.payload.decode("utf-8")).split(':')
        self.set_value(value[1])
        print("Received {} from {} Set PIN {} to {}".format(value, topic, self.get_pin(), value[1]))

    def disconnect(self):
        self.sub.disconnect()

    def set_value(self, value):
        GPIO.output(self.channel, int(value))

    def get_pin(self):
        return self.channel

    def run(self):
        self.sub.set_listener(self.process_message)
        self.sub.loop_forever()

# How to use
#ACTUATOR_ID = "overflow_water_value" # Must be unique in MQTT
#ACTUATOR_CHANNEL = 5
#TEST_MQTT_HOST = "test.mosquitto.org"
#TEST_MQTT_PORT = 1883
#TEST_MQTT_TOPIC = "fish_tank/water_level"
#TEST_MQTT_QOS = 0 # Optional
#DEBUG = True # Optional
#actuator = Actuator(ACTUATOR_ID, ACTUATOR_CHANNEL, TEST_MQTT_HOST, TEST_MQTT_PORT, TEST_MQTT_TOPIC, TEST_MQTT_QOS, DEBUG)
#actuator.run()
