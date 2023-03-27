#Gradebook Builder
#
#24 MARCH 2023

class Rank():
  def __init__(self, nama, nilai):
    self.nama = nama
    self.nilai = nilai
    
  def penentuan(self):
    if self.nilai >= 90 and self.nilai <= 100:
      print(self.nama,"Value A+,CONGRATULATIONS")
    elif self.nilai >= 80 and self.nilai <= 89:
      print(self.nama,"Value A,Bagus. Pertahankan")
    elif self.nilai >= 70 and self.nilai <= 79:
      print(self.nama,"Value B,Tetap semangat")
    elif self.nilai >= 60 and self.nilai <= 69:
      print(self.nama,"Value C,Tingkatkan Lagi")
    elif self.nilai >= 50 and self.nilai <= 59:
      print(self.nama,"Value D,Jangan menyerah")
    else:
      print(self.nama,"Belajar Yang Giat ok!!!!!!!!")
      
def Masukan(): 
  nama = input("Masukan Nama? ")
  nilai = int(input("Masukan Nilai? "))
  t = Rank(nama,nilai)
  t.penentuan()
Masukan()



