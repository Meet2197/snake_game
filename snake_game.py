import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Snake and food initialization
snake = [(100, 100), (90, 100), (80, 100)]  # Starting snake position
snake_dir = "RIGHT"  # Initial direction
food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
        random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

# Score
score = 0

# Font for displaying score
font = pygame.font.Font(None, 36)


def draw_snake(snake_body):
    """Draws the snake on the screen."""
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(
            segment[0], segment[1], CELL_SIZE, CELL_SIZE))


def draw_food(food_pos):
    """Draws the food on the screen."""
    pygame.draw.rect(screen, RED, pygame.Rect(
        food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))


def display_score(score):
    """Displays the score on the screen."""
    score_surface = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surface, (10, 10))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Control snake direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != "DOWN":
        snake_dir = "UP"
    if keys[pygame.K_DOWN] and snake_dir != "UP":
        snake_dir = "DOWN"
    if keys[pygame.K_LEFT] and snake_dir != "RIGHT":
        snake_dir = "LEFT"
    if keys[pygame.K_RIGHT] and snake_dir != "LEFT":
        snake_dir = "RIGHT"

    # Move the snake
    head_x, head_y = snake[0]
    if snake_dir == "UP":
        head_y -= CELL_SIZE
    if snake_dir == "DOWN":
        head_y += CELL_SIZE
    if snake_dir == "LEFT":
        head_x -= CELL_SIZE
    if snake_dir == "RIGHT":
        head_x += CELL_SIZE

    # New head position
    new_head = (head_x, head_y)
    snake = [new_head] + snake[:-1]

    # Check for collision with food
    if new_head == food:
        snake.append(snake[-1])  # Grow the snake
        score += 1
        food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

    # Check for collisions with walls
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        print("Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    # Check for collisions with itself
    if new_head in snake[1:]:
        print("Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the snake and food
    draw_snake(snake)
    draw_food(food)

    # Display the score
    display_score(score)

    # Refresh the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(10)
