from os import system

szam: int = None

print("Adjon meg egy számot: ", end="")
szam = int(input())

system("cls")

if (szam >= 0):
    print("Pozitív", end="")
else:
    print("Negatív", end="")