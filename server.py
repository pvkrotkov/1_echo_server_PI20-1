from socket import *

# данные сервера
host = 'localhost'
port = 777
addr = (host, port)

client = [] # Массив где храним адреса клиентов
print ('Start Server')

# socket - функция создания сокета
# первый параметр socket_family может быть AF_INET или AF_UNIX
# второй параметр socket_type может быть SOCK_STREAM(для TCP) или SOCK_DGRAM(для UDP)
udp_socket = socket(AF_INET, SOCK_DGRAM)
# bind - связывает адрес и порт с сокетом
udp_socket.bind(addr)

while 1 :
         data , addres = udp_socket.recvfrom(1024)
         #print (addres[0], " // ", addres[1])
         if  addres not in client :
            client.append(addres)# Если такого клиента нету , то добавить
            print('client appended')
         for clients in client :
                 if clients == addres :
                     udp_socket.sendto(data, clients)
                     print(clients[1])
                     print(bytes.decode(data))
