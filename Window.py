import pygame

WIDTH = 500
HEIGHT = 500
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Main window
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AntLife")
g_clock = pygame.time.Clock()

run = True
while run:
    g_clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Rendering
    window.fill(WHITE)
    pygame.display.flip()

pygame.quit()
