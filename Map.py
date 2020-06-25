import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.default = "grass"
        self.state = self.default


class Map(object):
    def __init__(self, seed, width, height, size):
        self.width = width
        self.height = height
        self.size = size
        self.seed = seed
        self.TileArray = []
