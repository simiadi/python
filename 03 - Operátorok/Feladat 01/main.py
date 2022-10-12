from os import system

print("Adja meg az a értékét: ", end="")
a: float = float(input())
print("Adja meg a b értékét: ", end="")
b: float = float(input())
eredmeny: float = a + b

system("cls")

print(f"Eredmény: {eredmeny}")