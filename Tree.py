import pygame


class Tree(pygame.sprite.Sprite):
    """docstring for Tree"""
    def __init__(self, game, x, y, *arg):
        super().__init__(arg)
        self.game = game
        self.surface = pygame.Surface([40, 40])
        self.image = pygame.image.load('assets/tree1.jpg')
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)



