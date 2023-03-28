# All About the Loop
#
#28 MARCH 2023
class repet():

  def __init__(self, goAgain, answer, counter, addAnother):
    self.goAgain = goAgain
    self.answer = answer
    self.counter = counter
    self.addAnother = addAnother

  def methode(self):
    while True:
      print("This program is running")
      self.goAgain = input("Go again?: ")
      if self.goAgain == "no":
        break
    print("Aww, I was having a good time")

  def methode1(self):
    while True:
      self.counter = 0
      self.answer = int(input("Enter a number: "))
      print("Adding it up!!! ")
      self.counter += self.answer
      print("Current total is", self.counter)
      self.addAnother = input("add another? ")
      if self.addAnother == "no":
        break
    print("Bye!!!")


def call():
  t = repet("", 0, "", "")
  t.methode()
  t.methode1()


call()