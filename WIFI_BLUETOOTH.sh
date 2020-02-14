#!/bin/bash

airmon-ng start wlan0

i = $1

timeout -sHUP $1 airodump-ng wlan0mon --write wifi_info
 

rm wifi_info-01.cap
rm wifi_info-01.log.csv
rm wifi_info-01.kismet.csv
rm wifi_info-01.kismet.netxml

airmon-ng stop wlan0mon

sleep 10s

service bluetooth start

sleep 5s

hcitool -i hci0 scan >> bluetooth_info.txt

sleep 10s

python3 ./app.py

sleep 10s

rm wifi_info-01.csv

echo All done 
