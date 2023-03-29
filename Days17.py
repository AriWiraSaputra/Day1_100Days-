# Let's Cheat Continue
#
#28 MARCH 2023


class next17():
    def __init__(self, direction,player1,player2):
        self.direction = direction
        self.player1 = player1
        self.pplayer2 = player2
       
    def Methode1(self):
        while True:
            print("You are in a corridor, do you go left or right?")
            self.direction = input("> ")
            if self.direction == "right":
                print("You have fallen to your death")
                continue
            elif self.direction == "left":
                break
            else:
                print("ahh! you're a genius,you've won")
              
    def Methode2(self):
      #from getpass import getpass as input
      player1 = 0
      player2 = 0
 
      while True:
        self.player1 = input("Enter your chose player 1: ")
        self.player2 = input("Enter your chose Player 2: ")
        #Rock, Paper, Scissors
        if self.player1 =="rock" and self.player2 == "paper":
          player2 +=1
          if player2 == 3:
             print("Score Player2 =", player2 ,"Congratulation player2,  you win!!!")
             break
        elif self.player1 =="rock" and self.player2 == "scissors":
          player1 +=1
          if player1 == 3:
             print("Score Player1 =", player1 ,"Congratulation player1,  you win!!!")
             break
        elif self.player1 =="scissors" and self.player2 == "rock":
          player2 +=1
          if player2 == 3:
             print("Score Player2 =", player2 ,"Congratulation player2,  you win!!!")
             break
        elif self.player1 =="scissors" and self.player2 == "paper":
          player1 +=1
          if player1 == 3:
             print("Score Player1 =", player1 ,"Congratulation player1,  you win!!!")
             break
        elif self.player1 =="paper" and self.player2 == "rock":
          player1 +=1
          if player1 == 3:
             print("Score Player1 =", player1 ,"Congratulation player1,  you win!!!")
             break
        elif self.player1 =="paper" and self.player2 == "scissors":
          player2 +=1
          if player2 == 3:
             print("Score Player2 =", player2 ,"Congratulation player2,  you win!!!")
             break
        elif self.player1 =="rock" and self.player2 == "rock":
          continue
        elif self.player1 =="scissors" and self.player2 == "scissors":
          continue
        elif self.player1 =="paper" and self.player2 == "paper":
          continue
          
def call():
    start = next17("","","")
    start.Methode1()
    start.Methode2()


call()