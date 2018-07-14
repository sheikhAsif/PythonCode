import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCk_STREAM)
host="192.168.136.1"
port=1234
server_socket.connect((host,port))
d = server_socket.recv()
d = d.decode()
while d:
    f = open("file.txt","wb")
    f.write(d)
print("data recieved ")
