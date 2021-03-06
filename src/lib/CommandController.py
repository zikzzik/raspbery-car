from pynput import keyboard
from .SocketClient import SocketClient
import sys


class CommandController:

    def __init__(self, car_name, host="localhost", port="port"):
        self.car_name = car_name
        self.client = SocketClient(lambda x: print("receive", x), host=host, port=port)
        self.client.send(f"connect {self.car_name}")
        self.speed = 50

    def forward(self):
        self.client.send("forward")

    def backward(self):
        self.client.send("backward")

    def left(self):
        self.client.send("left")

    def right(self):
        self.client.send("right")

    def speed_up(self):
        self.speed += 5
        self.client.send(f"speed {self.speed}")

    def speed_down(self):
        self.speed -= 5
        self.client.send(f"speed {self.speed}")

    def on_press(self, key):
        ref_key_dict = {"z": self.forward, "s": self.backward, "q": self.left, "d": self.right, "r": self.speed_up,
                        "f": self.speed_down}
        try:
            print(key.char)
            if key.char in ref_key_dict.keys():
                ref_key_dict[key.char]()
        except AttributeError:
            print('special key {0} pressed'.format(key))
            print("bye !")
            sys.exit()

    def run(self):
        with keyboard.Listener(
                on_press=self.on_press,
        ) as listener:
            listener.join()


if __name__ == '__main__':
    CommandController("ma_voiture").run()

