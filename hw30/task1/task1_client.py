from socket import *

local_ip = "localhost"
local_port = 2022
buffer_size = 1024
while True:
    try:

        msg = input("Please enter the message: ")
        s = socket(AF_INET, SOCK_DGRAM)
        if msg == "quit":
            s.close()
            break
        s.connect((local_ip, local_port))
        s.send(msg.encode())
        msg_from_server = s.recvfrom(buffer_size)
        print(msg_from_server)
    finally:
        s.close()
