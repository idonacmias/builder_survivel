import pygame

class Player(pygame.sprite.Sprite):
    """docstring for Player"""
    def __init__(self, game, *arg):
        super().__init__(arg)
        self.game = game
        self.player_idole_path = 'player_stand_1.jpg'
        self.image = pygame.image.load(f'assets/{self.player_idole_path}')
        self.rect = self.image.get_rect()
        self.rect.move_ip(100, 100)


        self.interactive_radius = 35
        self.speed = 3

    @property
    def position(self):
        return [self.x, self.y]


    def update(self, keys):
        self.move_player(keys)
        self.extract_resorce(keys)

    def move_player(self, keys):
        temp_x = self.rect.x
        temp_y = self.rect.y
        self.rect.x = (keys[pygame.K_d] - keys[pygame.K_a]) * self.speed + self.rect.x
        self.rect.y = (keys[pygame.K_s] - keys[pygame.K_w]) * self.speed + self.rect.y
        if self.rect.x < 0 or self.rect.x > self.game.EDGE_x or self.is_collide_with_objects(self.game.solid_objects):
            self.rect.x = temp_x
        if self.rect.y < 0 or self.rect.y > self.game.EDGE_y or self.is_collide_with_objects(self.game.solid_objects):
            self.rect.y = temp_y


    def is_collide_with_objects(self, group):
         return pygame.sprite.spritecollide(self, group, False)


    def extract_resorce(self, keys):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            sprites = self.game.resorce_objects
            clicked_sprites = [s for s in sprites if s.rect.collidepoint(mouse_pos)]
            self.rect.scale_by_ip(self.interactive_radius)
            if pygame.sprite.spritecollide(self, clicked_sprites, False):
                clicked_sprite = clicked_sprites[0]
                if self.game.inventory.add(clicked_sprite):
                    clicked_sprite.remove(self.game.resorce_objects)
                    clicked_sprite.remove(self.game.all_sprite)
            
            self.rect.scale_by_ip(1/self.interactive_radius)    




