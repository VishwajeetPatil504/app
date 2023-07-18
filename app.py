import pygame
import random

# Initialize the game
pygame.init()

# Set up the screen
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the snake and food
snake_pos = [[100, 50]]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
food_spawn = True

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game loop
game_over = False
direction = "RIGHT"
change_to = direction
score = 0

# Function to display the snake
def draw_snake():
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

# Function to display the food
def draw_food():
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

# Game over function
def show_game_over():
    font = pygame.font.SysFont(None, 40)
    text = font.render("Game Over! Your score: " + str(score), True, BLACK)
    screen.blit(text, (width // 6, height // 3))

# Game over check
def check_game_over():
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= width or snake_pos[0][1] < 0 or snake_pos[0][1] >= height:
        return True
    if snake_pos[0] in snake_body[1:]:
        return True
    return False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"

    # Update snake direction
    direction = change_to

    # Move the snake
    if direction == "RIGHT":
        snake_pos[0][0] += 10
    if direction == "LEFT":
        snake_pos[0][0] -= 10
    if direction == "UP":
        snake_pos[0][1] -= 10
    if direction == "DOWN":
        snake_pos[0][1] += 10

    # Snake body movement
    snake_body.insert(0, list(snake_pos[0]))
    if snake_pos[0] == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn new food
    if not food_spawn:
        food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
        food_spawn = True

    # Refresh the screen
    screen.fill(BLACK)
    draw_snake()
    draw_food()
    pygame.display.update()

    # Check game over
    if check_game_over():
        screen.fill(BLACK)
        show_game_over()
        pygame.display.update()
        pygame.time.wait(2000)
        game_over = True

    # Set the game speed
    clock.tick(15)

# Quit the game
pygame.quit()
