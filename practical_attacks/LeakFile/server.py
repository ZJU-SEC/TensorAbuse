import socket
# create a TCP/IP socket
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket to local port

server_address=('0.0.0.0',1234)
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

        if data.find(b"PRI * HTTP/2.0") == 0:
            continue
        data_index = data.find(b"grpc-timeout")
        if data_index > 0:
            data_index += 47
        else:
            data_index = 0
        data_end = data.find(b"\x12\x07\x08\x03")
        file_content = data[data_index:data_end]
        
        if data_end == -1:
            file_content = data[data_index:]
        print("\nimportant file content from ", client_address, " = \n", file_content, "\n")