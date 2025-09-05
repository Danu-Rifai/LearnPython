import requests

api_key = "6c944c50f7050b92c4811f46"
url = "https://v6.exchangerate-api.com/v6/6c944c50f7050b92c4811f46/latest/USD"

response = requests.get(url)

data = response.json()

jumlahUang = int(input("masukan jumlah uang (USD): "))
nilaiDasar = "USD"
convertTo = input("masukan mau ke mata uang apa? cth: IDR, EUR, JPY : ").upper()

if convertTo in data['conversion_rates']:
    converResult = jumlahUang*data['conversion_rates'][convertTo]
    print(f"{jumlahUang} {nilaiDasar} bernilai {converResult} {convertTo}")
else:
    print("data tidak ada")