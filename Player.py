import pygame

#constents
EDGE_X = 1907
EDGE_y = 1125

class Player(pygame.sprite.Sprite):
    """docstring for Player"""
    def __init__(self, game, *arg):
        super().__init__(arg)
        self.game = game
        self.x = 100
        self.y = 200
        self.radius_rect = 20
        self.interactive_radius = 35
        self.speed = 3

        self.surface = pygame.Surface([10, 10])
        self.player_idole_path = 'player_stand_1.jpg'
        self.image = pygame.image.load(f'assets/{self.player_idole_path}')

        self.rect = self.surface.get_rect()
        self.rect.move_ip(100, 100)
        self.inventory = pygame.sprite.Group()

    @property
    def position(self):
        return [self.x, self.y]


    def update(self):
        keys = pygame.key.get_pressed()
        self.move_player(keys)
        self.extract_resorce(keys)
        self.display_inventory(keys)

    def move_player(self, keys):
        temp_x = self.rect.x
        temp_y = self.rect.y
        self.rect.x = (keys[pygame.K_d] - keys[pygame.K_a]) * self.speed + self.rect.x
        self.rect.y = (keys[pygame.K_s] - keys[pygame.K_w]) * self.speed + self.rect.y
        if self.rect.x < 0 or self.rect.x > EDGE_X or self.is_collide_with_objects(self.game.solid_objects):
            self.rect.x = temp_x
        if self.rect.y < 0 or self.rect.y > EDGE_y or self.is_collide_with_objects(self.game.solid_objects):
            self.rect.y = temp_y


    def is_collide_with_objects(self, group):
         return pygame.sprite.spritecollide(self, group, False)


    def extract_resorce(self, keys):
        if pygame.mouse.get_pressed()[0]:
            print('mouse pressed')
            mouse_pos = pygame.mouse.get_pos()
            sprites = self.game.resorce_objects
            clicked_sprites = [s for s in sprites if s.rect.collidepoint(mouse_pos)]
            self.rect.scale_by_ip(self.interactive_radius)
            if pygame.sprite.spritecollide(self, clicked_sprites, False):
                clicked_sprite = clicked_sprites[0]
                clicked_sprite.kill() # this will remove the sprite from all grupes! 
                self.inventory.add(clicked_sprite)
                print(clicked_sprite)
            
            self.rect.scale_by_ip(1/self.interactive_radius)    



    def display_inventory(self, keys):
        if keys[pygame.K_e]:
            print(self.inventory)


    