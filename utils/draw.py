from settings import GREEN, WHITE
from pygame import Surface
import pygame


def draw_text(surface: Surface, text: str, size: int, x: int, y: int, color: tuple = WHITE) -> None:
    """Draws text on a surface.

    Args:
        surface: Surface where the text will be drawn.
        text: Text to be drawn.
        size: Size of the text.
        x: X coordinate of the text's top-center point.
        y: Y coordinate of the text's top-center point.
        color: Color of the text. Default value is WHITE.
    """
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def draw_live_bar(surface: Surface, x: int, y: int, valueReference: float) -> None:
    """Draws a life bar on a surface.

    Args:
        surface: Surface where the life bar will be drawn.
        x: X coordinate of the top-left corner of the bar.
        y: Y coordinate of the top-left corner of the bar.
        valueReference: Percentage of remaining life.
    """
    bar_length = 100
    bar_height = 10
    fill = (valueReference / 100) * bar_length
    border = pygame.Rect(x, y, bar_length, bar_height)
    fill = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surface, GREEN, fill)
    pygame.draw.rect(surface, WHITE, border, 2)
