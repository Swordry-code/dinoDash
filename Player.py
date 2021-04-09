import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.vitesse = 1
        self.dash = True
        self.image = pygame.transform.scale(pygame.image.load("assets/sprite/dino_idle.png"), (72, 72))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 358
        self.is_dashing = False

    def move_right(self):
        self.rect.x += self.vitesse
    
    def move_left(self):
        self.rect.x -= self.vitesse
    
    def dash_left(self):
        self.is_dashing = True
        fin_dash = self.rect.x - 30
        while self.rect.x > fin_dash:
            self.rect.x -= 5
        self.is_dashing = False

    def dash_right(self):
        self.is_dashing = True
        fin_dash = self.rect.x + 30
        while self.rect.x < fin_dash:
            self.rect.x += 5
        self.is_dashing = False
        