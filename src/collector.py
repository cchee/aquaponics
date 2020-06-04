# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Data Collector class - an instance of this class provide simple interface to take
#                        event from MQTT and insert them as measurement based on topic
#                        into InfluxDB
#
import signal
import sys
from agent import Agent
from influxdb import InfluxDBClient
from mqttsub import MQTTSubscriber

class DataCollector(Agent):

    def __init__(self, name, mqtthost, mqttport, topic, qos=0, debug=False):
        super().__init__({signal.SIGINT : self.signal_handler})
        self.sub = MQTTSubscriber(name, mqtthost, mqttport, topic, qos, debug)
        self.dbconn = None

    def signal_handler(self, sig, frame):
        print('Ctrl-C pressed. Cleanup.')
        self.disconnect()
        sys.exit(0)

    def set_dbconn(self, dbhost, dbport, dbuser, dbpass, dbname):
        self.dbconn = InfluxDBClient(dbhost, dbport, dbuser, dbpass, dbname)

    def process_message(self, client, userdata, message):
        topic = str(message.topic)
        value = str(message.payload.decode("utf-8")).split(':')
        print("Received {} from {}".format(value, topic))
        if (self.dbconn != None):
            self.dbconn.insert()

    def disconnect(self):
        self.sub.disconnect()
        if (self.dbconn != None):
            self.dbconn.disconnect()

    def run(self):
        if (self.dbconn != None):
            self.sub.set_listener(self.process_message)
            self.sub.loop_forever()
        else:
            print("influxdb connection is not initialize.")
            sys.exit(1)

# How to use
#COLLECTOR_ID = "data_collector" # Must be unique in MQTT
#TEST_MQTT_HOST = "test.mosquitto.org"
#TEST_MQTT_PORT = 1883
#TEST_MQTT_TOPIC = "fish_tank/#"
#TEST_MQTT_QOS = 0 # Optional
#DEBUG = True # Optional
#DB_HOST = "localhost"
#DB_PORT = 8086
#DB_USER = "aqua"
#DB_PASSWD = "swimming"
#DB_NAME = "aquaponics"
#collector = DataCollector(COLLECTOR_ID, TEST_MQTT_HOST, TEST_MQTT_PORT, TEST_MQTT_TOPIC, TEST_MQTT_QOS, DEBUG)
#collector.set_dbconn(DB_HOST, DB_PORT, DB_USER, DB_PASSWD, DB_NAME)
#collector.run()

