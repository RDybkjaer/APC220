# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


def main():
    s = sock(socket.AF_INET, socket.SOCK_STREAM)
    for i in range(0, 200, 10):
        string = "Hello world! " + str(i)
        s.senddata(string)
        data = s.recvdata()
        print("Echoed: " + data.decode("utf-8"))
    s.sock.close()


class sock:
    sock: socket.socket

    def __init__(self, param1, param2):
        self.s = socket.socket(param1, param2)
        self.s.connect((HOST, PORT))

    def senddata(self, string: str):
        sb = string.encode("utf-8")
        sl = len(sb)
        self.s.sendall(sl.to_bytes(2, "little"))
        self.s.sendall(sb)

    def recvdata(self):
        bl = self.s.recv(2)
        rescsize = int.from_bytes(bl, "little")
        print("\t\t Received size: " + str(rescsize))
        data = self.s.recv(rescsize)
        return data


if __name__ == "__main__":
    main()
