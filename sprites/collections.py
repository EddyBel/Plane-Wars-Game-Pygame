from groups import ASTEROIDS_GROUP, BULLET_GROUP
from soungs import ASTEROID_EFFECT
from settings import SCORE, DONE_LOOP
import pygame


class Collections:

    def __init__(self, player):
        self.player = player
        self.done_loop = DONE_LOOP
        self.score = SCORE

    def CollisionAsteridePlayer(self):
        hit = pygame.sprite.spritecollide(self.player, ASTEROIDS_GROUP, True)
        if hit:
            self.player.live -= 25
            if self.player.live <= 0:
                print("GAME OVER")
                return True

    def CollisionAsteroidBullet(self):
        hit = pygame.sprite.groupcollide(
            ASTEROIDS_GROUP, BULLET_GROUP, True, True)
        for h in hit:
            self.score += 1
            ASTEROID_EFFECT.play()
            return True
