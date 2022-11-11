from os import system

szam: int = None

print("Adjon meg egy számot: ", end="")
szam = int(input())

system("cls")

if (szam % 2 == 0):
    print("A szám páros", end="")
else:
    print("A szám páratlan", end="")

if (szam < 0):
    print("A szám negatív", end="")
else:
    print("A szám pozitív", end="")

if (szam % 5 == 0):
    print("A szám osztható 5-tel", end="")
else:
    print("A szám nem osztható 5-tel", end="")