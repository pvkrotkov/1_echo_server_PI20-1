import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('10.0.2.15', 64444))

message = ''
msg = input('Enter text: ')
while msg!='exit':
	message+=msg+' '
	msg = input('Enter text: ')

sock.send(message.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())
