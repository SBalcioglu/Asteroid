from circleshape import *
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.color = "white"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.radius, 2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vel_a = self.velocity.rotate(random.uniform(random_angle, -random_angle))
            vel_b = self.velocity.rotate(random.uniform(-random_angle, random_angle))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_a.velocity = vel_a * 1.2
            asteroid_b.velocity = vel_b * 1.2

class Shot(CircleShape):
    def __init__(self,x,y,SHOT_RADIUS):
        super().__init__(x,y,SHOT_RADIUS)
        self.color = "red"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.radius, SHOT_RADIUS) 
        
    def update(self, dt):
        self.position += (self.velocity * dt)