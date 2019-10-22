#!/usr/bin/env sh

echo url="https://www.duckdns.org/update?domains=seed-it&token=e7270911-1842-4813-92fd-2c8f693e86ec&verbose=true&pi=&ipv6=" | curl -k -o ~/Git/PiMium/duckdns/duck.log -K -

