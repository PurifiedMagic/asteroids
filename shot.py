import pygame

from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Draw shot bullets
    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, 2)

    # Update shot bullets
    def update(self, dt):
        self.position += (self.velocity * dt)