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

name = user_details()
sport = getsport()
event = get_event_details()



print ("Hi " + name + "," + " you are planning to play " + sport + ".")
