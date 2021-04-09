import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.vitesse = 10
        self.dash = True
        self.image = pygame.transform.scale(pygame.image.load("assets/sprite/dino_idle.png"), (96, 96))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.is_dashing = False
        self.idle_animation = [pygame.image.load("assets/sprite/idle1.png"), pygame.image.load("assets/sprite/idle2.png"), pygame.image.load("assets/sprite/idle3.png"), pygame.image.load("assets/sprite/idle4.png")]
        self.moving_left = False
        self.moving_right = False

    def default_rect_pos(self, screen):
        self.rect.x = 20
        self.rect.y = screen.get_height() - self.rect.height
    def move_right(self):
        self.moving_left = False
        self.moving_right = True
        self.rect.x += self.vitesse
    
    def move_left(self):
        self.moving_left = True
        self.moving_right = False
        self.rect.x -= self.vitesse
    
    def dash_left(self):
        self.is_dashing = True
        fin_dash = self.rect.x - 300
        while self.rect.x > fin_dash:
            self.rect.x -= 50
        self.is_dashing = False

    def dash_right(self):
        self.is_dashing = True
        fin_dash = self.rect.x + 300
        while self.rect.x < fin_dash:
            self.rect.x += 50
        self.is_dashing = False