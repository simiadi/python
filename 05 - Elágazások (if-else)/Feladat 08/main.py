from os import system

szam: int = None

print("Adjon meg egy számot: ", end="")
szam = int(input())

system("cls")

if (szam % 4 == 0 and szam % 6 == 0):
    print("A szám osztható 4-gyel és 6-tal is", end="")
elif (szam % 4 == 0 and szam % 6 != 0):
    print("A szám osztható 4-gyel, de 6-tal nem", end="")
elif (szam % 4 != 0 and szam % 6 == 0):
    print("A szám osztható 6-tal, de 4-gyel nem", end="")
else:
    print("A szám nem osztható 4-gyel és 6-tal se", end="")