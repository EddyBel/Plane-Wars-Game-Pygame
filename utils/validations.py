import pygame


def validate_key(KEY_USE: list) -> bool:
    keystate = pygame.key.get_pressed()
    for KEY in KEY_USE:
        if keystate[KEY]:
            return True

    return False
