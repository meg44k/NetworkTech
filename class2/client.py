import socket
import signal
import time

signal.signal(signal.SIGINT, signal.SIG_DFL)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "127.0.0.1"
PORT = 50000


socket.connect((HOST, PORT))

time.sleep(3)

BUFSIZE = 256

data = socket.recv(BUFSIZE)#受け取るrecive
print(data.decode("utf-8"))

msg = "bye\n"

try:
    socket.sendall(msg.encode("UTF-8"))#encode()は引数省略可
except:
    print("sendall function failed")


socket.close()