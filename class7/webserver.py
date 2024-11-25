import mysock
import sys
import socket
import datetime
import os
import mimetypes

def make_response(method, SecFetchDest, request_uri):
    response_header = {}
    dt_now = datetime.datetime.now()
    response_header["Date"] =  dt_now.strftime("%a, %d %b %Y %H:%M:%S JST")#%a:曜日%d:日%b:月
    response_header["Server"] = "NEGI-SERVER"

    if method != "GET":
        return 501, "Not Implemented", response_header, ""
    
    if request_uri[-1] == "/":
        request_uri += "index.html"

    if not os.path.exists(f".{request_uri}"):
        if SecFetchDest == "document":
            with open(f"./404.html","rb") as f:
                message_body = f.read()
                response_header["Content-Length"] = len(message_body)
                response_header["Content-Type"] = mimetypes.guess_type(request_uri)[0]
                return 404, "Not Found", response_header, message_body
        elif SecFetchDest == "image":
            with open(f"./undefinedImage.png","rb") as f:
                message_body = f.read()
                response_header["Content-Length"] = len(message_body)
                response_header["Content-Type"] = mimetypes.guess_type(request_uri)[0]
                return 404, "Not Found", response_header, message_body
        
    with open(f".{request_uri}","rb") as f:
        message_body = f.read()
        response_header["Content-Length"] = len(message_body)
        response_header["Content-Type"] = mimetypes.guess_type(request_uri)[0]
        return 200, "OK", response_header, message_body

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

    CRLF = "\r\n"
    http_version = "1.1"

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

    SecFetchDest = req_header["Sec-Fetch-Dest"]
    
    print(f"method is {method}")
    print(f"uri is {request_uri}")
    print(f"protocol is {protocol}")
    print("request header is ")
    print(req_header)

    status_code, reason_phrase, response_header, message_body = make_response(method, SecFetchDest, request_uri)

    try:
        status_line = f"{protocol} {status_code} {reason_phrase}{CRLF}"
        sock.sendall(status_line.encode())
        for key in response_header:
            sock.sendall(f"{key}: {response_header[key]}{CRLF}".encode())
        sock.sendall(CRLF.encode())
        sock.sendall(message_body)#message_bodyはバイナリモードで開かれているのでエンコード不要
    except:
        print("failed to send http response.")
        return

    

if __name__ == "__main__":
    mysock.enable_ctrl_c()
    sock = mysock.prepare_socket_s()
    if sock is None:
        sys.exit(1)

    while True:
        sock_c, _ = sock.accept()
        commun(sock_c)
        sock_c.close()