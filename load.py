import pandas as pd
from pymongo import MongoClient

# Membaca data yang sudah ditransformasi
data = pd.read_csv('transformed_data.csv')  # memasukan file CSV yang sudah ditransformasi

# Mengonversi DataFrame menjadi dictionary 
data_dict = data.to_dict(orient='records')

# Koneksi ke MongoDB 
client = MongoClient('mongodb+srv://auliarizkirumahhorbo:auliya@aul-p.fc96f.mongodb.net/')
db = client['literacy_data']  # Nama database
collection = db['literacy_rates']  # Nama collection

# Insert data ke MongoDB
collection.insert_many(data_dict)

print("Data berhasil dimasukkan ke MongoDB")


# Menampilkan beberapa data dari MongoDB
for doc in collection.find().limit(5):
    print(doc)
