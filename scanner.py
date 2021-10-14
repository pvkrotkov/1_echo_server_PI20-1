import socket
from threading import Thread

N = 2**16 - 1
ports = []


def scan(ip, start, finish):
    for port in range(start, finish):
        sock = socket.socket()
        try:
            sock.connect((ip, port))
            # print("Порт", port, "открыт")
            ports.append(port)
            msg = 'scanner_command'
            sock.send(msg.encode())
        except:
            continue
        finally:
            sock.close()


def mainn(ip, amount_of_ports):
    i_step = (N - 1024)//amount_of_ports
    # print(i_step)
    for i in range(1024, N, i_step):
        t = Thread(target=scan, args=(ip, i, i+i_step))
        t.start()


# mainn('127.0.0.1', 1000)
