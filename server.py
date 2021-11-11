from socket import *
udp_sock = socket(AF_INET, SOCK_STREAM)
host = gethostname()
port = 9090
udp_sock.bind((host, port))
udp_sock.listen(4)
conn, address = udp_sock.accept()
print(address)
data_out = ''
client_list = []
while True:
	data_in = conn.recv(1024)
	if not (address in client_list):
		client_list.append(address)
	if not data_in:
		break
	data_out += data_in.decode()
	conn.send(data_in)
	for i in client_list:
		if i != address:
			udp_socket.sendto(b'hello', i)
	print(data_out)
udp_socket.close()
