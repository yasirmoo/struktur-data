from array import *
bilangan1 = array('i',[10,20,30,40,50]) #Data utama yang akan olah

formula1 = bilangan1[0] + bilangan1[1] * bilangan1[0] #Rumus hitungan, akan di tarik untuk hasil perhitungan
formula2 = bilangan1[1] + bilangan1[1] * bilangan1[0] 

print (bilangan1[0])
print (bilangan1[1])

print (bilangan1[0],"+",bilangan1[1],"*",bilangan1[0],"=",formula1) #tugas menampilkan string dan hasil penjumlahan
print (bilangan1[1],"+",bilangan1[1],"*",bilangan1[0],"=",formula1)
