from os import system

szam: int = None
szam2: int = None

print("Adjon meg egy számot: ", end="")
szam = int(input())

print("Adjon meg egy másik számot: ", end="")
szam2 = int(input())

system("cls")

if (szam > szam2):
    print(f"A két szám: {szam2}, {szam}", end="")
elif (szam < szam2):
    print(f"A két szám: {szam}, {szam2}", end="")
else:
    print("A két szám egyenlő", end="")