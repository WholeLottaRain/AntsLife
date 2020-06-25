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


