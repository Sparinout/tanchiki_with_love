from variables import *
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect(('192.168.0.108', 10000))
def send(string):
    try:
        sock.send(string.encode())
    except:
        pass

def receive():
    try:
        return sock.recv(1024).decode()
    except:
        pass