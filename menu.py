import pygame
import sys

def show_game_over_menu(screen, WIDTH, HEIGHT, BLACK, WHITE):
    """Display the game over menu with buttons."""
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, WHITE)
    screen.fill(BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 150))

    # Button properties
    button_width, button_height = 200, 50
    restart_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - 50, button_width, button_height)
    quit_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 50, button_width, button_height)

    # Draw buttons
    pygame.draw.rect(screen, WHITE, restart_button)
    pygame.draw.rect(screen, WHITE, quit_button)

    # Button text
    font = pygame.font.Font(None, 36)
    restart_text = font.render("Restart", True, BLACK)
    quit_text = font.render("Quit", True, BLACK)
    screen.blit(restart_text, (restart_button.centerx - restart_text.get_width() // 2, restart_button.centery - restart_text.get_height() // 2))
    screen.blit(quit_text, (quit_button.centerx - quit_text.get_width() // 2, quit_button.centery - quit_text.get_height() // 2))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):  # Restart button clicked
                    return True
                if quit_button.collidepoint(event.pos):  # Quit button clicked
                    pygame.quit()
                    sys.exit()