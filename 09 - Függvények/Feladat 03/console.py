def getNameFromConsole() -> str:
    name: str = None

    while (name == None):
        print("Adja meg a nevét: ", end="")
        name = input()

    return name

def getAgeFromConsole() -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncateString: str = None

    while (number == None):
        print("Adja meg az életkorát: ", end="")
        temp = input()
        truncateString = temp.replace(".", "").replace("-", "")
        isNumber = truncateString.isnumeric()

        if(isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg!")

    return number

def printToConsole(name: str, age: int) -> None:
    print(f"{name} ön {age} éves!")