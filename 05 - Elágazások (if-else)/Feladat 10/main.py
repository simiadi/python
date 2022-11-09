from os import system

szam: int = None

print("Adjon meg egy számot: ", end="")
szam = int(input())

system("cls")

if (szam % 2 == 0 and szam % 3 == 0):
    print("ZIZI", end="")
elif (szam % 2 == 0):
    print("BIZ", end="")
elif (szam % 3 == 0):
    print("BAZ", end="")
else:
    print("A szám nem osztható 2-vel és 3-mal se", end="")