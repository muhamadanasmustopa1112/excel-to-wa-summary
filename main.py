import pandas as pd
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

# Konfigurasi
API_KEY = os.getenv("STARSENDER_API_KEY")  # API Key dari Starsender
PHONE = os.getenv("PHONE_NUMBER")  # Format internasional: 628xxx
API_URL = "https://api.starsender.online/api/send"

//
# Baca file Excel
df = pd.read_excel("data/laporan.xlsx")
total_penjualan = df["jumlah"].sum()
produk_terlaris = df.groupby("produk")["jumlah"].sum().idxmax()

# Buat pesan ringkasan
pesan = (
    f"📊 *Ringkasan Penjualan Hari Ini*\n"
    f"- Total Penjualan: Rp{total_penjualan:,.0f}\n"
    f"- Produk Terlaris: {produk_terlaris}\n"
    f"Data lengkap ada di Excel. 🚀"
)

# Data yang dikirim
data = {
    "messageType": "text",
    "to": PHONE,
    "body": pesan,
    "delay": 5  # Delay 5 detik sebelum dikirim
}

# Headers dengan API Key langsung (tanpa Bearer)
headers = {
    "Content-Type": "application/json",
    "Authorization": API_KEY
}

# Kirim ke Starsender
response = requests.post(API_URL, headers=headers, data=json.dumps(data))

# Cek respons
if response.status_code == 200:
    print("✅ Pesan berhasil dikirim!")
else:
    print(f"❌ Gagal: {response.status_code} - {response.text}")
