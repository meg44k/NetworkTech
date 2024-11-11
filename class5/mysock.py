import socket
import signal

#ctrl+cを有効化
def enable_ctrl_c():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

#待受ソケットの生成・
def prepare_socket_s(my_addr="",myport=50000):
    #ソケットを生成
    sock = socket.socket()
    if socket is None:
        print("failed to create a socket")
        return None
    
    try:
        sock.bind((my_addr, myport))
        sock.listen()
    except:
        print("failed to listen")
        sock.close()
        return None
    
    return sock

# 通信用ソケットを生成
def prepare_socket_c(target_addr,target_port=80):
    #ソケットを生成
    sock = socket.socket()
    if sock is None:
        print("failed to create a socket")
        return None
    
    #ターゲットに接続
    try:
        sock.connect(target_addr,target_port)
    except:
        print("failed to connect")
        sock.close()
        return None
    
    return sock