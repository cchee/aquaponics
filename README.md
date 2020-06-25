# aquaponics

Indoor Aquaponics Automation

This is based on Raspberry Pi 3B (may look into Pi 4 later if budget allows). To integrate with analog sensors, MCP3208 is used as analog digital converter (ADC).

## Goals

* To have real-time event based sensors for fish tank pH, temperature, water level (sump tank), planting area's temperature and humidity, grow light intensity, EC and ppm monitoring
* To have actuator to automate fish feed, grow lights and dehumidifier in planting area, fish tank water outlet flow control and water pump.
* To utilize time series data collection to have real-time data visualization
* To have secure OS and software stack for IoT.

## Hardware Technology Stack

* Raspberry Pi 3B (or newer)
* XKC-Y25-V contact-less water sensors
* Rio Rand 8-channel 12V relay
* Ehcotech 1" 12V DC Solenoid Valve

## Software Technology Stack

* Raspbian Buster (Need additional steps to secure installation)
* Docker
* Python 3.8
* Mosquitto
* InfluxDB
* Grafana
