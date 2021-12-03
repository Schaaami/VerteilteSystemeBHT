from clientserver import ClientServer
from udp_broadcast import UDPBroadcast
import threading
import time

def main():
    server = ClientServer()
    u = UDPBroadcast()
    print(u.get_intf())
    print(u.get_broadcast())
    broadcast_thread = threading.Thread(target=u.start_loop, daemon=True)
    server_thread = threading.Thread(target=server.start_server_loop, daemon=True)
    broadcast_thread.start()
    server_thread.start()
    
    while True:
        time.sleep(1) #Wait for keyboard interrrupt

if __name__ == "__main__":
    # Startet den Fibonacci Server und den Broadcast auf alle Interfaces
    main()