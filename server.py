import socket
import pygame
import time

clock = pygame.time.Clock()
FPS = 120

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind(('192.168.0.105', 10000))

main_socket.setblocking(0)
main_socket.listen(2)

players_sockets = []

while len(players_sockets) < 2:
    try:
        new_socket, addr = main_socket.accept()
        print(addr, 'connected')
        new_socket.setblocking(0)
        players_sockets.append(new_socket)
    except:
        pass

connection = '0'
for sock in players_sockets:
    try:
        connection = '1'
        sock.send(connection.encode())
    except:
        pass

while True:
    clock.tick(FPS)
    for i in range(2):
        try:
            data = players_sockets[i].recv(1024)
            players_sockets[1-i].send(data)
        except:
            pass