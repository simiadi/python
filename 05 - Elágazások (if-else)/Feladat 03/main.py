from os import system

szam: int = None

print("Adjon meg egy számot: ", end="")
szam = int(input())

system("cls")

if (szam > -30 and szam < 40):
    print("A szám -30 és 40 között van", end="")
else:
    print("A szám nem -30 és 40 között van", end="")