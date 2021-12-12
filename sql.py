import sqlite3
conn = sqlite3.connect('planes.db')
# conn.execute("CREATE TABLE planes (id INTEGER PRIMARY KEY, manufacturer TEXT, model TEXT, airline TEXT, quantity INTEGER)")

conn.execute('INSERT INTO planes VALUES(1, "Boeing", 737, "alaska", 2)')