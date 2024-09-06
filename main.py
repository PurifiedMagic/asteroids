# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player_pos_x = SCREEN_WIDTH / 2
    player_pos_y = SCREEN_HEIGHT / 2
    
    player = Player(player_pos_x, player_pos_y)

    while True:
        # Check for game window close event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Set and update screen background fill colour to black
        # Draw player every frame
        pygame.Surface.fill(screen, ("black"))

        player.draw(screen)

        pygame.display.flip()


        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()