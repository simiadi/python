from os import system

kezdo: int = None
veg: int = None

print("Adja meg a kezdőértéket: ", end="")
kezdo = int(input())

print("Adja meg a végértéket: ", end="")
veg = int(input())

system("cls")

for i in range(kezdo, veg - 1, 2):
    print(i)