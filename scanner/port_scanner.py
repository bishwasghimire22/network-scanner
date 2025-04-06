import socket


def scan_ports(ip, ports=[21, 22, 23, 25, 53, 80, 110, 443, 445, 3306, 8080]):
    open_ports = []
    print(f"[*] Scanning {ip} for ports...")
    for port in ports:
        try:
            sock = socket.create_connection((ip, port), timeout=1)
            open_ports.append(port)
            sock.close()
        except:
            continue
    return open_ports
