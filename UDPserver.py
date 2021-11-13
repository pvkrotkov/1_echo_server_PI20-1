#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket
from datetime import datetime
database = []


HOST = '127.0.0.1'
PORT = 5555
BIND = (HOST, PORT)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(BIND)
while True:
    current_time = datetime.now().time()
    data, ad = sock.recvfrom(1024)
    print(ad, 'присоединился в ', current_time)
    if ad not in database:
        print('Добавлен новый пользователь')
        database.append(ad)
    for i in database:
        if i != ad:
            sock.sendto(data, i)

