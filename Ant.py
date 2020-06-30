import pygame


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

    def update(self, ex_map):
        if self.target is False:
            self.watch(ex_map)
        else:
            print("Found berry at " + str(self.target_position))

    def watch(self, ex_map):
        side_ax = int(self.rect.x / self.scale - self.vision)
        side_bx = int(self.rect.x / self.scale + self.vision)
        side_ay = int(self.rect.y / self.scale - self.vision)
        side_by = int(self.rect.y / self.scale + self.vision)
        if side_ax < 0:
            side_ax = 0
        if side_bx >= ex_map.width / ex_map.scale:
            side_bx = int(ex_map.width / ex_map.scale) - 1
        if side_ay < 0:
            side_ay = 0
        if side_by >= ex_map.height / ex_map.scale:
            side_by = int(ex_map.height / ex_map.scale) - 1
        self.vision_matrix = (side_ax, side_bx, side_ay, side_by)

        for x in range(side_ax, side_bx):
            for y in range(side_ay, side_by):
                if ex_map.TileArray[x][y].id == 3:
                    self.target = True
                    self.target_position = x, y

    def move_to_cell(self, x, y):
        self.rect.center = (x * self.scale, y * self.scale)

    def get_cell(self):
        return int(self.rect.x / self.scale), int(self.rect.y / self.scale)

