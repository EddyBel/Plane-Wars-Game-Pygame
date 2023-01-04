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
    try:
        with open(SCORE_FILE, 'r') as f:
            score = int(f.read())
        return int(score)
    except:
        return 0


def saveSettings() -> None:

    settings = {
        "viewFPS": FPS,
        "numberAsteroids": NUMBER_ASTEROIDS
    }

    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f)


def loadSettings():
    try:
        with open(SETTINGS_FILE, 'r') as f:
            settings = json.load(f)
            return settings
    except:
        return {}
