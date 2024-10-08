import sys
import pygame

from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    # Create sprite object groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Add objects to sprite groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        # Check for game window close event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Set and update screen background fill colour to black
        # Draw player every frame
        pygame.Surface.fill(screen, ("black"))

        # Update group objects
        for obj in updatable:
            obj.update(dt)

        # End game if an asteroid collides with the player
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
        
        
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
                

        # Draw group objects
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()