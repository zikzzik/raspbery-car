from lib.SocketConnection import SocketConnection


message = "register ma_voiture"

s = SocketConnection("localhost", 9345).create_client()
s.my_socket.send(message.encode())
while True:
    print(s.my_socket.recv(2048).decode())

if __name__ == "__main__":
    pass