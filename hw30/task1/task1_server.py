from socket import *

local_ip = "localhost"
local_port = 2022
buffer_size = 1024
reply_from_server = str.encode("reply from server : your data was successfully received.")
udp_s = socket(AF_INET, SOCK_DGRAM)
udp_s.bind((local_ip, local_port))
print("The udp server is working now ")
try:
    while True:
        connection_adrres_pair = udp_s.recvfrom(buffer_size)
        msg = connection_adrres_pair[0]
        adress = connection_adrres_pair[1]
        print(f"The data from client: {msg.decode()}")
        udp_s.sendto(reply_from_server, adress)
finally:
    udp_s.close()
