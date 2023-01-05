def obtainCoordinates(reference: int, landmarks, width: int, height: int) -> tuple:
    x = int(landmarks.landmark[reference].x * width)
    y = int(landmarks.landmark[reference].y * height)
    return (x, y)


def scale(max: int, min: int, value: float) -> float:
    result = 2 * (value - min) / (max - min) - 1
    if result < -1:
        return -1
    elif result > 1:
        return 1
    return result


def scale_of_range(max: int, min: int, value: float, out_max: float = 1, out_min: float = -1) -> float:
    result = (out_max - out_min) * (value - min) / (max - min) + out_min
    if result < out_min:
        return out_min
    elif result > out_max:
        return out_max
    return result
