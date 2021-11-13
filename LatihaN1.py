#Program penentuan predikat nilai

nama = input("Masukkan Nama : ")
uts = input("masukkan nilai UTS : ")
uas = input("Masukkan nilai UAS : ")
tugas = input ("Masukkan nilai Tugas : ")

hasil = (int(tugas)*.2) + (int(uts)*.4) + (int(uas)*.4)
keterangan = ("Tidak Lulus" , "Lulus") [hasil > 60]
if hasil >80:
    predikat = "A"
elif hasil >70:
    predikat = "B"
elif hasil >50:
    predikat = "C"
else :
    predikat = "D"

print("\nNama", nama)
print("UTS", uts)
print("UAS",uas)
print("Tugas",tugas)
print("Hasil",hasil)
print("Predikat",predikat)
print("Keterangan",keterangan)
