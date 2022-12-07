from os import system

hossz: int = None
szelesseg: int = None
muvelet: str = None
eredmeny1: float = None
eredmeny2: float = None
eredmeny3: float = None

print("Adja meg a téglalap hosszát (cm): ", end="")
hossz = int(input())

print("Adja meg a téglalap szélességét (cm): ", end="")
szelesseg = int(input())

print("Mit szeretnél kiszámolni?\nTerület --> t\nKerület --> k\nÁtló --> a ", end="")
muvelet = str(input())

system("cls")

match muvelet:
    case "t":
        eredmeny1 = hossz * szelesseg
        print(f"Téglalap területének az értéke: {eredmeny1}", end="")
    case "k":
        eredmeny2 = (hossz + szelesseg) * 2
        print(f"Téglalap kerületének az értéke: {eredmeny2}", end="")
    case "a":
        eredmeny3 = (math.pow(hossz,2) + math.pow(szelesseg,2)) 
        print(f"Téglalap átlójának az értéke: {eredmeny3}", end="")
    case _:
        print("Ezt nem tudod kiszámolni!", end="")