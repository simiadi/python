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

def guessRandomNumber(start, end, rndNumber) -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncateString: str = None
    count: int = None

    while (number is not rndNumber):
        print(f"Találja ki a {start} és {end} közötti random generált számot: ", end="")
        temp = input()
        truncateString = temp.replace(".", "").replace("-", "")
        isNumber = truncateString.isnumeric()
        count += 1

        if(isNumber and temp == rndNumber):
            number = float(temp)
        elif(isNumber and temp > rndNumber):
            print(f"Nem talált, próbálja újra! A beírt szám nagyobb mint a random generált!")
        elif(isNumber and temp < rndNumber):
            print(f"Nem talált, próbálja újra! A beírt szám kisebb mint a random generált!")
        else:
            print("Nem számot adott meg!")

    return [number, count]


def printToConsole(result: float) -> None:
    print(f"{result}")