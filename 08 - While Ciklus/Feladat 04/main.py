number: int = None
sum: int = 0
temp: str = None
isNumber: bool = False
truncateString: str = None
count: int = 0

while (number == None or sum < 101):
    print("Adjon meg egy számot: ", end="")
    temp = input()
    truncateString = temp.replace(".", "").replace("-", "")
    isNumber = truncateString.isnumeric()

    if(isNumber):
        number = int(temp)
        sum = sum + number
        count += 1
        print(f"A megadott szám: {number}")
        print(f"Ennyi számot adtál meg eddig: {count}")
        if sum > 100:
            print("A megadott számaid összege meghaladta a 100-at!")
    else:
        print("Nem számot adott meg!")
    
