import pygame
from Sprites import BaseSprite


class Inventory(pygame.sprite.Sprite):
    """docstring for Inventory"""
    def __init__(self, game):
        self.game = game        
        self.cells = pygame.sprite.Group()
        self.hide = False
        self.K_e_holder = True
        row_number = 10 
        col_number = 10 
        first_cell = Cell.create_image('empty_cell')
        width, hight = first_cell.get_size()    
        for row in range(row_number):
            row = row * width + 500
            for col in range(col_number):
                col = col * hight + 100
                
                Cell(self.game, row, col, first_cell.copy(), 
                     self.cells)

    def add(self, resorce):
        empty_cell = 0
        for cell in self.cells:
            if type(cell.resorce) == type(resorce) and cell.quantity < resorce.max_stack:
                cell.quantity += 1
                return 1

            elif not empty_cell and not cell.resorce:
                empty_cell = cell

        else:
            if empty_cell:
                empty_cell.resorce = resorce
                empty_cell.quantity = 1
                empty_cell.shrink_image()
                return 1

            else:
                return None

    def update(self, keys):
        self.reveal_or_hide(keys)

    def reveal_or_hide(self, keys):
        if keys[pygame.K_e] and self.K_e_holder:
            self.K_e_holder = False
            if self.hide:  self.hide = False
            else: self.hide = True

        elif not keys[pygame.K_e]:
            self.K_e_holder = True

    
class Cell(BaseSprite):
    """docstring for Cell"""


    def __init__(self, *arg):
        super().__init__(*arg)
        self.resorce = 0
        self.quantity = 0
        

    def shrink_image(self):
        new_image = pygame.transform.scale(self.resorce.image, self.image.get_size())
        pos = (self.rect.x, self.rect.y)
        self.image = new_image
        self.image.blit(self.game.screen, pos)