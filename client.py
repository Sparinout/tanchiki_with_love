from variables import *
import socket
import threading

def f():
    sock.send(input().encode())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect(('192.168.0.108', 10000))

while True:
    thr1 = threading.Thread(target=f).start()

    try:
        data = sock.recv(128)
        data = data.decode()
        print(data)
    except:
        pass
