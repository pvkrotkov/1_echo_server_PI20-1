import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
print(addr)

msg = ''

def proc():
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		conn.send(data)

print(msg)

p1 = threading.Thread(target = proc, name = "t1")
p1.start()
conn.close()
