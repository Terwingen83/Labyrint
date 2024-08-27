import pygame
import os.path
from src.models.position import Position

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

GRASS_IMAGE = pygame.image.load('../images/terrain/grass/green.png')
TILE_SIZE = Position(72, 72)



def map_output(screen):
    for y in range(10):
        for x in range(10):
            screen.blit(GRASS_IMAGE, (72 * x, 72 * y))


while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("purple")


    map_output(screen)

    # Render the graphics here.
    # ...

    pygame.display.flip()
    clock.tick(60)