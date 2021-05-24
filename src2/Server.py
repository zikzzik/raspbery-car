import threading
from lib.SocketConnection import SocketConnection
from Registry import Registry
from Controller import Controller
from Car import Car
from Errors import *


class Server:

    def __init__(self, host: str = "", port: int = 9345):
        self.host = host
        self.port = port
        self.socket_connection = None

        self.socket_connection = SocketConnection(self.host, self.port).create_server()
        self.car_registry = Registry()
        self.controller_registry = Registry()

        self.lock = threading.Lock()

    def run(self):
        print("Server started !")
        while True:
            print("a")
            client_socket, (host, port) = self.socket_connection.accept()
            message = client_socket.recv(2048).decode()
            threading.Thread(target=self.route_message, args=(message,),
                             kwargs={"host": host, "port": port, "socket": client_socket}).start()

    def route_message(self, message, **kwargs):
        route_dict = {"connect": self.connect,
                      "register": self.register,
                      "forward": self.forward}

        message_list = message.split(" ")
        fun_name = message_list.pop(0)
        route_dict[fun_name](*message_list, **kwargs)

    def connect(self, robot_name, host, port, socket):
        # car
        if robot_name not in self.car_registry.keys():
            print(f"Car {robot_name} doesn't exist")
            socket.send("unknown".encode())
            return
        if robot_name not in self.car_registry.keys(used=False):
            print(f"Car {robot_name} already used")
            socket.send("already_used".encode())
            return

        # controller
        try:
            self.lock.acquire()
            self.controller_registry.add(Controller(host, port, socket, robot_name))
        except AlreadyExistError:
            print("User already exist !")
            socket.send("user_already_exist".encode())
            return
        finally:
            self.lock.release()

        self.lock.acquire()
        self.car_registry[robot_name].used = True
        self.lock.release()

        print(f"Connected controller: {host} -> {robot_name}")
        socket.send("ok".encode())
        return

    def register(self, robot_name, host, port, socket):
        try:
            self.lock.acquire()
            self.car_registry.add(Car(robot_name, host, port, socket))
        except AlreadyExistError:
            print("Car already exist !")
            socket.send("already_exist".encode())
            return
        finally:
            self.lock.release()
        print(f"register car: {host} -> {robot_name} ")
        socket.send("ok".encode())
        return

    def forward(self, host, port, socket):
        if host in self.car_registry.keys():
            car_socket = self.car_registry[host]
        else:
            socket.send("unknown_car".encode())
            return

        command = self.apply_modify_car("forward")
        car_socket.send(command.encode())
        return

    def apply_modify_car(self, command):
        return command



if __name__ == "__main__":
    Server("localhost", 9345).run()