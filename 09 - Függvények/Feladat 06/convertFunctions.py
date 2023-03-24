def convertCelsius(value: float, unit: str) -> float:
    result: float = None

    if(unit == "F"):
        result = 9/5 * value + 32
    else:
        result = value + 273.15

    return result