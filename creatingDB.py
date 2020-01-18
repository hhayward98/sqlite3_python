import sqlite3

sqlite_file = '/root/Desktop/Projects/raspbery_pi_zero/database.sqlite' # remeber to change PATH for each OS

table_name1 = 'WIFI_info'

table_name2 = 'Bluetooth_info'

column_1 = 'ESSID'

column_2 = 'MAC_Adress'

column_3 = 'Name'

column_4 = 'Network_type'

column_type = "TEXT"



conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


# creating the table and column for wifi info
c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn=table_name1, nf=column_1, ft=column_type))

c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn=table_name2, nf=column_2, ft=column_type))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name2, cn=column_3, ct=column_type))

conn.commit()
conn.close()


