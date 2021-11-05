import socket, threading, time

key = 8194

shutdown = False
join = False

def receving (name, sock):
        while not shutdown:
                try:
                        while True:
                                data, addr = sock.recvfrom(1024)
                                #print(data.decode("utf-8"))

                                #Начало
                                decrypt = ""; k = False
                                for i in data.decode("utf-8"):
                                        if i == ":":
                                                k = True
                                                decrypt += i
                                        elif k == False or i == " ":
                                                decrypt += i
                                        else:
                                                decrypt += chr(ord(i)^key)
                                print(decrypt)
                                #Конец

                                time.sleep(0.2)
                except:
                        pass

host = "10.0.2.15"
port = 0

server = ("10.0.2.15",9090)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

alias = input("Name: ")

#функция, чтобы другие могли видеть сообщение при вводе
rT = threading.Thread(target = receving, args = ("RecvThread",s))
rT.start()

while shutdown == False:
        #новый пользователь
        if join == False:
                s.sendto(("["+alias + "] => join chat ").encode("utf-8"),server)
                join = True
        #для пользователя, который уже в чате
        else:
                try:
                        message = input()

		        #шифрование сообщения пользователя
                        crypt = ""
                        for i in message:
                                crypt += chr(ord(i)^key)
                        message = crypt

                        #проверяем, что сообщение не пустое
                        if message != "":
                                s.sendto(("["+alias + "] : "+message).encode("u>

                        #время сна, чтобы севрвер не лег
                        time.sleep(0.2)
                except:
                        #выход из чата
                        s.sendto(("["+alias + "] <= left chat ").encode("utf-8">
                        shutdown = True

rT.join()
s.close()

