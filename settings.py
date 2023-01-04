import pygame

# pygame
CLOCK = pygame.time.Clock()

# Paths and Files
SCORE_FILE = './score.txt'
SETTINGS_FILE = './settings.txt'
PATHS_ASTEROIDS = ["./assets/asteroid.png", "./assets/asteroid2.png"]
PATH_BULLET = "./assets/bullet.png"
PATH_PLAYER = "./assets/player.png"

# Screen and Game
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 500
CAPTION = "Bullet Hell"
NUMBER_ASTEROIDS = 8
MIN_ASTEROIDS_IN_SCREEN = 5
SCORE = 0
DONE_LOOP = False
FPS = True

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Soungs
PATH_SOUNTRACK = './assets/music/Sountrack-2.mp3'
PATH_SOUNG_BLASTER = './assets/music/Blaster.mp3'
PATH_SOUNG_ASTEROID = './assets/music/Asteroid_Over.wav'
