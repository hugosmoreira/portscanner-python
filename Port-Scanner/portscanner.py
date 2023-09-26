import socket
from IPy import IP
import threading

# Define the maximum number of threads to use
MAX_THREADS = 50

def print_pirate_face():
    """
    Prints an ASCII art representation of a pirate face.
    """
    print("   ______   ")
    print("  /  o o \\  ")
    print(" |  > ^ < |  Ahoy Matey!")
    print("  \\ \\_-_/ /  ")
    print("   `-----`   ")

def scan(target, start_port=0, end_port=1000):
    """
    Scans the specified target (IP or domain name).

    :param target: IP address or domain name to be scanned.
    :param start_port: Starting port number for the scan.
    :param end_port: Ending port number for the scan.
    """
    converted_ip = check_ip(target)
    print('\n' + '[*** Scanning Target]' + str(target))
    
    # Split the port range into chunks and scan each chunk in a separate thread.
    threads = []
    for port in range(start_port, end_port + 1):
        if threading.active_count() <= MAX_THREADS:
            thread = threading.Thread(target=scan_port, args=(converted_ip, port))
            threads.append(thread)
            thread.start()
        else:
            port += 1

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

def check_ip(ip):
    """
    Checks if the provided input is an IP address or a domain name.
    If it's a domain name, it returns the corresponding IP address.

    :param ip: IP address or domain name.
    :return: IP address.
    """
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    """
    Fetches the banner from the socket connection.

    :param s: Socket object.
    :return: Received banner (if any).
    """
    try:
        s.send(b'Who are you?\r\n')  # Send a generic message to possibly trigger a response
        return s.recv(1024)
    except:
        return ""

def scan_port(ipaddress, port):
    """
    Scans a specific port on the provided IP address.

    :param ipaddress: IP address to be scanned.
    :param port: Port number to be scanned.
    """
    try:
        with socket.socket() as sock:
            sock.settimeout(1)
            sock.connect((ipaddress, port))
            banner = get_banner(sock)
            if banner:
                print(f'[+] Open Port {port}: {banner.decode().strip()}')
            else:
                print(f'[+] Open Port {port}')
    except (socket.timeout, socket.error):
        pass

if __name__ == "__main__":
    print_pirate_face()
    targets = input('[+] Enter Target/s To Scan (Split multiple targets with ,): ')

    # Check if there are multiple targets to scan.
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
