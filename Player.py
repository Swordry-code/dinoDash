import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.vitesse = 1
        self.dash = True
        self.image = pygame.image.load("assets/sprite/dino_idle.png")
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 358

        