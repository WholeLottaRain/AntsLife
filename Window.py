import pygame
from Generation import *

WIDTH = 500
HEIGHT = 500
FPS = 30
SEED = 30
SIZE = 5

# Main window
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AntLife")
g_clock = pygame.time.Clock()
world = map_init(SEED, WIDTH, HEIGHT, SIZE)
map_sprites = pygame.sprite.Group()
map_sprites.add(world.TileArray)
regenerate(world,1)
run = True
while run:
    g_clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if event.button == 1:
                print("Default cell state: " + world.TileArray[int(position[0] / SIZE)][int(position[1] / SIZE)].default)
                print("Real cell state: " + world.TileArray[int(position[0] / SIZE)][int(position[1] / SIZE)].state)
                print("Coords: " + str(int(position[0] / SIZE)), str(int(position[1] / SIZE)))

    map_sprites.update()
    # Rendering
    window.fill(WHITE)
    map_sprites.draw(window)
    pygame.display.flip()

pygame.quit()

