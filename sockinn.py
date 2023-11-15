import socket


def main():
    print("Hello world!")
    addr = ("", 65432)  # all interfaces, port 65432
    # Creates socket
    sockit = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binds address?
    sockit.bind((addr))
    while 1:
        # Wait for someone to ask to connect - listen
        sockit.listen(1)
        # Accept connection - Conn is the socket for the connection, addr is the address of the other end
        conn, addr = sockit.accept()
        # Using conn
        with conn:
            print(f"Connected by {addr}")
            while True:
                rescsize = 1024
                data = conn.recv(rescsize)
                if data:
                    print(data)
                    conn.close()


if __name__ == "__main__":
    main()
