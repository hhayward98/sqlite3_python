import sqlite3


sqlite_file = '/Users/hunte/sqlite3_python/my_db.sqlite'  #database file name

table_name = 'my_table_2'

id_column = 'column_1'

column_name = 'column_2'


#connecting to database
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


# inserts an id with a specific value in a second column

try:
	#inserts a row with a specific value
	c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".format(tn=table_name, idf=id_column, cn=column_name))

except sqlite3.IntegrityError:
	print('ERROR: ID alreading exists in PRIMARY KEY column {}'.format(id_column))


# tries to insert an ID ( if it dose not exist yet)
# with a spcific value in a second column
c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".format(tn=table_name, idf=id_column, cn=column_name))

c.execute("UPDATE {tn} SET {cn}=('HI World') WHERE {idf}=(123456)".format(tn=table_name, cn=column_name, idf=id_column))


conn.commit()
conn.close()
