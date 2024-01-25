import pygame
from Tree import Tree
from random import randrange

class Map:
    """docstring for Map"""
    def __init__(self, game):
        self.game = game
        self.create_tree()
        

    def create_tree(self):
        number_of_trees = 5
        for i in range(number_of_trees):
            x = randrange(1500)   
            y = randrange(1100)
            tree = Tree(self.game, x, y,
                        self.game.solid_objects, 
                        self.game.all_sprite, 
                        self.game.resorce_objects)
