# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# MQTTSubscriber class - this class subscribes to a specific MQTT topic 
#                        and process message from MQTT broker
#
import paho.mqtt.client as MQTT
import time

class MQTTSubscriber:

    mqtthost = None
    mqttport = None
    topic = ""
    qos = 0
    interval = 1
    name = ""
    sender = ""
    session = None
    data = None

    def __init__(self, name, mqtthost, mqttport, topic, qos):
        self.name = name
        self.sender = "{}".format(self.name)
        self.mqtthost = mqtthost
        self.mqttport = mqttport
        self.topic = topic
        self.qos = qos
        self.session = MQTT.Client(self.sender, True, None, MQTT.MQTTv311, "tcp")
        self.session.connect(self.mqtthost, self.mqttport)
        self.session.subscribe(self.topic, self.qos)

    def get_name(self):
        return self.name

    def set_listener(self, msg_listener):
        self.session.on_message = msg_listener

    def loop_start(self):
        self.session.loop_start()

    def loop(self):
        self.session.loop()

    def loop_forever(self):
        self.session.loop_forever()

    def disconnect(self):
        self.session.loop_stop()
        self.session.unsubscribe(self.topic)
        self.session.disconnect()
