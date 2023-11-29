#!/usr/bin/env python3
import socket


class sock(socket.socket):
    isServer: bool

    def __init__(self, HOST, PORT, isServer: bool = False):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.isServer = isServer
        if isServer:
            self.bind((HOST, PORT))
        else:
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

    def lyt(self) -> socket.socket:
        # TODO: Kald den et bedre navn
        # TODO: Smid en exception hvis det ikke er en server
        self.listen()
        # Accept connection - Conn is the socket for the connection, addr is the address of the other end

        conn, addr = self.accept()
        if conn:
            print("Connected by " + str(addr))
            return conn
        else:
            print("No connection")
            return None
