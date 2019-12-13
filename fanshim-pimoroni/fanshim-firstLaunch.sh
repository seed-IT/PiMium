#!/bin/sh

git clone https://github.com/pimoroni/fanshim-python.git ~/Git/fanshim-python
cd ~/Git/fanshim-python
sudo ./install.sh
cd ~/Git/fanshim-python/examples
sudo ./install-service.sh --on-threshold 60 --off-threshold 50 --delay 2 --brightness 128

