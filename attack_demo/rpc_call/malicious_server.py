import socket
#创建一个TCP/IP socket对象
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定socket到本地IP和端口

server_address=('0.0.0.0',1111)
server_socket.bind(server_address)

#监听socket
server_socket.listen(5)
while True:
    print('等待客户端连接...')
    client_socket, client_address =server_socket.accept()
    print('接收到客户端连接:', client_address)
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print('接收到客户端数据:', data)