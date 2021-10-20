import socket
import threading
from contextlib import closing
def vvod (maks, chto, ymol):
        while True:
                #chis = "ymol"
                chis = input("vvedite " +chto+ " ili ymol dli znachenia po ymolchaniy "+str(ymol)+ ": ")
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
def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]



'''
sock.setblocking(1)



msg = poluch(sock)
print(msg)
if msg == 'Здравствуйте, мы ещё не знакомы. Представьтесь, пожалуйста':
        otprav(file, sock, input())
        print(poluch(sock))
        otprav(file, sock, input())
        print(poluch(sock))
else:
        msg = 'Неверный пароль'
        while msg == 'Неверный пароль':
                print(poluch(sock))
                otprav(file, sock, input())
                msg = poluch(sock)
                print(msg)
        
while True:
        msg = input('Msg: ')
        if otprav(file, sock, msg)==False or msg == "exit":
                break
#'''



def poluch():
     while True:
        try:
             data = sock.recv(1024)
             print(data.decode('utf-8'))
             #sock.send(data)
        except OSError:
                break

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
nom = vvod(65535, "vash port", 52865)#62670

try:
        sock.bind(('', nom))
except OSError:
        nom = find_free_port()
        print('Ошибка. Выбранный вами код сервера уже занят, код сервера будет изменён автоматически. Новый код: ', nom)
        sock.bind(('', nom))
file = open('log_client'+str(nom)+'.txt', 'w')
file.write('vash port - '+str(nom)+'\n')
 
nom_pod = vvod(65535, "port podkluchenia", 53480)
file.write('port podkluchenia - '+str(nom_pod)+'\n')
ipe =''
ipeym = [127, 0, 0, 1]
for i in range (4):
        ipe += str(vvod(255, str(i+1)+" element ip", ipeym[i]))+'.'
ipe = ipe[:-1]
file.write('ip podkluchenia - '+str(ipe)+'\n')
sock.connect((ipe, nom_pod))

sock.send(('').encode('utf-8'))
stream = threading.Thread(target= poluch)
stream.start()


#'''
def otprav( msg):#file, sock,
        #msg = input()
        dlin = len(msg)
        sock.send((str(dlin)+' '*(6-len(str(dlin)))+msg).encode('utf-8'))
        '''try:
                sock.recv(1024)
                
        except ConnectionAbortedError:
                file.write('Ошибка. Сервер разорвал подключение')
                return(False)
        else:
                #msg = data.decode()
                #sock.send(data)
                #return(msg)
                return(True)#'''
#poluch()
while True:
    msg = input('Vvedite soobshenie: ')
    
    otprav(msg)
    if msg == 'exit':
        #sock.recv(1024)
        break

sock.close()
file.write("exit")
file.close()
