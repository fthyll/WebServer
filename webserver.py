import socket # mengimpor library socket
import os # mengimpor library os

# membuat socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP

# mengaitkan socket ke alamat dan port tertentu
server_address = ('localhost', 8080) # alamat IP dan port
server_socket.bind(server_address) # mengikat socket ke alamat dan port

# mendengarkan koneksi masuk
server_socket.listen(5) # parameter: jumlah koneksi yang dapat diterima
print('Server is listening on port 8080...') # pesan yang akan ditampilkan

while True:
    # menerima koneksi masuk
    client_socket, client_address = server_socket.accept() # parameter: socket dan alamat client
    print(f'Connection from {client_address} has been established!') # pesan yang akan ditampilkan

    # menerima data dari client
    data = client_socket.recv(1024).decode('utf-8') # parameter: jumlah byte yang akan diterima
    print(f'Received data from client: {data}') # pesan yang akan ditampilkan

    # memparsing HTTP request
    request_method = data.split(' ')[0] # mengambil request method
    request_file = data.split(' ')[1]

    # mencari file yang diminta oleh client
    file_path = os.getcwd() + request_file
    if os.path.isfile(file_path):
        # membuka file dan membacanya
        with open(file_path, 'rb') as file:
            file_content = file.read()
        # membuat HTTP response message
        response = 'HTTP/1.1 200 OK\n\n' + file_content.decode('utf-8')
    else:
        # jika file tidak ditemukan, mengirimkan pesan "404 Not Found"
        file_path = os.getcwd() + '/error/404.html'
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                file_content = file.read()
            response = 'HTTP/1.1 404 Multiple Choices\n\n' + file_content.decode('utf-8')
        else:
            response = 'HTTP/1.1 404 Not Found\n\n404 Not Found'        

    # mengirimkan response message ke client
    client_socket.sendall(response.encode('utf-8'))

    # menutup koneksi dengan client
    client_socket.close()
