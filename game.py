import pygame
from entities import Player
from entities import Ball



pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong on Py")
clock = pygame.time.Clock()
player_1 = Player(screen, 125, 200, "Red")
player_2 = Player(screen, 645, 200, "Blue")
bola = Ball(screen, 400, 300)

game_objects = [player_1, player_2, bola]

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_1.y -= player_1.velocidade

    if keys[pygame.K_s]:
        player_1.y += player_1.velocidade

    if keys[pygame.K_UP]:
        player_2.y -= player_2.velocidade

    if keys[pygame.K_DOWN]:
        player_2.y += player_2.velocidade

    screen.fill ((0, 166, 251))

    for obj in game_objects:
        if isinstance(obj, Ball):
            obj.update(player_1, player_2)
        else:
            obj.update()

    for obj in game_objects:
        obj.draw()

    pygame.draw.rect(screen, "white", [100, 20, 600, 560], 2)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()