import socket

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
    try:
        sock.send(string.encode())
    except:
        pass

def receive():
    '''
    Функция получения информации с сервера.
    Возвращает раскодированную строку в виде списка с элементами типа float.
    '''
    try:
        return list(map(float, sock.recv(2048).decode().split()))
    except:
        pass

def disconnection_flag():
    '''
    Функция отправки команды в виде '0', оповещающей сервер об отключении игрока от него.
    '''
    try:
        sock.send('0'.encode())
    except:
        pass
