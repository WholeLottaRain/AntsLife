import pygame


class Building(pygame.sprite.Sprite):
    def __init__(self, scale):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.image = pygame.Surface((self.scale, self.scale))
        self.image.fill((139, 0, 255))
        self.rect = self.image.get_rect()


class Anthill(Building):
    def __init__(self, scale):
        super().__init__(scale)
        self.color = (150, 75, 0)
        self.name = "anthill"
        self.size = 5
