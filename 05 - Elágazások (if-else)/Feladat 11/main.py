from os import system

szam: int = None

print("Adjon meg egy számot: ", end="")
szam = int(input())

system("cls")

if (szam % 2 == 0):
    print("A szám páros", end="")
else:
    print("", end="")