#Days_4 "Print" in Color!
#
#17 MARCH 2023

def exercise_1():
  Text = ("Welcome to your adventure simulator. I am going to ask you a bunch of question and then create an epic story with you as the start")
  print(Text)
  print("___________________________________________\n")
  Name = input("What is your name?: ")
  Worst = input("What is your worst enemy's name : ")
  Super = input("What is your superpower: ")
  Live = input("Where do you live: ")
  Food = input("What is your favorite food: ")
  print("Hello", Name ,"!Your ability to",Super,"will make sure you never have to look at", Worst, "again. Go eat", Food, "as you walk down the streets of", Live, "and use ",Super,"for good and not evil!" )
  print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")

#Call 
def Call():
  exercise_1()

Call()