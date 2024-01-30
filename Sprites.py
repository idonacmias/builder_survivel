import pygame


class CollidieingError(Exception):
    pass



class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, game, x, y, image, *arg):
        super().__init__(*arg)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)

        
    @classmethod
    def create_image(cls, image_path):
        return pygame.image.load(f'assets/{image_path}.jpg')
         

class Resorce(BaseSprite):
    def __init__(self, *arg):
        super().__init__(*arg)
        self.max_stack = 2
        self.start_colision_chack()

    def start_colision_chack(self):
        if self.is_collide_with_objects(self.game.solid_objects):
            self.kill()
            raise CollidieingError()

    def is_collide_with_objects(self, group):
        spritecolide = pygame.sprite.spritecollide(self, group, False)
        if len(spritecolide) > 1 and self in group:
            return True


class Tree(Resorce):
    def __init__(self, *arg):
        super().__init__(*arg)

class Stone(Resorce):
    def __init__(self, *arg):
        super().__init__(*arg)


