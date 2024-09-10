import pygame
import os.path

from src.models.map import Map
from src.models.entity import Wall
from src.models.position import Position

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

GRASS_IMAGE = pygame.image.load('../images/terrain/grass/green.png')
WALL = pygame.image.load('../images/terrain/mountains/dry-tile.png')
WATER = pygame.image.load('../images/terrain/water/coast-tropical-A01.png')

TILE_SIZE = Position(72, 72)

level1 = Map(maxsize=Position(20, 20))
# weiterarbeit an mauerbau

def draw_map(screen):
    screen_size_x, screen_size_y = screen.get_size()
    hexagon_tile_size_x = TILE_SIZE.x * 3 / 4

    offset_x = TILE_SIZE.x / 4
    offset_y = TILE_SIZE.y / 2

    for y in range(round(screen_size_y / TILE_SIZE.y) + 1):
        for x in range(round(screen_size_x / hexagon_tile_size_x) + 1):
            if x % 2 == 0:
                screen.blit(GRASS_IMAGE, (hexagon_tile_size_x * x - offset_x, TILE_SIZE.y * y - offset_y))
            else:
                screen.blit(GRASS_IMAGE, (hexagon_tile_size_x * x - offset_x, TILE_SIZE.y * y + TILE_SIZE.y / 2 - offset_y))


def draw_entity(screen, entity):
    hexagon_tile_size_x = TILE_SIZE.x * 3 / 4
    offset_x = TILE_SIZE.x / 4
    offset_y = TILE_SIZE.y / 2

    x = entity.position.x
    y = entity.position.y
    if x % 2 == 0:
        screen.blit(WALL, (hexagon_tile_size_x * x - offset_x, TILE_SIZE.y * y - offset_y))
    else:
        screen.blit(WALL, (hexagon_tile_size_x * x - offset_x, TILE_SIZE.y * y + TILE_SIZE.y / 2 - offset_y))






while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("purple")




    draw_map(screen)

    draw_entity(screen, Wall(Position(3, 3)))
    draw_entity(screen, Wall(Position(3, 7)))

    # Render the graphics here.
    # ...

    pygame.display.flip()
    clock.tick(60)