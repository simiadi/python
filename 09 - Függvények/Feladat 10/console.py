def getNumberInRangeFromConsole(start, end) -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncateString: str = None

    while (number == None):
        print(f"Adjon meg egy {start} és {end} közötti számot: ", end="")
        temp = input()
        truncateString = temp.replace(".", "").replace("-", "")
        isNumber = truncateString.isnumeric()

        if(isNumber and temp in range(start, end)):
            number = float(temp)
        elif(temp not in range(start, end)):
            print(f"A megadott szám nem {start} és {end} között van!")
        else:
            print("Nem számot adott meg!")

    return number

def printToConsole(result: float) -> None:
    print(f"{result}")