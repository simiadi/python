number: int = None
temp: str = None
isNumber: bool = False
truncateString: str = None
numbers: int = None
count: int = 0

while (number == None or number > 99 or number < 1):
    print("Adjon meg egy páros számot: ", end="")
    temp = input()
    truncateString = temp.replace(".", "").replace("-", "")
    isNumber = truncateString.isnumeric()

    if(isNumber):
        number = int(temp)
        if number > 99 or number < 1:
            print("A megadott szám nem egyjegyű vagy kétjegyű pozitív egész szám!")
        else:
            for numbers in range(1,number):
                if numbers % 2 == 0:
                    print(numbers)
            print("")
            for numbers in range(1,number):
                if numbers % 5 == 0:
                    print(numbers)
            print("")
            for numbers in range(1,number):
                if numbers % 11 == 0:
                    count += 1
            print(count)
            print("")
            for numbers in range(1,number):
                if numbers % 7 == 3:
                    print(numbers)
    else:
        print("Nem számot adott meg!")