#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    input = int(input())
    s.connect((HOST, PORT))
    s.sendall(input.to_bytes(input.bit_length(), 'big'))
    data = s.recv(1024)

print('Received', repr(data))
