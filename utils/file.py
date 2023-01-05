from settings import SCORE, SCORE_FILE, SETTINGS_FILE, FPS, NUMBER_ASTEROIDS
import json


def saveScore(score: int) -> None:
    """Saves a score to a file.

    Args:
        score: Score to be saved.
    """
    with open(SCORE_FILE, 'w') as f:
        f.write(str(score))


def loadScore() -> int:
    """Loads a score from a file.

    Returns:
        The score as an integer. If the file does not exist or cannot be
        read, returns 0.
    """
    try:
        with open(SCORE_FILE, 'r') as f:
            score = int(f.read())
        return int(score)
    except:
        return 0


def saveSettings() -> None:
    """Saves game settings to a file.

    The settings dictionary contains the following key-value pairs:
        viewFPS: FPS setting.
        numberAsteroids: Number of asteroids.
    """
    settings = {
        "viewFPS": FPS,
        "numberAsteroids": NUMBER_ASTEROIDS
    }

    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f)


def loadSettings():
    """Loads game settings from a file.

    Returns:
        A dictionary containing the game settings. If the file does not
        exist or cannot be read, returns an empty dictionary.
    """
    try:
        with open(SETTINGS_FILE, 'r') as f:
            settings = json.load(f)
            return settings
    except:
        return {}
