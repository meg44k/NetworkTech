import socket
import signal
import asyncio

signal.signal(signal.SIGINT, signal.SIG_DFL)

async def handle_client(client_socket):
    BUFSIZE = 256

    async def recv_data():
        while True:
            data = await loop.sock_recv(client_socket, BUFSIZE)
            print(data.decode("utf-8"))

    async def send_data():
        while True:
            msg = "[client] : " + input("[client] > ")
            try:
                await loop.sock_sendall(client_socket, msg.encode("UTF-8"))
            except:
                print("sendall function failed")

    await asyncio.gather(recv_data(), send_data())

async def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = "127.0.0.1"
    PORT = 50000

    await loop.sock_connect(client_socket, (HOST, PORT))

    await handle_client(client_socket)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
