import pygame

pygame.init()
pygame.font.init()
pygame.display.set_caption("Keys")
screen_height = 800
screen_width = 600
screen = pygame.display.set_mode((screen_height, screen_width))

white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.SysFont("Arial", 60)


running = True

while running:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            x = font.render(str(key), True, white)
            y = x.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(x, y)
            pygame.display.update()
            if event.key == pygame.K_q:
                running = False
