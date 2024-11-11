import mysock
import sys


def extract_one_row(sock):
    CRLF = "\r\n"
    BUFSIZE = 1

    req = ""
    while req.find(CRLF) < 0:
        data = sock.recv(BUFSIZE)
        if not data:
            break
        req += data.decode()

    return req

def commun(sock):
    # BUFSIZE = 1024
    # data = sock.recv(BUFSIZE)

    CRLF = "\r\n"
    http_version = "1.1"
    status_code = 200
    reason_phrase = "OK"
    message_body = "<!DOCTYPE html>\n"
    message_body += "<HTML>\n"
    message_body += "<HEAD><META CHARSET='UTF-8'><HEAD>\n"
    message_body += "<BODY>\n"
    message_body += "この人生たった一度きり\n"
    message_body += "<BODY>\n"
    message_body += "<HTML>\n"

    # if data:
    #     print(data.decode())
    
    print(extract_one_row(sock))

    try:
        status_line = f"HTTP/{http_version} {status_code}{CRLF}"
        sock.sendall(status_line.encode())
        sock.sendall(CRLF.encode())
        sock.sendall(message_body.encode())
    except:
        print("failed to send http response.")
        return

    

if __name__ == "__main__":
    mysock.enable_ctrl_c()
    sock = mysock.prepare_socket_s()
    if sock is None:
        sys.exit(1)

    sock_c, _ = sock.accept()
    commun(sock_c)
    sock_c.close()
    sock.close()
