from os import system

szam1: int = None
szam2: int = None
muvelet: str = None
eredmeny1: float = None
eredmeny2: float = None
eredmeny3: float = None
eredmeny4: float = None

print("Adj meg egy számot: ", end="")
szam1 = int(input())

print("Adj meg egy másik számot: ", end="")
szam2 = int(input())

print("Milyen műveletet szeretnél elvégezni? (+,-,*,/) ", end="")
muvelet = str(input())

system("cls")

match muvelet:
    case "+":
        eredmeny1 = szam1 + szam2
        print(f"Eredmény: {eredmeny1}", end="")
    case "-":
        eredmeny2 = szam1 - szam2
        print(f"Eredmény: {eredmeny2}", end="")
    case "*":
        eredmeny3 = szam1 * szam2
        print(f"Eredmény: {eredmeny3}", end="")
    case "/":
        eredmeny4 = szam1 / szam2
        print(f"Eredmény: {eredmeny4}", end="")
    case _:
        print("Nincs ilyen művelet!", end="")