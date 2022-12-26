#Tugas Terstruktur II

#No 1
dict = {
  "NIM": "20121097",
  "Nama": "Yasir Arafat",
  "Kelas": "Teknik Informatika",
  "Alamat": "Pasekaran"
}
print (dict)

#no 2
print ("---"*22)
print ("\t APLIKASI SEDERHANA MENGGUNAKAN STRING DAN ARRAY")
print ("---"*22)
print("NIM \t : %s" %dict["NIM"])
print("Nama \t : %s" %dict["Nama"])
print("Kelas \t : %s" %dict["Kelas"])
print("Alamat \t : %s" %dict["Alamat"])

#No 3
Kata = ["UNISS", "di", "belajar", "pada", "Mahasiswa", "data", "ruang",
"lab", "struktur", "semester", "tema", "Array", "String","dan", "di", "dengan", "Batang",3]
A=Kata[4] #mahasiswa
B=Kata[0] #UNISS
C=Kata[16] #Batang
D=Kata[9] #semester
E=Kata[17] #3
F=Kata[2] #belajar
G=Kata[8] #struktur
H=Kata[5] #Data
I=Kata[1] #Di
J=Kata[6]  #Ruang
K=Kata[7] #Lab
L=Kata[15] #Dengan
M=Kata[10] #Tema
N=Kata[11] #Array
O=Kata[13] #Dan
P=Kata[12] #String

print (A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P)

#no 4
from array import *
Nilai = array('i',[1,3,4,5,10,15,20])
formula1 = Nilai[4] + Nilai[1] * Nilai[5] 
formula2 = Nilai[1] * (Nilai[1] + Nilai[0]) / (Nilai[1] - Nilai [0])
formula3 = Nilai[5] ** 2 * Nilai[1] + Nilai[3] 
formula4 = Nilai[5] - Nilai[3] * Nilai[2] 
print ("---"*18)
print ("\t APLIKASI SEDERHANA MENGGUNAKAN ARRAY")
print ("---"*18)
print (Nilai[4],"+",Nilai[1],"*",Nilai[5],"=",formula1)
print (Nilai[1],"*",Nilai[1]+Nilai[0],":",Nilai[1]-Nilai[0],"=",(int(formula2)))
print (Nilai[5],"\b²","*",Nilai[1],"+",Nilai[3],"=",formula3)
print (Nilai[5],"-",Nilai[3],"*",Nilai[2],"=",formula4)


