# from lib.SocketConnection import SocketConnection
import time

# s = SocketConnection("localhost", 9345).create_client()
#
# message = "connect ma_voiture"
# s.my_socket.send(message.encode())
# print("1", s.my_socket.recv(2048).decode())
#
# time.sleep(2)
#
# message = "forward"
# s = SocketConnection("localhost", 9345).create_client()
# s.my_socket.send(message.encode())
# print("2", s.my_socket.recv(2048).decode())

from lib.SocketClient import SocketClient

s = SocketClient(lambda x: print("receive", x), host="localhost", port=9345)
s.send("connect ma_voiture")
time.sleep(1)
s.send("forward")
time.sleep(1)
s.send("forward")
time.sleep(1)
s.send("backward")
time.sleep(1)
s.send("left")
time.sleep(1)
s.send("backward")
time.sleep(1)
s.send("right")


if __name__ == "__main__":
    pass