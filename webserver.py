import socket #import modul socket
import os #import modul os

# membuat socket TCP (1)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #membuat objek socket TCP

# mengaitkan socket ke alamat dan port tertentu
server_address = ('localhost', 8080) #membuat objek server_address
server_socket.bind(server_address) #mengaitkan server_socket ke server_address

# mendengarkan koneksi masuk
server_socket.listen(1) #mendengarkan koneksi masuk dengan parameter backlog 1
print('Server is listening on port 8080...') #menampilkan pesan server sedang mendengarkan koneksi masuk

while True: #looping forever
    # menerima koneksi masuk
    client_socket, client_address = server_socket.accept()#menerima koneksi masuk dan menyimpannya ke client_socket dan client_address
    print(f'Connection from {client_address} has been established!')#menampilkan pesan koneksi telah berhasil dibuat

    # menerima data dari client
    data = client_socket.recv(1024).decode('utf-8')#menerima data dari client dan menyimpannya ke data
    print(f'Received data from client: {data}')#menampilkan pesan data telah diterima

    # memparsing HTTP request(2)
    request_method = data.split(' ')[0] #mengambil request method
    request_file = data.split(' ')[1]#mengambil request file

    # mencari file yang diminta oleh client(3)
    file_path = os.getcwd() + request_file #menggabungkan current working directory dengan request file
    if os.path.isfile(file_path): #jika file ditemukan
        # membuka file dan membacanya
        with open(file_path, 'rb') as file:#membuka file dengan mode read binary
            file_content = file.read()#membaca file dan menyimpannya ke file_content
        # membuat HTTP response message(4)
        response = 'HTTP/1.1 200 OK\n\n' + file_content.decode('utf-8')
    elif request_file == "/500":
        # membuat HTTP response message untuk error 500
        response = 'HTTP/1.1 500 Internal Server Error\n\nError: Server Error'
    elif request_file == "/300":
        # membuat HTTP response message untuk error 300
        response = 'HTTP/1.1 300 Multiple Choices\n\nError: Multiple Choices'
    else:
        # jika file tidak ditemukan, mengirimkan pesan "404 Not Found"(6)
        response = 'HTTP/1.1 404 Not Found\n\n404 Not Found'

    # mengirimkan response message ke client(5)
    client_socket.sendall(response.encode('utf-8'))

    # menutup koneksi dengan client
    client_socket.close()
