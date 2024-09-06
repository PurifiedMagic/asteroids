import random
import pygame

from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Draw asteroids
    def draw(self, screen):
        self.asteroid = pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)

    # Update asteroids
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_one.velocity = self.velocity.rotate(random_angle) * 1.2
        asteroid_two.velocity = self.velocity.rotate(-random_angle) * 1.2