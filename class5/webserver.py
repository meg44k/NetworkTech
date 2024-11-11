import mysock
import sys
import socket

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
    BUFSIZE = 1024
    # data = sock.recv(BUFSIZE)

    CRLF = "\r\n"
    http_version = "1.1"

    # if data:
    #     print(data.decode())
    
    # print(extract_one_row(sock))
    sock.settimeout(1)
    try:
        one_row = extract_one_row(sock)
        http_req = [one_row.replace(CRLF,"")]
        while one_row != "":
            one_row = extract_one_row(sock)
            http_req.append(one_row.replace(CRLF,""))
    except socket.timeout: 
        print("HTTP Request受信完了")

    print(http_req)



    request_line = http_req[0]
    request_line_divided = request_line.split(" ")
    method = request_line_divided[0]
    request_uri = request_line_divided[1]
    protocol = request_line_divided[2]

    req_header = {}
    for header in http_req[1:-1]:
        key, value = header.split(": ")
        req_header[key] = value
    
    print(f"method is { method}")
    print(f"uri is {request_uri}")
    print(f"protocol is {protocol}")
    print("request header is ")
    print(req_header)

    status_code = 200
    reason_phrase = "OK"
    message_body = "<!DOCTYPE html>\n"
    message_body += "<HTML>\n"
    message_body += "<HEAD><META CHARSET='UTF-8'><HEAD>\n"
    message_body += "<BODY>\n"
    if "Accept-Language" in req_header:
        if req_header["Accept-Language"][:2] == "ja":
            message_body += "この人生たった一度きり\n"
        else:
            message_body += "Hello\n"
    message_body += "<BODY>\n"
    message_body += "<HTML>\n"

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
