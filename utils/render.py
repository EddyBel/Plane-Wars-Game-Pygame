from sprites.enemie import Asteroid
from groups import ALL_SPRITES, ASTEROIDS_GROUP, BULLET_GROUP
from settings import NUMBER_ASTEROIDS, MIN_ASTEROIDS_IN_SCREEN, KEY_SHOOT
from utils.validations import validate_key
import random
import time


async def renderAsteroids() -> None:
    """Renders asteroids on the screen.

    If there are fewer asteroids than the minimum specified by
    MIN_ASTEROIDS_IN_SCREEN, new asteroids will be created and added
    to the asteroids group until the desired number is reached.
    """
    countAsteroids = len(ASTEROIDS_GROUP.sprites())

    if countAsteroids <= MIN_ASTEROIDS_IN_SCREEN:
        for i in range(NUMBER_ASTEROIDS):
            asteroid = Asteroid()
            ALL_SPRITES.add(asteroid)
            ASTEROIDS_GROUP.add(asteroid)


async def renderBullets(shoot) -> None:
    count_bullets = len(BULLET_GROUP.sprites())
    key_shoot = validate_key(KEY_SHOOT)

    if key_shoot:
        if count_bullets < 5:
            shoot()
            time.sleep(0.5)
