belanja = [
    {"nama": "keyboard", "harga": 800000},
    {"nama": "monitor", "harga": 1700000}
]

totalHarga = sum(item["harga"] for item in belanja)
print(totalHarga)