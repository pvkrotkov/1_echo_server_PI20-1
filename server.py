from socket import *

#host = 'empire-org.fun'
host = 'localhost'
port = 9090
addr = (host, port)

udp_socket = socket(AF_INET, SOCK_DGRAM)

udp_socket.bind(addr)

client_list = []

while True:

    print('wait data...')

    conn, addr = udp_socket.recvfrom(1024)
    data = conn.decode()
    if not (addr in client_list):
        client_list.append(addr)

    if data == 'exit':
        break

    for c_addr in client_list:
        if c_addr != addr:
            udp_socket.sendto(b'hello', c_addr)

    print(data)

udp_socket.close()
