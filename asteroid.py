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