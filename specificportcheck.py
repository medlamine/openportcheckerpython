import threading
import socket

class PortChecker(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.host, self.port))
            print(f"Port {self.port} is open")
        except:
            print(f"Port {self.port} is closed")
        finally:
            s.close()

# Create a list of ports to check
ports = [80, 443, 22, 21]

# Create a thread for each port
threads = []
for port in ports:
    t = PortChecker("www.example.com", port)
    threads.append(t)

# Start the threads
for t in threads:
    t.start()

# Wait for the threads to finish
for t in threads:
    t.join()
