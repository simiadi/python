from os import system

x: int = None
y: int = None
z: int = None

print("Adja meg az x értékét: ", end="")
x = int(input())

print("Adja meg az y értékét: ", end="")
y = int(input())

print("Adja meg a z értékét: ", end="")
z = int(input())

system("cls")

if (x % y == 0 and x % z == 0):
    print("Az x osztható y-nal és z-vel is", end="")
elif (x % y == 0):
    print("Az x osztható y-nal", end="")
elif (x % z == 0):
    print("Az x osztható z-vel", end="")
else:
    print("Az x nem osztható y-nal és z-vel se", end="")