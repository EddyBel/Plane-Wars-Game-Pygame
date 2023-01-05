import pygame
import time

# pygame and time
CLOCK = pygame.time.Clock()
TIME_INIT = time.perf_counter()

# Screen and Game
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 500
TITLE = "BULLET"
CAPTION = "Bullet Hell"
NUMBER_ASTEROIDS = 8
MIN_ASTEROIDS_IN_SCREEN = 5
SCORE = 0
DONE_LOOP = False
FPS = True
USE_FACIAL_RECOGNITION = True

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ROSE = (255, 113, 137)
# GREEN = (113, 255, 122)
BLUE = (126, 113, 255)

# CAMERA OPTIONS
FACE_POINT_BOTTOM = 152
FACE_POINT_TOP = 10
FACE_POINT_LEFT = 234
FACE_POINT_RIGHT = 454
FACE_POINT_CENTER = 1

# ANGLES
MIN_ANGLE = 70
MAX_ANGLE = 110

# SETTINGS WINDOW CAMERA
KEY_DELETE = ord("q")
SCREEN = [700, 700]

# Paths and Files
SCORE_FILE = './score.txt'
SETTINGS_FILE = './settings.txt'
PATHS_ASTEROIDS = ["./assets/sprites/asteroid.png",
                   "./assets/sprites/asteroid2.png"]
PATH_BULLET = "./assets/sprites/bullet.png"
PATH_PLAYER = "./assets/sprites/player.png"
PATH_BACKGROUND = "./assets/sprites/background.png"

# Soungs
PATH_SOUNTRACK = './assets/music/Sountrack.mp3'
PATH_SOUNG_BLASTER = './assets/music/Blaster.mp3'
PATH_SOUNG_ASTEROID = './assets/music/Asteroid_Over.wav'
PATH_SOUNG_PLAYER_EXPLOSION = './assets/music/player_explosión.mp3'

# Game keys
KEY_UP = [pygame.K_w, pygame.K_UP]
KEY_DOW = [pygame.K_s, pygame.K_DOWN]
KEY_LEFT = [pygame.K_a, pygame.K_LEFT]
KEY_RIGHT = [pygame.K_d, pygame.K_RIGHT]
KEY_SHOOT = [pygame.K_SPACE, pygame.K_e]
KEY_QUIT = [pygame.K_q]
