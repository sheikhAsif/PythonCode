import socket
server_socket = socket.socket()
host = getuserbyname(getusername(())
port = 1234
server_socket.bind((host,port))
server_socket.listen()
print("server listening...")
client_socket,client_addr=server_socket.accept()
file = input("Enter file address :")
f = open(file,mode="rb")
d = f.read()
while d:
    client_socket.send(d.encode())
print("file sent...")



    
