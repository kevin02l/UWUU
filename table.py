# Buat koneksi ke server MySQL
import mysql.connector
db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="uasbigdata"  # Ganti dengan nama database yang telah Anda buat

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Definisikan struktur tabel 'users'

create_table_query = """
CREATE TABLE diabet (
    id INT  PRIMARY KEY,
    kode_provinsi VARCHAR(255),
    kode_kabupaten VARCHAR(255),
   nama_kabupaten_kota VARCHAR(255),
   jumlah_penderita_dm_yang_mendapat_pelayanan VARCHAR(255),
   satuan VARCHAR(255),
   tahun VARCHAR(255)
)

"""

 

# Eksekusi perintah SQL untuk membuat tabel

db_cursor.execute(create_table_query)

 

# Komit perubahan ke database

db_connection.commit()

 

# Tutup cursor dan koneksi