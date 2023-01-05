from settings import PATH_SOUNTRACK, PATH_SOUNG_BLASTER, PATH_SOUNG_ASTEROID, PATH_SOUNG_PLAYER_EXPLOSION
import pygame

pygame.mixer.init()

# Sountrack
SOUNTRACK = pygame.mixer.music.load(PATH_SOUNTRACK)
pygame.mixer.music.set_volume(0.1)

# Effects
BLASTER_EFFECT = pygame.mixer.Sound(PATH_SOUNG_BLASTER)
ASTEROID_EFFECT = pygame.mixer.Sound(PATH_SOUNG_ASTEROID)
PLAYER_EXPLOSION_EFFECT = pygame.mixer.Sound(PATH_SOUNG_PLAYER_EXPLOSION)

# Volumes
BLASTER_EFFECT.set_volume(0.2)
ASTEROID_EFFECT.set_volume(0.2)
PLAYER_EXPLOSION_EFFECT.set_volume(0.2)
