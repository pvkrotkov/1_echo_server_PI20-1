#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 9091))
message = input("Введите сообщение:  ")





sock.send(message.encode())

data = sock.recv(1024)
sock.close()

print(data.decode())





