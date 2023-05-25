
print("==============================")
print("Hitung Gaji")
print("==============================")

jabatan=input("Masukkan Jabatan Anda : ")
jk=int(input("Masukkan Jumlah Jam Kerja : ") )
jl=float(input("Masukkan Jumlah Jam Lembur : ") )
abs=float(input("Masukkan Jumlah Tidak Hadir : ") )


tjk=jk * 15000
tjl=jl * 10000
um=jk * 10000
tabs=abs * 100000

if jabatan=="Manager":
    gaji = 6500000
elif jabatan=="wakil manager":
    gaji = 4500000
elif jabatan=="Kepala sub bagian":
    gaji = 3000000
elif jabatan=="HRD":
    gaji = 2000000
    
tot=gaji-tjk+tjl+um-tabs

print("Jabatan = ",jabatan)
print("Gaji Pokok (belum termasuk bonus dan potongan) = ",gaji)
print("Gaji Setelah Perhitungan = ",tot)