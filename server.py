#How to create a TCP Server in Python3

import socket

#socket.socket creates a a network socket
#socket.AF_INET specifies the address family, in this case, AF_INET, which stands for IPv4. It means that the socket will use the IPv4 protocol for communication. IPv4 is the older version of the Internet Protocol.
#socket.SOCK_STREAM specifies the type of socket. SOCK_STREAM means that it's a streaming socket, which is used for reliable, connection-oriented communication. It's often associated with protocols like TCP (Transmission Control Protocol) that provide a reliable and ordered data stream.

serverSocket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

host = socket.gethostname() #Gets IP of host or server
port = 4000

serverSocket.bind((host, port)) #Bind the serverSocket to the host and the port

serverSocket.listen(3) #Tell your server to listen, the number specifies how many devices can connect, you can have as many as you want. 

while True:
    clientSocket, address = serverSocket.accept() #Accept information coming in from the client

    print(f"Received connection from: {str(address)}")

    message = 'Thank you for connecting to the server' + "\r\n"

    clientSocket.send(message.encode('ascii'))

    clientSocket.close()

