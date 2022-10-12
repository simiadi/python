from os import system

print("Adja meg a nevét: ", end="")
nev: str = str(input())
print("Adjon meg egy billentyűt: ", end="")
billentyu: str = str(input())

system("cls")

print(f"{nev} ön a/az {billentyu} billentyűt nyomta meg!")