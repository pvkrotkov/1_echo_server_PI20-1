#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading

HOST = '127.0.0.1'
PORT = 5555
BIND = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, 0))

nick = input("Введите ваше имя: ")
sock.sendto(f'\n{nick} в чате!'.encode(), BIND)


def get():
    while True:
        data = sock.recv(1024)
        print(data.decode('UTF-8'))
trhread = threading.Thread(target=get)
trhread.start()
while True:
    msg = input("Вы: ")
    sock.sendto(f'{nick} сообщает: {msg}'.encode(), BIND)
