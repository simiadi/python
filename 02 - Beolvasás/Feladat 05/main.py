from os import system

print("Adja meg a kedvenc együttesének a nevét: ", end="")
egyuttes: str = str(input())
print("Adja meg a legjobb zeneszámát: ", end="")
szam: str = str(input())
print("Adja meg a zeneszám hosszát (percben): ", end="")
szamhossz: float = float(input())

system("cls")

print(f"Az ön kedvenc együttesének {egyuttes} a legjobb zeneszáma {szam} melynek hossza {szamhossz} perc!")