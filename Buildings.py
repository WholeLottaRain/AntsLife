import pygame


class Anthill(pygame.sprite.Sprite):
    def __init__(self, scale):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.image = pygame.Surface((self.scale, self.scale))
        self.rect = self.image.get_rect()
        self.color = (150, 75, 0)
        self.image.fill(self.color)
        self.name = "anthill"
        self.id = 20
        self.size = 5

