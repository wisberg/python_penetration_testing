import socket

clientSocket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

host = socket.gethostname()

port = 4000

clientSocket.connect((host, port))

message = clientSocket.recv(1024)

clientSocket.close()

print(message.decode('ascii'))