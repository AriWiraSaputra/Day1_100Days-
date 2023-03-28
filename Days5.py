#Days_5 "if this else that?!""
#
#18 MARCH 2023

def exercise_1():
  name = input("what's your name?: ")
  if name == "Davit" :
    print("Welcome Dude!")
    print("You're just the baldest dude I've ever seen")
  else:
    print("Who on earth are you?!...")
    
def exercise_2():
  catsOrDogs = input("Are you a cat person? Or a dog person?: ")
  if catsOrDogs == "cat":
    print("Meowwww")
  else:
    print("Woof")

def exercise_3():
  drink = input("Do you prefer coffe or tea?")
  if drink == "coffe":
    print("Tea is Better")
  else:
    print("Excellent choice")

def challenge():
  Text = ("--Marvel Movie Character Creator--")
  print(Text)
  like = input("Do you like 'hanging around'?:")
  if like == "no":
    print("Then you're not Spider-Man")
  else:
    print("Nice")
  have = input("Do you have a 'gravelly' voice?: ")
  if have == "no":
    print("Aww, then you're not korg")
  else:
    print("Nice")
  feel = input("Do you often feel'Marvelouse?: ")
  if feel == "yes":
    print("Aha! You're Caption Marvel! Hi!")
  
def call():
  exercise_1()
  exercise_2()
  exercise_3()
  challenge()

call()