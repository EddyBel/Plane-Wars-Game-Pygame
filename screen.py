from pygame import Surface
import pygame
import settings


class Screen:
    """Represents the game screen.

    Attributes:
        width: Width of the screen.
        height: Height of the screen.
        background: Background color of the screen.
        caption: Title of the screen.
    """

    def __init__(self) -> None:
        """Initializes the screen's attributes.

        The values for width, height, background and caption are obtained
        from the settings module.
        """
        self.width = settings.SCREEN_WIDTH
        self.height = settings.SCREEN_HEIGHT
        self.background = 0, 0, 0
        self.caption = settings.CAPTION

    def createWindow(self) -> Surface:
        """Creates the screen window.

        Sets the screen's title with the caption attribute and
        returns the created window with the dimensions specified
        by the width and height attributes.
        """
        pygame.display.set_caption(self.caption)
        return pygame.display.set_mode(size=(self.width, self.height))
