import socket

import pygame


# Функция подключения нескольких игроков к серверу
def connecting():
    while len(players_sockets) < 2:
        clock1.tick(1)
        try:
            new_socket, addr = main_socket.accept()
            print(addr, 'connected')
            new_socket.setblocking(0)
            players_sockets.append(new_socket)
        except:
            pass

    for sock in players_sockets:  # Отправляем флаг подключения новым клиентам
        try:
            connection = '1'
            sock.send(connection.encode())
        except:
            pass


clock1 = pygame.time.Clock()
FPS = 30

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind(('192.168.0.105', 10000))

main_socket.setblocking(0)
main_socket.listen(2)

players_sockets = []

connecting()

while True:
    clock1.tick(FPS)
    for i in range(2):
        try:
            data = players_sockets[i].recv(2048)
            if data.decode() != '0':
                players_sockets[1 - i].send(data)
            else:
                players_sockets[1 - i].send('2'.encode())
                players_sockets = []
                print('All players disconnected')
                connecting()
                break
        except:
            pass
