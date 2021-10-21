import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9090

sock.bind((host, port))
sock.listen(4)
conn, address = sock.accept()
print(address)
data_out = ''
while True:
	data_in = conn.recv(1024)
	if not data_in:
		break
	data_out += data_in.decode()
	conn.send(data_in)
print(data_out)
conn.close()
