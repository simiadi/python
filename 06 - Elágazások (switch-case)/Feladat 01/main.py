from os import system

nap: int = None

print("A hét hányadik napja van ma? ", end="")
nap = int(input())

system("cls")

match nap:
    case 1:
        print("Hétfő van ma", end="")
    case 2:
        print("Kedd van ma", end="")
    case 3:
        print("Szerda van ma", end="")
    case 4:
        print("Csütörtök van ma", end="")
    case 5:
        print("Péntek van ma", end="")
    case 6:
        print("Szombat van ma", end="")
    case 7:
        print("Vasárnap van ma", end="")
    case _:
        print("Nincs ilyen nap a héten", end="")