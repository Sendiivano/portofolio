print("------------------------")

print("Aplikasi Menghitung Total Harga Barang")

print("------------------------")

no1 = int(input("Masukkan Jumlah Barang yang akan dibeli : "))


if (no1 < 100):
    tot = no1 * 10000
    print("Harga yang harus anda bayar adalah : ", tot)
elif (no1 >= 100) and (no1 < 150):
    tot = no1 *  9500
    print("Harga yang harus dibayar adalah : ", tot)
elif (no1 >= 150):
    tot = no1 * 9000
    print("Harga yang harus dibayar adalah : ", tot)

