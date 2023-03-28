#Nesting Dolls Code
#
#19 MARCH 2023

def exercise_1():
  activity=input("What are you doing in sunday? ")
  if activity.lower() == "joging":
    print(activity.capitalize(),"is healthy lifestyle!!!.")
    Where =input("Where do you joging? ")
    if Where == "Hi":
      print(activity.capitalize(),"in",Where,"a great place!!!")
    else:
      print("interesting place")
  elif activity.lower() == "sleep":
    print(activity.capitalize(),"bad habits!!!")
  else:
    print("have a nice day")
def call():
  exercise_1()
call()