from os import system

nev: str = str(input("Adja meg a nevét: "))
magassag: float = float(input("Adja meg a magasságát (méterben): "))

system("cls")

print(f"{nev} az ön magassága {magassag}m!")