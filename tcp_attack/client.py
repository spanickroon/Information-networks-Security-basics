import socket
from threading import Thread

import const_tcp
import time


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((const_tcp.TCP_IP, const_tcp.TCP_PORT))

    def senging(self):
        while True:
            msg = f'Hello! I`m {self.sock.getsockname()[1]} sock number'
            self.sock.send(msg.encode('UTF-8'))
            time.sleep(3)
        self.sock.close()

    def start(self):
        send_thread = Thread(target=self.senging)
        send_thread.start()


if __name__ == '__main__':
    new_client = Client()
    new_client.start()
