import pygame

from Game import Game

pygame.init()

screen = pygame.display.set_mode((612, 382))
pygame.display.set_caption("Dino Le Fifou")

clock = pygame.time.Clock()

background = pygame.image.load("assets/images/background_star.jpg")

game = Game()

running = True



while running:

    screen.blit(background, (0, 0))
    screen.blit(game.dino.image, game.dino.rect)

    if game.touches_pressees.get(pygame.K_q) and game.dino.rect.x > 0:
        game.dino.move_left()
    elif game.touches_pressees.get(pygame.K_d) and game.dino.rect.x < (screen.get_width() - game.dino.rect.width):
        game.dino.move_right()
    elif game.touches_pressees.get(pygame.K_d) and game.touches_pressees.get(pygame.K_a) and game.dino.rect.x < (screen.get_width() - game.dino.rect.width) and not game.dino.is_dashing:
        game.dino.dash_right()
    if game.touches_pressees.get(pygame.K_q) and game.touches_pressees.get(pygame.K_a) and game.dino.rect.x > 0 and not game.dino.is_dashing:
        game.dino.dash_left()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            game.touches_pressees[event.key] = True

        if event.type == pygame.KEYUP:
            game.touches_pressees[event.key] = False

    pygame.display.flip()

    clock.tick(60)
