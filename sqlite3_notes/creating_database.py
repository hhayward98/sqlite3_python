import sqlite3


sqlite_file = '/Users/hunte/sqlite3_python/my_db.sqlite'  #database file name

table_name1 = 'my_table_1'

table_name2 = 'my_table_2' 

new_field = 'column_1'

field_type = 'INTEGER'


#connecting to the database file

conn = sqlite3.connect(sqlite_file)

c = conn.cursor()


# creating sqlite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn=table_name1, nf=new_field, ft=field_type))

# creating a second table with 1 column and set as Pramary Key
# Primary Key must have unique values
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=table_name2, nf=new_field, ft=field_type))


conn.commit()
conn.close()