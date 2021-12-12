def user_details():
  name = input("Please enter your name ")       
  return name

name = user_details()

def getsport():
  options = ["swimming", "running"]  
  for i in range (len(options)):
   print(i , ":" , options[i])
  sel_sport = input("select a sport: ") 
  return options[int(sel_sport)]

sport = getsport()

print ("Hi " + name + "," + " you are planning to play " + sport + ".")
