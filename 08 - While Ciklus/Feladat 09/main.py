number: int = None
temp: str = None
isNumber: bool = False
truncateString: str = None

while (number == None or number > 999 or number < 100):
    print("Adjon meg egy számot: ", end="")
    temp = input()
    truncateString = temp.replace(".", "").replace("-", "")
    isNumber = truncateString.isnumeric()

    if(isNumber):
        number = int(temp)
        if number > 999 or number < 100:
            print("A megadott szám nem háromjegyű!")
    else:
        print("Nem számot adott meg!")

if number % 7 == 0:
    print("A megadott szám osztható 7-tel!")
else:
    print("A megadott szám nem osztható 7-tel!")
    