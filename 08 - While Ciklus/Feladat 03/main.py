import random

number: int = None
guess: int = None
temp: str = None
isNumber: bool = False
truncateString: str = None
count: int = 0

number = random.randrange(0,9)

while (guess == None or (guess < 0 or guess > 9) or guess is not number):
    if count == 5:
        print("Maximum 5 alkalommal próbálkozhatsz!")
        break
    
    print("Adjon meg egy 0 és 9 közötti egész számot: ", end="")
    temp = input()
    truncateString = temp.replace(".", "").replace("-", "")
    isNumber = truncateString.isnumeric()

    if(isNumber):
        guess = int(temp)
        if guess == number:
            print(f"Kitaláltad a számot: {number}")
        else:
            print("Nem találtad el a számot, próbáld újra!")
    else:
        print("Nem számot adott meg!")

    count += 1
