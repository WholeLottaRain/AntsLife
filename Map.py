import pygame


class Map(object):
    def __init__(self, seed, width, height, scale):
        self.width = width
        self.height = height
        self.scale = scale
        self.seed = seed
        self.TileArray = []


class Grass(pygame.sprite.Sprite):
    def __init__(self, scale):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.image = pygame.Surface((self.scale, self.scale))
        self.rect = self.image.get_rect()
        self.color = (0, 255, 0)
        self.image.fill(self.color)
        self.name = "grass"
        self.id = 1


class Water(pygame.sprite.Sprite):
    def __init__(self, scale):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.image = pygame.Surface((self.scale, self.scale))
        self.rect = self.image.get_rect()
        self.color = (0, 0, 255)
        self.image.fill(self.color)
        self.name = "water"
        self.id = 2
