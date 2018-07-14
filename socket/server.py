import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 12345
server_socket.bind((host,port))
print("Server socket sucessfully created on IP : {} at port {}".format(host,port))
server_socket.listen()
print("Server is waiting for client to connect ... \n\n")
client_socket,client_addr=server_socket.accept()
print("client is connected")
print(client_socket)
print(client_addr)
print("client's Ip {}:{}\n\n".format(*client_addr))
while True:
    msg = input("\nserver->")
    if msg.strip().lower() == "bye":
        client_socket.send(msg.encode())
        print("connection is closed by server")
        client_socket.close()
        server_socket.close()
        break
    client_socket.send(msg.encode())
    c_msg = client_socket.recv(1024)
    print("\t\t\tclient->",c_msg.decode())
    if c_msg.decode().lower().strip() == "bye":
        print("COnnection closed by client")
        client_socket.close()
        server_socket.close()
        break
