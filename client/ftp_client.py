import http.client

# Mengatur host dan port server
HOST = 'localhost'
PORT = 8080

# Membuat koneksi dengan server
conn = http.client.HTTPConnection(HOST, PORT)

# Meminta input pengguna
file_path = input("Masukkan path file yang ingin Anda minta: ")

# Mengirim permintaan ke server
conn.request('GET', file_path)

# Menerima respon dari server
response = conn.getresponse()

# Membaca data respon sebagai string
data = response.read().decode('utf-8')

# Menampilkan respon di terminal client
print(data)

# Menutup koneksi dengan server
conn.close()
