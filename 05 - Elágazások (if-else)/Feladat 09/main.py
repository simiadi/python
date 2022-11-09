from os import system

x: int = None
y: int = None

print("Adja meg az x értékét: ", end="")
x = int(input())

print("Adja meg az y értékét: ", end="")
y = int(input())

system("cls")

if (x % y == 0):
    print("Az y osztója az x-nek", end="")
else:
    print("Az y nem osztója az x-nek", end="")