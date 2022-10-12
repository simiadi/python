from os import system

print("Adja meg az a értékét: ", end="")
a: float = float(input())
print("Adja meg a b értékét: ", end="")
b: float = float(input())
print("Adja meg a c értékét: ", end="")
c: float = float(input())
eredmeny: float = (a * b) / c

system("cls")

print(f"Eredmény: {eredmeny}")