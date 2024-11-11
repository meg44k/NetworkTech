import socket
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)#SIGINT:Ctl+C,SIG_DFL:キーボード入力をできるようにする

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#接続要求を待機するためのソケット IPv4 TCP(引数省略可)
sock.bind(('', 80))
sock.listen()#接続要求を待機に設定している(待ち状態に入っているだけではない)
sock_c , addr = sock.accept()#通信を行うためのソケット

msg = "k21182"

try:
    sock_c.sendall(msg.encode("UTF-8"))#encode()は引数省略可
except:
    print("sendall function failed")

BUFSIZE = 2048

data = sock_c.recv(BUFSIZE)
print(data.decode("utf-8"))

sock_c.close()
sock.close()
