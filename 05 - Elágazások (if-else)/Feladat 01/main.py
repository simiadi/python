from os import system

szam: int = None

print("Adjon meg egy számot: ", end="")
szam = int(input())

system("cls")

if (szam > 0):
    print("A szám nagyobb 0-nál", end="")
else:
    print("A szám nem nagyobb 0-nál", end="")