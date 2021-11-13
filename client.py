#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server
while True:
    command = input()
    if command != 'exit':
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(command.encode())
            data = s.recv(1024)
            print('Received', data.decode('UTF-8'))
    if command == 'exit':
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'exit')
            data = s.recv(1024)
            print('Received', data.decode('UTF-8'))
            print('Соединение разорвано')
        break
    else:
        continue
