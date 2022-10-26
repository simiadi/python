from os import system

a: float = None
b: float = None
c: float = None
d: float = None
eredmeny: float = None

print("Adja meg az a értékét: ", end="")
a = float(input())
print("Adja meg a b értékét: ", end="")
b = float(input())
print("Adja meg a c értékét: ", end="")
c = float(input())
print("Adja meg a d értékét: ", end="")
d = float(input())
eredmeny = (a + b) / (c - d)

system("cls")

print(f"Eredmény: {eredmeny}")