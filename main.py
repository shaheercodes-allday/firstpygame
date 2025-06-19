import pygame
# exit() function will help in exiting the while loop safely
# break is unsafe 
from sys import exit

pygame.init()

def display_score():
    current_score = pygame.time.get_ticks() - START_TIME
    score_surface = font.render(f"{current_score}", False, "white")
    score_rect = score_surface.get_rect(center = (283, 50))
    screen.blit(score_surface, score_rect)

# Frame Per Second to ensure the game won't run too fast
FPS = 60
DISPLAY_WIDTH, DISPLAY_HEIGHT = 576, 350
START_TIME = 0

# Create a display surface and set the size of the window 
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
# Clock to control time (FPS)
clock = pygame.time.Clock()
# Setting up the font
font = pygame.font.Font("fonts/joystix.otf", 20)

# Set the window caption
pygame.display.set_caption("Running Rogue")

# Create required surfaces
sky_surface = pygame.image.load("graphics/purple-sky.png")
ground_surface = pygame.image.load("graphics/ground.png")

rogue_surface = pygame.image.load("characters/Rogue/rogue.png")
# Create rectangle and bind it to the rogue_surface 
# to control positioning more easily
rogue_rect = rogue_surface.get_rect(bottomleft = (30, 250))

player_gravity = 0

centipede_surface = pygame.image.load("characters/Centipede.png")
centipede_rect = centipede_surface.get_rect(bottomright = (420, 250))

game_active = True
centipede_speed = 4

while True:
    # The event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and rogue_rect.bottom >= 250:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                centipede_rect.right = 420
                game_active = True
                START_TIME = pygame.time.get_ticks()

        # Draw images
    if game_active:
        screen.blit(sky_surface, (0, 0))
        display_score()
        screen.blit(ground_surface, (0, 250))
        # Rogue suraface has the position coordinates of its rectangle
        screen.blit(rogue_surface, rogue_rect)

        centipede_rect.x -= centipede_speed 
        if centipede_rect.right <= 0: centipede_rect.left = 576
        screen.blit(centipede_surface, centipede_rect)

        # Gravity on player
        player_gravity += 1
        rogue_rect.y += player_gravity

        if rogue_rect.bottom > 250: rogue_rect.bottom = 250

        # pygame.draw.rect(screen, "red", rogue_rect)
        # pygame.draw.rect(screen, "blue", centipede_rect) 

        if rogue_rect.colliderect(centipede_rect):
            game_active = False
    else:
        screen.fill("blue")

    # Update the window
    pygame.display.update()
    clock.tick(FPS)