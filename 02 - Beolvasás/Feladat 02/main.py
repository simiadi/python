from os import system

nev: str = str(input("Adja meg a nevét: "))
szuletesiev: int = int(input("Adja meg a születési évét: "))

system("cls")

print(f"{nev} ön {szuletesiev} született!")