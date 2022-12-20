import socket

<<<<<<< HEAD
'''
Данная часть кода (клиент) отвечает за взаимодействие игрока с сервером.
'''
client_IP = '192.168.0.105'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создание socketa
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) # установка параметров socketa
sock.connect((client_IP, 10000)) # подключение socketa к серверу
def send(string):
    '''
    Функция кодировки и отправки заданной строку на сервер.
    string: отправляемая строка
    '''
=======
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect(('192.168.0.105', 10000))
def send(string):
>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
    try:
        sock.send(string.encode())
    except:
        pass

def receive():
<<<<<<< HEAD
    '''
    Функция получения информации с сервера.
    Возвращает раскодированную строку в виде списка с элементами типа float.
    '''
=======
>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
    try:
        return list(map(float, sock.recv(2048).decode().split()))
    except:
        pass

def disconnection_flag():
<<<<<<< HEAD
    '''
    Функция отправки команды в виде '0', оповещающей сервер об отключении игрока от него.
    '''
    try:
        sock.send('0'.encode())
    except:
        pass
=======
    try:
        sock.send('0'.encode())
    except:
        pass
>>>>>>> dd058846afa42c1a7bf727b5db836de33200d25c
