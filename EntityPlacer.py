import random
from Buildings import Anthill


def init_entity(building, ex_map):
    random.seed(ex_map.seed)
    rand_x = int(random.randint(0, ex_map.width/ex_map.scale))
    if rand_x > int(ex_map.width/ex_map.scale) - building.size:
        rand_x -= building.size
    rand_y = int(random.randint(0, ex_map.height/ex_map.scale))
    if rand_y > int(ex_map.height/ex_map.scale) - building.size:
        rand_y -= building.size
    for x in range(building.size):
        for y in range(building.size):
            ex_map.TileArray[rand_x + x][rand_y + y].image.fill(building.color)
            ex_map.TileArray[rand_x + x][rand_y + y].state = building.name


def create_anthill(ex_map):
    anthill = Anthill(ex_map.scale)
    init_entity(anthill, ex_map)
