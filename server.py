import socket

fwq = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

fwq.bind(('localhost', 9090))

print('Начать чат! ')

while True:

    data, addr = fwq.recvfrom(1024)

    recvmsg = data.decode('utf-8')

    if recvmsg == 'exit!':
        print("Другой участник добровольно закончил чат с тобой, пока!")
        break

    print('client msg: ' + recvmsg)
    replymsg = input('Ответить:')

    fwq.sendto(replymsg.encode('utf-8'), addr)

fwq.close()
