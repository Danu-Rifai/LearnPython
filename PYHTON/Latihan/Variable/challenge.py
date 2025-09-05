from datetime import date

tahunSekarang = int(date.today().strftime("%Y"))
namaDepan = "Danu"
namaBelakang = "Rifai"
tahunLahir = 2008

print(f"Halo, nama lengkap saya {namaDepan} {namaBelakang}. Saya berusia {tahunSekarang - tahunLahir} tahun.")