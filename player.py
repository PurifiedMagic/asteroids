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
        
        # Move forwards when "W" key is pressed
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)

        # Move forwards when "S" key is pressed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(dt * -1)

        # Rotate left when "A" key is pressed
        if keys[pygame.K_a]  or keys[pygame.K_LEFT]:
            self.rotate(dt * -1)

        # Rotate right when "D" key is pressed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        # Shoot shots when "SPACE" key is pressed
        if keys[pygame.K_SPACE]:
            self.shoot(self.position)
    
    def shoot(self, position):
        shot_spawn = pygame.Vector2(position)
        shot = Shot(shot_spawn.x, shot_spawn.y, SHOT_RADIUS)

        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Draw shot bullets
    def draw(self, screen):
        self.shot = pygame.draw.circle(screen, "blue", self.position, 2)

    # Update shot bullets
    def update(self, dt):
        self.position += (self.velocity * dt)