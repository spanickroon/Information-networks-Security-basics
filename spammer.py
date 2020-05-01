import socket
from threading import Thread

import const_tcp


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((const_tcp.TCP_IP, const_tcp.TCP_PORT))

    def senging(self):
        while True:
            self.sock.send('hack'.encode('UTF-8'))
        self.sock.close()

    def start(self):
        send_thread = Thread(target=self.senging)
        send_thread.start()


if __name__ == '__main__':
    new_client = Client()
    new_client.start()
