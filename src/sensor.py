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
from gpio import has_multi_thread
from gpio import has_event_based
from mqttpub import MQTTPublisher

BOUNCE_TIME = 200
GND_PIN = 39
INTERVAL = 1

def process_message(client, userdata, message):
    topic = str(message.topic)
    value = str(message.payload.decode("utf-8"))
    print("Sent:{}:{}".format(topic, value))

def signal_handler(sig, frame):
    print('Ctrl-C pressed. GPIO cleanup.')
    sensor.disconnect()
    GPIO.cleanup()
    sys.exit(0)

class Sensor(GPIOMonitor):

    pub = None
    channel = GND_PIN
    interval = INTERVAL
    edge = None

    def __init__(self, name, channel, interval, edge, mqtthost, mqttport, topic, qos, retain):
        super().__init__(GPIO.BCM, False, signal.SIGINT, signal_handler)
        self.pub = MQTTPublisher(name, mqtthost, mqttport, topic, qos, retain)
        self.pub.set_listener(process_message)
        self.channel = channel
        self.interval = interval
        self.edge = edge

    def disconnect(self):
        self.pub.disconnect()

    def notify(self, channel):
        state = GPIO.input(channel)
        print("Received {} from PIN {}".format(state, channel));
        self.pub.send_msg(state)

    def callback(self):
        GPIO.setup(self.channel, GPIO.IN, pull_up_down=self.edge)
        if (self.edge == GPIO.PUD_UP):
            GPIO.add_event_detect(self.channel, GPIO.RISING, self.notify, bouncetime=BOUNCE_TIME)
        elif (self.edge == GPIO.PUD_DOWN):
            GPIO.add_event_detect(self.channel, GPIO.FALLING, self.notify, bouncetime=BOUNCE_TIME)
        else:
            GPIO.add_event_detect(self.channel, GPIO.BOTH, self.notify, bouncetime=BOUNCE_TIME)

    def polling(self):
        GPIO.setup(self.channel, GPIO.IN, pull_up_down=self.edge)
        self.pub.loop_start()
        while True:
            self.notify()
            time.sleep(self.interval)

    def run(self):
        if (has_multi_thread(self.get_version())):
            self.callback()
            self.pub.loop_forever()

        elif (has_event_based(self.get_version())):
            self.callback()
            self.pub.loop_forever()

        else:
            self.polling()

# How to use
#TEST_MQTT_HOST = "test.mosquitto.org"
#TEST_MQTT_PORT = 1883
#sensor = Sensor("thermometer", 6, INTERVAL, GPIO.PUD_UP, TEST_MQTT_HOST, TEST_MQTT_PORT, "fish_tank/temperature", 0, True)
#sensor.run()
