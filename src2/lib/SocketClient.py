import socket


class SocketClient:
    def __init__(self, callback, host="localhost", port=9000, header=64, disconnect_msg="exit"):
        self.callback = callback
        self.host = host
        self.port = port
        self.header = header
        self.disconnect_msg = disconnect_msg
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def send(self, msg):
        b_msg = msg.encode()
        msg_length = len(b_msg)
        send_length = str(msg_length).encode()
        send_length += b' ' * (self.header - len(send_length))
        self.client.send(send_length)
        self.client.send(b_msg)
        self.callback(self.client.recv(2048).decode())


if __name__ == "__main__":
    s = SocketClient(lambda x: print("receive", x))
    s.send("conn ma")
    s.send("forward")
    s.send("backward")
    s.send("left")