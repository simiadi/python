from os import system

nev: str = str(input("Adja meg a nevét: "))
billentyu: str = str(input("Adjon meg egy billentyűt: "))

system("cls")

print(f"{nev} ön a/az {billentyu} billentyűt nyomta meg!")