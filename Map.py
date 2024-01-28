import pygame
from Sprites import Tree, Stone, CollidieingError
from random import randrange

class Map:
    """docstring for Map"""
    def __init__(self, game):
        self.game = game
        self.create_stones()
        self.create_trees()

    def create_trees(self):
        number_of_trees = 5
        for i in range(number_of_trees):
            first_tree = Tree.create_image('tree1')
            width, hight = first_tree.get_size()    
            while True:
                try:
                    x = randrange((self.game.EDGE_x - width))   
                    y = randrange((self.game.EDGE_y - hight))
                    tree = Tree(self.game, x, y, first_tree.copy(),
                                self.game.solid_objects, 
                                self.game.all_sprite, 
                                self.game.resorce_objects)

                except CollidieingError:
                    None

                except Exception as e:
                    raise e

                else:
                    break
                


    def create_stones(self):
        number_of_stone = 5
        for _ in range(number_of_stone):
            self.create_patch_of_stone()
            
    def create_patch_of_stone(self):
            size = 100
            y = randrange(1500)
            d_y = y + randrange(3, size)   
            x = randrange(1100)
            first_stone = Stone.create_image('stone')
            width, hight = first_stone.get_size()    
            for i in range(y, d_y, width):
                d_x = x + randrange(3, size)
                for j in range(x, d_x, hight):
                    Stone(self.game,i, j, first_stone.copy(),
                          self.game.all_sprite, 
                          self.game.resorce_objects)
