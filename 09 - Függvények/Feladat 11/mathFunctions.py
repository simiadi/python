def getDistanceBetweenCoordinates(x1, x2, y1, y2) -> float:
    distance: float = None

    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    return distance