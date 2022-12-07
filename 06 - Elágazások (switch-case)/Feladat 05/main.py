from os import system

szam1: int = None
szam2: int = None
muvelet: str = None
eredmeny1: float = None
eredmeny2: float = None

print("Add meg az egyik ellenállás értékét: ", end="")
szam1 = int(input())

print("Add meg a másik ellenállás értékét: ", end="")
szam2 = int(input())

print("Sorosan vagy párhuzamosan vannak bekötve az ellenállások? (s vagy p) ", end="")
muvelet = str(input())

system("cls")

match muvelet:
    case "s":
        eredmeny1 = szam1 + szam2
        print(f"Ellenállások eredő értéke soros bekötés esetén: {eredmeny1}", end="")
    case "p":
        eredmeny2 = (szam1 + szam2) / (szam1 * szam2)
        print(f"Ellenállások eredő értéke párhuzamos bekötés esetén: {eredmeny2}", end="")
    case _:
        print("Nincs ilyen bekötés!", end="")