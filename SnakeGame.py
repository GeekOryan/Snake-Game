import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Oryan's Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 30)

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

WIDTH =  600
HEIGHT = 400
block_size = 20
snake = [(100, 100)]
direction = (block_size, 0)
score = 0


def spawn_food():
    x = random.randrange(0, 600, block_size)
    y = random.randrange(0, 400, block_size)
    return (x, y)

food = spawn_food()
game_over = False

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
                
    if not game_over:
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])
        
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            game_over = True
        elif new_head in snake:
            game_over = True
        else:
            snake.insert(0, new_head)
            if new_head == food:
                food = spawn_food()
                score += 1
            else:
                snake.pop()
            
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], block_size, block_size))
    pygame.draw.rect(screen, RED, (food[0], food[1], block_size, block_size))
    
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    if game_over:
        game_over_text = font.render("GAME OVER - Close window to exit", True, WHITE)
        screen.blit(game_over_text, (60, 180))
        
    pygame.display.update()
    clock.tick(10)
    
pygame.quit()