import socket
# create a TCP/IP socket
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket to local port

server_address=('0.0.0.0',1236)
server_socket.bind(server_address)

# listen to socket
server_socket.listen(5)
while True:
# waiting for connection
    print('waiting for connection...')
    client_socket, client_address =server_socket.accept()
    print('connection from IP address:', client_address)
    while True:
    # receive the data
        data = client_socket.recv(1024)
        if not data:
            break
        print('recv data:', data)