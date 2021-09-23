from socket import *
from threading import *
import sys

host = 'localhost'
port = 9090
addr = (host, port)

udp_socket = socket(AF_INET, SOCK_DGRAM)


def client():
    while True:
        client_data = input('write to server: ')
        if not client_data:
            udp_socket.close()
            sys.exit(1)

        client_data_b = str.encode(client_data)
        udp_socket.sendto(client_data_b, addr)


def server():
    while True:
        print(udp_socket.recvfrom(1024))


if __name__ == "__main__":
    client = Thread(target=client)
    server = Thread(target=server)

    client.start()
    server.start()

