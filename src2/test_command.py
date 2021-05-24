from lib.SocketConnection import SocketConnection


s = SocketConnection("localhost", 9345).create_client()

message = "connect ma_voiture"
s.my_socket.send(message.encode())

# print(s.my_socket.recv(2048).decode())
#
# message = "connect ma_voiture"
# s.my_socket.send(message.encode())
#
# print(s.my_socket.recv(2048).decode())

message = "forward"
print(message)
s.my_socket.send(message.encode())
print(s.my_socket.recv(2048).decode())

if __name__ == "__main__":
    pass