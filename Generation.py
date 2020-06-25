import random
from opensimplex import OpenSimplex
from Map import Map
from Map import Tile

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)




def map_init(seed, width, height, size):
    new_map = Map(seed, width, height, size)
    for x in range(int(new_map.width / new_map.size)):
        new_map.TileArray.append([])
        for y in range(int(new_map.height / new_map.size)):
            new_map.TileArray[x].append(Tile(size))
            new_map.TileArray[x][y].rect.center = x * new_map.size, y * new_map.size
    return new_map


def regenerate(ex_map, gen_type):
    if gen_type == 1:
        simplex = OpenSimplex(ex_map.seed)
        for x in range(int(ex_map.width / ex_map.size)):
            for y in range(int(ex_map.height / ex_map.size)):
                if simplex.noise2d(x, y) <= 0.5:
                    ex_map.TileArray[x][y].image.fill(GREEN)
                    ex_map.TileArray[x][y].default = "grass"
                    ex_map.TileArray[x][y].state = "grass"
                if simplex.noise2d(x, y) > 0.5:
                    ex_map.TileArray[x][y].image.fill(BLUE)
                    ex_map.TileArray[x][y].default = "water"
                    ex_map.TileArray[x][y].state = "water"
    if gen_type == 2:
        random.seed(ex_map.seed)
        for x in range(int(ex_map.width / ex_map.size)):
            for y in range(int(ex_map.height / ex_map.size)):
                if random.random() <= 0.5:
                    ex_map.TileArray[x][y].image.fill(GREEN)
                if random.random() > 0.5:
                    ex_map.TileArray[x][y].image.fill(BLUE)
