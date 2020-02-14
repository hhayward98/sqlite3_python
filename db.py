import sqlite3

sqlite_file = '/root/Desktop/git_res/sqlite3_file/database.sqlite' # remeber to chaange PATH for each OS


conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

