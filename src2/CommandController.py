from pynput import keyboard
from lib.SocketClient import SocketClient
import sys


class CommandController:

    def __init__(self, car_name):
        self.car_name = car_name
        self.client = SocketClient(lambda x: print("receive", x), host="localhost", port=9345)
        self.client.send(f"connect {self.car_name}")

    def forward(self):
        self.client.send("forward")

    def backward(self):
        self.client.send("backward")

    def left(self):
        self.client.send("left")

    def right(self):
        self.client.send("right")

    def on_press(self, key):
        ref_key_dict = {"z": self.forward, "s": self.backward, "q": self.left, "d": self.right}
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

