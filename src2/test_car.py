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

    connected = True
    while connected:
        msg_length = s.client.recv(s.header).decode()
        if msg_length:
            msg_length = int(msg_length)
            msg = s.client.recv(msg_length).decode()
            if msg == s.disconnect_msg:
                connected = False

            print("action :", msg)

    s.client.close()
