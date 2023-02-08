age: int = None
temp: str = None
isNumber: bool = False
truncateString: str = None
ageGroup: str = None

while (age == None or ageGroup == None):
    print("Adjon meg egy életkort 0-tól 99-ig: ", end="")
    temp = input()
    truncateString = temp.replace(".", "").replace("-", "")
    isNumber = truncateString.isnumeric()

    if(isNumber):
        age = int(temp)
        if age >= 0 and age <= 99:
            if age >= 0 and age <= 6:
                ageGroup = "Gyerek"
            elif age > 6 and age <= 18:
                ageGroup = "Iskolás"
            elif age > 18 and age <= 64:
                ageGroup = "Dolgozó"
            elif age > 64:
                ageGroup = "Nyugdíjas"

            print(f"Az általad megadott életkor ebbe a korosztályba tartozik: {ageGroup}")
        else:
            print("Helytelen életkort adtál meg!")
    else:
        print("Nem számot adott meg!")
