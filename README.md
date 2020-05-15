# aquaponics
Indoor Aquaponics Automation

This is based on Raspberry Pi 3B (may look into Pi 4 later if budget allows). To integrate with analog sensors, MCP3208 is used as analog digital converter (ADC).

Goals
* To have real-time event based sensors for fish tank pH, temperature, water level (sump tank), planting area's temperature and humidity, grow light intensity
* To have actuator to automate fish feed, grow lights and dehumidifier in planting area, fish tank water outlet flow control and water pump.
* To utilize time series data collection to have real-time data visualization
* To have secure OS and softare stack for IoT.

Technology Stack
* Raspberry Pi 3B (or newer)
* TBD (Experimenting with Ubuntu Core, Ubuntu Server 20.04 and maybe Raspbian to see which one is securer)
* Docker
* Python 3.8 (may be later on for ML)
* Node-Red
* Mosquitto
* InfluxDB
* Grafana
