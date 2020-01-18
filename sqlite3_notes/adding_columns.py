import sqlite3

sqlite_file = '/Users/hunte/sqlite3_python/my_db.sqlite'  #database file name

table_name = 'my_table_2'

id_column = 'primary_column' # name of the Primary Key colunm

new_column1 = 'column_2'

new_column2 = 'column_3'

column_type = 'TEXT' # other variables are, INTEGER, TEXT, NULL, REAL, BLOB

default_val = 'Hello World' 

#connecting to database
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


# adding new column without row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name, cn=new_column2, ct=column_type))


# adding a new column with defalut row value

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'".format(tn=table_name, cn=new_column2, ct=column_type, df=default_val))


#committing changes then closing the connection to the database
conn.commit()
conn.close()


