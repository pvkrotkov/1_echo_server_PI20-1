import socket
import errno
from socket import SHUT_RDWR
import random

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
conn, addr = sock.accept()
print(addr)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = ''
def main():
	global sock
	users = []
	try:
		port = int(input("Введите порт, который хотите открыть: "))
		sock.bind(('', port))
	except socket.error as e:
		if(e.errno == errno.EADDRINUSE):
			print("Данный порт уже занят!")
			while True:
				try:
					port = random.randint(0, 65535)
					sock.bind(('', port))
					print("Новый порт: ", port)
					break
				except:
					continue
	while True:
		try:
			data, conn = sock.recvfrom(1024)
			if conn not in users:
				users.append(conn)
			#print(conn)
			if(data.decode("UTF-8") == "exit"):
				users.reverse()
				for i in range(0, len(users)):
					sock.sendto(b"exit", (users[i]))
				sock.close()
				break
			if(data.decode("UTF-8") == ""):
				continue
		except KeyboardInterrupt:
			sock.close()
			break
		else:
			print("Message: ", data.decode("UTF-8"))
			msg = input("Введите сообщение: ")
			sock.sendto(msg.encode(), (conn))

while True:
	data = conn.recv(1024)
	msg = data.decode()
	conn.send(data)
	if(data.decode() == "exit"):
		break
	print(msg)
	#print(users)

conn.close()

main()