# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Sensor class - instance of this class monitor edge up/down of a specific GPIO channel
#                  and then publishes to MQTT for value changes.
#
import RPi.GPIO as GPIO
import signal
import sys
import time
from gpio import GPIOMonitor
from mqttpub import MQTTPublisher

BOUNCE_TIME = 200
GND_PIN = 39
INTERVAL = 1

def signal_handler(sig, frame):
    print('Ctrl-C pressed. GPIO cleanup.')
    sensor.disconnect()
    GPIO.cleanup()
    sys.exit(0)

class Sensor(GPIOMonitor):

    def __init__(self, name, channel, interval, edge, mqtthost, mqttport, topic, qos, retain, debug = False):
        super().__init__(GPIO.BCM, False, signal.SIGINT, signal_handler)
        self.pub = MQTTPublisher(name, mqtthost, mqttport, topic, qos, retain, debug)
        self.pub.set_listener(self.process_message)
        self.channel = channel
        self.interval = interval
        self.edge = edge
        self.debug = debug

    def process_message(self, client, userdata, message):
        topic = str(message.topic)
        value = str(message.payload.decode("utf-8"))
        print("Sent:{}:{}".format(topic, value))

    def disconnect(self):
        self.pub.disconnect()

    def notify(self, channel):
        state = GPIO.input(channel)
        if (self.debug):
            print("Received {} from PIN {}".format(state, channel));
        self.pub.send_msg(state)

    def callback(self):
        if (self.edge == GPIO.PUD_UP):
            GPIO.setup(self.channel, GPIO.IN, pull_up_down=self.edge)
            GPIO.add_event_detect(self.channel, GPIO.RISING, self.notify, bouncetime=BOUNCE_TIME)
        elif (self.edge == GPIO.PUD_DOWN):
            GPIO.setup(self.channel, GPIO.IN, pull_up_down=self.edge)
            GPIO.add_event_detect(self.channel, GPIO.FALLING, self.notify, bouncetime=BOUNCE_TIME)
        else:
            GPIO.setup(self.channel, GPIO.IN)
            GPIO.add_event_detect(self.channel, GPIO.BOTH, self.notify, bouncetime=BOUNCE_TIME)

    def polling(self):
        GPIO.setup(self.channel, GPIO.IN, pull_up_down=self.edge)
        while True:
            self.notify()
            time.sleep(self.interval)

    def run(self):
        if (self.is_multi_thread()):
            self.callback()
            self.pub.loop_forever()

        elif (self.is_event_based()):
            self.callback()
            self.pub.loop_forever()

        else:
            # Polling causes high CPU usage
            # Use polling if and only if GPIO library does not support multithread and event
            self.polling()

# How to use
#TEST_MQTT_HOST = "test.mosquitto.org"
#TEST_MQTT_PORT = 1883
#sensor = Sensor("thermometer", 6, INTERVAL, GPIO.PUD_UP, TEST_MQTT_HOST, TEST_MQTT_PORT, "fish_tank/temperature", 0, True)
#sensor.run()
