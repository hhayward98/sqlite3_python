import sqlite3
import db
from db import *

sqlite_file = '/root/Desktop/git_res/sqlite3_file/database.sqlite'


c.execute('SELECT * FROM WIFI_info')

all_rows = c.fetchall()
print(all_rows)


c.execute('SELECT * FROM Bluetooth_info')

all_rows = c.fetchall()
print(all_rows)