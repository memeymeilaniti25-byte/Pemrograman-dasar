total_belanja = 250000
if total_belanja > 500000:
    diskon = total_belanja *0.2
elif total_belanja > 250000:
    diskon = total_belanja * 0.1
else:
    diskon = 0

total_bayar = total_belanja - diskon
print (f"Total belanja memey: Rp.{total_belanja:,},Diskon yang didapat: Rp. {diskon:,}, Total yang harus dibayar: Rp. {total_bayar:,}")
