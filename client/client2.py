import socket

HOST = 'localhost'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Sending a request to the server
request = 'GET /index.html HTTP/1.1\r\nHost: localhost\r\n\r\n'
client.sendall(request.encode('utf-8'))

# Receiving the response from the server
response = client.recv(1024).decode('utf-8')

# Displaying the response in the client's terminal
print(response)

client.close()
