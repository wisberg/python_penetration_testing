import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Enter the IP Address you wish to scan: \n")
port = input("Enter the port you wish to scan: \n")

def portScan(port):
    if s.connect_ex((host, int(port))):
        print("The port is closed")
    else:
        print("The port is open")

portScan(port)