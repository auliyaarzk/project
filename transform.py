import pandas as pd

# Membaca data dari file CSV yang Anda miliki
data = pd.read_csv('UNdata_literacy rate.csv')  # Ganti dengan path ke file CSV Anda

# Fungsi untuk mengategorikan literacy rate
def categorize_literacy(rate):
    if rate < 40:
        return 'Low'
    elif 40 <= rate < 70:
        return 'Medium'
    else:
        return 'High'

# Menambahkan kolom 'literacy_category' berdasarkan 'Observation Value'
data['literacy_category'] = data['Observation Value'].apply(categorize_literacy)

# Menambahkan kolom 'literacy_level' berdasarkan kategori literasi
data['literacy_level'] = data['literacy_category'].apply(lambda x: 'Needs Improvement' if x == 'Low' else 'Satisfactory')

# Menambahkan kolom 'info' yang menggabungkan 'Reference Area' dan 'literacy_level'
data['info'] = data['Reference Area'] + ' - ' + data['literacy_level']

# Menyimpan data yang sudah ditransformasi ke file CSV (opsional, jika ingin menyimpannya)
data.to_csv('transformed_data.csv', index=False)

# Menampilkan hasil data setelah transformasi
print(data.head())  # Menampilkan 5 baris pertama dari data yang sudah ditransformasi
