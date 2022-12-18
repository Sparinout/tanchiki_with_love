import socket

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind(('localhost', 10000))

main_socket.setblocking(0)
main_socket.listen(2)

players_sockets = []

while True:
    try:
        new_socket, addr = main_socket.accept()
        print(addr, 'connected')
        new_socket.setblocking(0)
        players_sockets.append(new_socket)
    except:
        pass

    for sock in players_sockets:
        try:
            data = sock.recv(1024)
            for sock1 in players_sockets:
                if sock1 != sock:
                    sock1.send(data)
        except:
            pass