import socket
import signal
import asyncio

signal.signal(signal.SIGINT, signal.SIG_DFL)

async def handle_client(sock_c):
    BUFSIZE = 256
    msg = "==Connected=="
    sock_c.sendall(msg.encode("UTF-8"))

    async def recv_data():
        while True:
            data = await loop.sock_recv(sock_c, BUFSIZE)
            print(data.decode("utf-8"))

    async def send_data():
        while True:
            msg = "[server] : " + input("[server] > ")
            try:
                await loop.sock_sendall(sock_c, msg.encode("UTF-8"))
            except:
                print("sendall function failed")

    await asyncio.gather(recv_data(), send_data())

async def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 50000))
    sock.listen()
    sock.setblocking(False)  # Non-blocking

    print("Waiting for connection...")
    sock_c, addr = await loop.sock_accept(sock)
    print(f"Connected by {addr}")

    await handle_client(sock_c)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
