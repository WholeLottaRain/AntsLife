import random
from Buildings import Anthill


def init_building(building, ex_map):
    random.seed(ex_map.seed)
    rand_x = int(random.randint(0, ex_map.width/ex_map.scale))
    if rand_x > int(ex_map.width/ex_map.scale) - building.size:
        rand_x -= building.size
    rand_y = int(random.randint(0, ex_map.height/ex_map.scale))
    if rand_y > int(ex_map.height/ex_map.scale) - building.size:
        rand_y -= building.size
    for x in range(building.size):
        for y in range(building.size):
            ex_map.TileArray[rand_x + x][rand_y + y].kill()
            ex_map.TileArray[rand_x + x][rand_y + y] = building.__class__(ex_map.scale)
            ex_map.TileArray[rand_x + x][rand_y + y].rect.center = (rand_x + x) * ex_map.scale, (rand_y + y) * ex_map.scale


def create_anthill(ex_map):
    anthill = Anthill(ex_map.scale)
    init_building(anthill, ex_map)
