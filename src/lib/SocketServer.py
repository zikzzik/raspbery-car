import socket
import threading


class SocketServer:

    def __init__(self, callback, host="", port=9000, header=64, disconnect_msg="exit"):
        self.host = host
        self.port = port
        self.header = header
        self.disconnect_msg = disconnect_msg
        self.callback = callback
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))

    def handle_client(self, my_socket, host, port):
        connected = True
        while connected:
            # msg_length = my_socket.recv(self.header).decode()
            # if msg_length:
            #     msg_length = int(msg_length)
            #     msg = my_socket.recv(msg_length).decode()
            #     if msg == self.disconnect_msg:
            #         connected = False
            msg = my_socket.recv(1048).decode()
            res = self.callback(msg, my_socket=my_socket, host=host, port=port)
            my_socket.send(res.encode())

        my_socket.close()

    def start(self):
        self.server.listen()
        print(f"[LISTENING] Server is listening on")
        while True:
            conn, (host, port) = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, host, port))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == "__main__":
    SocketServer(lambda x: print("route", x)).start()
