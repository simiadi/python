from os import system

a: float = None
b: float = None
eredmeny: float = None

print("Adja meg az a értékét: ", end="")
a = float(input())
print("Adja meg a b értékét: ", end="")
b = float(input())
eredmeny = a + b

system("cls")

print(f"Eredmény: {eredmeny}")