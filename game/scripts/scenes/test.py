import pygame

pygame.init()

running = True

surface = pygame.display.set_mode((600, 600))

pygame.time.Clock().tick(60)

pygame.draw.rect(surface, (199, 31, 214), ((100, 100), (400, 400)))




while running:
    pygame.draw.rect(surface, (255, 255, 255), (200, 200, 200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()