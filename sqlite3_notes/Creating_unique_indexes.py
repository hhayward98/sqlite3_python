import sqlite3

sqlite_file = '/Users/hunte/sqlite3_python/my_db.sqlite'  #database file name

table_name = 'my_table_2'

id_column = 'column_1'

new_column = 'unique_names' 

column_type = 'TEXT'

index_name = 'unique_index'


conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


#adding a new column and update some record 
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_name, cn=new_column, ct=column_type))

c.execute("UPDATE {tn} SET {cn}='Hunter_H' WHERE {idf}=123456".format(tn=table_name, idf=id_column, cn=new_column))


#creating a unique index
c.execute('CREATE INDEX {ix} on {tn}({cn})'.format(ix=index_name, tn=table_name, cn=new_column))

# dropping the index
# aviod confics with update/insert functions
c.execute('DROP INDEX {ix}'.format(ix=index_name))


conn.commit()
conn.close()