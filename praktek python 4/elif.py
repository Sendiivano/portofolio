
nilai=float(input("Masukkan Nilai Anda: "))

if nilai>=80:
    ket="A"
elif nilai>=70:
    ket="B"
elif nilai>=60:
    ket="C"
elif nilai>=50:
    ket="D"
elif nilai<50:
    ket="E"
    
print("Nilai Mutu Anda ",ket)