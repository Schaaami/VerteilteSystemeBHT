import socket

from fibonacci import Fibonacci

class ClientServer:
    def start_server_loop(self):
        print("Server-Loop started!")
        HOST = ''  # Standard loopback interface address (localhost)
        PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
        def int_to_bytes(x: int) -> bytes:
            return x.to_bytes((x.bit_length() + 7) // 8, 'big')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            while True:
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        strings = str(data, 'utf8')
                        num = int(strings)
                        num = Fibonacci(num)
                        conn.sendall(bytes(str(num), 'utf8'))
                        print(data)


