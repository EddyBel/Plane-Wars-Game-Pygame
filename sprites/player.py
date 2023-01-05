from sprites.bullet import Bullet
from settings import PATH_PLAYER, SCREEN_WIDTH, SCREEN_HEIGHT, USE_FACIAL_RECOGNITION, KEY_DOW, KEY_LEFT, KEY_RIGHT, KEY_UP
from camera.utils import scale_of_range
from utils.validations import validate_key
import pygame
import groups
import soungs


class Player (pygame.sprite.Sprite):
    """A player sprite that can move around and shoot bullets.

    The player's initial position is in the center of the screen. The player
    has a certain amount of live points, which can be reduced when the player
    is hit by an asteroid.
    """

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
        self.move_head = 0
        self.use_facial_recognition = USE_FACIAL_RECOGNITION

    def update(self):
        """Updates the position and state of the player.

        The player's speed is controlled by the arrow keys or WASD keys. The
        player cannot move off the edges of the screen.
        """

        self.speed_X = 0
        self.speed_Y = 0

        if not self.use_facial_recognition:

            key_up = validate_key(KEY_UP)
            key_down = validate_key(KEY_DOW)
            key_left = validate_key(KEY_LEFT)
            key_right = validate_key(KEY_RIGHT)

            if key_left:
                self.speed_X = -5
                if self.rect.left + self.speed_X < 0:
                    self.speed_X = 0
            elif key_right:
                self.speed_X = 5
                if self.rect.right + self.speed_X > self.width:
                    self.speed_X = 0
            if key_up:
                self.speed_Y = -5
                if self.rect.top + self.speed_Y < 0:
                    self.speed_Y = 0
            elif key_down:
                self.speed_Y = 5
                if self.rect.bottom + self.speed_Y > self.height:
                    self.speed_Y = 0

        else:
            if self.move_head < 0:
                speed = scale_of_range(-1, 0, self.move_head, 15, 5)
                self.speed_X = -speed
                if self.rect.left + self.speed_X < 0:
                    self.speed_X = 0
            elif self.move_head > 0:
                speed = scale_of_range(1, 0, self.move_head, 15, 5)
                self.speed_X = speed
                if self.rect.right + self.speed_X > self.width:
                    self.speed_X = 0

        self.rect.x += self.speed_X
        self.rect.y += self.speed_Y

    def shoot(self):
        """Shoots a bullet from the player's position.

        A bullet sprite is created and added to the ALL_SPRITES and BULLET_GROUP
        sprite groups, and the blaster sound effect is played.
        """

        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.all_sprites.add(bullet)
        self.bullet_list.add(bullet)
        self.blaster_soung.play()
