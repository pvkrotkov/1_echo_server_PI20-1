import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('127.0.0.1', 9090))

msg = input()
while len(msg) != 0:
    sock.send(msg.encode())

    data = sock.recv(1024)
    if msg == 'exit':
        sock.close()
        break

    print(data.decode())
    msg = input()
