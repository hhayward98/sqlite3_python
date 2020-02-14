import sqlite3

sqlite_file = '/root/Desktop/git_res/sqlite3_file/database.sqlite' # remeber to change PATH for each OS


conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


# creating the table and column for wifi info
c.execute('CREATE TABLE WIFI_info(BSSID text not null unique)');

# creating the table and column for bluetooth info
c.execute('CREATE TABLE Bluetooth_info(MAC_Adress text not null unique)');

conn.commit()
conn.close()


