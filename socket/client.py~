import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "192.168.136.1"
port = 12345
server_socket.connect((host,port))
while True:
    s_msg = server_socket.recv(1024)
    print("\t\t\tserver->",s_msg.decode())
    if s_msg.decode().strip().lower() == "bye":
        print("connection closed by server")
        server_socket_close()
        break
    msg = input("\nclient->")
    server_socket.send(msg.encode())
    if msg.strip().lower() == "bye":
        server_socket.send(msg.encode())
        print("connection is closed by client")
        server_socket.closed()
        break

