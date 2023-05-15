import socket

# Membuat socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menentukan alamat server dan port yang akan dikoneksi
server_address = ('localhost', 8080)

# Menghubungi server
client_socket.connect(server_address)
print('Connected to the server!')

while True:
    # Menerima log message dari server
    log_message = client_socket.recv(1024).decode('utf-8')

    # Menampilkan log message
    print(log_message)

# Menutup koneksi dengan server
client_socket.close()
