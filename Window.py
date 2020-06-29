import pygame
from Generation import *
from EntityPlacer import *
from Ant import Ant

WIDTH = 500
HEIGHT = 500
FPS = 30
SEED = 30
SCALE = 5

# Main window
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AntLife")
g_clock = pygame.time.Clock()
world = map_init(SEED, WIDTH, HEIGHT, SCALE)
regenerate(world)
create_anthill(world)
ant = Ant(SCALE)
map_sprites = pygame.sprite.Group()
ant_sprites = pygame.sprite.Group()
map_sprites.add(world.TileArray)
ant_sprites.add(ant)
run = True
while run:
    g_clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if event.button == 1:
                print("Id: " + str(world.TileArray[int(position[0] / SCALE)][int(position[1] / SCALE)].id))
                print("Cell: " + world.TileArray[int(position[0] / SCALE)][int(position[1] / SCALE)].name)
                print("Coords: " + str(int(position[0] / SCALE)), str(int(position[1] / SCALE)))
    ant_sprites.update(world)
    map_sprites.update()
    # Rendering
    window.fill(WHITE)
    map_sprites.draw(window)
    ant_sprites.draw(window)
    pygame.display.flip()

pygame.quit()

