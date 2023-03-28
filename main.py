# Let's Cheat Continue
#
#28 MARCH 2023


class next17():

    def __init__(self, direction):
        self.direction = direction

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


def call():
    start = next17("")
    start.Methode1()


call()