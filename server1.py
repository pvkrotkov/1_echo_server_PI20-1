import socket

sock = socket.socket()

sock.bind(('', 9091))

sock.listen(2)

message = ''

while message != 'exit':
    conn, addr = sock.accept()
    
    print(addr)
    
    
    

    message = ''

    while True:

        data = conn.recv(1024)
        if not data:
            break
        message += data.decode()
        conn.send(data.upper())
        print(message)

conn.close()
