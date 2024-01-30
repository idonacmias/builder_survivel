import pygame
import sys
from Player import Player
from Map import Map
from Inventory import Inventory

class Game:
    """
    the root of all the objects in the app, 
    can run itself
    """

    def __init__(self):
        self.screen = pygame.display.set_mode()
        self.EDGE_x = 1900
        self.EDGE_y = 1125
        self.all_sprite = pygame.sprite.Group()
        self.solid_objects = pygame.sprite.Group()
        self.resorce_objects = pygame.sprite.Group()
        self.inventory_items = pygame.sprite.Group()
        self.map = Map(self)
        self.player = Player(self, self.all_sprite)
        self.inventory = Inventory(self)

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
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        self.inventory.update(keys)

    def draw(self):
        self.screen.fill('blue')
        self.all_sprite.draw(self.screen)
        if self.inventory.hide: self.inventory.cells.draw(self.screen)
        pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()