def getWordFromConsole() -> str:
    word: str = None

    while (word == None):
        print("Adjon meg egy szót: ", end="")
        word = input()

    return word

def getSameLetters(n1: str, n2: str) -> int:
    n1: str = None
    n2: str = None
    count: int = 0

    for i in range(min(len(n1), len(n2))):
        if n1[i] == n2[i]:
            count += 1

    return count

def printToConsole(result: float) -> None:
    print(f"Ennyi karakterük egyezik meg: {result}")