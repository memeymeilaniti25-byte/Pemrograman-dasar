jarak = int(input("Massukkan jarak yang ditempuh :"))
waktu = int(input("Massukkan waktu tempuh :"))
kecepatan = jarak / waktu
if kecepatan > 80:
    print("Kecepatan tinggi")
else:
    print("kecepatan rendah")
print (f"kecapatan rata-rata: {kecepatan} km/jam")