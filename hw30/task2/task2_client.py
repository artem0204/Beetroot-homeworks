from socket import *
host = "localhost"
port = 9065
buffer_size = 1024
while True:
    try:
        msg = input("pleas enter your message, but in first time enter key:(your key) ")
        sock = socket(AF_INET,SOCK_DGRAM)
        sock.connect((host,port))
        sock.send(msg.encode())
        msg_from_server = sock.recvfrom(buffer_size)
        msg1 = msg_from_server[0]
        print(msg1.decode())
        if msg == "close":
            sock.close()
            break
    finally:
        sock.close()
