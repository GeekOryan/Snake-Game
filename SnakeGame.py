import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Oryan's Snake Game")
clock = pygame.time.Clock()

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

block_size = 20
snake = [(100, 100)]
direction = (block_size, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = (block_size, 0)
            elif event.key == pygame.K_LEFT:
                direction = (-block_size, 0)
            elif event.key == pygame.K_UP:
                direction = (0, -block_size)
            elif event.key == pygame.K_DOWN:
                direction = (0, block_size)
    
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    snake.insert(0, new_head)
    snake.pop()
    
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], block_size, block_size))
    pygame.display.update()
    clock.tick(10)

pygame.quit()