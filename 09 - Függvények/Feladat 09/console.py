def getValueFromConsole() -> float:
    number: float = None
    temp: str = None
    isNumber: bool = False
    truncateString: str = None

    while (number == None):
        print("Adja meg mennyi forintot szeretne átváltani: ", end="")
        temp = input()
        truncateString = temp.replace(".", "").replace("-", "")
        isNumber = truncateString.isnumeric()

        if(isNumber):
            number = float(temp)
        else:
            print("Nem számot adott meg!")

    return number

def getCurrencyFromConsole() -> str:
    currency: str = None

    while (currency == None):
        print("Adja meg a valutát (JPY, USD vagy CHF): ", end="")
        currency = input().upper()

        if(currency not in ["JPY", "USD", "CHF"]):
            print("Nem megfelelő valuta!")

    return currency

def printToConsole(result: float) -> None:
    print(f"{result}")