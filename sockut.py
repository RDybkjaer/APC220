import socket


def main():
    print("Hello world!")
    addr = ("", 65432)  # all interfaces, port 65432
    sockit = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockit.bind((addr))
    sockit.listen(1)
    conn, addr = sockit.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)


if __name__ == "__main__":
    main()
