import pygame, sys
from settings import *
#Here we all atributes in the class we use it to define what operations can be done my a variable

class Game:
    def __init__ (self):
        #here we initiate pygame
        pygame.init()
        #display serfece that is the basic setup we need for pigame
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        self.clock = pygame.time.Clock()

    def run(self):
          while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()

            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(FPS)
if __name__ == '__main__':
    game=Game()
    game.run()
    