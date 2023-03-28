#Nesting Dolls Code
#
#19 MARCH 2023

def exercies_1():
  TvShow = input("What is your favorite character? ")
  if TvShow == "Peppa Pig":
    print("Ugh,Why?")
    FaveCharacter = input("Who is Your Favorite Character? ")
    if FaveCharacter == "Daddy pig":
      print("Right answer")
    else:
      print("Nah, Dady pig's the greatest")
  elif TvShow == "paw patrol":
    print("Aww, sad times")
  else:
    print("Yeah, That's cool and all....")

def exercies_2():
  order = input("what would you like to order: pizza or humberger?")
  if order == "humburger":
    print("Tanks you")
    cheese = input("Do you wont cheese? ")
    if cheese == "yes":
      print("No cheese it is")
    else:
      print("allright")
  elif order == "pizza":
    print("Pizza coming up")
    toppings = input("do you wont pepperoni on that?")
    if toppings == "yes":
      print("we will add pepperoni")
    else:
      print("your pizza will not have pepperoni")
  else:
    print("please, order again")

def exercies_3():
  Movie = input("What kind of movies do you like? ")
  if Movie == "Marvel":
    print("Nice Movie!!!...")
    Filem = input("What kind of movies do you like a Harry Potter? ")
    if Filem == "yes":
      print("nice Movies")
    else:
      print("i think so...")
  elif Movie == "disny":
    print("I like Too")
  else:
    print("I don't like Movie, I like Music")
    
def call():
  exercies_1()
  exercies_2()
  exercies_3()
call()
