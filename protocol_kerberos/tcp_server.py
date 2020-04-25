import socket
from threading import Thread

import constants


class TCPServer:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((constants.TCP_IP, constants.TCP_PORT))
        self.sock.listen()

    def listening_client(self, connection, address):
        print(f'Connection address: {address}')

        while True:
            data = connection.recv(constants.BUFFER_SIZE)
            if not data:
                break
            print(f'\nSender: {address}\nMessage: {data.decode("UTF-8")}')
        connection.close()

        print(f'Stop connection: {address}')

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
