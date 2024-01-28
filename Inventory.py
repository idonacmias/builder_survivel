import pygame
from Sprites import MySprite


class Inventory(pygame.sprite.Sprite):
    """docstring for Inventory"""
    def __init__(self, game):
        self.game = game        
        self.cells = pygame.sprite.Group()
        self.hide = False
        self.K_e_holder = True
        row_number = 10 
        col_number = 10 
        first_cell = Cell.create_image('tree1')
        width, hight = first_cell.get_size()    
        for row in range(row_number):
            row = row * width + 500
            for col in range(col_number):
                col = col * hight + 100
                
                Cell(self.game, row, col, first_cell.copy(), 
                     self.cells)

    def update(self, keys):
        self.display_inventory(keys)

    def display_inventory(self, keys):
        if keys[pygame.K_e] and self.K_e_holder:
            self.K_e_holder = False
            if self.hide:  self.hide = False
            else: self.hide = True

        elif not keys[pygame.K_e]:
            self.K_e_holder = True

class Cell(MySprite):
    """docstring for Cell"""
    HIGHT  = 100
    WIDTH  = 100
    def __init__(self, *arg):
        super().__init__(*arg)
        
        