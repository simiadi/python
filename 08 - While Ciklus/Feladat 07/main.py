number: int = None
greaterNumber: int = None
temp: str = None
isNumber: bool = False
truncateString: str = None

print("Adjon meg egy számot: ", end="")
temp = input()
truncateString = temp.replace(".", "").replace("-", "")
isNumber = truncateString.isnumeric()

while (number == None or (number < 0 or number > 9)):
    print("Adjon meg egy számot: ", end="")
    temp = input()
    truncateString = temp.replace(".", "").replace("-", "")
    isNumber = truncateString.isnumeric()

    if(isNumber):
        number = float(temp)
        print(f"Számot adott meg: {number}")
    else:
        print("Nem számot adott meg!")
