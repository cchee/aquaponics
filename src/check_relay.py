# Copyright 2020 All right reserved
# Author: Chester Chee <chester.chee@gmail.com>
#
# Relay Checker - this is a simple Python script to toggle through a set of GPIO pins in
#                 Raspberry Pi which are mapped to Rio Rand 8-channel relay module
import RPi.GPIO as GPIO
import time

INTERVAL = 1
GPIO.setmode(GPIO.BCM)

pinList = [14, 15, 18, 23, 24, 25, 8, 7]

print("Initialize...")
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

try:
    print("Individual Toggle Test...")
    for i in pinList:
        print("GPIO {} LOW".format(i))
        GPIO.output(i, GPIO.LOW)
        time.sleep(INTERVAL)
        print("GPIO {} HIGH".format(i))
        GPIO.output(i, GPIO.HIGH)
        time.sleep(INTERVAL)
    print("Group Toggle Test...")
    for i in pinList:
        print("GPIO {} LOW".format(i))
        GPIO.output(i, GPIO.LOW)
    time.sleep(INTERVAL)
    print("Reset...")
    GPIO.cleanup()
    print("Done")

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()

