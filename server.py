#!/usr/bin/env python3
import SOCKET


HOST = ""
PORT = 65432


def main():
    print("Hello world!")
    s = SOCKET.sock(HOST, PORT, True)
    while True:
        # Wait for someone to ask to connect - listen
        conn = s.lyt()
        # Using conn
        with conn:
            while True:
                bl = conn.recv(2)
                rescsize = int.from_bytes(bl, "little")
                print(rescsize)
                data = conn.recv(rescsize)
                if data:
                    print(data)
                    conn.sendall(rescsize.to_bytes(2, "little"))
                    conn.sendall(data)
                if not data:
                    break


if __name__ == "__main__":
    main()
