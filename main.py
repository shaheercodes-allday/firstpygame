import pygame
# exit() function will help in exiting the while loop safely
# break is unsafe 
from sys import exit

pygame.init()

# Frame Per Second to ensure the game won't run too fast
FPS = 60
DISPLAY_WIDTH, DISPLAY_HEIGHT = 800, 500

# Create a display surface and set the size of the window 
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT)) 
# Clock to control time (FPS)
clock = pygame.time.Clock()

# Set the window caption
pygame.display.set_caption("First Game")

while True:
    # The event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw images

    # Update the window
    pygame.display.update()
    clock.tick(FPS)