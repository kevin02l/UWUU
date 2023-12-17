import mysql.connector

import pandas as pd

 

# Buat koneksi ke server MySQL

db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="uasbigdata"

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Contoh pernyataan SQL SELECT

select_query = "SELECT * FROM diabet"

 

# Eksekusi pernyataan SELECT

db_cursor.execute(select_query)

 

# Ambil hasil SELECT

results = db_cursor.fetchall()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()

 

# Konversi hasil SELECT menjadi dataframe pandas

df = pd.DataFrame(results, columns=["ID", "kode_provinsi", "kode_kabupaten", "nama_kabupaten_kota", "jumlah_penderita_dm_yang_mendapat_pelayanan", "satuan", "tahun "])

 

# Simpan dataframe sebagai file Excel

df.to_csv("data_diabet.csv", index=False)

 

print("Data telah disimpan dalam file csv 'data_diabet.csv'") #csv / xlsx

 