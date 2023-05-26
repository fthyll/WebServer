import socket

# Membuat socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menentukan alamat server dan port yang akan dikoneksi
server_address = ('localhost', 8080)

# Menghubungi server
client_socket.connect(server_address)
print('Connected to the server!')

while True:
    # Meminta input dari pengguna
    message = input("Masukkan pesan yang ingin Anda kirim (ketik 'exit' untuk keluar): ")

    # Mengirim pesan ke server
    client_socket.sendall(message.encode('utf-8'))

    if message.lower() == 'exit':
        break

    # Menerima respon dari server
    response = client_socket.recv(1024).decode('utf-8')

    # Menampilkan respon dari server
    print(response)

# Menutup koneksi dengan server
client_socket.close()
