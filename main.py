from sprites.player import Player
from sprites.collections import Collections
from utils.render import renderAsteroids
from utils.draw import draw_text, draw_live_bar
from utils.file import saveScore, saveSettings, loadScore
from groups import ASTEROIDS_GROUP, ALL_SPRITES
from screen import Screen
from settings import SCREEN_WIDTH, CLOCK, SCORE, DONE_LOOP, FPS
import pygame
import sys
import asyncio
import groups

pygame.init()

# Window
window = Screen()
screen = window.createWindow()
background = pygame.image.load("./assets/background.png").convert()

# Player
player = Player()
groups.ALL_SPRITES.add(player)

# Collections
collections = Collections(player)

# Save and load values
try:
    saveSettings()
except:
    print("Error Save")

try:
    loadScoreValue = loadScore()
    print(loadScoreValue)
    SCORE = loadScoreValue
except:
    SCORE = 0


async def mainLoop(done, score, fps):
    while not done:
        CLOCK.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    player.shoot()

        hit_asteroid = collections.CollisionAsteridePlayer()
        if hit_asteroid:
            done = True

        hit_bullet = collections.CollisionAsteroidBullet()
        if hit_bullet:
            score += 1

        await renderAsteroids()

        ALL_SPRITES.update()
        screen.blit(background, [0, 0])
        ALL_SPRITES.draw(screen)

        text_score = "Score: {}".format(str(score))
        text_fps = "FPS: {}".format(str(int(CLOCK.get_fps())))

        draw_text(screen, text_score, 25, SCREEN_WIDTH // 2, 10)
        draw_live_bar(screen, 5, 5, player.live)

        if fps:
            draw_text(screen, text_fps, 25, SCREEN_WIDTH - 54, 10)

        saveScore(score)
        pygame.display.flip()


if __name__ == "__main__":
    pygame.mixer.music.play(loops=-1)
    asyncio.run(mainLoop(DONE_LOOP, SCORE, FPS))
    pygame.quit()
