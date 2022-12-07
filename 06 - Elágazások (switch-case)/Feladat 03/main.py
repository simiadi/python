from os import system

udito: int = None

print("Üdítők:\nCoca Cola --> 1\nPepsi --> 2\nFanta --> 3\nSprite --> 4\n", end="")

print("Hányas számű üdítőt szeretnéd? ", end="")
udito = int(input())

system("cls")

match udito:
    case 1:
        print("Sikeres vásárlás! (Coca Cola)", end="")
    case 2:
        print("Sikeres vásárlás! (Pepsi)", end="")
    case 3:
        print("Sikeres vásárlás! (Fanta)", end="")
    case 4:
        print("Sikeres vásárlás! (Sprite)", end="")
    case _:
        print("Nincs ilyen üdítő!", end="")