from os import system

nap: str = None

print("Milyen nap van ma? ", end="")
nap = str(input())

system("cls")

match nap:
    case "Hétfő":
        print("A hét 1. napja van ma", end="")
    case "Kedd":
        print("A hét 2. napja van ma", end="")
    case "Szerda":
        print("A hét 3. napja van ma", end="")
    case "Csütörtök":
        print("A hét 4. napja van ma", end="")
    case "Péntek":
        print("A hét 5. napja van ma", end="")
    case "Szombat":
        print("A hét 6. napja van ma", end="")
    case "Vasárnap":
        print("A hét 7. napja van ma", end="")
    case _:
        print("Nincs ilyen nap a héten!", end="")