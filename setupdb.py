import sqlite3
conn = sqlite3.connect('sportstimer.db')
conn.execute("CREATE TABLE sportstimer (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, sport_type TEXT, sport TEXT, length INTEGER, total_time REAL)")



                                      