# Let's Cheat Continue
#
#29 MARCH 2023


class challenge18():

  def __init__(self, number, testing):
    self.number = number
    self.testing = testing

  def methode(self):
    self.number = 50
    while self.testing in range(0, 100):
      if self.testing > self.number:
        print("angka sangat besar")
      elif self.testing < self.number:
        print("angka sangat kecil")


def call():
  testing = challenge18(input("masukan angka"))
  testing.methode()


call()