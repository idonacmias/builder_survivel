import pygame


class CollidieingError(Exception):
    """docstring for CollidieingError"""
    pass



class MySprite(pygame.sprite.Sprite):
    """docstring for MySprite"""
    def __init__(self, game, x, y, image, *arg):
        super().__init__(*arg)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)

        if self.is_collide_with_objects(self.game.solid_objects):
            self.kill()
            raise CollidieingError()

    def is_collide_with_objects(self, group):
        spritecolide = pygame.sprite.spritecollide(self, group, False)
        if len(spritecolide) > 1 and self in group:
            return True

    @classmethod
    def create_image(cls, image_path):
        return pygame.image.load(f'assets/{image_path}.jpg')
         


class Tree(MySprite):
    def __init__(self, *arg):
        super().__init__(*arg)

class Stone(MySprite):
    """docstring for Stone"""
    def __init__(self, *arg):
        super().__init__(*arg)
        
# class Stone(pygame.sprite.Sprite):
#     """docstring for Stone"""

#     def __init__(self, game, image, x, y, *arg):
#         super().__init__(arg)
#         self.game = game
#         self.image = image
#         self.rect = self.image.get_rect()
#         self.rect.move_ip(x, y)


#     @classmethod
#     def create_image(cls):
#         return pygame.image.load('assets/stone.jpg')
         



