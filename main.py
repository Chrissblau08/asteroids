import pygame
from constants import *
from player import * 
from asteroid import * 
from asteroidfield import * 
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = updatable, drawable
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # RGB für Schwarz

        hits = []
        for asteroid in asteroids.sprites():
            for shot in shots.sprites():
                if asteroid.collides_with(shot):
                    hits.append((asteroid, shot))

        # Danach alle zerstören
        for asteroid, shot in hits:
            print("Asteroid hit!")
            asteroid.split()
            shot.kill()

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return

        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()