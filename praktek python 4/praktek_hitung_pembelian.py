print("==============================")
print("==============================")
print("==============================")

paket=input("Masukkan nama paket = ")
beli=float (input("Masukkan jumlah paket yang dibeli = "))

if paket=="Boom 1":
    harga = 35000
elif paket=="Boom 2":
    harga = 45000
elif paket=="Boom 3":
    harga = 50000

jumlah_pkt = (float(beli * harga))
jumlah =(float( beli * harga) * 0.11)
total = (float(jumlah + jumlah_pkt ))

print("Jumlah yang harus dibayarkan adalah ",total)