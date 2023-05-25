
print("==============================")
print("Hitung Nilai")
print("==============================")

nt=int(input("Masukkan Nilai Tugas : "))
nq=int(input("Masukkan Nilai Quiz : "))
nuts=int(input("Masukkan Nilai UTS : "))
nuas=int(input("Masukkan Nilai UAS : "))



if nuas >= 80 :
    bonus= 6
elif nuas >= 70:
    bonus= 4
elif nuas >= 66:
    bonus= 2

tot=nt+nq+nuts+nuas+bonus
    
print("==============================")
print("Nilai Anda adalah = ",tot)
print("==============================")