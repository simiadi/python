from os import system

megjelenesiev: int = int(input("Adja meg a kedvenc filmének a megjelenési évét: "))
rendezonev: str = str(input("Adja meg a rendező nevét: "))
filmcim: str = str(input("Adja meg a film címét: "))
foszereplonev: str = str(input("Adja meg a főszereplő nevét: "))

system("cls")

print(f"{megjelenesiev}-ban/ben {rendezonev} rendezésében megjelent a/az {filmcim} című film {foszereplonev} főszereplésével!")