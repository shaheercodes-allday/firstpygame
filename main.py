import pygame
# exit() function will help in exiting the while loop safely
# break is unsafe 
from sys import exit

pygame.init()

# Frame Per Second to ensure the game won't run too fast
FPS = 60
DISPLAY_WIDTH, DISPLAY_HEIGHT = 550, 440

# Create a display surface and set the size of the window 
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT)) 
# Clock to control time (FPS)
clock = pygame.time.Clock()
# Setting up the font
font = pygame.font.Font("fonts/joystix.otf", 20)

# Set the window caption
pygame.display.set_caption("First Game")

# Create required surfaces
sky_surface = pygame.image.load("graphics/purple-sky.png")
text_surface = font.render("Hello, Pygame!", False, "white")

while True:
    # The event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw images
    screen.blit(sky_surface, (0, 0))
    screen.blit(text_surface, (170, 50))

    # Update the window
    pygame.display.update()
    clock.tick(FPS)