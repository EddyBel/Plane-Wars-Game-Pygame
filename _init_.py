from camera.camera import camera, cv2, viewCamera
from sprites.player import Player
from sprites.collections import Collections
from utils.render import renderAsteroids, renderBullets
from utils.draw import draw_text, draw_live_bar
from utils.file import saveScore, saveSettings, loadScore
from utils.validations import validate_key
from utils.time import measure_time
from groups import ALL_SPRITES, BULLET_GROUP
from screen import Screen
from soungs import PLAYER_EXPLOSION_EFFECT
from settings import SCREEN_WIDTH, CLOCK, SCORE, DONE_LOOP, FPS, PATH_BACKGROUND, USE_FACIAL_RECOGNITION, KEY_QUIT, KEY_SHOOT, TITLE, SCREEN_HEIGHT
import pygame
import sys
import asyncio
import groups

pygame.init()

# Window
window = Screen()
screen = window.createWindow()
background = pygame.image.load(PATH_BACKGROUND).convert()

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


def draw_menu_over():
    screen.blit(screen, [0, 0])
    draw_text(screen, TITLE, 30, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(screen, "Thank you for playing, do you want to play again ?",
              25, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text(screen, "Press the m key to restart", 15,
              SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        CLOCK.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    waiting = False


async def mainLoop(done: bool, score: int, fps: bool = True):
    """Main function that will run the entire game.

    Args:
        done (bool): Indicates if the game loop will be running.
        score (int): Number of player points.
        fps (bool): Variable indicating whether to display fps.
    """

    pygame.mixer.music.play(loops=-1)
    gameOver = False
    while not done:
        CLOCK.tick(60)  # Clock
        if gameOver:
            draw_menu_over()
            gameOver = False
            player.live = 100

        # ------------------------- Camera functions
        if USE_FACIAL_RECOGNITION:
            response = await viewCamera(True, True)
            player.move_head = response["value"]
            if response['is_loop']:
                break

        # --------------------------- Game Functions

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            elif e.type == pygame.KEYDOWN:
                key_shoot = validate_key(KEY_SHOOT)
                if key_shoot:
                    player.shoot()

        # Exit the game
        isQuit = validate_key(KEY_QUIT)
        if isQuit:
            break

        # ---------------------------- Game Colitions
        hit_asteroid = collections.CollisionAsteridePlayer()
        if hit_asteroid:
            PLAYER_EXPLOSION_EFFECT.play()
            gameOver = True
            # done = True

        hit_bullet = collections.CollisionAsteroidBullet()
        if hit_bullet:
            score += 1

        # ---------------------------- Render new sprites
        await renderAsteroids()

        # ---------------------------- Sprite functions
        ALL_SPRITES.update()
        screen.blit(background, [0, 0])
        ALL_SPRITES.draw(screen)

        # ------------------------------- Render texts
        text_score = "Score: {}".format(str(score))
        text_fps = "FPS: {}".format(str(int(CLOCK.get_fps())))
        text_time = "TIME: {}".format(str(measure_time()))

        draw_text(screen, text_score, 25, SCREEN_WIDTH // 2, 10)
        draw_live_bar(screen, 5, 5, player.live)
        draw_text(screen, text_time, 25, SCREEN_WIDTH // 2, 40)

        if fps:
            draw_text(screen, text_fps, 25, SCREEN_WIDTH - 54, 10)

        # ----------------------------------- Save data
        saveScore(score)
        pygame.display.flip()


if __name__ == "__main__":
    # -------------------- Starts the game loop
    asyncio.run(mainLoop(DONE_LOOP, SCORE, FPS))

    # -------------------- Ends all functions
    pygame.quit()
    camera.release()
    cv2.destroyAllWindows()
