import os
import pygame
import time
import random

WIDTH, HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Dodge")
BG = pygame.transform.scale(pygame.image.load("image/space_image.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

def draw(player):
    WIN.blit(BG, (0,0))

    pygame.draw.rect(WIN, "red", player)
    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(200, HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH,PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(player)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >=0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL
    pygame.quit()

if __name__ == "__main__":
    main()