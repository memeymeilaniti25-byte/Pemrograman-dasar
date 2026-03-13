lebar = int(input("Masukkan lebar persegi panjang: "))
panjang = int(input("Masukkan panjang persegi panjang: "))
luas = panjang * lebar
keliling = 2 * (panjang + lebar)
if luas > 100:
    print("Luas besar")
else:
        print ("Luas kecil")