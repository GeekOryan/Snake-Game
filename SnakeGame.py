import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Oryan's Snake Game")
clock = pygame.time.Clock()

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

x = 100
y = 100
speed = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += speed
            elif event.key == pygame.K_LEFT:
                x -= speed
            elif event.key == pygame.K_UP:
                y -= speed
            elif event.key == pygame.K_DOWN:
                y += speed
    
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, (x, y, 20, 20))
    pygame.display.update()
    clock.tick(10)

pygame.quit()