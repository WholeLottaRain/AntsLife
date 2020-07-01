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
        self.color = (178, 236, 93)
        self.image.fill(self.color)
        self.name = "grass"
        self.id = 1


class Water(pygame.sprite.Sprite):
    def __init__(self, scale):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.image = pygame.Surface((self.scale, self.scale))
        self.rect = self.image.get_rect()
        self.color = (60, 102, 222)
        self.image.fill(self.color)
        self.name = "water"
        self.id = 2


class Berry(pygame.sprite.Sprite):
    def __init__(self, scale):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.image = pygame.Surface((self.scale, self.scale))
        self.rect = self.image.get_rect()
        self.color = (255, 30, 66)
        self.image.fill(self.color)
        self.name = "berry"
        self.id = 3
        self.eaten = False
        self.booked = False

    def touched(self):
        self.image.fill((0, 255, 0))
        self.eaten = True
