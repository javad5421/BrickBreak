# brick break simple game designed with pygame
import pygame
import random
from PyGame.BrickBreak.menu import show_game_over_menu

#initialize pygame
pygame.init()

# set up the game window
WIDTH, HEIGHT = 860, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# variables
countdown = False
score = 0

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# paddle properties
paddle_width = 100
Paddle_height = 10
paddle_speed = 10 
paddle = pygame.Rect((WIDTH - paddle_width) // 2, HEIGHT - Paddle_height - 10, paddle_width, Paddle_height)

# ball properties
ball_radius = 10
ball_speed = [5, -5]  # [x_speed, y_speed]
ball = pygame.Rect(WIDTH // 2 - ball_radius, HEIGHT // 2 - ball_radius, ball_radius * 2, ball_radius * 2)

# brick properties
brick_width = 75
brick_height = 30
brick_color = [RED, YELLOW, GREEN, BLUE]
# create a grid of bricks
bricks = []
rows = 5
cols = 10
for row in range(rows):
    for col in range(cols):
        brick = pygame.Rect(col * (brick_width + 5) + 35, row * (brick_height + 10) + 35, brick_width, brick_height)
        bricks.append((brick , random.choice(brick_color)))

#display the score
def show_score(screen, score, WHITE):
    """Display the current score on the screen."""
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))  # Display the score at the top-left corner

#display the countdown
def show_countdown(screen, WIDTH, HEIGHT, WHITE):
    """Display a transparent countdown from 3 to 1 and then 'Go'."""
    font = pygame.font.Font(None, 74)
    for count in ["3", "2", "1", "Go"]:
        # Render the countdown text
        text = font.render(count, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 + 100))
        pygame.display.flip()
        pygame.time.delay(1000)
        screen.fill((0, 0, 0, 0), text_rect)

# Start the game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # handle paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed

    # move the ball
    ball.left += ball_speed[0]
    ball.top += ball_speed[1]

    # check for collision with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.bottom >= HEIGHT:
        # game over
        countdown = False
        score = 0
        if not show_game_over_menu(screen, WIDTH, HEIGHT, BLACK, WHITE):
            running = False
        else:
            # Reset game state
            ball = pygame.Rect(WIDTH // 2 - ball_radius, HEIGHT // 2 - ball_radius, ball_radius * 2, ball_radius * 2)
            ball_speed = [5, -5]
            paddle = pygame.Rect((WIDTH - paddle_width) // 2, HEIGHT - Paddle_height - 10, paddle_width, Paddle_height)
            bricks = []
            for row in range(rows):
                for col in range(cols):
                    brick = pygame.Rect(col * (brick_width + 5) + 35, row * (brick_height + 10) + 35, brick_width, brick_height)
                    bricks.append((brick, random.choice(brick_color)))

    # check for collision with paddle
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # check for collision with bricks
    for brick, color in bricks[:]:
        if ball.colliderect(brick):
            ball_speed[1] = -ball_speed[1]
            bricks.remove((brick, color))
            score += 10
            break

    # fill the screen with white color
    screen.fill(BLACK)

    # draw the paddle
    pygame.draw.rect(screen, WHITE, paddle)

    # draw the ball
    pygame.draw.ellipse(screen, WHITE, ball)

    # draw the bricks
    for brick , color in bricks:
        pygame.draw.rect(screen, color, brick)

    # display the score
    show_score(screen, score, WHITE)

    if not countdown:
        countdown = True
        show_countdown(screen, WIDTH, HEIGHT, WHITE)

    # update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()