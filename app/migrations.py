import sqlite3

# Connect to source and destination databases
source_conn = sqlite3.connect('database.db')

# Create cursors for source and destination databases
source_cursor = source_conn.cursor()

# Retrieve data from source database
source_cursor.execute("DROP TABLE IF EXISTS player")
sql = '''CREATE TABLE IF NOT EXISTS player (
            id INTEGER PRIMARY KEY,
            name TEXT
        )'''
source_cursor.execute(sql)

source_conn.close()

