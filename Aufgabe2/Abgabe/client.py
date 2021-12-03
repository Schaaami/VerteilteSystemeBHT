#!/usr/bin/env python3

import socket

class Client:

    @staticmethod
    def get_fibonacci(HOST, PORT, num):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(bytes(str(num), 'utf8'))
            data = s.recv(1024)
            return (str(data, 'utf8'))


if __name__ == "__main__":
    # Debug Code
    print(Client.get_fibonacci("127.0.0.1", 65432, 17))
