import sqlite3

sqlite_file = '/root/Desktop/Projects/raspbery_pi_zero/database2.sqlite' # remeber to chaange PATH for each OS


conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

