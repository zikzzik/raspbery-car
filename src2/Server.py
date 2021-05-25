import threading
from lib.SocketConnection import SocketConnection
from lib.SocketServer import SocketServer
from lib.SocketClient import SocketClient
from Registry import Registry
from Controller import Controller
from Car import Car
from Errors import *


class Server:

    def __init__(self, host: str = "", port: int = 9345):
        self.host = host
        self.port = port
        self.socket_connection = None

        # self.socket_connection = SocketConnection(self.host, self.port).create_server()
        self.socket_server = SocketServer(self.route_message, self.host, self.port)
        self.car_registry = Registry()
        self.controller_registry = Registry()

        self.lock = threading.Lock()

    # def run(self):
    #     print("Server started !")
    #     while True:
    #         client_socket, (host, port) = self.socket_connection.accept()
    #         message = client_socket.recv(2048).decode()
    #         self.route_message(message, host=host, port=port, socket=client_socket)
    #         # threading.Thread(target=self.route_message, args=(message,),
    #         #                  kwargs={"host": host, "port": port, "socket": client_socket}).start()

    def run(self):
        self.socket_server.start()

    def route_message(self, message, **kwargs):
        route_dict = {"connect": self.connect,
                      "register": self.register,
                      "forward": self.forward,
                      "backward": self.backward,
                      "left": self.left,
                      "right": self.right,
                      }

        message_list = message.split(" ")
        fun_name = message_list.pop(0)
        assert fun_name in route_dict.keys(), f"Mauvais message {message}"
        kwargs["my_socket"] = SocketClient.from_socket(kwargs["my_socket"])

        return route_dict[fun_name](*message_list, **kwargs)

    def connect(self, robot_name, host, port, my_socket):
        # car
        if robot_name not in self.car_registry.keys():
            print(f"Car {robot_name} doesn't exist")
            return "unknown"
        if robot_name not in self.car_registry.keys(used=False):
            print(f"Car {robot_name} already used")
            return "already_used"

        # controller
        try:
            self.lock.acquire()
            self.controller_registry.add(Controller(host, port, my_socket, robot_name))
        except AlreadyExistError:
            print("User already exist !")
            return "user_already_exist"
        finally:
            self.lock.release()

        self.lock.acquire()
        self.car_registry[robot_name].used = True
        self.lock.release()

        print(f"Connected controller: {host} -> {robot_name}")
        return "ok"

    def register(self, robot_name, host, port, my_socket):
        try:
            self.lock.acquire()
            self.car_registry.add(Car(robot_name, host, port, my_socket))
        except AlreadyExistError:
            print("Car already exist !")
            return "already_exist"
        finally:
            self.lock.release()
        print(f"register car: {host} -> {robot_name} ")
        return "ok"

    def forward(self, host, port, my_socket):
        if host in self.controller_registry.keys():
            car_name = self.controller_registry[host].car_name
        else:
            return "unknown_controller"

        if car_name in self.car_registry.keys():
            car_socket = self.car_registry[car_name].socket
        else:
            return "unknown_car"

        command = self.apply_modify_car("forward")
        car_socket.send(command)
        return "ok"

    def backward(self, host, port, my_socket):
        if host in self.controller_registry.keys():
            car_name = self.controller_registry[host].car_name
        else:
            return "unknown_controller"

        if car_name in self.car_registry.keys():
            car_socket = self.car_registry[car_name].socket
        else:
            return "unknown_car"

        command = self.apply_modify_car("backward")
        car_socket.send(command)
        return "ok"

    def left(self, host, port, my_socket):
        if host in self.controller_registry.keys():
            car_name = self.controller_registry[host].car_name
        else:
            return "unknown_controller"

        if car_name in self.car_registry.keys():
            car_socket = self.car_registry[car_name].socket
        else:
            return "unknown_car"

        command = self.apply_modify_car("left")
        car_socket.send(command)
        return "ok"

    def right(self, host, port, my_socket):
        if host in self.controller_registry.keys():
            car_name = self.controller_registry[host].car_name
        else:
            return "unknown_controller"

        if car_name in self.car_registry.keys():
            car_socket = self.car_registry[car_name].socket
        else:
            return "unknown_car"

        command = self.apply_modify_car("right")
        car_socket.send(command)
        return "ok"

    def apply_modify_car(self, command):
        return command



if __name__ == "__main__":
    Server("localhost", 9345).run()