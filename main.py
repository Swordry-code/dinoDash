import pygame

from Game import Game

pygame.init()

screen = pygame.display.set_mode((612, 382))
pygame.display.set_caption("Dino Le Fifou")

background = pygame.image.load("assets/images/background_star.jpg")

game = Game()

running = True

while running:

    screen.blit(background, (0, 0))
    screen.blit(game.dino.image, game.dino.rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                game.dino.rect.x += game.dino.vitesse

#Test Github