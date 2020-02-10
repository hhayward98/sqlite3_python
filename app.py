import sqlite3
import db
from db import *
import csv


def WIFI():

	ESSID_list = []
	network_list = []
	start = 0
	end = 1
	file = open('wifi_info-01.log.csv', 'r')
	line = file.readline()
	BSSID_list = []
	for line in file:
		data = line.split(',')
		BSSID = data[3]
		if BSSID not in BSSID_list:
			BSSID_list.append(BSSID)

	for i in BSSID_list:
		c.execute('INSERT or IGNORE INTO WIFI_info (BSSID) VALUES("{sd}")'.format(sd=i))
		

	
	conn.commit()

# make the database only add unique BSSID


	# c.execute('SELECT * FROM WIFI_info')

	# all_rows = c.fetchall()
	# print(all_rows)





def BLUEtooth():

	MAC_list = []

	file = open('bluetooth_info.txt')
	for line in file:
		MAC = line[:18]
		MAC.strip(" ")
		MAC_list.append(MAC)



	MAC_list.remove(MAC_list[0])

	for i in MAC_list:
		c.execute('INSERT or IGNORE INTO Bluetooth_info (MAC_Adress) VALUES("{num}")'.format(num=i))


	conn.commit()
	
	# c.execute('SELECT * FROM Bluetooth_info')

	# all_rows = c.fetchall()
	# print(all_rows)

	
	

		


WIFI()
BLUEtooth()

conn.close()


