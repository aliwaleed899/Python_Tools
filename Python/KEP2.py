import socket

from django.db import connection 

server_ip=input ('[+] Enter The Server IP :')
server_port = int(input('[+] Enter Server Port :'))

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind((server_ip,server_port))
soc.listen(1)
print('Server Listening... ')
connection, address=soc.accept()
print("Addres of The Client :",address)

while True :
    output=connection.recv(1024)
    if not output:
        break
    connection.sendall(b"Message Receive !")
print(output.decode('utf-8'))
connection.close()
