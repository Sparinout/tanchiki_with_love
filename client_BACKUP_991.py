import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect(('192.168.0.105', 10000))
def send(string):
    try:
        sock.send(string.encode())
    except:
        pass

def receive():
    try:
<<<<<<< HEAD
        return list(map(float, sock.recv(1024).decode().split()))
=======
        return list(map(float, sock.recv(128).decode().split()))
>>>>>>> main
    except:
        return