from os import system

szam: int = None

print("Adjon meg egy számot: ", end="")
szam = int(input())

system("cls")

if (szam < 20 and szam > 10):
    print("A szám 10 és 20 között van", end="")
elif (szam < -10 and szam > -20):
    print("A szám -10 és -20 között van", end="")
else:
    print("A szám nem 10 és 20, vagy -10 és -20 között van", end="")