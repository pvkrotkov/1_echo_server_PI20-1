import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input('Введите IP-адрес входа:')
port = 9090
address = (host, port)
sock.connect((host, port))
print('Введите exit, чтобы выйти.')
while True:
  data_out = input('Введите сообщение:')
  if data_out == 'exit':
    break
  while len(data_out) != 0:
    sock.send(data_out.encode())
  data_in = sock.recv(1024)
  print(data_in.decode())
sock.close()
