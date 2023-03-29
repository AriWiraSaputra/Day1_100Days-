#Rock, Paper, Scissors = 
#
#22 MARCH 2023

from getpass import getpass as input

class suit():
  def __init__(self,player1,player2):
    self.player1 = player1
    self.player2 = player2

  def methode(self):
    if self.player1 == "r":
      if self.player2 =="s":
        print("player1, You Winnn!!!!...")
        print("player2, You loseee!!!!...")
      elif self.player2=="p":
        print("player1,You Losee!!!!...")
        print("player2,You Winnnn!!!!...")
      else:
        print("player1, player2,You seri!!!!...")
    elif self.player1 =="p":
      if self.player2=="r":
        print("player1, You Winnn!!!!...")
        print("player2, You loseee!!!!...")
      elif self.player2=="s":
        print("player1,You Losee!!!!...")
        print("player2,You Winnnn!!!!...")
      else:
        print("player1, player2,You seri!!!!...")
    else:
      if self.player2 =="r":
        print("player1,You Losee!!!!...")
        print("player2,You Winnnn!!!!...")
      elif self.player2 =="p":
        print("player1,You Winnn!!!!...")
        print("player2,You loseee!!!!...")
      else:
         print("player1,player2,You seri!!!!...")

def call():
  while True:
    player1 = input("Masukan Pilihan player 1: ")
    player2 = input("masukan pilihan player 2: ")
    t = suit(player1, player2)
    t.methode()
call()