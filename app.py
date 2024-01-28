import pygame
import sys
from Player import Player
from Map import Map

class Game:
    """
    the root of all the objects in the app, 
    can run itself
    """

    def __init__(self):
        self.screen = pygame.display.set_mode()
        self.all_sprite = pygame.sprite.Group()
        self.solid_objects = pygame.sprite.Group()
        self.resorce_objects = pygame.sprite.Group()
        self.map = Map(self)
        self.player = Player(self, self.all_sprite)
        self.is_runing = True


    def run(self):
        while self.is_runing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_runing = False
                    sys.exit()        
          
            self.update()
            self.draw()


    def update(self):
        self.player.update()

    def draw(self):
        self.screen.fill('blue')
        self.all_sprite.draw(self.screen)
        pygame.display.update()



if __name__ == '__main__':
    game = Game()
    game.run()