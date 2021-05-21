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

    #while True:
        #movement = input("whats is your direction ")
        #print(movement)

    #clock = pygame.time.Clock()
    #pygame.display.set_mode((800, 600))
    #pygame.init()
    #while True:
    #    time = clock.tick(40)

        # GESTION DES EVENEMENTS
     #   for event in pygame.event.get():
     #       if event.type == pygame.QUIT:
    #            pygame.quit()
    #            sys.exit(0)

        # TOUCHES APPUYEES
     #   keys = pygame.key.get_pressed()

        # MAJ DE L'AFFICHAGE
     #   if keys[pygame.K_LEFT]:
     #       print("left")
     #   if keys[pygame.K_RIGHT]:
     #       print('right')
     #   if keys[pygame.K_UP]:
     #       print('up')
     #   if keys[pygame.K_DOWN]:
      #      print('down')
