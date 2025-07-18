import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    aster_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatables.update(dt)
        for asteroid in asteroids:
            if player.is_colliding_with(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.is_colliding_with(shot):
                    asteroid.split()
                    shot.kill()
                    continue
        for drawable in drawables:
            drawable.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()