#Nesting Dolls Code
#
#20 MARCH 2023

def exercise_1():
  MyScore = int(input("Your Score: "))
  if MyScore > 1000:
    print("Winner!!!")
  else:
    print("Try again😭")

def exercise_2():
  myPI = float(input("What is PI to 3dp? "))
  if myPI == 3.142:
    print("It's Number ", myPI)
  else:
    print("Try again")
def exercise_3():
  score = int(input("What was your score on the test? "))
  if score >= 80:
    print("Not too shabby")
  elif score > 70:
    print("acceptable")
  else:
    print("Dude, you need to study more!")
def call():
  exercise_1()
  exercise_2()
  exercise_3()
  
call()