from os import system

print("Adja meg a kedvenc filmének a megjelenési évét: ", end="")
megjelenesiev: int = int(input())
print("Adja meg a rendező nevét: ", end="")
rendezonev: str = str(input())
print("Adja meg a film címét: ", end="")
filmcim: str = str(input())
print("Adja meg a főszereplő nevét: ", end="")
foszereplonev: str = str(input())

system("cls")

print(f"{megjelenesiev}-ban/ben {rendezonev} rendezésében megjelent a/az {filmcim} című film {foszereplonev} főszereplésével!")