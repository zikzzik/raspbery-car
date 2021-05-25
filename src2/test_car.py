# from lib.SocketConnection import SocketConnection
# import time
#
# message = "register ma_voiture"
#
# s = SocketConnection("localhost", 9345).create_client()
# s.my_socket.send(message.encode())
# while True:
#     print(".", end="")
#     print(s.my_socket.recv(2048).decode(), end="")
#     time.sleep(5)

from lib.SocketClient import SocketClient
import time

if __name__ == "__main__":
    s = SocketClient(lambda x: print("receive", x), host="localhost", port=9345)
    s.send("register ma_voiture")

    s.wait_many_responses()
