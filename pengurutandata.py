#Urutkan data dari yang terkecil ke yang terbesar

umur_adik = input("Umur adik : ")
umur_kakak = input("Umur kakak : ")
umur_ayah = input("Umur ayah : ")
umur_ibu = input("Umur ibu : ")

data = [umur_adik, umur_kakak, umur_ayah, umur_ibu]

data.sort()

print("Maka urutan umur dari yang paling muda hingga yang paling tua adalah :",data)
#.short() digunakan untuk mengurutkan data dari yang terkecil ke yang terbesar
#input harus dengan digit angka yang sama