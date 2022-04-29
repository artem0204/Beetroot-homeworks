from socket import *

socket = socket(AF_INET, SOCK_STREAM)
socket.connect(("localhost", 9090))
request = None

try:
    while request != "quit":
        request = input("Write message here: ")
        if request:
            socket.send(request.encode("utf8"))
            response = socket.recv(255).decode("utf8")
            if response:
                print(f"response from server - OK")
            else:
                print("No response from server ")
except KeyboardInterrupt:
    socket.close()
