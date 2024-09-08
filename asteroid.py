from circleshape import CircleShape
import pygame
from constants import *
from main import *
import random




class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen , "white", self.position, self.radius, 2)
    def update(self,dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        new_vector1 = self.velocity.rotate(random_angle)
        new_vector2 = self.velocity.rotate(-random_angle)
        ast1_angle = random_angle
        ast2_angle = random_angle * -1
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x,self.position.y,new_rad)
        asteroid2 = Asteroid(self.position.x,self.position.y,new_rad)
        asteroid1.velocity = new_vector1 * 1.2
        asteroid2.velocity = new_vector2 * 1.2
        
