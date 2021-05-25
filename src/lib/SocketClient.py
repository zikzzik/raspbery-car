import socket


class SocketClient:
    def __init__(self, callback=None, host="localhost", port=9000, header=64, disconnect_msg="exit", my_socket=None):
        self.callback = callback
        self.host = host
        self.port = port
        self.header = header
        self.disconnect_msg = disconnect_msg
        if my_socket is None:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.host, self.port))
        else:
            self.client = my_socket

    def send(self, msg):
        b_msg = msg.encode()
        msg_length = len(b_msg)
        send_length = str(msg_length).encode()
        send_length += b' ' * (self.header - len(send_length))
        self.client.send(send_length)
        self.client.send(b_msg)
        if self.callback is not None:
            self.callback(self.client.recv(2048).decode())

    @classmethod
    def from_socket(cls, my_socket, callback=None):
        return cls(my_socket=my_socket, callback=callback)

    def wait_many_responses(self):
        connected = True
        while connected:
            msg_length = self.client.recv(self.header).decode()
            if msg_length:
                msg_length = int(msg_length)
                msg = self.client.recv(msg_length).decode()
                if msg == self.disconnect_msg:
                    connected = False

                print("action :", msg)

        self.client.close()

