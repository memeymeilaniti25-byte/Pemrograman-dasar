angka_pertama = int(input("Masukkan angka pertama:"))
angka_kedua = int(input("Masukkan angka kedua:"))
angka_ketiga = int(input("Masukkan angka ketiga:"))

if angka_pertama > angka_kedua and angka_pertama > angka_ketiga:
    print (f"Angka terbesar adalah {angka_pertama}")
elif angka_kedua > angka_pertama and angka_kedua > angka_ketiga:
    print (f"Angka terbesar adalah {angka_kedua}")
else:
    print (f"Angka terbesar adalah {angka_ketiga}")