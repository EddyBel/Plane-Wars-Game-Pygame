from sprites.enemie import Asteroid
from groups import ALL_SPRITES, ASTEROIDS_GROUP
from settings import NUMBER_ASTEROIDS, MIN_ASTEROIDS_IN_SCREEN
import random


async def renderAsteroids():
    countAsteroids = len(ASTEROIDS_GROUP.sprites())

    if countAsteroids <= MIN_ASTEROIDS_IN_SCREEN:
        for i in range(NUMBER_ASTEROIDS):
            asteroid = Asteroid()
            ALL_SPRITES.add(asteroid)
            ASTEROIDS_GROUP.add(asteroid)
