#concatenating atau mengabungkan beberapa string jadi 1
#days 3
def exercise_1():
  Number = input("Give Me a Number : ")
  Group = input("Give me a Collective Noun for a Group Of Things:")
  Thing = input("Give me the name of a Weird or wacky thing: ")
  print("No I don't think that", Number,"is a", Group,
        "of",Thing,".that's just odd.")

def exercise_2():
  print("------------------------------------------------------")
  yourName = input("Name: ")
  whatYear = input("What year is it?: ")
  print(yourName, "thinks it is", whatYear)

def excercise_3():
  print("------------------------------------------------------")
  Food_Type = input("Name a Food: ")
  Plant_Type = input("Name a Type of Plant: ")
  Cooking_Method = input("Name a Method of Cooking: ")
  Desc = input("What Word Describes Burned Food: ")
  Item = input("Name a DIY Item: ")
  print(Cooking_Method, Food_Type,"with", Desc, Plant_Type, "on a bed of", Item)
  
#manggil Fungsi
def call():
  exercise_1()
  exercise_2()
  excercise_3()

  
call()