import pygame
from sys import exit
from random import randint 
pygame.init()

def display_score():
    current_score = pygame.time.get_ticks() - START_TIME
    score = int(current_score / 1000)
    score_surface = font.render(f"SCORE {score}", False, "white")
    score_rect = score_surface.get_rect(center = (283, 50))
    screen.blit(score_surface, score_rect) 
    return score 

def update_obstacles(ol):
    if ol:
        for o in ol:
            screen.blit(centipede_surface, o)
            o.x -= 5
    
        ol = [x for x in ol if x.x > -100]
        return ol
    else:
        return []

# Constants
# Frame Per Second to ensure the game won't run too fast
FPS = 60
DISPLAY_WIDTH, DISPLAY_HEIGHT = 576, 350
START_TIME = 0

# Variables
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

rogue_surface = pygame.image.load("characters/Rogue/Walk/walk1.png")
# Create rectangle and bind it to the rogue_surface 
# to control positioning more easily
rogue_rect = rogue_surface.get_rect(bottomleft = (30, 250))

rogue_stand = pygame.image.load("characters/Rogue/rogue.png")
rogue_stand = pygame.transform.rotozoom(rogue_stand, 0, 2)
rogue_stand_rect = rogue_stand.get_rect(center = (283, 175))

player_gravity = 0

centipede_surface = pygame.image.load("characters/Centipede.png")
centipede_rect = centipede_surface.get_rect(bottomright = (420, 250))

game_title = font.render("Running Rogue", False, "white")
game_title_rect = game_title.get_rect(center = (283, 50))
replay_hint = font.render("Press space to play agian!", False, "white")
replay_hint_rect = replay_hint.get_rect(center = (283, 290))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1600)

obstacle_list = []

game_active = False
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
            if event.type == obstacle_timer:
                obstacle_list.append(centipede_surface.get_rect(bottomright = (randint(600, 1000), 250)))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                obstacle_list = []
                game_active = True
                START_TIME = pygame.time.get_ticks()

        # Draw images
    if game_active:
        screen.blit(sky_surface, (0, 0))
        score = display_score()
        screen.blit(ground_surface, (0, 250))
        # Rogue suraface has the position coordinates of its rectangle
        screen.blit(rogue_surface, rogue_rect)

        # Gravity on player
        player_gravity += 1
        rogue_rect.y += player_gravity

        if rogue_rect.bottom > 250: rogue_rect.bottom = 250

        obstacle_list = update_obstacles(obstacle_list)

        for o in obstacle_list:
            if rogue_rect.colliderect(o):
                game_active = False 

        # pygame.draw.rect(screen, "red", rogue_rect)
        # pygame.draw.rect(screen, "blue", centipede_rect) 
    else:
        screen.fill((25, 25, 25))
        screen.blit(rogue_stand, rogue_stand_rect)
        screen.blit(game_title, game_title_rect)
        if START_TIME == 0:
            screen.blit(replay_hint, replay_hint_rect)
        else:
            final_score = font.render(f"Score - {score}", False, "white")
            final_score_rect = final_score.get_rect(center = (283, 290))
            screen.blit(final_score, final_score_rect)

    # Update the window
    pygame.display.update()
    clock.tick(FPS)