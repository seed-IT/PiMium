#!/bin/sh
# This one will automatically clone the repo with all the code for the RaspBerry
# It will also install the necessary modules

sudo apt update -y
sudo apt upgrade -y
sudo pip install RPI.GPIO adafruit-blinka adafruit-bme280 adafruit-circuitpython-bme280
sudo pip3 install RPI.GPIO adafruit-blinka adafruit-bme280 adafruit-circuitpython-bme280
sudo pip install --upgrade setuptools
cd /
git clode https://github.com/seed-IT/PiMium.git rose

