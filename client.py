import socket
from time import sleep
sock = socket.socket()
sock.setblocking(1)
sock.connect(('10.38.165.12', 9090))
msg = input()
while len(msg) != 0:
  sock.send(msg.encode())
  data = sock.recv(1024)
  if_exit = msg.lower()
  if if_exit == "exit": 
    sock.close()
    break
  print(data.decode())
