from opensimplex import OpenSimplex
from Map import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def map_init(seed, width, height, scale):
    new_map = Map(seed, width, height, scale)
    for x in range(int(new_map.width / new_map.scale)):
        new_map.TileArray.append([])
        for y in range(int(new_map.height / new_map.scale)):
            new_map.TileArray[x].append(Grass(new_map.scale))
            new_map.TileArray[x][y].rect.center = x * new_map.scale, y * new_map.scale
    return new_map


def regenerate(ex_map):
    simplex = OpenSimplex(ex_map.seed)
    for x in range(int(ex_map.width / ex_map.scale)):
        for y in range(int(ex_map.height / ex_map.scale)):
            if 0.85 > simplex.noise2d(x, y) > 0.7:
                ex_map.TileArray[x][y].kill()
                ex_map.TileArray[x][y] = Water(ex_map.scale)
                ex_map.TileArray[x][y].rect.center = x * ex_map.scale, y * ex_map.scale
            if simplex.noise2d(x, y) > 0.85:
                ex_map.TileArray[x][y].kill()
                ex_map.TileArray[x][y] = Berry(ex_map.scale)
                ex_map.TileArray[x][y].rect.center = x * ex_map.scale, y * ex_map.scale

