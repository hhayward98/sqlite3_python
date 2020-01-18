import sqlite3

sqlite_file = '/root/Desktop/Projects/raspbery_pi_zero/database.sqlite' # remeber to chaange PATH for each OS

table_name1 = 'WIFI_info'

table_name2 = 'Bluetooth_info'

column_1 = 'ESSID'

column_2 = 'MAC_Adress'

column_3 = 'Name'

column_4 = 'Network_type'

column_type = "TEXT"


conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

