# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# MQTTPublisher class - this class public message in specific format via a specific topic to MQTT broker
#
from mqttsub import MQTTSubscriber

class MQTTPublisher(MQTTSubscriber):

    def __init__(self, hostname, pid, name, mqtthost, mqttport, topic, qos, retain):
        super().__init__(hostname, pid, name, mqtthost, mqttport, topic, qos, retain)

    def send_msg(self, state):
        self.session.publish(self.topic, "{}:{}".format(self.get_name(), state), self.qos, self.retain)
        return state
