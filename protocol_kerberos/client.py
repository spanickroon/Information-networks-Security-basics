import socket

import constants


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((constants.TCP_IP, constants.TCP_PORT))

    def start(self):
        while True:
            self.sock.send(input().encode('UTF-8'))
        s.close()


if __name__ == '__main__':
    new_client = Client()
    new_client.start()
