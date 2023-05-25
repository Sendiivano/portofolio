print("------------------------")

print("Aplikasi Menghitung Gaji")

print("------------------------")


no1 = int(input("Masukkan Jenis Golongan (antara 1 - 4): "))
no2 = int(input("Masukkan Jam Kerja (per minggu) : "))

g1 = 3000
g2 = 3500
g3 = 4000
g4 = 5000
#-------------------------------------
if (no1 == 1 )  and (no2 <= 40):
    tot = no2 * g1
    print("Gaji Anda :" , tot)
elif (no1 == 1 )  and (no2 > 40):
    tot = no2 * (g1 * 1.5)
    print("Gaji Anda :" , tot)
    #-------------------------------------
elif (no1 == 2 )  and (no2 > 40):
    tot = no2 * (g2 * 1.5)
    print("Gaji Anda :" , tot)
elif (no1 == 2 )  and (no2 <= 40):
    tot = no2 * g2
    print("Gaji Anda :" , tot)
    #-------------------------------------
elif (no1 == 3 )  and (no2 <= 40):
    tot = no2 * g3
    print("Gaji Anda :" , tot)
elif (no1 == 3 )  and (no2 > 40):
    tot = no2 * (g3 * 1.5)
    print("Gaji Anda :" , tot)
    #-------------------------------------
elif (no1 == 4 )  and (no2 <= 40):
    tot = no2 * g4
    print("Gaji Anda :" , tot)
elif (no1 == 4 )  and (no2 > 40):
    tot = no2 * (g4 * 1.5)
    print("Gaji Anda :" , tot)


