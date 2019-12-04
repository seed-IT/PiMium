#!/bin/bash

if [ $# -gt 1 ]
then
        echo "Check arguments..."
        echo "Usage: sudo ./duck.sh h3r3-1s-duckdns-t0k3n"
else
        echo "Given token is: $1"
        echo url="https://www.duckdns.org/update?domains=seed-it&token=$1&verbose=true&pi=&ipv6=" | curl -k -o ~/Git/PiMium/duckdns/duck.log -K -
fi
