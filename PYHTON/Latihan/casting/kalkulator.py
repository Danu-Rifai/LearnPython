# kalkulator

angka1 = int(input("masukan angka pertama: "))
angka2 = int(input("masukan angka kedua: "))

print("\nPilih 1, 2, 3, atau 4\n" \
"1. Penjumlahan\n" \
"2. Pengurangan\n" \
"3. Perkalian\n" \
"4. Pembagian")
inputOperasi = int(input("pilih operasi: "))

if inputOperasi == 1:
    print(f"hasil dari {angka1} + {angka2} adalah {angka1+angka2}")
elif inputOperasi == 2:
    print(f"hasil dari {angka1} - {angka2} adalah {angka1-angka2}")
elif inputOperasi == 3:
    print(f"hasil dari {angka1} x {angka2} adalah {angka1*angka2}")
elif inputOperasi == 4:
    print(f"hasil dari {angka1} : {angka2} adalah {angka1/angka2}")
else: 
    print("anda memilih angka yang salah")