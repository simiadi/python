def getNumberFromConsole() -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncateString: str = None

    while (number == None):
        print("Adjon meg egy számot: ", end="")
        temp = input()
        truncateString = temp.replace(".", "").replace("-", "")
        isNumber = truncateString.isnumeric()

        if(isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg!")

    return number

def printToConsole(a: float, b: float, result: float, operator: str) -> None:
    print(f"{a} {operator} {b} = {result}")