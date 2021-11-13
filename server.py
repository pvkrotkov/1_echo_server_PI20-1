#!/usr/bin/env python3

import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 65432

print('Сервер включен')
while True:
    current_time = datetime.now().time()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Прослушивание порта...')

        conn, addr = s.accept()


        print(f'Connected by {addr} in %d:%d:%d ' % (current_time.hour, current_time.minute, current_time.second))
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
                check = data.decode("utf-8")
                print(f'Отправка данных клиенту - {data.decode("utf-8")}')
            if check == 'exit':
                print('Соединение разорвано')
                conn.close()
