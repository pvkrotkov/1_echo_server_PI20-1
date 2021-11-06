# Модуль socket для сетевого программирования
from socket import *

# данные сервера
addr = ('localhost', 9095)

# первый параметр socket_family может быть AF_INET или AF_UNIX
# второй параметр socket_type может быть SOCK_STREAM(для TCP) или SOCK_DGRAM(для UDP)
udp_socket = socket(AF_INET, SOCK_DGRAM)
# bind - связывает адрес и порт с сокетом
udp_socket.bind(addr)

sp = []
while True:
    # recvfrom - получает UDP сообщения
    text, addr = udp_socket.recvfrom(1024)
    
    if addr not in sp:
        sp.append(addr)
    print(sp)
    # sendto - передача сообщения UDP
    if len(sp) == 2:
        if addr == sp[0]:
            udp_socket.sendto(text, sp[1])
        elif addr == sp[1]:
            udp_socket.sendto(text, sp[0])

udp_socket.close()
