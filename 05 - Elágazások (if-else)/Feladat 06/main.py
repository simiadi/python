from os import system

szam: int = None
szam2: int = None
szam3: int = None

print("Adjon meg egy számot: ", end="")
szam = int(input())

print("Adjon meg egy másik számot: ", end="")
szam2 = int(input())

print("Adjon meg mégegy számot: ", end="")
szam3 = int(input())

system("cls")

if (szam > szam2 and szam2 > szam3):
    print(f"A három szám: {szam3}, {szam2}, {szam}", end="")
elif (szam > szam3 and szam3 > szam2):
    print(f"A három szám: {szam2}, {szam3}, {szam}", end="")
elif (szam2 > szam and szam > szam3):
    print(f"A három szám: {szam3}, {szam}, {szam2}", end="")
elif (szam2 > szam3 and szam3 > szam):
    print(f"A három szám: {szam}, {szam3}, {szam2}", end="")
elif (szam3 > szam2 and szam2 > szam):
    print(f"A három szám: {szam}, {szam2}, {szam3}", end="")
elif (szam3 > szam and szam > szam2):
    print(f"A három szám: {szam2}, {szam}, {szam3}", end="")
else:
    print("A három szám egyenlő", end="")