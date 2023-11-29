import socket


def main():
    print("Hello world!")
    addr = ("", 65432)  # all interfaces, port 65432
    # Creates socket
    sockit = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binds address?
    sockit.bind((addr))
    while True:
        # Wait for someone to ask to connect - listen
        sockit.listen()
        # Accept connection - Conn is the socket for the connection, addr is the address of the other end
        conn, addr = sockit.accept()
        # Using conn
        print(f"Connected by {addr}")
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
