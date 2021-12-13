import sqlite3
conn = sqlite3.connect('sports-timer.db')
# conn.execute("CREATE TABLE planes (id INTEGER PRIMARY KEY, manufacturer TEXT, model TEXT, airline TEXT, quantity INTEGER)")

conn.execute("CREATE TABLE sportstimer ( \
    id INTEGER PRIMARY KEY AUTOINCREMENT, \
    name TEXT, \
    sport TEXT, \
    sport_type TEXT, \
    length INTEGER \
    total_time REAL);")
