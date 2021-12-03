import socket
from client import Client
def main():
    print("Listen-Loop started!")
    HOST = ''  # Standard loopback interface address (localhost)
    PORT = 9876        # Port to listen on (non-privileged ports are > 1023)
    
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        while True:
            data = s.recvfrom(2048)
            print("IP " + str(data[1][0]) + " send the following message:\n" + str(data[0], 'utf8'))
            print("Fibonacci of 17: ", Client.get_fibonacci(str(data[1][0]), 65432, 17))


if __name__ == "__main__":
    # Listens for the Broadcast of our Fibonacci-Server and prints it. Afterwards it
    # lets the server generate a fibo-number and prints it after it was received
    main()