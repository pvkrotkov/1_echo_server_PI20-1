from socket import *

addr = ('localhost', 9095)
udp_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('Write to Client 2: ')
    if not data:
        udp_socket.close()
        break

    #encode - перекодирует введенные данные в байты, decode - обратно
    udp_socket.sendto(data.encode(), addr)
    data = udp_socket.recvfrom(1024)
    print('Client 2: ',(data[0]).decode(), '\n')


udp_socket.close()
