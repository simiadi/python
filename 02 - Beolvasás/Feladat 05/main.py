from os import system

egyuttes: str = str(input("Adja meg a kedvenc együttesének a nevét: "))
szam: str = str(input("Adja meg a legjobb zeneszámát: "))
szamhossz: float = float(input("Adja meg a zeneszám hosszát (percben): "))

system("cls")

print(f"Az ön kedvenc együttesének {egyuttes} a legjobb zeneszáma {szam} melynek hossza {szamhossz} perc!")