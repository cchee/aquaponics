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
* Rio Rand 8-channel 12V relay (digital signal) - on/off actuators

### Actuators
* Ehcotech 1" 12V DC Solenoid Valve (n/a, power on/off) - water refill
* Water pump 120V AC (n/a, power on/off) - circulate water
* Water heater 120V AC (n/a, power on/off) - maintain water temperature for aquaculture
* LED grow light (n/a, power on/off) - provide blue/red light for leaves and fruit grow respectively
* Fans 12V DC (n/a, power on/off) - humidity/temperature control

### Sensors
* XKC-Y25-V contact-less water sensors (digital signal) - detects water levels
* temperature sensors - detects room and water temperature - approximately 70F - 75F (varies on plant)
* humidity sensors - detects humidity - approximately 60% -70% (varies on plant)
* electro conductivity (EC) sensors - detects nutrient levels (varies on plant)
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

### System Layout
#### All-In-One Gravity I
* Fish tank on top shelf
* Grow beds in middle shelves
* Sump tank on bottom shelf
* Water pump in sump tank
* Fish tank drain to 2nd shelf, 2nd shelf drain to 3rd shelf, 3rd shelf drain to 4th shelf, and 4th to solid filter in the sump tank
* Each grow bed can use red worms to minimize clogging, hence, less maintenance
* Sump tank should have additional filter to ensure water pump is going to pump water without any large debris.
##### Pros
* Simple to setup
* Less mechnical parts
* Given there is no issue with clogging, no flooding when there is power outage
##### Cons
* Stop entire system when maintenance work is needed
* Limited shelf height for grow bed
##### Application
* Microgreen
* Lettuce
#### All-In-One Gravity II
* Grow beds on top four shelves
* Fish tank on bottom shelf
* Water pump in fish tank
* Fish tank pump to 1st shelf, 1st shelf drain to 2nd shelf, 2nd shelf drain to 3rd shelf, 3rd shelf drain to 4th shelf, 4th shelf drain to solid filter in the fish tank
* Each grow bed can use red worms to minimize clogging, hence, less maintenance
* Water pump needs to be placed within a filter bad to eliminate large solid debris
##### Pros
* Simple to setup
* Less mechnical parts
* Given there is no issue with clogging, no flooding when there is power outage
* One extra shelf for grow bed compares to All-In-On Gravity I
##### Cons
* Stop entire system when maintenance work is needed
* Limited shelf height for grow bed except the top shelf
* Extra maintenance work to clean up filter for water pump
##### Application
* Microgreen
* Lettuce

## Notes
* Bell siphon is used in flood-and-drain media bed to eliminate any mechnical part to minimize maintenance
* Red worms can be used in media bed to prevent clogging because they consume organic debris such as dead root, dead flowers and dead leaves from plants. They help to prevent mold on the grow bed due to organic debris left on grow bed surface. Worm casting also provide additional organic nutrients to plant.
* High temperature causes some of the vegetables to taste bitter. For example, lettuce.
