def getWordFromConsole() -> str:
    word: str = None

    while (word == None):
        print("Adjon meg egy szót: ", end="")
        word = input()

    return word

def printToConsole(result: str) -> None:
    print(f"Ennyi karakterük egyezik meg: {result}")