import threading
import socket

class BindingConnection(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port

    def run(self):
        # Create a socket and bind it to the specified host and port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))

        # Start listening for incoming connections
        s.listen()
        print(f"Listening for connections on {self.host}:{self.port}")

        # Accept incoming connections
        while True:
            conn, addr = s.accept()
            print(f"Received connection from {addr[0]}:{addr[1]}")
            # Do something with the connection (e.g. send data, receive data, etc.)
            # ...
            conn.close()

# Create a binding connection on localhost, port 8080
t = BindingConnection("localhost", 8080)
t.start()

# Wait for the thread to finish
t.join()
