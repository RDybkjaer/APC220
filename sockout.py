# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    for i in range(3):
        string = "Hello, world" + str(i) + "\n"
        sb = string.encode("utf-8")
        s.connect((HOST, PORT))
        s.sendall(sb)
        s.shutdown(socket.SHUT_WR)
        s.close()
