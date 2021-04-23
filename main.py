import pygame

from Game import Game

pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen_rect = screen.get_rect()
pygame.display.set_caption("Dino Le Fifou")

clock = pygame.time.Clock()

background = pygame.image.load("assets/images/background_star.jpg").convert()
background = pygame.transform.scale(background, (screen_rect.width, screen_rect.height))

game = Game()
game.dino.default_rect_pos(screen)

running = True

def update_screen():
    pygame.display.update()
    

while running:

    screen.blit(background, (0, 0))
    screen.blit(game.dino.image, game.dino.rect)


    if game.touches_pressees.get(pygame.K_ESCAPE):
        running = False
        pygame.quit()
    elif game.touches_pressees.get(pygame.K_q) and game.dino.rect.x > 0:
        if game.touches_pressees.get(pygame.K_a) and not game.dino.is_dashing:
            game.dino.dash_left()
            game.touches_pressees[pygame.K_a] = False
        else:
            game.dino.move_left()
    elif game.touches_pressees.get(pygame.K_d) and game.dino.rect.x < (screen.get_width() - game.dino.rect.width):
        if game.touches_pressees.get(pygame.K_a) and not game.dino.is_dashing:
            game.dino.dash_right()
            game.touches_pressees[pygame.K_a] = False
        else:
            game.dino.move_right()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            game.touches_pressees[event.key] = True

        if event.type == pygame.KEYUP:
            game.touches_pressees[event.key] = False
    
    pygame.display.update()

    clock.tick(60)
