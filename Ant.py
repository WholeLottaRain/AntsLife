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

    def update(self):
        pass

    def watch(self):
        side_ax = int(self.rect.x / self.scale - self.vision)
        side_bx = int(self.rect.x / self.scale + self.vision)
        side_ay = int(self.rect.y / self.scale - self.vision)
        side_by = int(self.rect.y / self.scale + self.vision)

        for x in range(side_ax, side_bx):
            for y in range(side_ay, side_by):
                pass
