#!/bin/bash


nmcli dev wifi >> wifi_info.txt

sleep 10s

service bluetooth start

sleep 5s

hcitool -i hci0 scan >> bluetooth_info.txt

sleep 10s

python3 ./app.py
