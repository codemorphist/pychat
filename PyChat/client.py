import socket
import select
from config import HOST, PORT


class Client():
    def __init__(slef):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((HOST, PORT))

    def send_message(self, message)
        # while True:
        #     sockets_list = [sys.stdin, server]

        #     read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

        #     for socks in read_sockets:
        #         if socks == server:
        #             message = socks.recv(2048)
        #         else:
        self.server.send(message.encode())

    def close_connection():
        self.server.close()
