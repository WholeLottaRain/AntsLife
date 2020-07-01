import pygame
import math
from PathFinder import find_path


class Ant(pygame.sprite.Sprite):
    def __init__(self, scale):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.image = pygame.Surface((self.scale, self.scale))
        self.rect = self.image.get_rect()
        self.color = (0, 0, 0)
        self.image.fill(self.color)
        self.rect.center = 250, 250
        self.name = "ant"
        self.id = 30
        self.vision = 20
        self.vision_matrix = (0, 0, 0, 0)
        self.target = False
        self.target_position = (0, 0)
        self.path = []
        self.path_index = 0

    def update(self, ex_map):
        if self.target is False:
            self.watch(ex_map)
        elif self.target is True:
            self.move_to_target(ex_map)

    def watch(self, ex_map):
        side_ax = int(self.rect.center[0] / self.scale - self.vision)
        side_bx = int(self.rect.center[0] / self.scale + self.vision)
        side_ay = int(self.rect.center[1] / self.scale - self.vision)
        side_by = int(self.rect.center[1] / self.scale + self.vision)
        if side_ax < 0:
            side_ax = 0
        if side_bx >= ex_map.width / ex_map.scale:
            side_bx = int(ex_map.width / ex_map.scale) - 1
        if side_ay < 0:
            side_ay = 0
        if side_by >= ex_map.height / ex_map.scale:
            side_by = int(ex_map.height / ex_map.scale) - 1
        self.vision_matrix = (side_ax, side_ay, side_bx, side_by)
        path_length = 999
        for x in range(side_ax, side_bx + 1):
            for y in range(side_ay, side_by + 1):
                if ex_map.TileArray[x][y].id == 3 and ex_map.TileArray[x][y].eaten is False \
                        and ex_map.TileArray[x][y].booked is False:
                    hypotenuse = math.sqrt((self.get_cell()[0]-x)*(self.get_cell()[0]-x) + (self.get_cell()[1]-y)*(self.get_cell()[1]-y))
                    if hypotenuse < path_length:
                        path_length = hypotenuse
                        self.target = True
                        self.target_position = x, y

        if self.target is True:
            self.path = find_path(ex_map, self.vision_matrix, self.get_cell(), self.target_position)
            self.target_position = self.path[len(self.path) - 1][0], self.path[len(self.path) - 1][1]
            ex_map.TileArray[self.target_position[0]][self.target_position[1]].booked = True
            print("Going to: " + str(self.path[len(self.path) - 1][0]) + " " + str(
                self.path[len(self.path) - 1][1]))

    def move_to_target(self, ex_map):
        if self.path_index < len(self.path):
            self.move_to_cell(self.path[self.path_index][0], self.path[self.path_index][1])
            self.path_index += 1
        if self.get_cell() == self.target_position:
            self.path_index = 0
            self.target = False
            self.path = []
            ex_map.TileArray[self.target_position[0]][self.target_position[1]].touched()

    def move_to_cell(self, x, y):
        self.rect.center = (x * self.scale, y * self.scale)

    def get_cell(self):
        return int(self.rect.center[0] / self.scale), int(self.rect.center[1] / self.scale)
