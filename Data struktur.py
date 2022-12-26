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
A=Kata[4]
B=Kata[1]
C=Kata[0]
D=Kata[16]
E=Kata[9]
F=Kata[17]
G=Kata[2]
H=Kata[14]
I=Kata[6]
J=Kata[7]
K=Kata[15]
L=Kata[10]
M=Kata[11]
N=Kata[12]
O=Kata[13]
P=Kata[8]
Q=Kata[5]
print (A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q)

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


