from lib.SocketConnection import SocketConnection
import time

s = SocketConnection("localhost", 9345).create_client()

message = "connect ma_voiture"
s.my_socket.send(message.encode())
print("1", s.my_socket.recv(2048).decode())

time.sleep(2)

message = "forward"
s = SocketConnection("localhost", 9345).create_client()
s.my_socket.send(message.encode())
print("2", s.my_socket.recv(2048).decode())

if __name__ == "__main__":
    pass