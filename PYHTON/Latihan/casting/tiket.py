print("Selamat datang di pemesanan tiket bioskop!")
pilihFilm = input("pilih jenis film ( Reguler / Premium ) :  ").capitalize()
jumlahTiket = int(input("mau berapa tiket? : "))

if pilihFilm == "Reguler":
    hargaTiket = 25000
    harga = jumlahTiket*hargaTiket
elif pilihFilm == "Premium":
    hargaTiket = 50000
    harga = jumlahTiket*hargaTiket
else: 
    print("kamu memilih jenis yang salah")

discount = 0
if jumlahTiket > 3:
    discount = harga*(10/100)

print(f"\n=== Detail Pemesanan ===\n" \
f"Jenis Film      : {pilihFilm}\n"
f"Jumlah Tiket    : {jumlahTiket}\n"
f"Harga Per Tiket : {hargaTiket}\n"
f"Diskon 10%      : {discount}\n"
f"Total Harga     : {harga - discount}\n"
f"=========================")