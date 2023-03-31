import socket


def main():

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    clientSocket, _ = server_socket.accept()  # wait for client

    while clientSocket.recv(1024):
        clientSocket.send(b"+PONG\r\n")


if __name__ == "__main__":
    main()
