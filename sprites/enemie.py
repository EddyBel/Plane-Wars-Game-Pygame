from settings import SCREEN_HEIGHT, SCREEN_WIDTH, PATHS_ASTEROIDS
import pygame
import random


class Asteroid (pygame.sprite.Sprite):
    """An asteroid sprite that moves downwards on the screen.

    The asteroid is initialized with a random image from the PATHS_ASTEROIDS
    list, a random size, a random angle of rotation, and random x and y
    speeds. The asteroid's initial x position is also randomized.
    """

    def __init__(self):
        super().__init__()
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

        self.path = random.choice(PATHS_ASTEROIDS)
        self.image = pygame.image.load(str(self.path)).convert()
        self.image.set_colorkey((0, 0, 0))
        size = random.randrange(20, 60)
        self.angle = random.randrange(0, 360)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.image = pygame.transform.rotate(self.image, self.angle)

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.width - self.rect.width)
        self.rect.y = random.randrange(-140, -100)
        self.speed_y = random.randrange(8, 10)
        self.speed_x = random.randrange(-2, 3)

    def update(self):
        """Updates the position and state of the asteroid.

        If the asteroid goes off the bottom of the screen, it is removed from
        any sprite groups.
        """
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        limitWidth = self.width + 20

        if self.rect.bottom > self.height or self.rect.left < -limitWidth or self.rect.right > limitWidth:
            self.kill()
