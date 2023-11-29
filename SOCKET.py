import socket


class sock(socket.socket):
    def __init__(self, HOST, PORT):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((HOST, PORT))

    def sendBytes(self, toSend: bytes):
        sl = len(toSend)
        self.sendall(sl.to_bytes(2, "little"))
        self.sendall(toSend)

    def sendString(self, string: str):
        sb = string.encode("utf-8")
        self.sendBytes(sb)

    def receiveBytes(self):
        bl = self.recv(2)
        rescsize = int.from_bytes(bl, "little")
        print("\t\t Received size: " + str(rescsize))
        data = self.recv(rescsize)
        return data
