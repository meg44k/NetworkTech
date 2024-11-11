import mysock
import sys

def commun(sock):
    BUFSIZE = 1024
    data = sock.recv(BUFSIZE)
    if data:
        print(data.decode())

    

if __name__ == "__main__":
    mysock.enable_ctrl_c()
    sock = mysock.prepare_socket_s()
    if sock is None:
        sys.exit(1)

    sock_c, _ = sock.accept()
    commun(sock_c)
    sock_c.close()
    sock.close()
