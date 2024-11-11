import socket
import signal
import asyncio

signal.signal(signal.SIGINT, signal.SIG_DFL)#SIGINT:Ctl+C,SIG_DFL:キーボード入力をできるようにする

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#接続要求を待機するためのソケット IPv4 TCP(引数省略可)
sock.bind(('', 50000))
sock.listen()#接続要求を待機に設定している(待ち状態に入っているだけではない)
sock_c , addr = sock.accept()#通信を行うためのソケット

BUFSIZE = 256

msg = "==Connected=="
sock_c.sendall(msg.encode("UTF-8"))

while True:
    data = sock_c.recv(BUFSIZE)

    if data.decode("utf-8") == "exit":
        sock_c.close()
        sock.close()
        print("Client was disconnected")
        break

    print(data.decode("utf-8"))
    data = None

    msg = input("[server] > ")
    try:
        sock_c.sendall(msg.encode("UTF-8"))#encode()は引数省略可
        if msg ==  "exit":
            sock_c.close()
            sock.close()
            break
        msg = None
    except:
        print("sendall function failed")
