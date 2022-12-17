import socket

def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        return True
    except:
        return False
    finally:
        s.close()

def check_ports(host, port_range):
    open_ports = []
    for port in range(port_range[0], port_range[1]+1):
        if check_port(host, port):
            open_ports.append(port)
    return open_ports

# Test which ports are open on www.example.com
open_ports = check_ports("www.example.com", (1, 1024))
print(f"Open ports: {open_ports}")
