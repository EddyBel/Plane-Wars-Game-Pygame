from groups import ASTEROIDS_GROUP, BULLET_GROUP
from soungs import ASTEROID_EFFECT
from settings import SCORE, DONE_LOOP
import pygame


class Collections:
    """A class that manages collisions between different sprites.

    The player and asteroid sprites are checked for collisions, and if a
    collision is detected, the appropriate action is taken (e.g. reducing
    the player's live points or increasing the score).
    """

    def __init__(self, player):
        self.player = player
        self.done_loop = DONE_LOOP
        self.score = SCORE

    def CollisionAsteridePlayer(self) -> bool or None:
        """Checks for a collision between the player and an asteroid.

        If a collision is detected, the player's live points are reduced. If
        the player's live points reach 0, the game is over.
        """
        hit = pygame.sprite.spritecollide(self.player, ASTEROIDS_GROUP, True)
        if hit:
            self.player.live -= 25
            if self.player.live <= 0:
                print("GAME OVER")
                return True

    def CollisionAsteroidBullet(self) -> bool or None:
        """Checks for a collision between an asteroid and a bullet.

        If a collision is detected, the asteroid is removed and the score is
        increased. The asteroid sound effect is played.
        """
        hit = pygame.sprite.groupcollide(
            ASTEROIDS_GROUP, BULLET_GROUP, True, True)
        for h in hit:
            self.score += 1
            ASTEROID_EFFECT.play()
            return True
