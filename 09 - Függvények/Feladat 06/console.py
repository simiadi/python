def getValueFromConsole() -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncateString: str = None

    while (number == None):
        print("Adja meg a celsius értéket: ", end="")
        temp = input()
        truncateString = temp.replace(".", "").replace("-", "")
        isNumber = truncateString.isnumeric()

        if(isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg!")

    return number

def getUnitFromConsole() -> str:
    unit: str = None

    while (unit == None):
        print("Adja meg a mértékegység nevét (F vagy K): ", end="")
        unit = input()

        if(unit not in ["F", "K"]):
            print("Nem megfelelő mértékegység!")

    return unit.upper()

def printToConsole(result: str, value: float, unit: str) -> None:
    print(f"{value} Celsius = {result} {unit}")