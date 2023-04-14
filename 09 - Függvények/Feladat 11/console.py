def getNameFromConsole() -> str:
    name: str = None

    while (name == None):
        print("Adja meg a nevét: ", end="")
        name = input().capitalize()

    return name

def getWeeklyHoursFromConsole() -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncateString: str = None

    while (number == None):
        print("Adja meg hány órát dolgozott a héten: ", end="")
        temp = input()
        truncateString = temp.replace(".", "").replace("-", "")
        isNumber = truncateString.isnumeric()

        if(isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg!")

    return number

def printToConsole(result: float, result2: float, currency: str) -> None:
    print(f"{currency} érték: {result} EUR érték: {result2}")