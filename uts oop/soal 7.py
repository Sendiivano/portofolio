print("------------------------")

print("Aplikasi Menentukan Bilangan paling besar dari 3 angka")

print("------------------------")

no1 = int(input("Masukkan Bilangan Pertama : "))
no2 = int(input("Masukkan Bilangan Kedua : "))
no3 = int(input("Masukkan Bilangan Ketiga : "))


if (no1 == no2 == no3):
    print("Bilangan yang anda masukkan sama besarnya")
elif (no1 >= no2 >= no3): 
    print("Bilangan Pertama adalah Bilangan Terbesar")
elif (no1 <= no2 >= no3):
    print("Bilangan Kedua adalah bilangan Terbesar")
elif (no1 <= no2 <= no3):
    print("Bilangan Ketiga adalah Bilangan Terbesar")

