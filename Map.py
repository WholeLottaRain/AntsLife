import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, scale):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.image = pygame.Surface((self.scale, self.scale))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.default = "grass"
        self.state = self.default


class Map(object):
    def __init__(self, seed, width, height, scale):
        self.width = width
        self.height = height
        self.scale = scale
        self.seed = seed
        self.TileArray = []
