import socket
import pygame

'''
Данная часть кода отвечает за обработку данных от игроков.
'''
def connecting():
    '''
    Функция подключения игроков к серверу.
    '''
    while len(players_sockets) < 2:
        clock1.tick(1) # наличие запросов на подключение проверяется каждую секунду
        try:
            new_socket, addr = main_socket.accept()
            print(addr, 'connected')
            new_socket.setblocking(0)
            players_sockets.append(new_socket)
        except:
            pass

    for sock in players_sockets:
        try:
            connection = '1'
            sock.send(connection.encode()) # отправляется команда '1' игрокам, уведомляющая о готовности начать игру
        except:
            pass

print('Server is ready to work')

clock1 = pygame.time.Clock()
server_IP = '192.168.0.105' # IP адрес локальной сети

server_FPS = 1200 # количество итераций сервера в секунду
main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP) # создание главного socketa
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) # установка параметров главного socketa
main_socket.bind((server_IP, 10000)) # подключение socketa к сети
main_socket.setblocking(0) # non-blocking mode
main_socket.listen(2) # к серверу подключаются два человека

players_sockets = [] # список подключенных socketов

connecting()

# основной цикл работы сервера
while True:
    clock1.tick(server_FPS)
    for i in range(2):
        try:
            data = players_sockets[i].recv(2048) # приём данных
            if data.decode() != '0': # если от игрока не поступил код о его отключении
                players_sockets[1 - i].send(data) # отправка данных второму игроку
            else:
                players_sockets[1 - i].send('2'.encode()) # отправка команды '2', означающей завершение игры
                players_sockets = [] # отключение второго игрока от сервера
                print('All players disconnected')
                connecting() # режим ожидания нового подключения обоих игроков
                break
        except:
            pass
