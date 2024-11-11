import socket
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "127.0.0.1"
PORT = 50000


socket.connect((HOST, PORT))

BUFSIZE = 256

while True:
    data = socket.recv(BUFSIZE)

    if data.decode("utf-8") ==  "exit":
        socket.close()
        print("Server was disconnected")
        break

    print(data.decode("utf-8"))
    data = None

    msg =input("[client] > ")
    try:
        socket.sendall(msg.encode("UTF-8"))#encode()は引数省略可
        if msg ==  "exit":
            socket.close()
            break
        msg = None
    except:
        print("sendall function failed")
