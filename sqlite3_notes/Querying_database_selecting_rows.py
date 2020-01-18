import sqlite3

sqlite_file = '/Users/hunte/sqlite3_python/my_db.sqlite'  #database file name

table_name = 'my_table_2'

id_column = 'column_1'

some_id = 123456

column_2 = 'column_2'

column_3 = 'cloumn_3'


conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# contents of all columns for row that match a certain value in 1 coulmn
c.execute('SELECT * FROM {tn} WHERE {cn}="Hi World"'.format(tn=table_name, cn=column_2))

all_rows = c.fetchall()
print('1):', all_rows)


# value of a particular column for rows that match a certain value in cloumn_1
c.execute('SELECT ({coi}) FROM {tn} WHERE {cn}="Hi World"'.format(coi=column_2, tn=table_name, cn=column_2))

all_rows = c.fetchall()
print('2):', all_rows)


#value of 2 particular columns for rows that match a certain value in 1 column
#c.execute('SELECT {coi1},{coi2} FROM {tn} WHERE {coi1}="Hi World"'.format(coi1=column_2, coi2=column_3, tn=table_name, cn=column_2))

all_rows = c.fetchall()
print('3):', all_rows)


# selecting only up to 10 rows that match a certain value in 1 column
c.execute('SELECT * FROM {tn} WHERE {cn}="Hi World" LIMIT 10'.format(tn=table_name, cn=column_2))

ten_rows = c.fetchall()
print('4):', ten_rows)


# check if a certain ID exists and print its column contents
c.execute("SELECT * FROM {tn} WHERE {idf}={my_id}".format(tn=table_name, cn=column_2, idf=id_column, my_id=some_id))

id_exists = c.fetchone()
if id_exists:
	print('5): {}'.format(id_exists))
else:
	print('5) {} does not exits'.format(some_id))

conn.close()

