import socket
from threading import Thread

import const_tcp


class TCPServer:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((const_tcp.TCP_IP, const_tcp.TCP_PORT))
        self.sock.listen()

    def listening_client(self, connection, address):
        print(f'Connection address: {address}')

        while True:
            data = connection.recv(const_tcp.BUFFER_SIZE)
            if not data:
                break
            print(f'\nSender: {address}\nMessage: {data.decode("UTF-8")}')
        connection.close()

        print(f'Stop connection: {address}')

    def authentication(self, key):
        pass

    def new_connection(self):
        while True:
            connection, address = self.sock.accept()

            if connection:
                new_client_thread = Thread(
                    target=self.listening_client,
                    args=(connection, address)
                    )
                new_client_thread.start()

    def start(self):
        parent_thread = Thread(target=self.new_connection)
        parent_thread.start()


if __name__ == '__main__':
    server = TCPServer()
    server.start()
