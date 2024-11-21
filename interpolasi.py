
Th1 = int(input("Masukkan Tahun Awal: "))
Th2 = int(input("Masukkan Tahun Akhir: "))
JP1 = float(input("Masukkan Jumlah Penduduk Awal (gunakan tanda koma untuk desimal): "))
JP2 = float(input("Masukkan Jumlah Penduduk Akhir (gunakan tanda koma untuk desimal): "))
TahunJP = int(input("Masukkan Tahun Perkiraan yang Diinginkan: "))


JPPerkiraan = JP1 + ((JP2 - JP1) / (Th2 - Th1)) * (TahunJP - Th1)

print(f"Jumlah Penduduk pada Tahun {TahunJP} adalah: {JPPerkiraan:.2f}")
