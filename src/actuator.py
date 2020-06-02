# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Actuator class - instance of this class subscribes to MQTT topic for update
#                  and then set specific GPIO pin to enable/disable actuator.
#
import RPi.GPIO as GPIO
import signal
import sys
from gpio import GPIOMonitor
from mqttsub import MQTTSubscriber

DEFAULT_PIN = 0

def signal_handler(sig, frame):
    print('Ctrl-C pressed. GPIO cleanup.')
    actuator.disconnect()
    GPIO.cleanup()
    sys.exit(0)

class Actuator(GPIOMonitor):

    def __init__(self, name, channel, mqtthost, mqttport, topic, qos, debug = False):
        super().__init__(GPIO.BCM, False, signal.SIGINT, signal_handler)
        self.sub = MQTTSubscriber(name, mqtthost, mqttport, topic, qos, debug)
        self.channel = channel
        GPIO.setup(self.channel, GPIO.OUT)

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
#TEST_MQTT_HOST = "test.mosquitto.org"
#TEST_MQTT_PORT = 1883
#actuator = Actuator("overflow_water_valve", 5, TEST_MQTT_HOST, TEST_MQTT_PORT, "fish_tank/water_level", 0, True)
#actuator.run()
