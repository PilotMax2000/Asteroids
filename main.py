# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    player = Player(x, y, 0)
    asteroid_field = AsteroidField()


    while True:
        for e in updatable:
            e.update(dt)
        
        for a in asteroids:
            if player.check_collision(a):
                print("Game over!")
                sys.exit(0)
            for bullet in shots:
                if a.check_collision(bullet):
                    a.split()
                    bullet.kill()
        
        #player.update(dt)
        pygame.Surface.fill(screen, (0,0,0))
        
        for e in drawable:
            e.draw(screen)

        #player.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()