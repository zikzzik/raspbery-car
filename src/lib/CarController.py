from .CarAction import CarAction
from .SocketClient import SocketClient


class CarController:
    def __init__(self, car_name="my_car", host="localhost", port=9000, action_time=1, speed=50):

        self.action_time = action_time
        self.speed = speed
        self.car_name = car_name
        self.car_action = CarAction()

        self.client = SocketClient(self.route_message, host=host, port=port)
        self.client.send(f"register {car_name}")

    def route_message(self, message):
        route_dict = {"forward": self.forward,
                      "backward": self.backward,
                      "left": self.left,
                      "right": self.right}

        if message in route_dict.keys():
            route_dict[message]()
        else:
            ValueError(f"Bad message {message}")

    def forward(self):
        self.car_action.forward(self.action_time, self.speed)

    def backward(self):
        self.car_action.backward(self.action_time, self.speed)

    def left(self):
        self.car_action.forward(self.action_time, self.speed)

    def right(self):
        self.car_action.right(self.action_time, self.speed)

    def run(self):
        self.client.wait_many_responses()
