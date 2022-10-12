from os import system

print("Adja meg a nevét: ", end="")
nev: str = str(input())
print("Adja meg a magasságát (méterben): ", end="")
magassag: float = float(input())

system("cls")

print(f"{nev} az ön magassága {magassag}m!")