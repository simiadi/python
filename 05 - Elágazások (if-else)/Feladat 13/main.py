from os import system

szam: int = None

print("Adjon meg egy számot: ", end="")
szam = int(input())

system("cls")

if (szam <= 9 and szam >= 0):
    print("A szám egyjegyű", end="")
elif (szam <= 99 and szam >= 10):
    print("A szám kétjegyű", end="")
elif (szam <= 999 and szam >= 100):
    print("A szám háromjegyű", end="")