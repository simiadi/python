from os import system

print("Adja meg a nevét: ", end="")
nev: str = str(input())
print("Adja meg a születési évét: ", end="")
szuletesiev: int = int(input())

system("cls")

print(f"{nev} ön {szuletesiev} született!")