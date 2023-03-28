# All About the Loop
#
#26 MARCH 2023

class looping():
  def __init__(self,counter,exit,text):
    self.counter = counter
    self.exit = exit
    self.text = text

  def methode(self):
    while self.counter < 10:
      print(self.counter)
      self.counter +=1
  def methode2(self):
    while self.exit != "yes":
      print("🥳")
      self.exit = input("exit?: ")
  def methode3(self):
    while self.text !="yes":
      self.text = input("What animal do you wont? ")
      if self.text =="cow":
        print("a cow goes moo")
        self.text = input("Do you want to exit: ")
      elif self.text =="lemur":
        print("Lemur goes awooga")
        self.text = input("Do you want to exit: ")
      else:
        self.text = input("Are you worng, Do you want to exit: ")

def call():
  testing = looping(1,"","")
  testing.methode()
  testing.methode2()
  testing.methode3()
call()