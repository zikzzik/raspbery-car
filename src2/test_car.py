from lib.SocketConnection import SocketConnection
import time

message = "register ma_voiture"

s = SocketConnection("localhost", 9345).create_client()
s.my_socket.send(message.encode())
while True:
    print(".", end="")
    print(s.my_socket.recv(2048).decode(), end="")
    time.sleep(5)

if __name__ == "__main__":
    pass