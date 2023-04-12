import random

def generateRandomNumberBetweenRange(start, end) -> float:
    number: float = None

    number = random.randrange(start, end)

    return number