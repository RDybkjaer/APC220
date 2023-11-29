# echo-client.py

import SOCKET

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


def main():
    s = SOCKET.sock(HOST, PORT)
    for i in range(0, 200, 10):
        string = "Hello world! " + str(i)
        s.sendString(string)
        data = s.receiveBytes()
        print("Echoed: " + data.decode("utf-8"))
    s.close()


if __name__ == "__main__":
    main()
