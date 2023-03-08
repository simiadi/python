def getNameFromConsole() -> str:
    name: str = None

    while (name == None):
        print("Adja meg a nevét: ", end="")
        name = input()

    return name

def getAgeFromConsole() -> int:
    age: int = None

    while (age == None):
        print("Adja meg az életkorát: ", end="")
        age = input()

    return age

def printToConsole(name: str, age: int) -> None:
    print(f"{name} ön {age} éves!")