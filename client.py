from socket import *
from threading import *
import sys
udp_sock = socket(AF_INET, SOCK_STREAM)
host = input('Введите IP-адрес входа:')
port = 9090
address = (host, port)
udp_sock.connect(address)
print('Введите exit, чтобы выйти.')
def client():
  while True:
    data_out = input('Введите сообщение:')
    if (data_out == 'exit') || (not data_out):
      udp_sock.close()
      sys.exit(1)
    data_in = str.encode(data_out)
    udp_sock.sendto(data_in, address)
def server():
  while True:
    print(udp_sock.recv(1024))
if __name__ == "__main__":
  client = Thread(target = client)
  server = Thread(target = server)
  client.start()
  server.start()
