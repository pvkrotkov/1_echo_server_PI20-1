import socket
import bcrypt
from contextlib import closing

def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]

def vvod (maks, chto, ymol):
        while True:
                chis = "ymol"
                #chis = input("vvedite " +chto+ " ili ymol dli znachenia po ymolchaniy "+str(ymol)+ ": ")
                if chis.isdigit(): #нуля до 65535
                        chis = int(chis)
                        if chis > -1 and chis < maks+1:
                                return (chis)
                        else:
                                print("vvodite chislo ot 0 do " + str(maks))
                elif chis == "ymol":
                        return(ymol)
                else:
                        print("nuzhno vvodit celoe chislo")
                        
 

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
nom = vvod(65535, "vash port", 53480)
try:
        sock.bind(('', nom))
except OSError:
        nom = find_free_port()
        print('Ошибка. Выбранный вами код сервера уже занят, код сервера будет изменён автоматически. Новый код: ', nom)
        sock.bind(('', nom))
f = open('log_server'+str(nom)+'.txt', 'w')
f.write('vash port - '+str(nom)+'\n')




#client = [] # Массив где храним адреса клиентов
client=[]

spic=[]
file = open('users_2.txt', 'r')
for line in file:
        spic.append(line.split(' NaMe '))
        
file.close()


def otprav(file, sock, msg, addr):
    try:
        sock.sendto(msg.encode('utf-8'), addr)
        '''try:
                sock.recvfrom(1024)
                
        except ConnectionAbortedError:
                file.write('Ошибка. Сервер разорвал подключение')
                return(False)
        else:
                return(True)'''
    except BrokenPipeError:
        return(False)
    else:
        return(True)
#'''
def  poluch(sock, file):
        data, addre = sock.recvfrom(1024)#conn
        msg = data.decode('utf-8')
        #sock.sendto(data, addre)
        dlin = str(msg[:6])
        if dlin != '':
            print('Получено сообщение длиной '+dlin+' символов: ')
            file.write('Получено сообщение длиной '+dlin+' символов: ')
        return(msg[6:], data, addre)#'''


zhdan =[]
prov = {}
new = []
pasw = {}
cl_name = {}
while True:#ConnectionResetError
        try:
            msg, conn, addr = poluch(sock, f)
            #'''
        except ConnectionResetError:
            print('', end='')
            #sock.shutdown(socket.SHUT_RDWR)
        except BrokenPipeError:
            print('', end='')#'''
        

        
        #conn , addr = sock.recvfrom(1024)#,msg
        #print('Соединено: '+str(addr))
        f.write('Сообщение от '+str(addr)+'\n')
        #print (addr[0], addr[1])
        if addr in prov:
            #msg = conn.decode()[6:]
            file = open("pas"+prov[addr]+".bin", "rb")
            key = file.read()
            file.close()
            if bcrypt.checkpw(bytes(msg, encoding='utf-8'), key):
                if otprav(f, sock, 'Пароль принят', addr):
                    client.append(addr)
                    cl_name.update([(addr, prov[addr])])
                del(prov[addr])
            elif otprav(f, sock, 'Неверный пароль', addr)==False:
                del(prov[addr])
            key=''
        elif addr in new:
            key=new.index(addr)
            if otprav(f, sock, 'Введите ваш пароль', addr):
                pasw.update([(addr, msg)])#prov.update([(addr,name)])
            del(new[key])
            
        elif addr in pasw:
            name=pasw[addr]
            msg = bcrypt.hashpw(bytes(msg, encoding='utf-8'), bcrypt.gensalt())
            file = open("users_2.txt", "a")
            file.write(str(addr)+' NaMe '+str(name)+'\n')
            file.close()
            file = open("pas"+str(name)+".bin", "wb")
            file.write(msg)
            file.close()
            #spic.append([str(addr), name, key])
            f.write('User '+str(name)+' add''+\n')
            spic.append([str(addr), msg])
            #otprav(f, sock, 'Спасибо', addr)
            otprav(f, sock, 'Имя и пароль сохранены', addr) 
            #print('Имя и пароль сохранены')
            client.append(addr)#.update(addr, name)
            cl_name.update([(addr, name)])
            del(pasw[addr])
        elif addr in zhdan:
            client.append(addr)
            del(zhdan[zhdan.index(addr)])
        elif addr not in client:
            for line in spic:
                if line[0] == str(addr):
                        name=line[1][:-1] 

                        if otprav(f, sock, ('Здравствуйте, '+name+'. Введите ваш пароль'), addr):
                            prov.update([(addr,name)])
                            #print(prov)#
                        break
            else:
                if otprav(f, sock, 'Здравствуйте, мы ещё не знакомы. Представьтесь, пожалуйста', addr):
                    new.append(addr)    
        elif msg == "exit":
            #sock.sendto(''.encode('utf-8'), addr)
            del(client[client.index(addr)])
            del(cl_name[addr])#sock.shutdown(socket.SHUT_RDWR)
            #sock.shutdown(socket.SHUT_RDWR)
            #msg, conn, addr = poluch(sock, f)
            #addr=''
            msg=''
            #razruv soedinenia
        elif msg !='':
            for i in client:
                if i != addr:
                    try:
                        otprav(f, sock, '{'+cl_name[addr]+'}: '+msg, i)
                    except ConnectionResetError:
                        zhdan.append(i)
                        del(client[client.index(i)])
                        #del(cl_name[addr])
                        #sock.shutdown(socket.SHUT_RDWR)
                    #except BrokenPipeError:
                    #continue
                #sock.sendto(sock,i)
        #print('kom')
f.write('exit')
f.close()
sock.close()