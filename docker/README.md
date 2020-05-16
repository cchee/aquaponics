To setup Node-Red, MQTT, InfluxDB and Grafana, we uses IOTstack.
To setup IOTstack, we need git and docker, and we uses the
following steps to setup.

* Download the latest Raspbian LTE (buster) and install it on SD card
* Logged in to the Raspberry Pi and run the following commands
* sudo raspi-config
* select Network Options to setup Wifi or network connection
* select Update in raspi-config
* select Change User Password in raspi-config
* select Localisation Options in raspi-config (optional)
* select Interfacing Options in raspi-config (disable ssh, enable SPI, enable ISC)
* sudp apt update
* sudp apt upgrade
* Secure Raspberry (https://www.raspberrypi.org/documentation/configuration/security.md)
* sudo apt install apt-utils curl git gpiod nginx python3-pip python3-paho-mqtt rsync 
* sudo pip3 install RPi.GPIO
* git clone https://github.com/gcgarner/IOTstack.git
* cd IOTstack
* ./menu.sh
*   select Install Docker 
*   select Backup options (setup and use DropBox for data backup, select Dropbox-Uploader)
*   select Miscellaneous Commands (select all options)
*   select Build Stack (select portainer, nodered influxdb, grafana, mosquitto)
* docker-compose up -d
* cat "0 * * * * sudo ~/IOTstack/scripts/docker_backup.sh > /dev/null 2>&1" > crontab -e

SECURITY ISSUES:
Docker does not honor ufw firewall rules, so external browser can still access port that were not supposedly accessible under UFW rules. Although gcgraner menu.sh does a lot of heavy lifting and in fact it is amazing and time saver, it does not include SSL yet. For home use, it seems fine as long as wifi access and firewall are setup properly.

One possible way to secure all docker container to use https is to setup nginx with reverse proxy, check out https://www.freecodecamp.org/news/docker-nginx-letsencrypt-easy-secure-reverse-proxy-40165ba3aee2/

To setup docker-compose.yml with ssl, ssl key and ssl cert files need to be created. Use scripts under aquaponics/scripts to generate self-signed SSL certificates

I have tried to secure docker with ufw, check out https://github.com/chaifeng/ufw-docker and to make sure ufw has the following rules, but it does not seem to work for me.
* sudo ufw default deny incoming
* sudo ufw allow ssh

NOTE:
To tie Node-Red with InfluxDB and Grafana together, check out https://www.youtube.com/watch?v=JdV4x925au0.  You can skip the part it talks about Peter's script setup and influxdb sql lite comparison if you are limited in time.

To access influxdb, after login to Raspberry Pi and use influx DB CLI
* docker exec -it influxdb /bin/bash
* influx
