import pygame
from Generation import *

WIDTH = 500
HEIGHT = 500
FPS = 30
SEED = 30
MAIN_SIZE = 5

# Main window
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AntLife")
g_clock = pygame.time.Clock()
world = map_init(SEED, WIDTH, HEIGHT, MAIN_SIZE)
map_sprites = pygame.sprite.Group()
map_sprites.add(world.TileArray)


run = True
while run:
    g_clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    map_sprites.update()
    # Rendering
    window.fill(WHITE)
    map_sprites.draw(window)
    pygame.display.flip()

pygame.quit()

