import mysock
import sys

def commun(sock,target):
    newline = "\r\n"
    http_req = ""

    http_req += f"GET / HTTP/1.1{newline}"
    http_req += f"Host: {target}{newline}"
    http_req += f"Connection: keep-alive{newline}"
    http_req += f'sec-ch-ua: "Chromium";v="129", "Not=A?Brand";v="8"{newline}'
    http_req += f"sec-ch-ua-mobile: ?0{newline}"
    http_req += f'sec-ch-ua-platform: "macOS"{newline}'
    http_req += f"DNT: 1{newline}"
    http_req += f"Upgrade-Insecure-Requests: 1{newline}"
    http_req += f"User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36{newline}"
    http_req += f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7{newline}"
    http_req += f"Sec-Fetch-Site: none{newline}"
    http_req += f"Sec-Fetch-Mode: navigate{newline}"
    http_req += f"Sec-Fetch-User: ?1{newline}"
    http_req += f"Sec-Fetch-Dest: document{newline}"
    http_req += f"Accept-Encoding: gzip, deflate, br, zstd{newline}"
    http_req += f"Accept-Language: ja,en-US;q=0.9,en;q=0.8{newline}"
    http_req += newline

    try: 
        sock.sendall(http_req.encode())
    except:
        print("failed to send http request")

    BUFSIZE = 1024
    data = sock.recv(BUFSIZE)
    if data:
        print(data.decode(errors="replace"))

if __name__ == "__main__":
    mysock.enable_ctrl_c()
    target = input("どこに接続しますか:")
    sock = mysock.prepare_socket_c(target)
    if sock is None:
        sys.exit(1)

    commun(sock,target)
    sock.close()