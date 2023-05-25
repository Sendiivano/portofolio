print("------------------------")

print("Aplikasi Menghitung Nilai Olahraga")

print("------------------------")

no1 = int(input("Masukkan Nilai MID : "))
no2 = int(input("Masukkan Nilai Tugas : "))
no3 = int(input("Masukkan Nilai UAS : "))

tot = (no1*0.3)+(no2*0.3)+(no3*0.4)

if (tot >= 85):
    print("Nilai Anda A")
elif (tot >=70) and (tot <85): 
    print("nilai Anda B")
elif (tot >= 55) and (tot < 70):
    print("Nilai anda C")
elif (tot < 55):
    print("Nilai Anda D")

