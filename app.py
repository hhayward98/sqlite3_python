import sqlite3
import db
from db import *


def WIFI():

	ESSID_list = []
	network_list = []

	file = open('wifi_info.txt', 'r')
	for line in file:
		line.strip()
		ESSID = line[:30]
		ESSID_list.append(ESSID)
	ESSID_list.remove(ESSID_list[0])

	for i in ESSID_list:
		c.execute('INSERT INTO WIFI_info (ESSID) VALUES("{sd}")'.format(sd=i))
		

	# c.execute('SELECT * FROM WIFI_info')

	# all_rows = c.fetchall()
	# print(all_rows)





def BLUEtooth():

	MAC_list = []
	Name_list = []

	file = open('bluetooth_info.txt')
	for line in file:
		MAC = line[:18]
		MAC.strip()
		MAC_list.append(MAC)

		Name = line[20:50]
		Name_list.append(Name)


	MAC_list.remove(MAC_list[0])

	for i in MAC_list:
		c.execute('INSERT INTO Bluetooth_info (MAC_Adress) VALUES("{num}")'.format(num=i))

	for i in Name_list:
		c.execute('INSERT INTO Bluetooth_info (Name) VALUES("{nm}")'.format(nm=i))



	
	# c.execute('SELECT * FROM Bluetooth_info')

	# all_rows = c.fetchall()
	# print(all_rows)

	
	

		
	

WIFI()
BLUEtooth()


