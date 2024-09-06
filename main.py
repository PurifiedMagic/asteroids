# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    while True:
        # Check for game window close event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Set and update screen background fill colour to black
        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()

        dt = clock.tick(60)/1000
        print(dt)



if __name__ == "__main__":
    main()