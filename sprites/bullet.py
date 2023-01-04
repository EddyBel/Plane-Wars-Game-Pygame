from settings import PATH_BULLET
import pygame


class Bullet (pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.image = pygame.image.load(PATH_BULLET)
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.speed_y = -10

    def update(self) -> None:
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()
