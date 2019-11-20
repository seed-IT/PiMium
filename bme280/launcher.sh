#!/bin/sh
#This script is used to automaticaly execute the script bme280.py.
#The bme280 will connect the BME sensor and the RaspBerry Pi.

cd /rose/bme280
sudo python3 bme280.py
cd ..
