import sqlite3
import json
import requests
from bottle import app, route, run
from bottle_cors_plugin import cors_plugin

from sqlite3.dbapi2 import Cursor
conn = sqlite3.connect('sportstimer.db')

def user_details():
  name = input("Please enter your name ")       
  return name



def getsport():
  options = ["swimming", "running"]  
  for i in range (len(options)):
   print(i , ":" , options[i])
  sel_sport = input("select a sport: ") 
  return options[int(sel_sport)]


def get_event_details():
  pool_length = input("Please enter the pool length in yards ")
  stroke = input("What stroke are you swimming ")
  event = {
    "pool_length": pool_length,
    "stroke": stroke
  }   
  return event


def save_event():  
  # mock event , use from webservice
  event = {
    "name": "Ishaan",
    "sport": "swimming",
    "sport_type": "freestyle",
    "pool_length": 25, 
    "total_time": 3208
  }
  # result = conn.execute('INSERT INTO sportstimer VALUES(event["name"], event["sport"], event["sport_type"], event["pool_length"], event["total_time"]')
  result = conn.execute('INSERT INTO sportstimer (name, sport, sport_type, length, total_time) values (?, ?, ?, ?, ?)', (event["name"], event["sport"], event["sport_type"], event["pool_length"], event["total_time"]))
  conn.commit()
  if result == 1:
    return "Saved"



def get_events():
  cur = conn.cursor()
  result = cur.execute('SELECT * from sportstimer')
  rows = cur.fetchall()
  return json.dumps(rows)
  # for row in rows:
  #   print (row)





# name = user_details()
# sport = getsport()
# event = get_event_details()
# save_event()


# print ("Hi " + name + "," + "
#  you are planning to play " + sport + ".")
@route('/events', method='GET')
def hello():
  return get_events()

@route('/events', method='POST')
def index():
  postdata = request.body.read()
  print(postdata)

app = app()
app.install(cors_plugin('*'))

run(host='localhost', port=8001, debug=True)