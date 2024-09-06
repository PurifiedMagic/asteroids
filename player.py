import pygame

from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Draw the player object
    def draw(self, screen):
        self.player = pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)

        # Move forwards when "W" key is pressed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(dt * -1)

        # Move backwards when "S" key is pressed
        if keys[pygame.K_a]  or keys[pygame.K_LEFT]:
            self.rotate(dt * -1)

        # Rotate right when "D" key is pressed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)