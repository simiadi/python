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

        if(isNumber):
            number = float(temp)

        if(isNumber and number in range(start, end)):
            print(f"A megadott szám: {number}!")
        elif(number not in range(start, end)):
            print(f"A megadott szám nem {start} és {end} között van!")
        else:
            print("Nem számot adott meg!")

    return number

def guessRandomNumber(start, end, rndNumber) -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncateString: str = None
    count: int = 0

    while (number != rndNumber):
        print(f"Találja ki a {start} és {end} közötti random generált számot: ", end="")
        temp = input()
        truncateString = temp.replace(".", "").replace("-", "")
        isNumber = truncateString.isnumeric()
        count += 1

        if(isNumber):
            number = float(temp)

        if(isNumber and number == rndNumber):
            print(f"Sikeresen kitaláltad a random generált számot!")
        elif(isNumber and number > rndNumber):
            print(f"Nem talált, próbálja újra! A beírt szám nagyobb mint a random generált!")
        elif(isNumber and number < rndNumber):
            print(f"Nem talált, próbálja újra! A beírt szám kisebb mint a random generált!")
        else:
            print("Nem számot adott meg!")

    return count


def printToConsole(count: int) -> None:
    print(f"{count} próbálkozásból találtad ki a random generált számot!")