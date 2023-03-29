def getXFromConsole() -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncateString: str = None

    while (number == None):
        print("Adja meg az x értékét: ", end="")
        temp = input()
        truncateString = temp.replace(".", "").replace("-", "")
        isNumber = truncateString.isnumeric()

        if(isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg!")

    return number

def getYFromConsole() -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncateString: str = None

    while (number == None):
        print("Adja meg az y értékét: ", end="")
        temp = input()
        truncateString = temp.replace(".", "").replace("-", "")
        isNumber = truncateString.isnumeric()

        if(isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg!")

    return number

def printToConsole(distance: float) -> None:
    print(f"A két pont távolsága: {distance}")