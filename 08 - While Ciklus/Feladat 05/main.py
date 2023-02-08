number: int = None
sum: int = 0
maxsum: int = None
temp: str = None
isNumber: bool = False
truncateString: str = None
count: int = 0

print("Adjon meg egy határértéket: ", end="")
temp = input()
truncateString = temp.replace(".", "").replace("-", "")
isNumber = truncateString.isnumeric()
maxsum = int(temp)

while (number == None or sum <= maxsum):
    print("Adjon meg egy számot: ", end="")
    temp = input()
    truncateString = temp.replace(".", "").replace("-", "")
    isNumber = truncateString.isnumeric()

    if(isNumber):
        number = int(temp)
        sum = sum + number
        count += 1
        print(f"A megadott szám: {number}")
        if sum > maxsum:
            print(f"A megadott számaid összege meghaladta az általad megadott határértéket: {maxsum}")
            print(f"Ennyi lépésből érted el a határértéket: {count}")
    else:
        print("Nem számot adott meg!")
    
