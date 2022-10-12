from os import system

print("Adja meg a nevét: ", end="")
nev: str = str(input())

system("cls")

print(f"Üdvözlöm {nev}!")