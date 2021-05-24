import os
#import pygame
import sys
from pynput import keyboard


class Controller:
    def __init__(self):
        pass

    def on_press(self, key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    def on_release(self, key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def run_listning(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()
            print(listener)


if __name__ == '__main__':
    Controller().run_listning()

