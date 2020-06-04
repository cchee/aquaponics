To setup Node-Red, MQTT, InfluxDB and Grafana, we uses ansible
Here are the steps to setup.

* Download the latest Raspbian LTE (buster) and install it on SD card
* Logged in to the Raspberry Pi and run the following commands
* echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" | sudo tee -a /etc/apt/sources.list.d/ansible.list
* sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
* sudo apt update
* sudo apt upgrade
* sudo apt install -y dirmngr
* suod apt install -y ansible
* Make sure /etc/ansible/hosts on master host has include the new raspberry pi hostname in at least one of the group.

Later on we are going to look into PXE boot installation for Raspberry Pi to setup everything via bare bone system with Ansible
and then use Ansible to manage all the needed updates, both configuration and software.

To keep things simple, there will be three Ansible playbooks
* One for Raspbian OS and security patches
* One for raspi-config
* One for bare bone software and basic configuration for all Raspberry Pi
* One for docker applications stack (Mosquitto, InfluxDB, Grafana)

