# aquaponics

Aquaponics Automation

This is based on Raspberry Pi 3B (may look into Pi 4 later if budget allows). To integrate with analog sensors, MCP3208 is used as analog digital converter (ADC).

## Goals

* To have real-time event based sensors for fish tank pH, temperature, water level (sump tank), planting area's temperature and humidity, grow light intensity, EC and ppm monitoring
* To have actuator to automate fish feed, grow lights and dehumidifier in planting area, fish tank water outlet flow control and water pump.
* To utilize time series data collection to have real-time data visualization
* To have secure OS and software stack for IoT.

## Hardware Technology Stack

* Raspberry Pi 3B (or newer)
* Rio Rand 8-channel 12V relay (digital signal)

### Actuators
* Ehcotech 1" 12V DC Solenoid Valve (n/a, power on/off) - water refill
* Water pump 120V AC (n/a, power on/off) - circulate water
* Fans 12V DC (n/a, power on/off) - temperature control

### Sensors
* XKC-Y25-V contact-less water sensors (digital signal) - detects water levels
* temperature sensors - detects air/water temperature - approximately 70F - 75F (depends on plant)
* humidity sensors - detects humidity - approximately 60% -70% (depends on plant)
* electro conductivity (EC) sensors - detects nutrient levels
* pH sensors - detects pH in water to optimize nutrient absorption by plant (ideal pH for all plants: 6.5 relative to water temperature)

## Software Technology Stack

* Raspbian Buster (Need additional steps to secure installation)
* Ansible - to automate deployment of OS and softare upgrade
* Docker - to containerize application stack
* Python 3.8 - custom software coding for aquaponics
* Mosquitto - messaging middleware
* InfluxDB - time series database
* Grafana - data visualization

## Infrastructure Setup
* Each rack is managed by one Raspberry Pi with sensors and actuators. All Raspberry Pi are managed through WiFi network, but it can be managed through wired network if budget allows.
* Each rack has five or less shelf depending on which aquaponics method is being used. Aquaponic methods are flood-and-drain media filled bed, vertical media filled tower, nutrient film technique (NFT) and raft (aka deep water culture). 
* Each rack has a water pump. Water outlets from pump go to fish tank and grow beds to maintain pressurize water flow, all water flow loop back to sump tank using gravity. Water outlet from pump with venturi attachment oxygenates water without a need for air pump in the system. Pressurize water flow with water valve provides flexibility to shut off any section of the system for maintenance without flooding.
* Each rack may have zero or more grow light, depends on which aquaponic method is being used in each rack or each shelf as well as the location of the rack (i.e indoor verse outdoor).

## Notes
* Bell siphon is used in flood-and-drain media bed to eliminate any mechnical part to minimize maintenance
* Red worms can be used in media bed to prevent clogging because they consume organic debris such as dead root, dead flowers and dead leaves from plants. They help to prevent mold on the grow bed due to organic debris left on grow bed surface. Worm casting also provide additional organic nutrients to plant.
* High temperature causes some of the vegetables to taste bitter. For example, lettuce.
