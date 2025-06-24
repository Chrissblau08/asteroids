import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        random_angle = random.uniform(20, 50)
        dir1 = self.velocity.rotate(random_angle) * 1.2
        dir2 = self.velocity.rotate(-random_angle) * 1.2

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = dir1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = dir2
    
