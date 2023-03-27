#525,600 minutes
#
#21 MARCH 2023

class times():
  def __init__(self, seconds=0, minutes=0, hours=0, days=0, months=0, year=0):
    self.seconds = seconds
    self.minutes = minutes
    self.hours = hours
    self.days = days
    self.months = months
    self.year = year
    
  def konversi_second(self):
    if self.seconds == "M" or self.seconds == "m" :
      self.seconds = int(input("Masukan Nilainya secondnya: "))
      t = self.seconds / 60
      print(t, "menit")
    elif self.seconds == "H" or self.seconds == "h":
      self.seconds = int(input("Masukan Nilainya secondnya: "))
      t = self.seconds / 3600
      print(t, "Hours")
    else:
      print("Masukan Nilai Yang bener")
  def Konversi_Menit(self):
    if self.minutes == "S" or self.minutes== "s" :
      self.minutes = int(input("Masukan Nilainya menitnya: "))
      t = self.minutes * 60
      print(t, "Second")
    elif self.minutes == "H" or self.minutes == "h" :
      self.minutes = int(input("Masukan Nilainya menitnya: "))
      t = self.minutes / 60
      print(t, "Hours")
    else:
      print("Masukan Nilai Yang bener!!")
      

def call(): 
  t = times()
  t.seconds = input("Masukkan nilai konversi second(menit atau jam) M/H: ")
  t.konversi_second()
  t.minutes = input("Masukkan nilai konversi Menit(second ke jam)  S/H:")
  t.Konversi_Menit()
  
call()