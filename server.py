from socket import *
import sys

host = 'localhost'
port = 777
addr = (host, port)

udp_socket = socket(AF_INET, SOCK_DGRAM)

while 1:
    data = input('write to server: ')
    data = str.encode(data)
    udp_socket.sendto(data, addr)
    data = bytes.decode(data)
    # print(data)
    # data = udp_socket.recvfrom(1024)

udp_socket.close()
