from sprites.bullet import Bullet
from settings import PATH_PLAYER, SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
import groups
import soungs


class Player (pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

        self.image = pygame.image.load(PATH_PLAYER).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.centerx = self.width // 2
        self.rect.centery = (self.height + 300) // 2
        self.speed_X = 0
        self.speed_Y = 0
        self.live = 100

        self.all_sprites = groups.ALL_SPRITES
        self.bullet_list = groups.BULLET_GROUP

        self.blaster_soung = soungs.BLASTER_EFFECT

    def update(self):
        self.speed_X = 0
        self.speed_Y = 0
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_a] or keystate[pygame.K_LEFT]:
            self.speed_X = -5
            if self.rect.left + self.speed_X < 0:
                self.speed_X = 0
        elif keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:
            self.speed_X = 5
            if self.rect.right + self.speed_X > self.width:
                self.speed_X = 0
        if keystate[pygame.K_w] or keystate[pygame.K_UP]:
            self.speed_Y = -5
            if self.rect.top + self.speed_Y < 0:
                self.speed_Y = 0
        elif keystate[pygame.K_s] or keystate[pygame.K_DOWN]:
            self.speed_Y = 5
            if self.rect.bottom + self.speed_Y > self.height:
                self.speed_Y = 0

        self.rect.x += self.speed_X
        self.rect.y += self.speed_Y

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.all_sprites.add(bullet)
        self.bullet_list.add(bullet)
        self.blaster_soung.play()
